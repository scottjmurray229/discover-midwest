#!/usr/bin/env node
/**
 * STEP 1: Sweep Downloads Folder — Move & Organize Video Clips
 *
 * Scans ~/Downloads/ for recently downloaded .mp4/.mov files,
 * identifies them, MOVES (not copies!) to raw-downloads/, and updates inventory.
 *
 * Scott downloads clips manually from Storyblocks (descriptive names) and
 * Shutterstock (numeric IDs only). This script handles both.
 *
 * Usage:
 *   node video-tracking/pipeline/1-sweep-downloads.cjs                  # Sweep all new clips
 *   node video-tracking/pipeline/1-sweep-downloads.cjs --dest boston     # Only process clips for boston
 *   node video-tracking/pipeline/1-sweep-downloads.cjs --dry-run        # Preview what would happen
 *   node video-tracking/pipeline/1-sweep-downloads.cjs --since 24       # Only files from last 24 hours
 */

const fs = require('fs');
const path = require('path');
const readline = require('readline');
const yaml = require('js-yaml');
const { loadConfig } = require('./config-loader.cjs');

const config = loadConfig();

// Parse CLI args
const args = process.argv.slice(2);
const destFilter = args.includes('--dest') ? args[args.indexOf('--dest') + 1] : null;
const dryRun = args.includes('--dry-run');
const sinceHours = args.includes('--since') ? parseInt(args[args.indexOf('--since') + 1]) : 72;

const DOWNLOADS_DIR = path.join(require('os').homedir(), 'Downloads');
const VIDEO_EXTENSIONS = ['.mp4', '.mov', '.avi', '.mkv', '.webm'];

// Interactive readline
const rl = readline.createInterface({ input: process.stdin, output: process.stdout });
const ask = (q) => new Promise(resolve => rl.question(q, resolve));

// Load inventory if it exists
let inventory = { entries: [] };
if (fs.existsSync(config.INVENTORY_PATH)) {
  inventory = yaml.load(fs.readFileSync(config.INVENTORY_PATH, 'utf8'));
}

// Get destination slugs that need downloads
function getNeededDestinations() {
  return inventory.entries
    .filter(e => e.stock_status === 'needs_download')
    .map(e => e.page)
    .filter((v, i, a) => a.indexOf(v) === i); // unique
}

// Scan Downloads for recent video files
function findDownloadedVideos() {
  if (!fs.existsSync(DOWNLOADS_DIR)) {
    console.error(`  Downloads folder not found: ${DOWNLOADS_DIR}`);
    return [];
  }

  const cutoff = Date.now() - (sinceHours * 60 * 60 * 1000);
  const files = [];

  for (const file of fs.readdirSync(DOWNLOADS_DIR)) {
    const ext = path.extname(file).toLowerCase();
    if (!VIDEO_EXTENSIONS.includes(ext)) continue;

    const filePath = path.join(DOWNLOADS_DIR, file);
    const stat = fs.statSync(filePath);
    if (!stat.isFile()) continue;
    if (stat.mtimeMs < cutoff) continue;

    files.push({
      name: file,
      path: filePath,
      size: stat.size,
      modified: stat.mtime,
      isShutterstock: /^shutterstock_\d+/i.test(file) || /^\d{8,}/.test(file),
      isStoryblocks: !(/^shutterstock_\d+/i.test(file) || /^\d{8,}/.test(file)),
    });
  }

  // Sort by modified time, newest first
  files.sort((a, b) => b.modified - a.modified);
  return files;
}

// Guess destination from descriptive filename (Storyblocks)
function guessDestination(filename, destinations) {
  const lower = filename.toLowerCase();
  for (const dest of destinations) {
    // Check if destination slug appears in filename
    if (lower.includes(dest.replace(/-/g, ''))) return dest;
    if (lower.includes(dest.replace(/-/g, ' '))) return dest;
    if (lower.includes(dest.replace(/-/g, '_'))) return dest;
    if (lower.includes(dest)) return dest;
  }
  return null;
}

// Guess clip type from filename
function guessSlot(filename) {
  const lower = filename.toLowerCase();
  if (lower.includes('aerial') || lower.includes('drone') || lower.includes('skyline') || lower.includes('panoram')) return 'hero';
  if (lower.includes('preview') || lower.includes('thumb')) return 'thumbnail';
  return 'break';
}

// Get target directory based on slot
function getTargetDir(slot) {
  if (slot === 'hero') return path.join(config.RAW_DOWNLOADS, 'heroes');
  if (slot === 'thumbnail') return path.join(config.RAW_DOWNLOADS, 'thumbnails');
  return path.join(config.RAW_DOWNLOADS, 'breaks');
}

// Generate filename
function getTargetFilename(destination, slot, section) {
  if (slot === 'hero') return `${destination}-hero.mp4`;
  if (slot === 'thumbnail') return `${destination}-preview.mp4`;
  return `${destination}-break-${section || 'general'}.mp4`;
}

// Move file (not copy!)
function moveFile(src, dest) {
  try {
    // Try rename first (same drive = instant)
    fs.renameSync(src, dest);
  } catch (err) {
    // Cross-drive: copy then delete
    fs.copyFileSync(src, dest);
    fs.unlinkSync(src);
  }
}

// Main process
async function main() {
  console.log('╔══════════════════════════════════════════════════════════╗');
  console.log('║   SWEEP DOWNLOADS — MOVE & ORGANIZE VIDEO CLIPS         ║');
  console.log('╚══════════════════════════════════════════════════════════╝');
  console.log();

  // Find videos in Downloads
  const videos = findDownloadedVideos();
  console.log(`  Found ${videos.length} video files in Downloads (last ${sinceHours}h)`);
  if (destFilter) console.log(`  Filtering: destination = ${destFilter}`);
  if (dryRun) console.log('  DRY RUN — no files will be moved');
  console.log();

  if (videos.length === 0) {
    console.log('  No new video files found in Downloads.');
    console.log(`  (Looking in: ${DOWNLOADS_DIR})`);
    console.log(`  (Extensions: ${VIDEO_EXTENSIONS.join(', ')})`);
    console.log(`  (Since: ${sinceHours} hours ago)`);
    rl.close();
    return;
  }

  // Show what we found
  const storyblocks = videos.filter(v => v.isStoryblocks);
  const shutterstock = videos.filter(v => v.isShutterstock);

  if (storyblocks.length > 0) {
    console.log(`  Storyblocks clips (descriptive names): ${storyblocks.length}`);
  }
  if (shutterstock.length > 0) {
    console.log(`  Shutterstock clips (ID-only names): ${shutterstock.length}`);
    console.log('  ⚠️  Shutterstock files need manual destination assignment!\n');
  }

  // Get all destination slugs from inventory
  const allDestinations = inventory.entries
    .map(e => e.page)
    .filter((v, i, a) => a.indexOf(v) === i);

  const stats = { moved: 0, skipped: 0, errors: 0 };

  for (let i = 0; i < videos.length; i++) {
    const video = videos[i];
    const sizeMB = (video.size / 1024 / 1024).toFixed(1);

    console.log(`\n${'─'.repeat(60)}`);
    console.log(`  [${i + 1}/${videos.length}] ${video.name}`);
    console.log(`  Size: ${sizeMB} MB | Modified: ${video.modified.toLocaleString()}`);
    console.log(`  Source: ${video.isShutterstock ? 'Shutterstock (ID only)' : 'Storyblocks (descriptive)'}`);

    // Try to auto-detect destination
    let destination = guessDestination(video.name, allDestinations);
    let slot = guessSlot(video.name);

    if (destination) {
      console.log(`  Auto-detected destination: ${destination}`);
    }

    // For Shutterstock or unmatched files, ask user
    if (!destination) {
      console.log(`\n  Available destinations: ${allDestinations.join(', ')}`);
      const input = await ask(`  Enter destination slug (or "skip"): `);
      if (input === 'skip' || input === 's') {
        console.log('  Skipped.');
        stats.skipped++;
        continue;
      }
      destination = input.trim();
    } else {
      const confirm = await ask(`  Use ${destination}? (y/n/skip/[other destination]): `);
      if (confirm === 'skip' || confirm === 's') {
        console.log('  Skipped.');
        stats.skipped++;
        continue;
      }
      if (confirm !== 'y' && confirm !== '') {
        destination = confirm.trim();
      }
    }

    // Apply destination filter
    if (destFilter && destination !== destFilter) {
      console.log(`  Skipped (doesn't match --dest ${destFilter})`);
      stats.skipped++;
      continue;
    }

    // Ask for slot type
    console.log(`  Detected type: ${slot}`);
    const slotInput = await ask(`  Type? (h=hero, b=break, t=thumbnail, or enter to accept "${slot}"): `);
    if (slotInput === 'h') slot = 'hero';
    else if (slotInput === 'b') slot = 'break';
    else if (slotInput === 't') slot = 'thumbnail';

    // For breaks, ask for section name
    let section = null;
    if (slot === 'break') {
      section = await ask('  Section name (e.g., "temples", "food", "nightlife"): ');
      if (!section) section = 'general';
    }

    // Build target path
    const targetDir = getTargetDir(slot);
    const targetFilename = getTargetFilename(destination, slot, section);
    const targetPath = path.join(targetDir, targetFilename);

    console.log(`\n  → ${targetFilename}`);
    console.log(`    ${targetDir}`);

    if (dryRun) {
      console.log('  [DRY RUN] Would move file');
      stats.moved++;
      continue;
    }

    // Create directory and move
    try {
      fs.mkdirSync(targetDir, { recursive: true });

      // Check for existing file
      if (fs.existsSync(targetPath)) {
        const overwrite = await ask('  File exists! Overwrite? (y/n): ');
        if (overwrite !== 'y') {
          console.log('  Skipped (file exists).');
          stats.skipped++;
          continue;
        }
      }

      moveFile(video.path, targetPath);
      console.log(`  ✅ Moved: ${video.name} → ${targetFilename}`);
      stats.moved++;

      // Update inventory
      const invEntry = inventory.entries.find(e =>
        e.page === destination && e.slot === slot && e.stock_status === 'needs_download'
      );
      if (invEntry) {
        invEntry.stock_status = 'downloaded';
        invEntry.file_path = targetPath;
        invEntry.notes = `Downloaded ${new Date().toISOString().split('T')[0]}. ${invEntry.notes || ''}`.trim();
      }
    } catch (err) {
      console.error(`  ❌ Error: ${err.message}`);
      stats.errors++;
    }
  }

  // Save updated inventory
  if (stats.moved > 0 && !dryRun) {
    fs.writeFileSync(config.INVENTORY_PATH, yaml.dump(inventory, {
      lineWidth: -1,
      quotingType: '"',
      forceQuotes: false,
    }));
    console.log(`\n  Inventory updated: ${config.INVENTORY_PATH}`);
  }

  console.log(`\n${'═'.repeat(60)}`);
  console.log('  SWEEP COMPLETE');
  console.log(`  Moved: ${stats.moved}`);
  console.log(`  Skipped: ${stats.skipped}`);
  console.log(`  Errors: ${stats.errors}`);
  console.log(`${'═'.repeat(60)}\n`);

  if (stats.moved > 0) {
    console.log('  Next step: Run Step 2 to compress & watermark');
    console.log('  node video-tracking/pipeline/2-batch-process.cjs');
  }

  rl.close();
}

main().catch(err => {
  console.error('Fatal error:', err);
  rl.close();
  process.exit(1);
});

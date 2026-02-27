# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Discover Midwest -- a travel guide website built with Astro 5, Tailwind CSS 4, and deployed to Cloudflare Pages. Content is markdown-based using Astro's content collections with Zod schemas.

## Commands

```bash
npm run dev       # Start dev server at localhost:4321
npm run build     # Production build to ./dist/
npm run preview   # Preview production build locally
```

No test runner is configured. No linter is configured.

## Branding

- Colors: Ocean Teal #0D7377 (primary), Warm Coral #E8654A (accent)
- Deep Night #1A2332 (headings/dark backgrounds)
- Sand #F5F0E8 (light background), Sky #E8F4F5 (alt background)
- Warm Gold #D4A574
- Fonts: Outfit (sans), DM Serif Display (serif)

## Regions

- great-lakes
- plains
- ohio-valley

## Architecture

### Content Collections (`src/content/`)

Two collections defined in `src/content/config.ts`:
- **destinations** -- Travel destination pages with typed schema (region enum: great-lakes/plains/ohio-valley, budgetPerDay in USD, highlights array, contentStatus workflow, gradientColors for per-destination theming)
- **blog** -- Articles with categories (destination, food, festival, practical, budget, culture)

Both collections use a `draft: true` default. Content status tracks: draft -> review -> published -> needs-update.

### Deployment

- Domain: discovermidwest.info
- D1 database: trip-planner-cache-mw (ID: 53624d6a-7fe7-4e8d-a4d2-6b97b7a74790)
- Cloudflare Pages via `@astrojs/cloudflare` adapter

## Destinations (13)

Chicago, St. Louis, Kansas City, Minneapolis, Milwaukee, Indianapolis, Cincinnati, Detroit, Cleveland, Columbus, Omaha, Des Moines, Madison

## Content Voice

- First-person singular -- Scott's perspective as a visitor
- Prices in USD only
- Honest, opinionated, insider perspective
- **Names rule:** Only use "Scott" and "I" in content. Never include names of family members, children, or other companions.

## Affiliate Links

- Booking.com: aid=2778866, label=discovermidwest
- GetYourGuide: partner_id=IVN6IQ3
- Viator: pid=P00290009
- SafetyWing: referenceID=24858745

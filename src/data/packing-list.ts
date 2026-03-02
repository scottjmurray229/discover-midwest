import type { PackingItem, PackingConfig, GearRecommendation } from './packing-base';

export const MIDWEST_ESSENTIALS: PackingItem[] = [
  { id: 'mw-layers', name: 'Cold-Weather Layering System', category: 'destination', description: 'Chicago wind chills hit -20°F in winter. Minneapolis averages 54 days below 0°F. Merino wool base layer + mid-fleece + waterproof shell is the only system that works.', essential: true, climate: ['cold', 'temperate'], amazonSearchFallback: 'cold+weather+layering+system+thermal' },
  { id: 'mw-windproof', name: 'Windproof Outer Layer', category: 'destination', description: 'The Midwest is flat and there is nothing to stop the wind. A jacket that\'s warm enough in still air becomes dangerously inadequate in Chicago lakefront winds. Wind-resistant outer shell is essential.', essential: true, climate: ['cold'], amazonSearchFallback: 'windproof+jacket+outdoor+cold+weather', affiliatePrice: '$60–120' },
  { id: 'mw-walkshoes', name: 'Waterproof / Insulated Footwear', category: 'destination', description: 'Midwest winters mean ice, slush, and snow on sidewalks. Sneakers become wet and cold within minutes. Waterproof boots with insulation are non-negotiable October–March.', essential: true, climate: ['cold'], amazonSearchFallback: 'waterproof+insulated+boots+winter+walking', affiliatePrice: '$80–150' },
  { id: 'mw-handwarmers', name: 'Hand Warmers (disposable)', category: 'destination', description: 'Stadium tailgating, outdoor festivals, and simply walking to your car at -10°F — disposable hand warmers are cheap insurance against the brutal cold. Pack more than you think you\'ll need.', essential: false, climate: ['cold'], amazonSearchFallback: 'hand+warmers+disposable+hothands', affiliatePrice: '$8–15' },
];

export const MIDWEST_GEAR_RECOMMENDATIONS: GearRecommendation[] = [
  { id: 'gr-mw-boots', name: 'Insulated Waterproof Boots', reason: 'Chicago slush, Minneapolis ice, and Cleveland lake-effect snow — waterproof insulated boots are the single most important Midwest winter purchase. The difference between miserable and comfortable.', amazonSearchFallback: 'insulated+waterproof+boots+winter+walking', affiliatePrice: '~$120' },
  { id: 'gr-mw-jacket', name: 'Windproof Parka', reason: 'The Midwest wind doesn\'t stop. A jacket rated for still-air 30°F becomes dangerously inadequate in Chicago lakefront -20°F wind chill. Windproof outer shell is non-optional.', amazonSearchFallback: 'windproof+parka+insulated+winter', affiliatePrice: '~$150' },
  { id: 'gr-mw-baselayer', name: 'Merino Wool Base Layer Set', reason: 'Merino wool stays warm when wet, regulates temperature, and resists odor. It\'s what locals wear under everything from September through April. Worth every dollar.', amazonSearchFallback: 'merino+wool+base+layer+thermal+set', affiliatePrice: '~$80' },
  { id: 'gr-mw-powerbank', name: 'High-Capacity Power Bank', reason: 'Cold kills phone batteries fast. At -10°F, a 100% charge can drop to 20% in 30 minutes of navigation. A power bank in your inner pocket keeps you from being stranded.', amazonSearchFallback: 'power+bank+20000mah+cold+weather', affiliatePrice: '~$35' },
  { id: 'gr-mw-bag', name: 'Insulated Daypack', reason: 'A daypack that keeps your water from freezing, your snacks unfrozen, and adds an extra insulation layer to your back on a -5°F Chicago architecture tour.', amazonSearchFallback: 'insulated+daypack+backpack+winter', affiliatePrice: '~$50' },
];

export const MIDWEST_CONFIG: PackingConfig = {
  sitePrefix: 'dmw',
  destination: 'Midwest',
  climate: ['temperate', 'cold'],
  currency: 'USD',
  plugType: 'Type A/B',
  plugVoltage: '120V',
  affiliateTag: 'discovermore-20',
  destinationEssentials: MIDWEST_ESSENTIALS,
  gearRecommendations: MIDWEST_GEAR_RECOMMENDATIONS,
};

export const SITE_CONFIG = MIDWEST_CONFIG;

export const MIDWEST_PACKING_FAQS = [
  { question: 'What should I pack for the Midwest?', answer: 'The essentials depend on season. Winter demands a layering system (merino base + fleece + windproof shell), waterproof insulated boots, and hand warmers. Summer is mild — light layers, comfortable walking shoes, and sun protection. The Midwest\'s flat terrain amplifies wind in every season.' },
  { question: 'How cold does the Midwest get?', answer: 'Chicago averages -5°F wind chill days in January, with extremes hitting -30°F. Minneapolis is colder — the record low is -41°F. Even fall and spring (October, March) can deliver surprise snowstorms and 20°F nights. Pack for colder than you expect.' },
  { question: 'What power adapter do I need for the Midwest?', answer: 'No adapter needed — the Midwest uses standard US Type A/B plugs at 120V/60Hz. Everything works as-is.' },
  { question: 'What\'s the best time to visit the Midwest?', answer: 'Late spring (May–June) and early fall (September–October) offer the best balance of mild weather and events. Summer (July–August) is warm and festival-heavy. Winter is for those who embrace it — or those visiting for specific events like Chicago architecture week or Minneapolis\'s frozen waterfalls.' },
  { question: 'What should I pack for Chicago specifically?', answer: 'Chicago\'s lakefront wind is in a category of its own. A windproof outer layer is essential in any season below 60°F. Pack layers that can handle a 30°F temperature swing from morning to afternoon, comfortable walking shoes for the city grid, and a compact umbrella for sudden Lake Michigan weather changes.' },
  { question: 'What should I NOT bring to the Midwest?', answer: 'In winter: thin dress shoes (the soles freeze and crack), non-waterproof boots, and a single heavy coat instead of layers. In summer: over-packing for heat (Midwest summers are warm but rarely brutal). Year-round: a car-dependent mindset — Chicago, Minneapolis, and Detroit all have usable transit systems.' },
];

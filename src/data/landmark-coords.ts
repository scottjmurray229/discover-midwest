// Popular Midwest POI coordinates for itinerary geocoding.
// Keyed by lowercase normalized name. Used by generate-itinerary.ts to resolve activity coordinates.

export const LANDMARK_COORDS: Record<string, { lat: number; lng: number }> = {
  // Chicago
  'millennium park': { lat: 41.8827, lng: -87.6233 },
  'navy pier': { lat: 41.8917, lng: -87.6063 },
  'art institute of chicago': { lat: 41.8796, lng: -87.6237 },
  'willis tower': { lat: 41.8789, lng: -87.6359 },
  'wrigley field': { lat: 41.9484, lng: -87.6553 },
  'magnificent mile': { lat: 41.8949, lng: -87.6240 },
  // St. Louis
  'gateway arch': { lat: 38.6247, lng: -90.1848 },
  'forest park': { lat: 38.6359, lng: -90.2847 },
  // Kansas City
  'country club plaza': { lat: 39.0430, lng: -94.5927 },
  'bbq district': { lat: 39.0851, lng: -94.5874 },
  // Minneapolis
  'minnehaha falls': { lat: 44.9153, lng: -93.2110 },
  'mall of america': { lat: 44.8549, lng: -93.2422 },
  // Detroit
  'motown museum': { lat: 42.3641, lng: -83.0886 },
  'detroit institute of arts': { lat: 42.3594, lng: -83.0645 },
  // Cleveland
  'rock and roll hall of fame': { lat: 41.5085, lng: -81.6954 },
  // Indianapolis
  'indianapolis motor speedway': { lat: 39.7951, lng: -86.2353 },
  // Cincinnati
  'findlay market': { lat: 39.1153, lng: -84.5186 },
  // Milwaukee
  'milwaukee art museum': { lat: 43.0401, lng: -87.8972 },
  // Columbus
  'german village': { lat: 39.9444, lng: -82.9899 },
  // Omaha
  'henry doorly zoo': { lat: 41.2260, lng: -95.9287 },
  // Madison
  'state street': { lat: 43.0752, lng: -89.3959 },
  // Des Moines
  'pappajohn sculpture park': { lat: 41.5849, lng: -93.6316 },
};

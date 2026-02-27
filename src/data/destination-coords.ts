// Shared destination coordinates — single source of truth
// Used by plan page + companion app + generate-itinerary API.

export const DESTINATION_COORDS: Record<string, { lat: number; lng: number; label: string }> = {
  chicago: { lat: 41.8781, lng: -87.6298, label: 'Chicago' },
  'st-louis': { lat: 38.6270, lng: -90.1994, label: 'St. Louis' },
  'kansas-city': { lat: 39.0997, lng: -94.5786, label: 'Kansas City' },
  minneapolis: { lat: 44.9778, lng: -93.2650, label: 'Minneapolis' },
  milwaukee: { lat: 43.0389, lng: -87.9065, label: 'Milwaukee' },
  indianapolis: { lat: 39.7684, lng: -86.1581, label: 'Indianapolis' },
  cincinnati: { lat: 39.1031, lng: -84.5120, label: 'Cincinnati' },
  detroit: { lat: 42.3314, lng: -83.0458, label: 'Detroit' },
  cleveland: { lat: 41.4993, lng: -81.6944, label: 'Cleveland' },
  columbus: { lat: 39.9612, lng: -82.9988, label: 'Columbus' },
  omaha: { lat: 41.2565, lng: -95.9345, label: 'Omaha' },
  'des-moines': { lat: 41.5868, lng: -93.6250, label: 'Des Moines' },
  madison: { lat: 43.0731, lng: -89.4012, label: 'Madison' },
};

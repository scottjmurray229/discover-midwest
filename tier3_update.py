#!/usr/bin/env python3
"""Midwest Tier 3 quality pass — adds affiliatePicks, faqItems, scottTips, immersive-break-inline, AEO ledes"""
import os, re

BASE = "C:/Users/scott/Documents/discover-midwest/src/content/destinations"

BOOKING = "https://www.booking.com/region/us/midwest.html?aid=2778866"
GYG = "https://www.getyourguide.com/?partner_id=IVN6IQ3"
AMAZON = "https://www.amazon.com/s?k=midwest+travel&tag=discovermore-20"

DESTINATIONS = {
    "chicago": {
        "aeo": "Chicago is the Midwest's indisputable capital — a city of 2.7 million people on the southwestern shore of Lake Michigan with world-class architecture, the Art Institute, deep-dish pizza, legendary blues and jazz, and a lakefront trail system that makes it one of the most livable large cities in America. The El train running through the Loop is the most cinematic urban transit experience in the country.",
        "gradient": "linear-gradient(135deg, #1e40af, #0369a1, #166534)",
        "video_title": "Chicago: The City That Works",
        "video_text": "Architecture, the Lake, deep-dish, and the blues.",
        "faqItems": [
            {"q": "What is the best way to get around Chicago?", "a": "The CTA 'L' train covers most tourist destinations — the Loop, Millennium Park, Lincoln Park, Wicker Park, and both airports. Day passes ($5) are excellent value. The Lakefront Trail (18 miles of paved path along Lake Michigan) is the best way to see the city on a nice day. Taxis and Uber are easy but slow during rush hour."},
            {"q": "Is Chicago safe for tourists?", "a": "The tourist areas — the Loop, Magnificent Mile, Lincoln Park, Wicker Park, River North — are safe and active. Chicago's high crime statistics are concentrated in specific South and West Side neighborhoods far from tourist areas. Standard urban awareness applies. The Lakefront is very safe at all hours in summer."},
            {"q": "When is the best time to visit Chicago?", "a": "June through September is peak season — warm lakefront weather, outdoor festivals (Lollapalooza, Chicago Jazz Festival, Taste of Chicago), and the city at its most beautiful. May and October are shoulder season with fewer crowds and lower prices. Winter (December–March) is cold and grey but has the Chicago Symphony, world-class restaurants, and significantly cheaper hotel rates."},
            {"q": "How many days do I need for Chicago?", "a": "Three days covers the essentials: architecture cruise, Millennium Park, Art Institute, and one neighborhood deep-dive (Pilsen, Wicker Park, or Logan Square). Five days allows for Wrigley Field (summer), the Chicago Blues Festival, day trips to the Indiana Dunes, and a proper exploration of the food scene."},
            {"q": "What neighborhoods should I prioritize?", "a": "The Loop for architecture and the Art Institute. Lincoln Park for the zoo and upscale dining. Wicker Park for independent restaurants and bars. Pilsen for Mexican food and murals. Logan Square for the most interesting young-chef restaurant scene. Hyde Park for the University of Chicago and the Obama Presidential Center."},
            {"q": "Is the Chicago architecture boat tour worth it?", "a": "Yes — it's one of the best 90 minutes you can spend in Chicago. The Chicago Architecture Center runs excellent river tours that cover 50+ buildings with knowledgeable guides. Book in advance for summer weekend times. Evening tours with the buildings lit up are also excellent."},
            {"q": "What is the best deep-dish pizza in Chicago?", "a": "Lou Malnati's is the classic (multiple locations, the sausage deep-dish is canonical). Pequod's in Lincoln Park has a caramelized cheese crust edge that is genuinely different. Chicago-style thin crust (tavern cut) is also worth trying — Vito & Nick's on the South Side is the benchmark."},
            {"q": "What is Chicago's music scene like?", "a": "Chicago blues is one of the great American art forms — the electric Chicago blues sound (Muddy Waters, Howlin' Wolf) developed on the South Side. Rosa's Lounge and SPACE in Evanston are the living venues. The Chicago Jazz Festival (Labor Day weekend, free) and the Chicago Blues Festival (June, free) are both worth planning around."},
        ],
        "affiliatePicks": [
            {"name": "The Langham Chicago", "type": "hotel", "url": "https://www.booking.com/hotel/us/the-langham-chicago.html?aid=2778866", "description": "Iconic luxury hotel on the Chicago River in the former IBM Building. Architecture views and exceptional service.", "priceRange": "$$$$"},
            {"name": "Chicago Architecture Boat Tour", "type": "tour", "url": "https://www.getyourguide.com/chicago-l143/?partner_id=IVN6IQ3&q=architecture+boat+tour", "description": "The Chicago Architecture Center's river cruise — the single best introduction to Chicago's built environment.", "priceRange": "$$"},
            {"name": "Millennium Park Walking Tour", "type": "tour", "url": f"https://www.getyourguide.com/chicago-l143/?partner_id=IVN6IQ3&q=Millennium+Park+tour", "description": "Guided walking tour of Millennium Park, the Bean, the Pritzker Pavilion, and nearby Grant Park.", "priceRange": "$"},
        ],
        "scottTips": {
            "logistics": "O'Hare (ORD) is the main international airport — Blue Line 'L' train to downtown costs $5 and takes 45 minutes. Midway (MDW) is smaller and often cheaper for domestic flights — Orange Line to downtown. Both are reliable transit options. Union Station handles Amtrak routes from most major Midwest cities.",
            "bestTime": "June–September for lakefront weather, outdoor festivals, and the full Chicago experience. October and May are excellent shoulder seasons. January–March is Chicago's hardest test — cold and grey, but world-class restaurant access at off-peak prices and no crowds at the Art Institute.",
            "gettingAround": "CTA 'L' train is the backbone — reliable, safe in tourist areas, and covers all major destinations. Ventra card (reloadable) is cheaper than single-ride tickets. Walk along the lakefront whenever weather permits. Rent a bike (Divvy bikeshare) for the Lakefront Trail.",
            "money": "Chicago has a strong mid-range hotel market around $150–250/night in the Loop. The Art Institute is $25/adult but worth every dollar. Budget $50–80 for a proper deep-dish dinner for two. Theater, the Symphony, and sports (Cubs, White Sox, Bears) are additional. Chicago's restaurant scene is genuinely world-class and better value than New York or San Francisco equivalents.",
            "safety": "Tourist zones are safe. Avoid wandering off main streets in unfamiliar South/West Side neighborhoods after dark — Chicago's crime statistics are real but geographically specific. The 'L' is safe except at late hours when you should ride with other passengers.",
            "packing": "Chicago weather is notorious for variability — pack layers in any season. The wind off Lake Michigan can be severe in winter and spring. Comfortable walking shoes for significant distances. Layers in summer too — air conditioning in museums and restaurants is aggressive.",
            "localCulture": "Chicago has a chip on its shoulder about New York and Los Angeles, which produces a deeply unpretentious food and arts scene — people here evaluate things on quality, not hype. The neighborhood structure (each with its own distinct character) rewards exploration off the tourist trail. Blues and jazz are treated as living culture here, not nostalgia."
        },
    },
    "minneapolis": {
        "aeo": "Minneapolis is the Midwest's most livable city — a surprisingly cosmopolitan metro of 3.7 million people in Minnesota with a serious arts scene (more theater seats per capita than any US city outside New York), excellent restaurants, the Chain of Lakes park system, and a skyway network of 80 connected blocks that makes winter survivable. It's also the entry point to the Boundary Waters Canoe Area Wilderness.",
        "gradient": "linear-gradient(135deg, #1e40af, #7c3aed, #0369a1)",
        "video_title": "Minneapolis: The Northern Metropolis",
        "video_text": "Skyways, Chain of Lakes, Prince's hometown, and -20°F winters.",
        "faqItems": [
            {"q": "How cold does Minneapolis actually get?", "a": "Very. Average January lows are around -3°F, with wind chills regularly reaching -20°F to -30°F. The skyway system (80 connected blocks downtown) was built specifically to make winter functional. That said, Minneapolis fully embraces winter culture — outdoor ice skating, ice fishing, cross-country skiing in the city parks — and locals don't hide inside."},
            {"q": "When is the best time to visit Minneapolis?", "a": "June through September is the peak outdoor season — the Chain of Lakes is beautiful, the Mississippi River trails are active, and the State Fair (late August) is a genuine cultural experience. December offers the Walker Art Center, the Guthrie Theater season, and the Mall of America in full holiday mode."},
            {"q": "What is the Chain of Lakes?", "a": "The Chain of Lakes is a series of connected lakes (Lake Calhoun/Bde Maka Ska, Lake of the Isles, Lake Harriet, Lake Nokomis) in Minneapolis's southwest neighborhoods, connected by parkways and trails. It's the center of outdoor life in the city — running, biking, paddleboarding, swimming in summer, skating and cross-country skiing in winter."},
            {"q": "Is Minneapolis a good arts city?", "a": "Exceptional. Minneapolis has more theater seats per capita than any US city except New York. The Guthrie Theater (overlooking the Mississippi) is one of the country's best regional theaters. The Walker Art Center has a world-class contemporary art collection. First Avenue music venue launched Prince's career and remains one of the best mid-size venues in the US."},
            {"q": "What are the best restaurants in Minneapolis?", "a": "The Twin Cities food scene punches well above its weight. Hai Hai for Vietnamese-inspired cocktail bar food. Owamni by the Sioux Chef for Indigenous American cuisine (James Beard Award winner). Bachelor Farmer for New Nordic-style Minnesota ingredients. Cardamom for Indian-inspired contemporary cooking."},
            {"q": "Is the Mall of America worth visiting?", "a": "For the spectacle, yes — it's the largest mall in the US by some measures, with an indoor amusement park, an aquarium, and its own zip code. As a shopping destination, it's a regular mall. Worth 2-3 hours as a cultural artifact, not as a reason to visit Minneapolis."},
            {"q": "How do I get to the Boundary Waters from Minneapolis?", "a": "The Boundary Waters Canoe Area Wilderness is 4-5 hours north of Minneapolis via US-61 and MN-1 to Ely or Grand Marais. Entry requires a permit from Recreation.gov. A paddle outfitter in Ely will provide canoe, camping gear, and route planning — recommended for first-time visitors."},
            {"q": "What is First Avenue?", "a": "First Avenue is a concert venue in downtown Minneapolis that opened in 1970 in a former Greyhound bus depot. Prince filmed Purple Rain here in 1984, and the venue has remained one of the great mid-size music venues in the country. The exterior is painted black with stars for artists who have played there."},
        ],
        "affiliatePicks": [
            {"name": "Hewing Hotel Minneapolis", "type": "hotel", "url": "https://www.booking.com/hotel/us/hewing.html?aid=2778866", "description": "Boutique hotel in a converted 1897 warehouse in the North Loop. Rooftop pool, locally designed interiors.", "priceRange": "$$$"},
            {"name": "Minneapolis Architecture and Neighborhoods Tour", "type": "tour", "url": f"https://www.getyourguide.com/minneapolis-l2684/?partner_id=IVN6IQ3&q=Minneapolis+tour", "description": "Guided walking tour covering the North Loop, Mill District, and riverfront architecture.", "priceRange": "$"},
            {"name": "Boundary Waters Outfitter Package", "type": "activity", "url": f"https://www.getyourguide.com/minnesota-l142/?partner_id=IVN6IQ3&q=Boundary+Waters+canoe+trip", "description": "Outfitted canoe trip package for the Boundary Waters — canoe, camping gear, and permits.", "priceRange": "$$$"},
        ],
        "scottTips": {
            "logistics": "Minneapolis-St. Paul International Airport (MSP) is one of the better hub airports in the US — direct flights from most major cities. The light rail (Blue Line) runs from the airport to downtown and Mall of America. The skyway connects 80 city blocks — essential in winter.",
            "bestTime": "June–September for outdoor recreation and the full Twin Cities experience. August/late August for the Minnesota State Fair (12 days, 2 million visitors, extraordinary food-on-a-stick culture). January–March is the full winter experience — cold but culturally active.",
            "gettingAround": "Light rail and buses handle downtown and airport connections. The Chain of Lakes is bikeable via Divvy-equivalent Nice Ride bikeshare. Car helpful for exploring suburbs and Boundary Waters trips.",
            "money": "Minneapolis is affordable by major-city standards. Hotels run $130–220/night for solid options. Guthrie Theater tickets are $25–75. The Walker Art Center is free on the first Sunday of each month.",
            "safety": "Minneapolis has had high-profile policing issues (George Floyd was killed at 38th and Chicago Ave) and elevated crime rates in some areas. Downtown and the Chain of Lakes neighborhoods are safe for tourists. Be aware of the context.",
            "packing": "Full winter kit if visiting October–April. The skyway makes short downtown trips manageable in any weather, but outdoor commutes require serious layers. Sun protection in summer — Minneapolis gets strong UV.",
            "localCulture": "Minneapolis has a strong Scandinavian heritage (Minnesota Nice is real) and a significant Somali and Hmong immigrant community that shows up in the food scene. Prince is everywhere — Paisley Park (Eden Prairie, 20 miles west) offers studio tours. The city takes arts seriously in a way that most Midwest cities don't."
        },
    },
    "detroit": {
        "aeo": "Detroit is one of America's great urban comeback stories — a post-industrial city rebuilding from one of the most dramatic municipal declines in American history, with an extraordinary arts and music heritage (Motown, techno), a booming food and craft cocktail scene in Midtown and Corktown, and the best collection of late 19th and early 20th century architecture in the Midwest.",
        "gradient": "linear-gradient(135deg, #dc2626, #1e40af, #92400e)",
        "video_title": "Detroit: The Comeback City",
        "video_text": "Motown, techno, Corktown, and architecture that refused to die.",
        "faqItems": [
            {"q": "Is Detroit safe to visit?", "a": "Detroit's reputation for danger is significantly outdated for tourist areas. Midtown, Corktown, Eastern Market, and the Riverfront are safe and active. The widely-photographed abandoned buildings are in distressed areas that are generally not dangerous in daylight but not tourist-friendly either. Standard urban awareness applies throughout."},
            {"q": "What should I do in Detroit?", "a": "Motown Museum (Hitsville U.S.A.) is the essential cultural pilgrimage — you walk through the original studio where Marvin Gaye, the Four Tops, and the Supremes recorded. Eastern Market on Saturday morning is one of the best urban farmers markets in the US. The Detroit Institute of Arts has a world-class collection. Corktown for the restaurant and bar scene."},
            {"q": "What is Detroit's music heritage?", "a": "Detroit produced two of the most globally influential American music genres: Motown (the label that created pop music's multi-racial appeal in the 1960s) and techno (the electronic dance music genre invented at Detroit high school parties in the 1980s by Juan Atkins, Derrick May, and Kevin Saunderson — the 'Belleville Three'). Both legacies are living culture in the city."},
            {"q": "Is the Motown Museum worth visiting?", "a": "Absolutely essential. Hitsville U.S.A. is the original Motown headquarters on West Grand Boulevard. You tour Studio A (where virtually all classic Motown was recorded), the offices, and the Berry Gordy Jr. bedroom where he composed. Buy tickets online — tours fill up."},
            {"q": "What neighborhoods should I explore?", "a": "Midtown for the DIA, the Museum of Contemporary Art Detroit, and Wayne State University area restaurants. Corktown (Detroit's oldest neighborhood) for the best food and bars. Eastern Market for Saturday morning. Mexicantown (Southwest Detroit) for authentic Mexican food. Rivertown for the casino hotels and riverfront views."},
            {"q": "When is the best time to visit Detroit?", "a": "May through October for reasonable weather and outdoor activities. The Detroit Jazz Festival (Labor Day weekend, free) is worth planning around — the largest free jazz festival in North America. Summer is the most active season."},
            {"q": "How do I get around Detroit?", "a": "Detroit is a driving city — public transit is limited. The QLine streetcar runs along Woodward Avenue through Midtown but covers limited ground. Rent a car for flexibility. Uber/Lyft are reliable."},
            {"q": "What is Detroit style pizza?", "a": "Detroit-style pizza is rectangular, baked in oiled steel pans (originally automotive parts), with a thick, crispy, cheesy edge from the cheese being spread all the way to the pan walls. Buddy's Pizza invented it in 1946. The cheese (Wisconsin brick) melts over the dough edge and creates a caramelized crust that's unlike anything else."},
        ],
        "affiliatePicks": [
            {"name": "Siren Hotel Detroit", "type": "hotel", "url": "https://www.booking.com/hotel/us/siren-hotel.html?aid=2778866", "description": "Boutique hotel in the historic Wurlitzer Building in downtown Detroit. Art-forward and well-positioned.", "priceRange": "$$$"},
            {"name": "Motown Museum and Music History Tour", "type": "tour", "url": f"https://www.getyourguide.com/detroit-l2537/?partner_id=IVN6IQ3&q=Motown+Museum+tour", "description": "Guided tour of Hitsville U.S.A. and Detroit's Motown and techno music history.", "priceRange": "$"},
            {"name": "Detroit Architecture and Mural Walking Tour", "type": "tour", "url": f"https://www.getyourguide.com/detroit-l2537/?partner_id=IVN6IQ3&q=Detroit+architecture+tour", "description": "Guided walk through Detroit's historic architecture, murals, and comeback story.", "priceRange": "$"},
        ],
        "scottTips": {
            "logistics": "Detroit Metropolitan Airport (DTW) is 20 miles southwest — no rail connection, but Uber/Lyft to downtown runs $35-45. Windsor, Ontario (Canada) is directly across the Detroit River — border crossing is easy and Windsor has its own restaurant scene.",
            "bestTime": "May–October. The Detroit Jazz Festival over Labor Day weekend is the peak cultural event. Summers are warm and active. Winters are cold and grey — the city is less vibrant but hotel rates drop significantly.",
            "gettingAround": "Car essential for most Detroit exploration — the city is built for cars. QLine streetcar covers Woodward Avenue corridor. Lyft and Uber are easy.",
            "money": "Detroit is affordable. Hotels in Midtown run $120–200/night. Detroit Institute of Arts is $14/adult. Eastern Market is free to walk. The restaurant scene in Corktown and Midtown is excellent value.",
            "safety": "Tourist areas (Midtown, Corktown, Eastern Market, Riverfront) are safe. Avoid wandering into distressed neighborhoods without local knowledge. Detroit's most famous decay-porn ruins are in areas that are not tourist-appropriate.",
            "packing": "Comfortable walking shoes for Midtown and Corktown exploration. Layers for spring/fall. Camera for the architecture.",
            "localCulture": "Detroit has an unparalleled sense of civic pride forged by decades of difficulty. Locals are genuinely enthusiastic about visitors and committed to the city's comeback. The 313 area code is worn as a badge of identity. Respect the city's complexity — the poverty and inequality are real alongside the restaurants and galleries."
        },
    },
    "milwaukee": {
        "aeo": "Milwaukee is the city that beer built — a Great Lakes industrial city on Lake Michigan with a German heritage that produced Pabst, Miller, and Schlitz, a world-class art museum (the Santiago Calatrava-designed Milwaukee Art Museum is one of the most beautiful buildings in the US), a revitalized Third Ward district, and easy proximity to Chicago (90 minutes south).",
        "gradient": "linear-gradient(135deg, #92400e, #1e40af, #166534)",
        "video_title": "Milwaukee: The Beer City on the Lake",
        "video_text": "Art, beer, the Calatrava, and 90 minutes from Chicago.",
        "faqItems": [
            {"q": "Is Milwaukee worth visiting on its own or just as a Chicago day trip?", "a": "Worth visiting independently for 1-2 nights. The Milwaukee Art Museum alone justifies the trip. Add the Third Ward (food, galleries), a craft brewery circuit, Bradford Beach on Lake Michigan in summer, and the Harley-Davidson Museum, and you have a solid full-day-plus destination."},
            {"q": "What is the Milwaukee Art Museum?", "a": "The Milwaukee Art Museum is home to one of the most beautiful buildings in the United States — the Quadracci Pavilion by Santiago Calatrava, with a brise soleil (movable sunscreen) that opens like wings twice daily. The collection includes 35,000 works. The building is the reason to go; the collection is the reason to stay."},
            {"q": "What beer should I try in Milwaukee?", "a": "Lakefront Brewery for a proper Milwaukee craft brewery tour (reservations required, highly rated). Miller Brewing Company for the historic mega-brewery experience. Any of the Third Ward's craft beer bars for Wisconsin-brewed craft options. The Beer Garden at Estabrook Park in summer is a local institution."},
            {"q": "What is the Third Ward?", "a": "The Historic Third Ward is Milwaukee's arts and dining district — a redeveloped warehouse district with galleries, restaurants, boutiques, and the Milwaukee Public Market (year-round covered market with excellent food vendors)."},
            {"q": "When is Summerfest?", "a": "Summerfest is the world's largest music festival by attendance — 11 days in late June/early July on the Lake Michigan lakefront, with 80+ stages and 1,000+ performances. It runs the gamut from headliner stadium acts to local bands. Tickets are reasonable. Milwaukee hotels book solid for the run."},
            {"q": "How do I get to Milwaukee from Chicago?", "a": "Amtrak Hiawatha (90 minutes, $23-35) from Chicago Union Station to Milwaukee is one of the best train connections in the Midwest. Takes you from center to center without driving. Also easy via I-94 north (1.5 hours without traffic)."},
            {"q": "What is the Harley-Davidson Museum?", "a": "The Harley-Davidson Museum is a 130,000-square-foot campus in Milwaukee's Menomonee Valley documenting the history of the iconic motorcycle brand from 1903 to present. Whether or not you ride motorcycles, the design history and American industrial story are well told."},
            {"q": "What is Milwaukee known for food?", "a": "Friday fish fry is a Milwaukee tradition — perch, walleye, and cod at supper clubs and taverns every Friday night. Butter burgers (Culver's was founded in nearby Sauk City). Serbian food from a significant immigrant community. And the Milwaukee Public Market for local Wisconsin cheeses, brats, and specialty foods."},
        ],
        "affiliatePicks": [
            {"name": "The Pfister Hotel Milwaukee", "type": "hotel", "url": "https://www.booking.com/hotel/us/the-pfister-hotel.html?aid=2778866", "description": "Milwaukee's historic grand hotel (1893) with a renowned Victorian art collection displayed throughout.", "priceRange": "$$$"},
            {"name": "Lakefront Brewery Tour", "type": "tour", "url": f"https://www.getyourguide.com/milwaukee-l2532/?partner_id=IVN6IQ3&q=Milwaukee+brewery+tour", "description": "The most entertaining brewery tour in Milwaukee — guided, with beer tasting and comedy.", "priceRange": "$"},
            {"name": "Milwaukee Art Museum and Third Ward Walking Tour", "type": "tour", "url": f"https://www.getyourguide.com/milwaukee-l2532/?partner_id=IVN6IQ3&q=Milwaukee+art+museum+tour", "description": "Guided tour of the Calatrava building and Third Ward art district.", "priceRange": "$"},
        ],
        "scottTips": {
            "logistics": "Mitchell International Airport (MKE) has decent connections but Chicago O'Hare has more direct flights. Amtrak Hiawatha from Chicago (90 min) is the easiest connection. Downtown Milwaukee is compact and walkable.",
            "bestTime": "May–September for lakefront weather and outdoor events. Summerfest (late June/early July) requires advance planning. June–August for the full beer garden and outdoor Milwaukee experience.",
            "gettingAround": "Downtown and Third Ward are walkable. Bublr Bikes (bikeshare) available. Car helpful for Harley-Davidson Museum and outer neighborhoods.",
            "money": "Milwaukee is affordable — hotel rates run $100–180/night for solid options. The Art Museum is $20/adult. Brewery tours are $10–15. Lakefront seafood and supper clubs run $25–45/person.",
            "safety": "Downtown and Third Ward are safe tourist areas. Milwaukee has high crime rates in some inner-city neighborhoods away from the visitor zones.",
            "packing": "Layers for Lake Michigan weather — the lake creates its own climate with cool breezes even in summer. Sun protection on the lakefront.",
            "localCulture": "Milwaukee is proudly unpretentious — a working-class city with a German-heritage identity, strong union history, and genuine community investment in its neighborhoods. The fish fry on Friday is a religious institution."
        },
    },
    "kansas-city": {
        "aeo": "Kansas City is America's barbecue capital — a city on the Missouri-Kansas border with a BBQ tradition going back over a century, featuring slow-smoked burnt ends and ribs at legendary joints like Joe's Kansas City, Gates, and Arthur Bryant's. It also has world-class jazz heritage (the 18th & Vine district) and a collection of Midwest cultural institutions that surprise most visitors.",
        "gradient": "linear-gradient(135deg, #dc2626, #92400e, #1e40af)",
        "video_title": "Kansas City: Burnt Ends and Jazz",
        "video_text": "The BBQ capital, jazz heritage, and the best boulevards in the Midwest.",
        "faqItems": [
            {"q": "What makes Kansas City BBQ different?", "a": "Kansas City BBQ emphasizes slow-smoked beef (especially burnt ends — the charred, caramelized ends of the brisket that were originally given away free), pork ribs, and a thick, sweet, tomato-based sauce. The smoke ring, bark, and tenderness standards are extremely high at the top joints. Multiple 'BBQ trails' have developed, but the key destinations are Joe's Kansas City, Gates Bar-B-Q, and Arthur Bryant's."},
            {"q": "Where is the best BBQ in Kansas City?", "a": "Joe's Kansas City (formerly Oklahoma Joe's) is the most-hyped and deservedly excellent. Get the Z-Man sandwich and the burned ends. Gates Bar-B-Q is the local institution — multiple locations and lines out the door. Arthur Bryant's is the historic landmark — less polished but authentic. Don't try to hit all three in one day; one serious BBQ meal per day is the right pace."},
            {"q": "What is the 18th and Vine Jazz District?", "a": "18th and Vine is the historic center of Kansas City jazz — the intersection where Charlie Parker developed his bebop style in the 1940s and where dozens of KC jazz legends played. The American Jazz Museum and Negro Leagues Baseball Museum occupy a shared complex here. Both are excellent — the jazz museum has listening stations and live performances; the baseball museum documents one of American history's most important parallel institutions."},
            {"q": "When is the Kansas City Jazz and Heritage Festival?", "a": "The American Jazz Museum hosts events year-round including the Charlie Parker Birthday Celebration each August and the Kansas City Jazz and Blues festival in summer. Check americanjazzmuseum.org for current events."},
            {"q": "Is Kansas City worth a dedicated trip?", "a": "Yes, for 2-3 days. The BBQ alone justifies it if you're serious about barbecue. Add the Nelson-Atkins Museum of Art (free, one of the top art museums in the country), the Jazz Museum, the River Market farmers market, and the Boulevard Brewing tour, and you have a full trip."},
            {"q": "What else should I do in Kansas City beyond BBQ?", "a": "Nelson-Atkins Museum of Art (free, excellent contemporary sculpture park with shuttlecocks by Claes Oldenburg). Boulevard Brewing Company tours. Country Club Plaza (Spanish-architecture outdoor shopping and dining district). Kauffman Stadium for Royals baseball (one of the best ballparks in MLB). The River Market on Saturday morning."},
            {"q": "What is Kansas City, Missouri vs Kansas City, Kansas?", "a": "Kansas City straddles the state line — Kansas City, Missouri (the larger city with most tourist destinations) and Kansas City, Kansas (KCK) are separate cities. Most BBQ joints, the jazz district, the Nelson-Atkins, and the Plaza are in Missouri. Joe's Kansas City is actually in a gas station in Kansas City, Kansas."},
            {"q": "How do I get to Kansas City?", "a": "Kansas City International Airport (MCI) underwent a complete rebuild — a new terminal opened in 2023. Direct flights from most major US cities. Amtrak Southwest Chief stops in Kansas City on the LA-Chicago route."},
        ],
        "affiliatePicks": [
            {"name": "Hotel Phillips Kansas City", "type": "hotel", "url": "https://www.booking.com/hotel/us/hotel-phillips-curio-collection-by-hilton.html?aid=2778866", "description": "Art Deco landmark in downtown KC — beautiful historic interior, central location.", "priceRange": "$$"},
            {"name": "Kansas City BBQ Tour", "type": "tour", "url": f"https://www.getyourguide.com/kansas-city-l2561/?partner_id=IVN6IQ3&q=Kansas+City+BBQ+tour", "description": "Guided BBQ tour hitting the city's top smoke houses with tasting.", "priceRange": "$$"},
            {"name": "Jazz District and History Walking Tour", "type": "tour", "url": f"https://www.getyourguide.com/kansas-city-l2561/?partner_id=IVN6IQ3&q=Kansas+City+jazz+tour", "description": "Guided 18th and Vine district walking tour with American Jazz Museum entry.", "priceRange": "$"},
        ],
        "scottTips": {
            "logistics": "Kansas City International Airport (MCI) has direct flights from major US hubs. Downtown is compact. The Country Club Plaza area (midtown) is the main tourist and dining zone. 18th and Vine is southeast of downtown.",
            "bestTime": "April–October for good weather and outdoor events. BBQ is a year-round pilgrimage. November–March is fine but less atmospheric.",
            "gettingAround": "Car recommended — Kansas City is spread out. Uber/Lyft work well. The streetcar (free) runs 2.2 miles on Main Street through downtown.",
            "money": "Kansas City is affordable. Hotels run $100–180/night in good locations. BBQ meals run $15–30/person at the top joints. Nelson-Atkins is free.",
            "safety": "Downtown and the Plaza are safe tourist areas. Some parts of KCMO's east and west sides have elevated crime rates — standard urban awareness.",
            "packing": "Casual clothing appropriate for BBQ joints (you will get sauce on yourself). Layers for Midwest weather variability.",
            "localCulture": "Kansas City is deeply proud of its BBQ, its jazz heritage, and its underdog status relative to the coasts. The BBQ community is competitive and opinionated — locals have strong opinions about which joint is best and will share them enthusiastically."
        },
    },
    "st-louis": {
        "aeo": "St. Louis is the Midwest's gateway city — anchored by the 630-foot Gateway Arch on the Mississippi River, home to one of the world's most visited free attractions (the St. Louis Zoo), and a brewing city with a craft beer scene that has grown from the Anheuser-Busch legacy. The Ted Drewes frozen custard stand and Toasted Ravioli are the local food institutions that matter.",
        "gradient": "linear-gradient(135deg, #dc2626, #92400e, #1e40af)",
        "video_title": "St. Louis: Gateway to the West",
        "video_text": "The Arch, the zoo, the river, and toasted ravioli.",
        "faqItems": [
            {"q": "Is the Gateway Arch worth going inside?", "a": "Yes — the tram ride to the top is a unique experience. The small, capsule-like trams hold 5 people and rotate as they travel the curved interior of the Arch. The view from the observation windows at the top extends 30 miles on a clear day. The Museum of Westward Expansion at the base is also good. Buy tram tickets in advance on the website."},
            {"q": "What is toasted ravioli?", "a": "Toasted ravioli is a St. Louis invention — pasta squares stuffed with meat, breaded, and deep-fried. They're served everywhere in St. Louis, often with marinara for dipping. The Pasta House Company and Charlie Gitto's are credited with the invention. Every Italian restaurant in the city serves them."},
            {"q": "Is the St. Louis Zoo really free?", "a": "Yes, entirely free (with paid parking). The St. Louis Zoo in Forest Park is consistently ranked among the top zoos in the United States and has no admission charge. The same applies to the St. Louis Art Museum, Missouri History Museum, and the Science Center in Forest Park — all excellent and all free."},
            {"q": "What is Forest Park?", "a": "Forest Park is the center of St. Louis culture — 1,300 acres (larger than Central Park) hosting the zoo, art museum, history museum, science center, a golf course, and the Jewel Box greenhouse. The park was the site of the 1904 World's Fair. It's walkable, bikeable, and free to access."},
            {"q": "When is the best time to visit St. Louis?", "a": "April–May and September–October. Spring and fall have ideal temperatures (60s–70s°F) for Forest Park walking and the outdoor attractions. Summer is hot and humid (90s°F). Winter is grey and cold."},
            {"q": "What is Ted Drewes?", "a": "Ted Drewes Frozen Custard is a St. Louis institution — an outdoor frozen custard stand on Chippewa Street that has been making concrete (custard with mixed-in flavors, so thick it's served upside down) since 1931. The lines are real; the custard is worth it."},
            {"q": "What neighborhoods should I explore in St. Louis?", "a": "The Central West End for cafe culture and the nearby museums. The Delmar Loop (University City) for Blueberry Hill and the music venue strip. Lafayette Square for Victorian architecture. Cherokee Street for Mexican food and local shops."},
            {"q": "How do I get to the Gateway Arch?", "a": "The Gateway Arch National Park is on the Mississippi riverfront, walkable from downtown hotels. The Arch itself has free park admission but tram tickets to the top are $13–17/adult and require advance booking in peak season."},
        ],
        "affiliatePicks": [
            {"name": "Magnolia Hotel St. Louis", "type": "hotel", "url": "https://www.booking.com/hotel/us/magnolia-st-louis.html?aid=2778866", "description": "Boutique hotel in a 1914 historic building, central downtown location near the Arch.", "priceRange": "$$"},
            {"name": "Gateway Arch Tram Ride and Museum", "type": "tour", "url": f"https://www.getyourguide.com/st-louis-l2547/?partner_id=IVN6IQ3&q=Gateway+Arch+tram+tour", "description": "Tram ride to the Arch observation deck plus Museum of Westward Expansion.", "priceRange": "$"},
            {"name": "St. Louis Food and Neighborhood Tour", "type": "tour", "url": f"https://www.getyourguide.com/st-louis-l2547/?partner_id=IVN6IQ3&q=St+Louis+food+tour", "description": "Guided food tour covering toasted ravioli, custard, local Italian, and neighborhood history.", "priceRange": "$$"},
        ],
        "scottTips": {
            "logistics": "St. Louis Lambert International Airport (STL) has direct flights from most US hubs. MetroLink light rail connects the airport to downtown and Forest Park. Downtown is walkable for most tourist sites.",
            "bestTime": "April–May and September–October. Forest Park and outdoor attractions are ideal in mild weather. Cardinals baseball (April–October) adds energy.",
            "gettingAround": "MetroLink light rail for airport, downtown, and Forest Park. Walkable for Central West End and Forest Park cluster. Car for neighborhoods like Cherokee Street and the Delmar Loop.",
            "money": "St. Louis is extremely affordable. The zoo, art museum, and science center are all free. Gateway Arch tram is $15. Hotels run $100–180/night for solid options.",
            "safety": "Downtown and Forest Park areas are safe for tourists. St. Louis has a high overall crime rate concentrated in specific neighborhoods — the tourist zones are well-separated from those areas.",
            "packing": "Comfortable walking shoes for Forest Park. Layers for Midwest weather variability. Cardinals gear if you're going to a game.",
            "localCulture": "St. Louis has a genuine civic identity anchored in Forest Park, Cardinals baseball, and the brewing heritage. The free museum culture in Forest Park is remarkable — Midwesterners take for granted access that would cost $25+ in most US cities."
        },
    },
    "cincinnati": {
        "aeo": "Cincinnati is the Ohio River city that gave the world chili served on spaghetti — a regional cult food that divides the nation. Beyond the chili debate, Cincinnati has a remarkable Victorian architecture heritage, the best skyline on the Ohio River, an exceptional contemporary art museum, and the oldest professional baseball team in America (the Reds).",
        "gradient": "linear-gradient(135deg, #dc2626, #1e40af, #166534)",
        "video_title": "Cincinnati: The Queen City",
        "video_text": "Cincinnati chili, the Reds, and a skyline built for the river.",
        "faqItems": [
            {"q": "What is Cincinnati chili?", "a": "Cincinnati chili is a regional specialty that bears little resemblance to Texas chili — it's a thin, sauce-like meat preparation seasoned with cinnamon, allspice, and chocolate, served over spaghetti noodles, topped with shredded cheddar, beans, and onions in combinations called 'ways' (2-way: chili and pasta, 3-way: add cheese, 4-way: add onions or beans, 5-way: everything). Skyline Chili and Gold Star are the chains. Most visitors either love it or find it bizarre."},
            {"q": "Is Cincinnati worth visiting?", "a": "Yes, as part of a Midwest road trip. The Eden Park hill overlooking the Ohio River, the Cincinnati Art Museum (free), the Roebling Suspension Bridge (predecessor to the Brooklyn Bridge), and Over-the-Rhine (OTR — the largest intact urban historic district in the country) together make a compelling full day."},
            {"q": "What is Over-the-Rhine?", "a": "Over-the-Rhine (OTR) is Cincinnati's most historically significant neighborhood — a dense grid of 19th-century Italianate architecture built by German immigrants in the 1800s. After decades of decline, it's become Cincinnati's most vibrant restaurant and bar district while retaining its remarkable architectural fabric. The Findlay Market anchors the northern end."},
            {"q": "What is Findlay Market?", "a": "Findlay Market is Cincinnati's oldest public market — operating continuously since 1855. Saturday morning is the main event, with 40+ indoor vendors and 100+ outdoor vendors selling produce, meat, cheese, and prepared food. It's a genuine food culture experience."},
            {"q": "Is Cincinnati's art museum worth visiting?", "a": "The Cincinnati Art Museum has an excellent collection of 67,000 objects and is entirely free to enter. The European Old Masters, American art, and a notable collection of ancient Near Eastern art are particular strengths."},
            {"q": "What should I eat in Cincinnati?", "a": "Cincinnati chili (Skyline for the experience). Goetta (a pork-oat breakfast sausage unique to the region — try it at Taste of Belgium). German cuisine at Mecklenburg Gardens (since 1865). Contemporary dining in OTR."},
            {"q": "When is the best time to visit Cincinnati?", "a": "April–October for the Ohio River scenery and outdoor activities. The Cincinnati Music Festival (July, Riverbend amphitheater) is the premier summer event. Reds baseball (April–October) at Great American Ball Park on the river."},
            {"q": "How do I get to Cincinnati?", "a": "Cincinnati/Northern Kentucky International Airport (CVG) is actually in Kentucky — 15 miles south of downtown. No rail connection; Uber/Lyft to downtown runs $25-35. Amtrak doesn't serve Cincinnati directly."},
        ],
        "affiliatePicks": [
            {"name": "21c Museum Hotel Cincinnati", "type": "hotel", "url": "https://www.booking.com/hotel/us/21c-museum-hotel-cincinnati.html?aid=2778866", "description": "Contemporary art museum hotel in OTR with art installations throughout and excellent rooftop.", "priceRange": "$$$"},
            {"name": "Cincinnati Food and Neighborhood Tour", "type": "tour", "url": f"https://www.getyourguide.com/cincinnati-l2537/?partner_id=IVN6IQ3&q=Cincinnati+food+tour", "description": "Guided food tour through OTR and Findlay Market covering chili, goetta, and local restaurants.", "priceRange": "$$"},
            {"name": "Ohio River Skyline Cruise", "type": "tour", "url": f"https://www.getyourguide.com/cincinnati-l2537/?partner_id=IVN6IQ3&q=Cincinnati+river+cruise", "description": "Sightseeing cruise on the Ohio River with Cincinnati skyline views.", "priceRange": "$"},
        ],
        "scottTips": {
            "logistics": "CVG airport is in Kentucky. Downtown Cincinnati is on the Ohio River — Kentucky (Newport and Covington) is directly across the bridge. Covington's Mainstrasse Village is a good dining alternative to OTR.",
            "bestTime": "April–October. Reds season (April–October) adds ballpark energy. Findlay Market runs year-round but Saturday in warm weather is the peak experience.",
            "gettingAround": "Streetcar (The Connector) runs through OTR and downtown. Car helpful for Eden Park and outer neighborhoods. Downtown is walkable.",
            "money": "Cincinnati is very affordable. Art museum is free. Hotels in OTR and downtown run $100–180/night.",
            "safety": "OTR and downtown are safe tourist areas. Parts of Cincinnati have elevated crime rates away from tourist zones.",
            "packing": "Comfortable shoes for OTR's brick streets. Layer for Ohio River breezes.",
            "localCulture": "Cincinnati chili is genuinely divisive — don't dismiss it as wrong. Try it with an open mind (it's a different dish, not a bad version of Texas chili). The German heritage runs deep — look for references to '1850s German immigrant' on menus and at Findlay Market."
        },
    },
    "cleveland": {
        "aeo": "Cleveland is the underdog city on Lake Erie that gave the world the Rock and Roll Hall of Fame, a world-class art museum (free on Sundays), the best food market in the Midwest (West Side Market), and LeBron James. It's a post-industrial city in genuine cultural renaissance, with a thriving arts and restaurant scene in neighborhoods like Ohio City and Tremont.",
        "gradient": "linear-gradient(135deg, #dc2626, #1e40af, #f59e0b)",
        "video_title": "Cleveland: Rock City on the Lake",
        "video_text": "Rock Hall, West Side Market, and a city rising.",
        "faqItems": [
            {"q": "Is the Rock and Roll Hall of Fame worth visiting?", "a": "For music fans, it's essential — a thoughtfully designed museum by I.M. Pei covering rock history from its blues and gospel roots through contemporary artists. Budget 3-4 hours. The inductee exhibits go deep on individual artists' contributions. Buy tickets online to skip the line."},
            {"q": "What is the West Side Market?", "a": "West Side Market is the best public market in the Midwest — a 1912 Beaux-Arts building in Ohio City with 100+ vendors selling produce, meat, cheese, Eastern European specialty foods, and prepared foods. Saturday morning is peak (very crowded). The pierogi (from Reilly's) and smoked meats are particular standouts."},
            {"q": "What neighborhoods should I explore?", "a": "Ohio City for the West Side Market, restaurants, and craft breweries. Tremont for the arts district and excellent dining. Downtown Cleveland for the Rock Hall, the Flats (riverfront), and Playhouse Square (the largest theater district outside NYC). Little Italy for the Cleveland Museum of Art and cafes."},
            {"q": "Is the Cleveland Museum of Art worth visiting?", "a": "Genuinely excellent and free (with a paid special exhibitions wing). The CMA has one of the top art collections in the US — particularly strong in medieval European, ancient Egyptian, and Asian art. The atrium design and gallery layout are exceptional."},
            {"q": "When is the best time to visit Cleveland?", "a": "May–October for Lake Erie access and outdoor activities. The Cleveland Orchestra (Severance Hall) runs September–May — one of the great orchestras in the world. Summer brings outdoor festivals and Indians/Guardians baseball."},
            {"q": "What food is Cleveland known for?", "a": "Polish Boy (kielbasa, fries, coleslaw, and BBQ sauce in a bun — a uniquely Cleveland creation). Pierogis at West Side Market. Corned beef sandwiches at Slyman's. Contemporary dining at Lola Bistro (Michael Symon's flagship)."},
            {"q": "Is Cleveland safe?", "a": "The tourist areas — Ohio City, Tremont, University Circle, downtown — are safe and active. Cleveland has elevated crime rates in some inner-city neighborhoods away from visitor zones. Standard urban awareness applies."},
            {"q": "What is Playhouse Square?", "a": "Playhouse Square is the largest performing arts center outside New York City — six restored historic theaters in a single city block downtown, with programming including Broadway shows, opera, ballet, and the Cleveland Orchestra pops. The restored chandeliers and grand lobby of the State Theatre alone are worth seeing."},
        ],
        "affiliatePicks": [
            {"name": "Metropolitan at the 9 Cleveland", "type": "hotel", "url": "https://www.booking.com/hotel/us/metropolitan-at-the-9-cleveland.html?aid=2778866", "description": "Boutique hotel in historic Euclid Avenue building. Well-positioned for downtown and Ohio City access.", "priceRange": "$$$"},
            {"name": "Rock and Roll Hall of Fame Tickets", "type": "activity", "url": f"https://www.getyourguide.com/cleveland-l2537/?partner_id=IVN6IQ3&q=Rock+and+Roll+Hall+of+Fame", "description": "Book Rock Hall tickets in advance for the best experience and skip-the-line access.", "priceRange": "$$"},
            {"name": "Cleveland Food and Neighborhoods Tour", "type": "tour", "url": f"https://www.getyourguide.com/cleveland-l2537/?partner_id=IVN6IQ3&q=Cleveland+food+tour", "description": "West Side Market, Ohio City, and Tremont guided food and neighborhood tour.", "priceRange": "$$"},
        ],
        "scottTips": {
            "logistics": "Cleveland Hopkins International Airport (CLE) is 15 miles southwest — RTA Red Line light rail connects to downtown. Downtown Cleveland is compact and walkable for the major tourist sites.",
            "bestTime": "May–October for the full experience. Cleveland Orchestra season (September–May) is a reason to visit in winter. West Side Market runs year-round.",
            "gettingAround": "RTA light rail for airport and downtown. Car helpful for Ohio City, Tremont, and University Circle clusters. Uber/Lyft available.",
            "money": "Cleveland is very affordable. Cleveland Museum of Art is free. Hotels run $100–175/night in Ohio City and downtown. Rock Hall is $32/adult.",
            "safety": "Tourist zones are safe. Cleveland has crime challenges in specific neighborhoods.",
            "packing": "Layers for Lake Erie wind — the lake creates its own microclimate.",
            "localCulture": "Cleveland has an endearing civic pride forged by decades of being the butt of jokes. The LeBron James legacy (born in Akron, won Cleveland's first title in 2016) is a genuine source of emotional meaning for the city. Cleveland sports fandom is intense and loyal."
        },
    },
    "columbus": {
        "aeo": "Columbus is Ohio's largest city and one of America's fastest-growing metros — a Big Ten university city with a young, entrepreneurial energy, a thriving Short North arts and restaurant district, and the National Veterans Memorial and Museum. It's the least-visited major Ohio city by tourists but has the best restaurant scene of the three.",
        "gradient": "linear-gradient(135deg, #dc2626, #1e40af, #166534)",
        "video_title": "Columbus: Ohio's Rising Capital",
        "video_text": "Short North, OSU, and the best food scene in Ohio.",
        "faqItems": [
            {"q": "Is Columbus worth visiting?", "a": "Yes, especially for foodies and design travelers. The Short North arts district has one of the better restaurant and gallery concentrations in the Midwest. The Ohio State campus (62,000 students) creates energy that spills into the surrounding neighborhoods. It's a city that locals are genuinely proud of."},
            {"q": "What is the Short North?", "a": "The Short North is Columbus's arts and dining district — a mile of High Street north of downtown with galleries, restaurants, boutiques, and bars. The Columbus Museum of Art is at the south end. Gallery Hop (first Saturday of each month) turns the district into an open arts evening."},
            {"q": "What should I eat in Columbus?", "a": "Jeni's Splendid Ice Creams (started here — multiple locations). Dirty Frank's Hot Dog Palace. Thurman Cafe for the massive Thurmanator burger. The North Market (year-round covered market, smaller than West Side Market but excellent). Skillet for brunch. Brassica for excellent fast-casual Mediterranean."},
            {"q": "What is Columbus known for beyond Ohio State?", "a": "The Columbus Museum of Art (good contemporary collection), the Franklin Park Conservatory and Botanical Gardens, the Short North gallery scene, and the Columbus Food Truck Scene (hundreds of trucks, strong year-round culture). Also COSI (Center of Science and Industry) for families."},
            {"q": "When is the best time to visit Columbus?", "a": "May–October for pleasant weather and outdoor Short North activity. Ohio State football season (September–November) means massive crowds and hotel premium pricing on game days — plan around it or embrace it."},
            {"q": "How do I get around Columbus?", "a": "Columbus is a driving city — public transit is limited. Uber/Lyft are the practical options. The Short North is walkable once you're there."},
            {"q": "What is the National Veterans Memorial and Museum?", "a": "The National Veterans Memorial and Museum (opened 2018) is a powerful and architecturally extraordinary building in downtown Columbus dedicated to the service and sacrifice of American veterans. Free admission. The elliptical concrete form creates an internal space that's genuinely affecting."},
            {"q": "Is Columbus near other Midwest destinations?", "a": "Columbus is about 2 hours from Cleveland, 1.5 hours from Cincinnati, and 3 hours from Pittsburgh. It's a viable base for an Ohio road trip hitting all three cities."},
        ],
        "affiliatePicks": [
            {"name": "Graduate Columbus", "type": "hotel", "url": "https://www.booking.com/hotel/us/graduate-columbus.html?aid=2778866", "description": "Short North boutique hotel with Ohio State-inspired design. Walking distance to the best restaurants.", "priceRange": "$$"},
            {"name": "Columbus Short North Food Tour", "type": "tour", "url": f"https://www.getyourguide.com/columbus-l2537/?partner_id=IVN6IQ3&q=Columbus+Ohio+food+tour", "description": "Guided food tour through the Short North covering the Columbus dining scene.", "priceRange": "$$"},
            {"name": "Franklin Park Conservatory Botanical Gardens", "type": "activity", "url": f"https://www.getyourguide.com/columbus-l2537/?partner_id=IVN6IQ3&q=Columbus+botanical+garden", "description": "Guided tour of the Franklin Park Conservatory — Chihuly glass art in botanical settings.", "priceRange": "$"},
        ],
        "scottTips": {
            "logistics": "John Glenn Columbus International Airport (CMH) has good connections to major US hubs. Downtown and Short North are 15 minutes from the airport. Hotels cluster in Short North and downtown.",
            "bestTime": "May–October for outdoor Short North life. Avoid Ohio State home football weekends unless you want the game experience.",
            "gettingAround": "Car or Lyft/Uber. Short North is walkable. North Market and Ohio State campus are bikeable from Short North.",
            "money": "Columbus is affordable. Hotels run $100–160/night in Short North. Restaurant meals in the $20–40/person range at most Short North spots.",
            "safety": "Short North and downtown are safe. Columbus has elevated crime rates in some neighborhoods away from tourist zones.",
            "packing": "Comfortable walking shoes for Short North. Camera for the gallery hop.",
            "localCulture": "Columbus has an earnest Midwest identity without the chip-on-shoulder of Detroit or Cleveland. The OSU culture is omnipresent — Buckeye gear everywhere. Jeni's Splendid Ice Creams is a point of civic pride that locals genuinely love."
        },
    },
    "indianapolis": {
        "aeo": "Indianapolis is the racing capital of the world — home to the Indianapolis 500, the most-attended single-day sporting event on the planet. Beyond Motor Speedway, it's a surprisingly accessible mid-size city with the best children's museum in the US, a renovated canal walk, and the bulk of its tourist attractions within walking distance of the convention hotel strip.",
        "gradient": "linear-gradient(135deg, #1e40af, #dc2626, #f59e0b)",
        "video_title": "Indianapolis: Racing Capital of the World",
        "video_text": "Indy 500, the Children's Museum, and a canal walk.",
        "faqItems": [
            {"q": "Is the Indianapolis Motor Speedway worth visiting even if I don't care about racing?", "a": "For the scale alone, yes. The Indianapolis Motor Speedway seats 250,000 spectators — a number so large that the entire populations of Monaco, San Marino, and Liechtenstein could fit inside. The IMS Museum has excellent exhibits on American automotive and racing history. The track tour is worthwhile."},
            {"q": "What is the best thing to do in Indianapolis?", "a": "The Children's Museum of Indianapolis — consistently ranked the best children's museum in the world (5 floors, 14 museums-within-a-museum, a full Dinosphere, and a Chihuly glass tower). Adults without children often enjoy it too. The Eiteljorg Museum of American Indians and Western Art is excellent and underrated."},
            {"q": "When is the Indianapolis 500?", "a": "The Indianapolis 500 (the 'Greatest Spectacle in Racing') runs on the Sunday of Memorial Day weekend — late May. Qualifying runs the preceding weekend. Hotel rooms within 30 miles book solid for race weekend. If you want to attend, plan 6+ months ahead and budget for premium pricing on everything."},
            {"q": "What is Mass Ave?", "a": "Massachusetts Avenue (Mass Ave) is Indianapolis's arts and culture corridor — a stretch of restaurants, galleries, bars, and theaters northeast of downtown. Locally the most active nightlife and dining strip."},
            {"q": "Is Indianapolis easy to navigate?", "a": "Very easy — the downtown circle layout (Monument Circle at the center) is logically organized, walkable, and well-connected. Most tourist attractions are within easy walking distance of the hotel cluster."},
            {"q": "What should I eat in Indianapolis?", "a": "The Indy restaurant scene has improved dramatically. Milktooth for the most Instagram-worthy brunch in the Midwest. St. Elmo Steak House (1902) for the legendary shrimp cocktail (horseradish-forward, very spicy). Tinker Street for local farm ingredients."},
            {"q": "When is the best time to visit Indianapolis beyond race weekend?", "a": "May (Indy 500) if you want racing. June–September for pleasant weather and the outdoor canal walk. The Brick Yard 400 (NASCAR, late July) is a second major racing event."},
            {"q": "What is the Indiana State Fair?", "a": "The Indiana State Fair runs for 17 days in August — one of the largest state fairs in the US. The usual state fair attractions (livestock, rides, food-on-a-stick) plus major musical acts."},
        ],
        "affiliatePicks": [
            {"name": "Bottleworks Hotel Indianapolis", "type": "hotel", "url": "https://www.booking.com/hotel/us/bottleworks-hotel-indianapolis.html?aid=2778866", "description": "Indianapolis's coolest hotel — in a converted 1931 Coca-Cola bottling plant with a microbrewery and food hall.", "priceRange": "$$$"},
            {"name": "Indianapolis Motor Speedway Tour", "type": "tour", "url": f"https://www.getyourguide.com/indianapolis-l2537/?partner_id=IVN6IQ3&q=Indianapolis+Motor+Speedway+tour", "description": "Track and museum tour at the IMS — includes riding the track by bus.", "priceRange": "$"},
            {"name": "Indianapolis Food and Neighborhoods Tour", "type": "tour", "url": f"https://www.getyourguide.com/indianapolis-l2537/?partner_id=IVN6IQ3&q=Indianapolis+food+tour", "description": "Guided food tour through Mass Ave and the Fountain Square neighborhood.", "priceRange": "$$"},
        ],
        "scottTips": {
            "logistics": "Indianapolis International Airport (IND) is 15 miles southwest — no rail, but the airport shuttle and Lyft are reliable. Downtown is very compact — the Circle Centre shopping mall, Monument Circle, and most hotels are within a few walkable blocks.",
            "bestTime": "May for the 500 (if you can get tickets and lodging). June–September for good weather. Year-round for the Children's Museum and IMS Museum.",
            "gettingAround": "Walkable downtown. Car or Lyft for IMS and outer neighborhoods. The Broad Ripple neighborhood (8 miles north) requires transportation.",
            "money": "Very affordable. Children's Museum is $30/adult, $25/child. IMS Museum and track tour is $15–25. Hotels in the $100–160/night range.",
            "safety": "Downtown and Mass Ave are safe tourist areas.",
            "packing": "Comfortable walking shoes for the downtown circle. Camera for Monument Circle.",
            "localCulture": "Indianapolis is earnest Midwestern — genuinely friendly, unpretentious, and proud of the 500 in a way that feels like civic religion. The racing heritage is real, not just marketing."
        },
    },
    "madison": {
        "aeo": "Madison is Wisconsin's state capital and home to the University of Wisconsin — a progressive college city built on an isthmus between two lakes, with a thriving Farmers Market on the Capitol Square (the largest producer-only farmers market in the US), excellent restaurants, and easy access to Devil's Lake State Park and Wisconsin's lake country.",
        "gradient": "linear-gradient(135deg, #dc2626, #166534, #1e40af)",
        "video_title": "Madison: Isthmus City",
        "video_text": "Two lakes, the Farmers Market, and the best college town in the Midwest.",
        "faqItems": [
            {"q": "What makes Madison's Farmers Market special?", "a": "The Dane County Farmers Market on Capitol Square (Saturdays, late April through November) is the largest producer-only farmers market in the United States — 150+ vendors circling the Wisconsin State Capitol, selling everything from cheese curds to heirloom tomatoes. Arrive early (7am–8am) for the best selection."},
            {"q": "Is Madison worth visiting for non-UW visitors?", "a": "Yes — the city's character extends well beyond campus. The State Street pedestrian corridor connecting the Capitol to the university, the lakefront parks (both Mendota and Monona), and the restaurant scene in the Willy Street and Monroe Street neighborhoods all reward exploration."},
            {"q": "What are the best outdoor activities near Madison?", "a": "Devil's Lake State Park (45 miles northwest) is Wisconsin's most visited state park — a glacially carved lake surrounded by quartzite bluffs with excellent hiking and swimming. The Military Ridge Trail (40 miles of paved cycling trail) runs west from the city. Olbrich and Vilas beaches on Lake Mendota are local swimming destinations."},
            {"q": "What should I eat in Madison?", "a": "Cheese curds are mandatory (the squeakier the fresher). Graze for farm-to-table Wisconsin ingredients. The Old Fashioned for the Wisconsin cocktail culture and cheese plates. Great Dane Pub for the original Madison brew pub experience. Ian's Pizza for the slice scene near campus."},
            {"q": "What is the Wisconsin State Capitol worth seeing?", "a": "The Wisconsin State Capitol is arguably the most beautiful state capitol building in the US — a Beaux-Arts dome taller than the US Capitol in Washington, visible from miles away. Free tours run throughout the day."},
            {"q": "When is the best time to visit Madison?", "a": "May–October for the Farmers Market, outdoor lakes, and campus energy. Wisconsin Badgers football season (September–November) transforms the city on game days — electric atmosphere but crowded and expensive."},
            {"q": "How do I get to Madison?", "a": "Dane County Regional Airport (MSN) has direct flights from Chicago, Minneapolis, Detroit, and a few other cities. Chicago to Madison is 2.5 hours by car. Amtrak has no direct Madison service."},
            {"q": "What is the Willy Street neighborhood?", "a": "Willy Street (Williamson Street) is Madison's most eclectic neighborhood — a diverse, progressive corridor with the Willy Street Co-op, independent restaurants, bike shops, and a strong community identity. Best explored on foot in the afternoon."},
        ],
        "affiliatePicks": [
            {"name": "Graduate Madison Hotel", "type": "hotel", "url": "https://www.booking.com/hotel/us/graduate-madison.html?aid=2778866", "description": "University-area boutique hotel on State Street, walking distance to Capitol Square and the Farmers Market.", "priceRange": "$$"},
            {"name": "Madison Food and Farmers Market Tour", "type": "tour", "url": f"https://www.getyourguide.com/madison-l2537/?partner_id=IVN6IQ3&q=Madison+Wisconsin+food+tour", "description": "Guided tour of Capitol Square Farmers Market and Wisconsin food culture.", "priceRange": "$"},
            {"name": "Devil's Lake State Park Guided Hike", "type": "tour", "url": f"https://www.getyourguide.com/madison-l2537/?partner_id=IVN6IQ3&q=Devil's+Lake+Wisconsin+hiking", "description": "Guided half-day hike at Devil's Lake — the bluff trails and lake views are spectacular.", "priceRange": "$"},
        ],
        "scottTips": {
            "logistics": "MSN airport has limited direct connections — Chicago O'Hare to Madison by car (2.5 hrs) is often the practical approach. State Street is the pedestrian spine — park once and walk.",
            "bestTime": "June–October for the full Madison experience. Saturday morning Farmers Market is a year-round reason to visit (April–November outdoor, indoor in winter). Avoid Badgers home football weekends for calm.",
            "gettingAround": "State Street and Capitol Square are walkable. Bike-share (BCycle) is excellent for the isthmus. Car for Devil's Lake and outer neighborhoods.",
            "money": "Madison is affordable. Hotels run $100–170/night. Restaurant meals on State Street run $15–35/person. Farmers Market is free to walk.",
            "safety": "Madison is one of the safest mid-size cities in the US.",
            "packing": "Layers for lake weather. Bike-appropriate clothing if using BCycle. Camera for the Capitol dome.",
            "localCulture": "Madison is consistently rated the most politically liberal city in the Midwest — heavily influenced by university culture and progressive Wisconsin politics. The Farmers Market is a genuine community institution, not a tourist performance."
        },
    },
    "des-moines": {
        "aeo": "Des Moines is Iowa's capital — a mid-size city that consistently surprises visitors with its quality of life, strong arts institutions (the Des Moines Art Center is one of the best mid-size art museums in the US), a craft beer scene that punches well above its weight, and the Iowa State Fair (the second-largest state fair in the US).",
        "gradient": "linear-gradient(135deg, #166534, #1e40af, #f59e0b)",
        "video_title": "Des Moines: Iowa's Capital Surprise",
        "video_text": "Art museum, Iowa State Fair, and a city that keeps getting better.",
        "faqItems": [
            {"q": "Is Des Moines worth visiting?", "a": "More than most people expect. The Des Moines Art Center (free) is genuinely excellent — a three-building complex designed by Eliel Saarinen, I.M. Pei, and Richard Meier, with a strong 20th-century and contemporary collection. The East Village neighborhood has an excellent restaurant and bar scene. The Iowa State Fair (August) is one of the great American events."},
            {"q": "What is the Iowa State Fair?", "a": "The Iowa State Fair runs 11 days in mid-August and draws 1 million visitors annually. It's one of the largest and most traditional state fairs in the US — butter sculptures (an Iowa cow sculpted in butter is the signature), livestock judging, carnival rides, live music, and a legendary variety of food on a stick. The political significance in presidential primary years (Iowa caucuses) means major candidates campaign here."},
            {"q": "What is the East Village in Des Moines?", "a": "The East Village is Des Moines's most vibrant neighborhood — a walkable stretch of restaurants, bars, boutiques, and galleries east of the State Capitol building. The Iowa Capitol (golden dome) at the neighborhood's edge is one of the most beautiful in the country."},
            {"q": "What should I eat in Des Moines?", "a": "Centro for upscale Italian in the East Village. Zombie Burger for creative burgers. Iowa Machine Shed for farm-style comfort food. The Greater Des Moines Botanical Garden cafe for a lighter option. Craft beer at Exile Brewing or 515 Brewing Company."},
            {"q": "When is the best time to visit Des Moines?", "a": "August for the State Fair. June–September for pleasant weather. Spring (April–May) for Des Moines arts events and lower crowds."},
            {"q": "How do I get to Des Moines?", "a": "Des Moines International Airport (DSM) has direct flights from Chicago, Minneapolis, Dallas, Denver, and other hubs. I-80 runs through the city."},
            {"q": "What outdoor activities are near Des Moines?", "a": "High Trestle Trail (25-mile bike trail with a dramatic bridge over the Des Moines River). Pappajohn Sculpture Park (free outdoor sculpture in the Western Gateway neighborhood — large-scale works including Alexander Calder). Gray's Lake Park for running and kayaking."},
            {"q": "What is the World Food Prize?", "a": "The World Food Prize is the foremost international award for achievement in food and agriculture, founded by Nobel Peace Prize laureate Norman Borlaug. The annual symposium in Des Moines each October draws global agricultural leaders."},
        ],
        "affiliatePicks": [
            {"name": "AC Hotel Des Moines East Village", "type": "hotel", "url": f"{BOOKING}&ss=Des+Moines+IA", "description": "Modern hotel in the East Village, walkable to the best restaurants and the State Capitol.", "priceRange": "$$"},
            {"name": "Des Moines Art Center and East Village Tour", "type": "tour", "url": f"{GYG}&q=Des+Moines+Iowa+tour", "description": "Guided tour of the Des Moines Art Center and East Village neighborhood.", "priceRange": "$"},
            {"name": "Iowa State Fair Experience", "type": "activity", "url": f"{GYG}&q=Iowa+State+Fair+tour", "description": "Guide to the Iowa State Fair — best food, events, and logistics for the 11-day August event.", "priceRange": "$"},
        ],
        "scottTips": {
            "logistics": "DSM airport has good connections to major Midwest hubs and some national cities. East Village and downtown are walkable. I-80 corridor puts Des Moines equidistant from Omaha (2.5 hrs) and Chicago (5 hrs).",
            "bestTime": "August for the State Fair. June–September for the full city experience.",
            "gettingAround": "Car helpful — Des Moines is spread out. East Village is walkable once there.",
            "money": "Very affordable. Art Center is free. Hotels run $90–150/night. Restaurant meals $15–35/person.",
            "safety": "One of the safer mid-size Midwest cities.",
            "packing": "Comfortable clothing for State Fair (it's outdoors in August heat). Walking shoes.",
            "localCulture": "Des Moines has a quietly strong civic identity — Iowans are genuinely proud of the State Fair as a living cultural institution, not just a tourist attraction."
        },
    },
    "omaha": {
        "aeo": "Omaha is Warren Buffett's hometown and Nebraska's largest city — a surprisingly sophisticated mid-size city with the Old Market district (the best urban historic commercial district in the Plains), an extraordinary zoo (consistently ranked in the top 5 in the US), and a steak culture that takes beef consumption seriously.",
        "gradient": "linear-gradient(135deg, #92400e, #1e40af, #166534)",
        "video_title": "Omaha: Warren Buffett's Hometown",
        "video_text": "Old Market, the best zoo in America, and steak culture.",
        "faqItems": [
            {"q": "Is Omaha worth visiting?", "a": "Absolutely for a 1-2 night stop. The Henry Doorly Zoo is legitimately extraordinary — widely considered the best zoo in the United States and often called the best in the world. The Old Market historic district has excellent dining and bars. The strategic location on I-80 makes it a natural road trip stop between Chicago and Denver."},
            {"q": "What is the Henry Doorly Zoo?", "a": "The Henry Doorly Zoo is consistently ranked the best zoo in the United States by USA Today and Tripadvisor. It has the world's largest indoor desert (Desert Dome), one of the largest indoor jungles, a free-flight aviary, aquarium, and butterfly pavilion. Budget a full day — it's a serious destination."},
            {"q": "What is the Old Market?", "a": "The Old Market is Omaha's historic commercial district — a walkable neighborhood of 1880s brick warehouses converted to restaurants, bars, galleries, and boutiques. The best urban historic district between Chicago and Denver. Saturday night in the Old Market is a genuine scene."},
            {"q": "What should I eat in Omaha?", "a": "A steak at Gorat's (Warren Buffett's favorite), Mahogany, or Upstream Brewing. The Old Market's dining options range from Italian to sushi. Block 16 for some of the most creative sandwiches in the Midwest. Charleston's for the prime rib experience."},
            {"q": "What is the Berkshire Hathaway Annual Meeting?", "a": "The Berkshire Hathaway Annual Meeting (Warren Buffett's company) draws 40,000+ shareholders to Omaha every May — effectively the 'Woodstock of capitalism.' Hotels book solid for a full week. If you're interested in the investment world, it's a remarkable event."},
            {"q": "When is the best time to visit Omaha?", "a": "May–October for pleasant weather and outdoor Old Market. The Berkshire Hathaway meeting (early May) brings a fascinating crowd but fills hotels."},
            {"q": "How do I get to Omaha?", "a": "Eppley Airfield (OMA) has direct flights from Chicago, Dallas, Denver, Minneapolis, and other hubs. I-80 puts Omaha 5 hours from Chicago and 8 hours from Denver."},
            {"q": "What else is worth seeing in Omaha?", "a": "Joslyn Art Museum (free Sundays, strong collection). Durham Museum (in the historic Union Station). The Lewis & Clark National Historic Trail Visitor Center. Strategic Air Command & Aerospace Museum (30 miles southwest, outstanding Cold War aviation collection)."},
        ],
        "affiliatePicks": [
            {"name": "Kimpton Cottonwood Hotel Omaha", "type": "hotel", "url": "https://www.booking.com/hotel/us/the-cottonwood-hotel.html?aid=2778866", "description": "Historic 1926 hotel beautifully restored — Omaha's most characterful lodging option.", "priceRange": "$$$"},
            {"name": "Henry Doorly Zoo Tickets", "type": "activity", "url": f"{GYG}&q=Omaha+Zoo+Henry+Doorly", "description": "Book Henry Doorly Zoo tickets in advance for the best experience at this world-class facility.", "priceRange": "$$"},
            {"name": "Omaha Old Market Food and History Tour", "type": "tour", "url": f"{GYG}&q=Omaha+Nebraska+food+tour", "description": "Guided walking tour of the Old Market's restaurants, history, and architecture.", "priceRange": "$"},
        ],
        "scottTips": {
            "logistics": "Eppley Airfield has decent Midwest connections. Old Market is 10 minutes from downtown hotels. The zoo is 5 miles from the Old Market.",
            "bestTime": "May–October. Avoid Berkshire meeting week (early May) unless attending.",
            "gettingAround": "Car recommended — Omaha is spread out. Old Market and downtown are walkable. Zoo requires car or rideshare.",
            "money": "Very affordable. Zoo is $23/adult. Hotels in Old Market run $120–180/night.",
            "safety": "Old Market and downtown are safe. Omaha has some elevated crime rates in inner-city neighborhoods.",
            "packing": "Comfortable shoes for Old Market and zoo walking. Camera — the zoo's environments are photogenic.",
            "localCulture": "Omaha's steak culture is genuine — this is cattle country, and a proper Omaha steak dinner is a cultural experience. Warren Buffett's enduring presence (he lives in the same modest house he bought in 1958) gives the city an underdog-made-good identity."
        },
    },
}

FRONTMATTER_CLOSE = "contentStatus: draft\ndraft: false"

def process_file(filepath, slug, data):
    """Add faqItems, affiliatePicks, scottTips, immersive-break-inline, and AEO to existing files."""
    content = open(filepath, 'r', encoding='utf-8').read()

    if "affiliatePicks:" in content and "affiliatePicks: []" not in content:
        print(f"SKIP {slug} — already has Tier 3")
        return

    # Build faqItems YAML
    faqItems_yaml = "faqItems:\n"
    for faq in data.get("faqItems", []):
        q = faq['q'].replace('"', "'")
        a = faq['a'].replace('"', "'")
        faqItems_yaml += f'  - question: "{q}"\n    answer: "{a}"\n'

    # Build affiliatePicks YAML
    affiliatePicks_yaml = "affiliatePicks:\n"
    for pick in data.get("affiliatePicks", []):
        affiliatePicks_yaml += f"""  - name: "{pick['name']}"
    type: {pick['type']}
    url: "{pick['url']}"
    description: "{pick['description']}"
    priceRange: "{pick['priceRange']}"
"""

    scottTips = data.get("scottTips", {})
    scottTips_yaml = f"""scottTips:
  logistics: "{scottTips.get('logistics', '').replace('"', "'")}"
  bestTime: "{scottTips.get('bestTime', '').replace('"', "'")}"
  gettingAround: "{scottTips.get('gettingAround', '').replace('"', "'")}"
  money: "{scottTips.get('money', '').replace('"', "'")}"
  safety: "{scottTips.get('safety', '').replace('"', "'")}"
  packing: "{scottTips.get('packing', '').replace('"', "'")}"
  localCulture: "{scottTips.get('localCulture', '').replace('"', "'")}"
"""

    new_fm_block = faqItems_yaml + affiliatePicks_yaml.rstrip() + "\n" + scottTips_yaml + "contentStatus: published\ndraft: false"
    content = content.replace(FRONTMATTER_CLOSE, new_fm_block)

    # Add immersive-break-inline and AEO in body
    if "immersive-break-inline" not in content:
        video_block = f"""<div class="immersive-break-inline">
  <video autoplay muted loop playsinline preload="metadata">
    <source src="/videos/destinations/{slug}-hero.mp4" type="video/mp4" />
  </video>
  <div class="ib-gradient" style="background: {data['gradient']};"></div>
  <div class="ib-content">
    <div class="ib-title">{data['video_title']}</div>
    <p class="ib-text">{data['video_text']}</p>
  </div>
</div>"""

        lines = content.split('\n')
        fm_count = 0
        fm_end = -1
        for i, line in enumerate(lines):
            if line.strip() == '---':
                fm_count += 1
                if fm_count == 2:
                    fm_end = i
                    break

        if fm_end >= 0:
            body_lines = lines[fm_end+1:]
            first_para_end = -1
            in_para = False
            for j, bl in enumerate(body_lines):
                if bl.strip() and not in_para:
                    in_para = True
                elif not bl.strip() and in_para:
                    first_para_end = j
                    break

            if first_para_end >= 0:
                aeo_text = data.get("aeo", "")
                new_body_lines = []
                if aeo_text:
                    new_body_lines.append(aeo_text)
                    new_body_lines.append("")
                new_body_lines.extend(body_lines[:first_para_end])
                new_body_lines.append("")
                new_body_lines.append(video_block)
                new_body_lines.append("")
                new_body_lines.extend(body_lines[first_para_end:])
                content = '\n'.join(lines[:fm_end+1]) + '\n' + '\n'.join(new_body_lines)

    open(filepath, 'w', encoding='utf-8').write(content)
    print(f"Done {slug}")


for slug, data in DESTINATIONS.items():
    filepath = f"{BASE}/{slug}.md"
    if not os.path.exists(filepath):
        print(f"SKIP {slug} — not found")
        continue
    process_file(filepath, slug, data)

print("Midwest Tier 3 complete")

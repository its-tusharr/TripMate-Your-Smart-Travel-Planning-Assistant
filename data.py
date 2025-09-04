# This file contains all the destination data for the travel assistant.

TRAVEL_DATA = {
    'agra': {
        'country': 'India',
        'best_time': 'October to March',
        'cost': {'low': '₹8,000 - ₹15,000', 'mid': '₹20,000 - ₹35,000', 'luxury': '₹50,000+'},
        'hotels': {'low': 'Budget hotels near Taj Ganj', 'mid': '4-star hotels like Radisson, Clarks Shiraz', 'luxury': 'The Oberoi Amarvilas, ITC Mughal'},
        'how_to_reach': {
            'air': 'Agra Airport (AGR) has limited connectivity. Delhi (DEL) is the preferred international airport (2-3 hours drive).',
            'train': 'Agra Cantt (AGC) is a major railway station on the Delhi-Mumbai and Delhi-Chennai routes.',
            'bus': 'Excellent connectivity via Yamuna Expressway from Delhi.'
        },
        'attractions': ['Taj Mahal 🕌', 'Agra Fort', 'Fatehpur Sikri', 'Mehtab Bagh'],
        'activities': ['Sunrise view of Taj Mahal', 'Exploring Mughal architecture', 'Shopping for marble handicrafts'],
        'food': ['Petha', 'Mughlai Cuisine', 'Bedai & Jalebi']
    },
    'andaman': {
        'country': 'India',
        'best_time': 'October to May',
        'cost': {'low': '₹25,000 - ₹35,000', 'mid': '₹50,000 - ₹70,000', 'luxury': '₹1,00,000+'},
        'hotels': {'low': 'Beachside Cottages', 'mid': 'Eco-Resorts', 'luxury': 'Taj Exotica Resort & Spa'},
        'how_to_reach': {
            'air': 'Fly to Veer Savarkar International Airport in Port Blair (IXZ).',
            'sea': 'Passenger ships are available from Chennai, Kolkata, and Visakhapatnam (takes 2-3 days).'
        },
        'attractions': ['Radhanagar Beach', 'Cellular Jail', 'Ross Island', 'Baratang Caves'],
        'activities': ['Scuba Diving 🤿', 'Snorkeling', 'Sea Walking', 'Glass Bottom Boat Ride'],
        'food': ['Fresh Seafood', 'Coconut-based Curries']
    },
    'bali': {
        'country': 'Indonesia',
        'best_time': 'April to October',
        'cost': {'low': '₹40,000 - ₹60,000', 'mid': '₹70,000 - ₹1,00,000', 'luxury': '₹1,50,000+'},
        'hotels': {'low': 'Guesthouses in Ubud', 'mid': 'Private villas in Seminyak', 'luxury': 'Luxury Resorts (e.g., Four Seasons)'},
         'how_to_reach': {
            'air': 'Fly to Ngurah Rai International Airport (DPS) in Denpasar.'
        },
        'attractions': ['Ubud Monkey Forest', 'Tanah Lot Temple', 'Mount Batur', 'Uluwatu Temple'],
        'activities': ['Surfing in Kuta 🏄‍♀️', 'Yoga and Meditation in Ubud', 'Exploring Rice Terraces'],
        'food': ['Nasi Goreng', 'Satay', 'Babi Guling'],
        'currency': 'Indonesian Rupiah (IDR). 1 INR ≈ 195 IDR',
        'visa': 'Visa on Arrival for Indian citizens (subject to change).'
    },
    'dubai': {
        'country': 'UAE',
        'best_time': 'November to March',
        'cost': {'low': '₹50,000 - ₹70,000', 'mid': '₹80,000 - ₹1,20,000', 'luxury': '₹2,00,000+'},
        'hotels': {'low': 'Budget hotels in Deira', 'mid': 'Hotels near Dubai Mall', 'luxury': 'Luxury Hotels (e.g., Burj Al Arab)'},
        'how_to_reach': {
            'air': 'Fly to Dubai International Airport (DXB), a major global hub.'
        },
        'attractions': ['Burj Khalifa', 'The Dubai Mall', 'Palm Jumeirah', 'Dubai Miracle Garden'],
        'activities': ['Desert Safari 🏜️', 'Dhow Cruise', 'Skydiving over The Palm', 'Shopping 🛍️'],
        'food': ['Shawarma', 'Al Harees', 'Luqaimat'],
        'currency': 'UAE Dirham (AED). 1 AED ≈ ₹22.7',
        'visa': 'Visa required. Often processed by airlines or hotels.'
    },
    'goa': {
        'country': 'India',
        'best_time': 'October to March',
        'cost': {'low': '₹15,000 - ₹25,000', 'mid': '₹30,000 - ₹50,000', 'luxury': '₹70,000+'},
        'hotels': {'low': 'Hostels (e.g., The Hosteller, Zostel)', 'mid': '3-Star Hotels (e.g., Resort Rio, The Park Baga)', 'luxury': '5-Star Resorts (e.g., Taj Exotica, W Goa)'},
        'how_to_reach': {
            'air': 'Fly to Dabolim Airport (GOI), which is well-connected to all major cities.',
            'train': 'Main railway stations are Madgaon (MAO) and Vasco da Gama (VSG).',
            'bus': 'Regular bus services are available from nearby cities like Mumbai and Pune.'
        },
        'attractions': ['Baga Beach', 'Calangute Beach', 'Dudhsagar Falls', 'Old Goa Churches'],
        'activities': ['Water Sports 🏄', 'Beach Hopping 🏖️', 'Scuba Diving', 'Enjoying Nightlife 🕺'],
        'food': ['Goan Fish Curry 🐟', 'Vindaloo', 'Bebinca'],
    },
    'kerala': {
        'country': 'India',
        'best_time': 'September to March',
        'cost': {'low': '₹20,000 - ₹30,000', 'mid': '₹40,000 - ₹60,000', 'luxury': '₹80,000+'},
        'hotels': {'low': 'Homestays and Guesthouses', 'mid': 'Houseboats in Alleppey, Resorts in Munnar', 'luxury': 'Luxury Resorts (e.g., Kumarakom Lake Resort)'},
        'how_to_reach': {
            'air': 'Three international airports: Cochin (COK), Trivandrum (TRV), and Calicut (CCJ).',
            'train': 'Extensive railway network connecting it to all major parts of India.',
            'bus': 'Well-connected by road to neighboring states like Karnataka and Tamil Nadu.'
        },
        'attractions': ['Alleppey Backwaters', 'Munnar Tea Gardens', 'Thekkady (Periyar National Park)', 'Varkala Beach'],
        'activities': ['Backwater Cruise 🛶', 'Kathakali Performance', 'Ayurvedic Massage', 'Spice Plantation Tour'],
        'food': ['Appam with Stew', 'Sadya', 'Puttu and Kadala Curry'],
    },
    'ladakh': {
        'country': 'India',
        'best_time': 'April to June',
        'cost': {'low': '₹30,000 - ₹40,000', 'mid': '₹50,000 - ₹70,000', 'luxury': '₹1,00,000+'},
        'hotels': {'low': 'Local Homestays', 'mid': 'Guesthouses in Leh', 'luxury': 'Luxury Camps and Hotels'},
        'how_to_reach': {
            'air': 'Leh Kushok Bakula Rimpochee Airport (IXL) is the main airport. Flights from Delhi are common.',
            'bus': 'Road trip via Manali-Leh Highway or Srinagar-Leh Highway (open only in summer months).'
        },
        'attractions': ['Pangong Lake', 'Nubra Valley', 'Magnetic Hill', 'Leh Palace'],
        'activities': ['Mountain Biking 🚴', 'River Rafting in Zanskar', 'Monastery Hopping ☸️', 'Stargazing'],
        'food': ['Thukpa', 'Momos 🥟', 'Skyu'],
    },
    'london': {
        'country': 'UK',
        'best_time': 'May to September',
        'cost': {'low': '₹1,20,000 - ₹1,80,000', 'mid': '₹2,20,000 - ₹3,50,000', 'luxury': '₹4,50,000+'},
        'hotels': {'low': 'Hostels in zones 2-3', 'mid': 'Hotels in Paddington/Kensington (e.g., Premier Inn)', 'luxury': 'The Savoy, The Dorchester'},
        'how_to_reach': { 'air': 'Fly to Heathrow (LHR), Gatwick (LGW), or other London airports.'},
        'attractions': ['The London Eye', 'Tower of London', 'Buckingham Palace', 'British Museum'],
        'activities': ['Ride a double-decker bus 🚌', 'Watch the Changing of the Guard', 'Explore Covent Garden', 'Take a Thames River cruise'],
        'food': ['Fish and Chips', 'Sunday Roast', 'Full English Breakfast', 'Afternoon Tea ☕'],
        'currency': 'Pound Sterling (GBP). 1 GBP ≈ ₹105',
        'visa': 'UK Standard Visitor visa required for Indian citizens.'
    },
    'maldives': {
        'country': 'Maldives',
        'best_time': 'November to April',
        'cost': {'low': '₹70,000 - ₹1,00,000 (on local islands)', 'mid': '₹1,50,000 - ₹2,50,000', 'luxury': '₹3,00,000+'},
        'hotels': {'low': 'Guesthouses on Maafushi', 'mid': 'Overwater Bungalows', 'luxury': 'Ultra-Luxury Private Resorts'},
        'how_to_reach': {
            'air': 'Fly to Velana International Airport (MLE) near the capital city, Malé.'
        },
        'attractions': ['Male City', 'Bioluminescent Beaches', 'Coral Reefs'],
        'activities': ['Snorkeling with Turtles 🐢', 'Diving with Manta Rays', 'Sunset Dolphin Cruise 🐬'],
        'food': ['Garudhiya (Fish Soup)', 'Mas Huni', 'Maldivian Curry'],
        'currency': 'Maldivian Rufiyaa (MVR). 1 MVR ≈ ₹5.4',
        'visa': 'Visa on Arrival for Indian citizens.'
    },
    'manali': {
        'country': 'India',
        'best_time': 'October to June',
        'cost': {'low': '₹15,000 - ₹25,000', 'mid': '₹35,000 - ₹55,000', 'luxury': '₹70,000+'},
        'hotels': {'low': 'Budget Guesthouses, Hostels in Old Manali', 'mid': 'Boutique Hotels, Riverside Resorts', 'luxury': 'Span Resort & Spa, Manu Allaya'},
        'how_to_reach': {
            'air': 'Nearest airport is Bhuntar (KUU), about 50 km away. Take a taxi or bus from there.',
            'train': 'Nearest major railway station is in Chandigarh (around 310 km away).',
            'bus': 'Excellent overnight bus connectivity from Delhi and Chandigarh.'
        },
        'attractions': ['Solang Valley', 'Rohtang Pass', 'Hidimba Devi Temple', 'Old Manali Café Street'],
        'activities': ['Paragliding 🪂', 'River Rafting', 'Skiing ⛷️ (in winter)', 'Cafe Hopping'],
        'food': ['Siddu (Local Bread)', 'Trout Fish', 'Momos', 'Thukpa']
    },
    'mumbai': {
        'country': 'India',
        'best_time': 'October to March',
        'cost': {'low': '₹20,000 - ₹30,000', 'mid': '₹40,000 - ₹60,000', 'luxury': '₹90,000+'},
        'hotels': {'low': 'Hostels in Colaba', 'mid': 'Business hotels in Andheri/Bandra', 'luxury': 'The Taj Mahal Palace, The Oberoi'},
        'how_to_reach': {
            'air': 'Chhatrapati Shivaji Maharaj International Airport (BOM) is one of India\'s busiest airports.',
            'train': 'A major hub for Indian Railways with terminals like CSMT, Dadar, and LTT.',
            'bus': 'Excellent connectivity to cities in Western and Southern India.'
        },
        'attractions': ['Gateway of India', 'Marine Drive', 'Elephanta Caves', 'Siddhivinayak Temple'],
        'activities': ['Explore Bollywood film city', 'Walk along Juhu Beach', 'Street food tour', 'Ferry ride to Elephanta ⛴️'],
        'food': ['Vada Pav', 'Pav Bhaji', 'Bhelpuri', 'Bombay Duck (fish)']
    },
    'new york': {
        'country': 'USA',
        'best_time': 'April to June & September to November',
        'cost': {'low': '₹1,50,000 - ₹2,00,000', 'mid': '₹2,50,000 - ₹4,00,000', 'luxury': '₹5,00,000+'},
        'hotels': {'low': 'Hostels in Brooklyn/Queens', 'mid': 'Mid-range hotels in Midtown (e.g., Hilton Garden Inn)', 'luxury': 'The Plaza, The Ritz-Carlton Central Park'},
        'how_to_reach': { 'air': 'Fly to John F. Kennedy (JFK), LaGuardia (LGA), or Newark (EWR) airports.'},
        'attractions': ['Times Square', 'Statue of Liberty 🗽', 'Central Park', 'Empire State Building'],
        'activities': ['Watch a Broadway show 🎭', 'Walk across the Brooklyn Bridge', 'Visit MoMA or The Met museum', 'Take a ferry to Staten Island'],
        'food': ['New York-style Pizza 🍕', 'Bagels', 'Hot Dogs from a street cart 🌭', 'Cheesecake'],
        'currency': 'US Dollar (USD). 1 USD ≈ ₹83',
        'visa': 'US Visa (e.g., B1/B2) required for Indian citizens.'
    },
    'paris': {
        'country': 'France',
        'best_time': 'April to June & September to October',
        'cost': {'low': '₹80,000 - ₹1,20,000', 'mid': '₹1,50,000 - ₹2,50,000', 'luxury': '₹3,00,000+'},
        'hotels': {'low': 'Hostels in Montmartre', 'mid': 'Boutique hotels in Le Marais', 'luxury': 'Palace hotels (e.g., The Ritz Paris)'},
        'how_to_reach': {
            'air': 'Fly to Charles de Gaulle Airport (CDG), the main international airport.'
        },
        'attractions': ['Eiffel Tower 🗼', 'Louvre Museum 🖼️', 'Notre-Dame Cathedral', 'Palace of Versailles'],
        'activities': ['Seine River Cruise ⛴️', 'Exploring Montmartre', 'Shopping on Champs-Élysées'],
        'food': ['Croissants 🥐', 'Macarons', 'Escargots 🐌', 'French Onion Soup'],
        'currency': 'Euro (EUR). 1 EUR ≈ ₹90',
        'visa': 'Schengen Visa required for Indian citizens.'
    },
    'phuket': {
        'country': 'Thailand',
        'best_time': 'November to February',
        'cost': {'low': '₹35,000 - ₹50,000', 'mid': '₹60,000 - ₹90,000', 'luxury': '₹1,20,000+'},
        'hotels': {'low': 'Hostels in Patong', 'mid': 'Resorts in Karon or Kata beach', 'luxury': 'Luxury Villas (e.g., Sri Panwa)'},
        'how_to_reach': {
            'air': 'Fly to Phuket International Airport (HKT).'
        },
        'attractions': ['Phi Phi Islands', 'Big Buddha', 'Patong Beach', 'Old Phuket Town'],
        'activities': ['Island Hopping Tour 🏝️', 'Snorkeling and Diving', 'Thai Massage'],
        'food': ['Pad Thai', 'Tom Yum Goong 🍤', 'Green Curry'],
        'currency': 'Thai Baht (THB). 1 THB ≈ ₹2.3',
        'visa': 'Visa on Arrival for Indian citizens (check current policies).'
    },
    'rajasthan': {
        'country': 'India',
        'best_time': 'October to March',
        'cost': {'low': '₹25,000 - ₹35,000', 'mid': '₹50,000 - ₹80,000', 'luxury': '₹1,20,000+'},
        'hotels': {'low': 'Haveli Stays, Budget Hotels', 'mid': 'Heritage Hotels (e.g., Samode Haveli)', 'luxury': 'Palace Hotels (e.g., Umaid Bhawan Palace)'},
        'how_to_reach': {
            'air': 'Major airports in Jaipur (JAI), Udaipur (UDR), and Jodhpur (JDH).',
            'train': 'Well-connected by rail with direct trains from cities like Delhi and Mumbai.',
            'bus': 'Excellent road network with luxury and state-run buses.'
        },
        'attractions': ['Jaipur (Hawa Mahal, Amber Fort)', 'Udaipur (City Palace, Lake Pichola)', 'Jaisalmer (Desert Safari)'],
        'activities': ['Camel Safari in Thar Desert 🐫', 'Hot Air Ballooning in Jaipur 🎈', 'Exploring Forts and Palaces'],
        'food': ['Dal Baati Churma', 'Laal Maas', 'Gatte ki Sabzi'],
    },
    'rishikesh': {
        'country': 'India',
        'best_time': 'September to November & March to April',
        'cost': {'low': '₹8,000 - ₹15,000', 'mid': '₹20,000 - ₹35,000', 'luxury': '₹50,000+'},
        'hotels': {'low': 'Ashrams & Guesthouses', 'mid': 'Boutique Stays near Laxman Jhula', 'luxury': 'Aloha on the Ganges, Taj Rishikesh Resort & Spa'},
        'how_to_reach': {
            'air': 'Nearest airport is Jolly Grant in Dehradun (DED), about 35 km away.',
            'train': 'Rishikesh (RKSH) has a railway station. Haridwar (HW) is a major nearby hub.',
            'bus': 'Well-connected by bus to Delhi, Haridwar, and other North Indian cities.'
        },
        'attractions': ['Laxman Jhula', 'Triveni Ghat', 'Neelkanth Mahadev Temple', 'Beatles Ashram'],
        'activities': ['River Rafting 🚣', 'Bungee Jumping', 'Ganga Aarti', 'Yoga Retreat 🧘'],
        'food': ['Aloo Puri', 'Chhole Bhature', 'Ayurvedic Herbal Teas']
    },
    'rome': {
        'country': 'Italy',
        'best_time': 'April to June & September to October',
        'cost': {'low': '₹90,000 - ₹1,30,000', 'mid': '₹1,80,000 - ₹2,80,000', 'luxury': '₹3,50,000+'},
        'hotels': {'low': 'Guesthouses near Termini Station', 'mid': 'Boutique hotels in Trastevere', 'luxury': 'Hotel de Russie, The St. Regis Rome'},
        'how_to_reach': { 'air': 'Fly to Leonardo da Vinci–Fiumicino Airport (FCO).'},
        'attractions': ['Colosseum', 'Roman Forum', 'Vatican City (St. Peter\'s Basilica)', 'Trevi Fountain'],
        'activities': ['Toss a coin in the Trevi Fountain', 'Explore the Vatican Museums', 'Eat gelato while walking 🍦', 'Take a pasta-making class'],
        'food': ['Pasta Carbonara 🍝', 'Pizza al Taglio', 'Gelato', 'Suppli'],
        'currency': 'Euro (EUR). 1 EUR ≈ ₹90',
        'visa': 'Schengen Visa required for Indian citizens.'
    },
    'shimla': {
        'country': 'India',
        'best_time': 'March to June (Summer) & December to February (Snowfall)',
        'cost': {'low': '₹10,000 - ₹15,000', 'mid': '₹20,000 - ₹35,000', 'luxury': '₹50,000+'},
        'hotels': {'low': 'Budget hotels on Mall Road', 'mid': 'Resorts with valley views', 'luxury': 'Luxury Hotels (e.g., The Oberoi Cecil)'},
        'how_to_reach': {
            'air': 'Nearest airport is in Jubbarhatti (SLV), 23 km away. Chandigarh (IXC) is a more connected alternative.',
            'train': 'Ride the famous toy train from Kalka (KLK) to Shimla.',
            'bus': 'Very well-connected by bus from Delhi, Chandigarh, and other nearby towns.'
        },
        'attractions': ['The Ridge', 'Mall Road', 'Jakhoo Temple', 'Kufri'],
        'activities': ['Toy Train Ride 🚂', 'Ice Skating', 'Trekking', 'Shopping at Lakkar Bazaar'],
        'food': ['Madra', 'Dhaam', 'Sidu'],
    },
    'singapore': {
        'country': 'Singapore',
        'best_time': 'February to April',
        'cost': {'low': '₹50,000 - ₹70,000', 'mid': '₹80,000 - ₹1,30,000', 'luxury': '₹2,00,000+'},
        'hotels': {'low': 'Capsule hotels in Chinatown/Little India', 'mid': 'Hotels in Clarke Quay (e.g., Novotel)', 'luxury': 'Marina Bay Sands, Raffles Hotel'},
        'how_to_reach': { 'air': 'Fly to Changi Airport (SIN), one of the world\'s best airports.'},
        'attractions': ['Gardens by the Bay', 'Marina Bay Sands Skypark', 'Sentosa Island', 'Singapore Zoo'],
        'activities': ['Night Safari', 'Explore hawker food centers', 'Shopping on Orchard Road 🛍️', 'Walk through the Cloud Forest'],
        'food': ['Hainanese Chicken Rice', 'Chilli Crab 🦀', 'Laksa', 'Kaya Toast'],
        'currency': 'Singapore Dollar (SGD). 1 SGD ≈ ₹62',
        'visa': 'Visa required for Indian citizens.'
    },
    'tokyo': {
        'country': 'Japan',
        'best_time': 'March to May (Cherry Blossoms) & September to November (Autumn Colors)',
        'cost': {'low': '₹1,00,000 - ₹1,50,000', 'mid': '₹2,00,000 - ₹3,00,000', 'luxury': '₹4,00,000+'},
        'hotels': {'low': 'Capsule hotels, Hostels in Shinjuku/Asakusa', 'mid': 'Business hotels (e.g., APA Hotel, Toyoko Inn)', 'luxury': 'Park Hyatt Tokyo, Mandarin Oriental'},
        'how_to_reach': { 'air': 'Fly to Narita (NRT) or Haneda (HND) international airports.'},
        'attractions': ['Shibuya Crossing', 'Tokyo Skytree', 'Senso-ji Temple', 'Meiji Jingu Shrine'],
        'activities': ['Experience a traditional tea ceremony 🍵', 'Visit a themed cafe (e.g., cat cafe)', 'Explore Akihabara Electric Town', 'Watch a Sumo practice'],
        'food': ['Sushi & Sashimi 🍣', 'Ramen 🍜', 'Tempura', 'Okonomiyaki'],
        'currency': 'Japanese Yen (JPY). 1 JPY ≈ ₹0.55',
        'visa': 'Visa required for Indian citizens.'
    },
    'udaipur': {
        'country': 'India',
        'best_time': 'September to March',
        'cost': {'low': '₹12,000 - ₹20,000', 'mid': '₹28,000 - ₹45,000', 'luxury': '₹70,000+'},
        'hotels': {'low': 'Guesthouses near Lake Pichola', 'mid': 'Heritage Hotels', 'luxury': 'The Leela Palace, Taj Lake Palace'},
        'how_to_reach': {
            'air': 'Maharana Pratap Airport (UDR) is located 22 km from the city.',
            'train': 'Udaipur City railway station (UDZ) is well-connected to major cities.',
            'bus': 'Regular bus services are available from cities like Delhi, Jaipur, and Ahmedabad.'
        },
        'attractions': ['City Palace', 'Lake Pichola', 'Jag Mandir', 'Saheliyon ki Bari'],
        'activities': ['Boat Ride 🚤 on Lake Pichola', 'Light & Sound Show', 'Shopping for Handicrafts'],
        'food': ['Dal Baati Churma', 'Gatte ki Sabzi', 'Kachori']
    },
    'varanasi': {
        'country': 'India',
        'best_time': 'October to March',
        'cost': {'low': '₹10,000 - ₹18,000', 'mid': '₹25,000 - ₹40,000', 'luxury': '₹60,000+'},
        'hotels': {'low': 'Guesthouses along the ghats', 'mid': 'Hotels in the Cantonment area', 'luxury': 'Brijrama Palace, Taj Ganges'},
        'how_to_reach': {
            'air': 'Lal Bahadur Shastri Airport (VNS) is about 26 km from the city center.',
            'train': 'Varanasi Junction (BSB) is a major railhead in North India.',
            'bus': 'Well-connected by road to nearby cities like Lucknow and Prayagraj.'
        },
        'attractions': ['Ganges River Ghats', 'Kashi Vishwanath Temple', 'Sarnath', 'Manikarnika Ghat'],
        'activities': ['Sunrise boat ride on the Ganges 🌅', 'Attending Ganga Aarti', 'Exploring narrow lanes', 'Sarnath excursion'],
        'food': ['Kachori Sabzi', 'Lassi', 'Chaat', 'Malaiyo']
    },
}

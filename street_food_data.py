"""
Street Food Showdown Dataset
Contains all Indian street food items with descriptions, slang names, and search terms
"""

STREET_FOODS = [
    # Savory Items
    {
        "name": "Pani Puri",
        "description": "A crispy hollow sphere filled with tangy spiced water and potato mix.",
        "slang": ["Golgappa", "Phuchka", "Puchka"],
        "search_terms": "pani puri golgappa indian street food"
    },
    {
        "name": "Vada Pav",
        "description": "A spicy potato fritter served inside a bun with chutneys.",
        "slang": ["Bombay Burger", "Vada Pao"],
        "search_terms": "vada pav bombay burger indian street food"
    },
    {
        "name": "Samosa",
        "description": "A crispy pastry filled with spiced potatoes and peas.",
        "slang": ["Samosa", "Singhara"],
        "search_terms": "samosa indian street food"
    },
    {
        "name": "Dosa",
        "description": "A thin, crispy crepe made from fermented rice and lentil batter.",
        "slang": ["Dosa", "Dosai"],
        "search_terms": "dosa indian street food"
    },
    {
        "name": "Bhel Puri",
        "description": "A mixture of puffed rice, vegetables, and tangy chutneys.",
        "slang": ["Bhel", "Bhel Puri"],
        "search_terms": "bhel puri indian street food"
    },
    {
        "name": "Pav Bhaji",
        "description": "Spiced mashed vegetables served with buttered bread rolls.",
        "slang": ["Pav Bhaji", "Bread Bhaji"],
        "search_terms": "pav bhaji indian street food"
    },
    {
        "name": "Chaat",
        "description": "A savory snack with crispy base, yogurt, and various toppings.",
        "slang": ["Chaat", "Chaat Papdi"],
        "search_terms": "chaat indian street food"
    },
    {
        "name": "Kebab",
        "description": "Grilled meat or vegetable skewers with aromatic spices.",
        "slang": ["Kebab", "Seekh Kebab"],
        "search_terms": "kebab indian street food"
    },
    {
        "name": "Aloo Tikki",
        "description": "Spiced potato patties served with chutneys and yogurt.",
        "slang": ["Aloo Tikki", "Tikki"],
        "search_terms": "aloo tikki indian street food"
    },
    {
        "name": "Puri",
        "description": "Deep-fried bread served with potato curry and chutneys.",
        "slang": ["Puri", "Poori"],
        "search_terms": "puri poori indian street food"
    },
    {
        "name": "Pakora",
        "description": "Vegetables dipped in spiced chickpea flour batter and deep-fried.",
        "slang": ["Pakora", "Pakoda"],
        "search_terms": "pakora pakoda indian street food"
    },
    {
        "name": "Kachori",
        "description": "Flaky pastry filled with spiced lentils or potatoes.",
        "slang": ["Kachori", "Kachauri"],
        "search_terms": "kachori kachauri indian street food"
    },
    {
        "name": "Dhokla",
        "description": "Steamed savory cake made from fermented rice and chickpea flour.",
        "slang": ["Dhokla", "Khaman"],
        "search_terms": "dhokla khaman indian street food"
    },
    {
        "name": "Khandvi",
        "description": "Thin rolls made from gram flour and yogurt, tempered with spices.",
        "slang": ["Khandvi", "Surali"],
        "search_terms": "khandvi surali indian street food"
    },
    {
        "name": "Thepla",
        "description": "Flatbread made from wheat flour, fenugreek leaves, and spices.",
        "slang": ["Thepla", "Methi Thepla"],
        "search_terms": "thepla methi thepla indian street food"
    },
    {
        "name": "Khaman",
        "description": "Soft, spongy savory cake made from gram flour and yogurt.",
        "slang": ["Khaman", "Khaman Dhokla"],
        "search_terms": "khaman dhokla indian street food"
    },
    {
        "name": "Fafda",
        "description": "Crispy, crunchy snack made from gram flour and carom seeds.",
        "slang": ["Fafda", "Gujarati Fafda"],
        "search_terms": "fafda gujarati indian street food"
    },
    {
        "name": "Poha",
        "description": "Flattened rice cooked with onions, potatoes, and mild spices.",
        "slang": ["Poha", "Kanda Poha"],
        "search_terms": "poha indian street food"
    },
    {
        "name": "Upma",
        "description": "Semolina cooked with vegetables and mild spices.",
        "slang": ["Upma", "Uppittu"],
        "search_terms": "upma indian street food"
    },
    {
        "name": "Idli",
        "description": "Steamed rice cakes made from fermented rice and lentil batter.",
        "slang": ["Idli", "Idly"],
        "search_terms": "idli idly indian street food"
    },
    {
        "name": "Vada",
        "description": "Crispy, deep-fried lentil fritters with a soft center.",
        "slang": ["Vada", "Medu Vada"],
        "search_terms": "vada medu vada indian street food"
    },
    {
        "name": "Uttapam",
        "description": "Thick pancake made from fermented rice and lentil batter with vegetables.",
        "slang": ["Uttapam", "Uthappam"],
        "search_terms": "uttapam uthappam indian street food"
    },
    {
        "name": "Pongal",
        "description": "Rice and lentil dish cooked with ghee, pepper, and cumin.",
        "slang": ["Pongal", "Ven Pongal"],
        "search_terms": "pongal indian street food"
    },
    {
        "name": "Biryani",
        "description": "Aromatic rice dish cooked with meat, vegetables, and fragrant spices.",
        "slang": ["Biryani", "Briyani"],
        "search_terms": "biryani indian street food"
    },
    
    # Sweet Items
    {
        "name": "Jalebi",
        "description": "Crispy, spiral-shaped sweet made from deep-fried flour batter soaked in sugar syrup.",
        "slang": ["Jalebi", "Jilapi"],
        "search_terms": "jalebi jilapi indian street food"
    },
    {
        "name": "Gulab Jamun",
        "description": "Soft, spongy milk-solid balls soaked in rose-flavored sugar syrup.",
        "slang": ["Gulab Jamun", "Gulab Jam"],
        "search_terms": "gulab jamun indian street food"
    },
    {
        "name": "Rasgulla",
        "description": "Soft, spongy cottage cheese balls soaked in light sugar syrup.",
        "slang": ["Rasgulla", "Rasgola"],
        "search_terms": "rasgulla rasgola indian street food"
    },
    {
        "name": "Imarti",
        "description": "Flower-shaped sweet made from urad dal flour, deep-fried and soaked in syrup.",
        "slang": ["Imarti", "Jangiri"],
        "search_terms": "imarti jangiri indian street food"
    },
    {
        "name": "Malpua",
        "description": "Sweet pancake made from flour, milk, and sugar, deep-fried and soaked in syrup.",
        "slang": ["Malpua", "Malpoa"],
        "search_terms": "malpua malpoa indian street food"
    },
    {
        "name": "Balushahi",
        "description": "Flaky, layered sweet pastry made from flour and ghee, soaked in sugar syrup.",
        "slang": ["Balushahi", "Badusha"],
        "search_terms": "balushahi badusha indian street food"
    },
    {
        "name": "Kaju Katli",
        "description": "Diamond-shaped sweet made from cashew nuts, sugar, and ghee.",
        "slang": ["Kaju Katli", "Kaju Barfi"],
        "search_terms": "kaju katli kaju barfi indian street food"
    },
    {
        "name": "Besan Ladoo",
        "description": "Round sweet balls made from gram flour, ghee, and sugar.",
        "slang": ["Besan Ladoo", "Besan Laddu"],
        "search_terms": "besan ladoo besan laddu indian street food"
    },
    {
        "name": "Mysore Pak",
        "description": "Rich sweet made from gram flour, ghee, and sugar, originating from Mysore.",
        "slang": ["Mysore Pak", "Mysorepa"],
        "search_terms": "mysore pak mysorepa indian street food"
    },
    {
        "name": "Rava Ladoo",
        "description": "Sweet balls made from semolina, coconut, and sugar.",
        "slang": ["Rava Ladoo", "Rava Laddu"],
        "search_terms": "rava ladoo rava laddu indian street food"
    },
    {
        "name": "Coconut Ladoo",
        "description": "Sweet balls made from fresh coconut, sugar, and cardamom.",
        "slang": ["Coconut Ladoo", "Nariyal Laddu"],
        "search_terms": "coconut ladoo nariyal laddu indian street food"
    },
    {
        "name": "Til Ladoo",
        "description": "Sweet balls made from sesame seeds, jaggery, and nuts.",
        "slang": ["Til Ladoo", "Til Laddu"],
        "search_terms": "til ladoo til laddu indian street food"
    },
    {
        "name": "Moti Choor",
        "description": "Sweet made from tiny pearl-like balls of gram flour, soaked in sugar syrup.",
        "slang": ["Moti Choor", "Moti Chur"],
        "search_terms": "moti choor moti chur indian street food"
    },
    {
        "name": "Ghevar",
        "description": "Honeycomb-like sweet made from flour, deep-fried and soaked in sugar syrup.",
        "slang": ["Ghevar", "Ghewar"],
        "search_terms": "ghevar ghewar indian street food"
    },
    {
        "name": "Petha",
        "description": "Sweet made from ash gourd, flavored with rose water and cardamom.",
        "slang": ["Petha", "Agra Petha"],
        "search_terms": "petha agra petha indian street food"
    },
    {
        "name": "Kalakand",
        "description": "Sweet made from milk solids, sugar, and flavored with cardamom.",
        "slang": ["Kalakand", "Milk Cake"],
        "search_terms": "kalakand milk cake indian street food"
    },
    {
        "name": "Cham Cham",
        "description": "Cylindrical sweet made from cottage cheese, soaked in sugar syrup.",
        "slang": ["Cham Cham", "Chom Chom"],
        "search_terms": "cham cham chom chom indian street food"
    },
    {
        "name": "Pantua",
        "description": "Deep-fried sweet made from cottage cheese and semolina, soaked in syrup.",
        "slang": ["Pantua", "Langcha"],
        "search_terms": "pantua langcha indian street food"
    },
    {
        "name": "Ledikeni",
        "description": "Sweet made from cottage cheese and semolina, named after Lady Canning.",
        "slang": ["Ledikeni", "Lady Kenny"],
        "search_terms": "ledikeni lady kenny indian street food"
    },
    {
        "name": "Sandesh",
        "description": "Sweet made from fresh cottage cheese and sugar, often flavored with cardamom.",
        "slang": ["Sandesh", "Sondesh"],
        "search_terms": "sandesh sondesh indian street food"
    },
    {
        "name": "Laddu",
        "description": "Round sweet balls made from flour, sugar, and ghee.",
        "slang": ["Laddu", "Ladoo"],
        "search_terms": "laddu ladoo indian street food"
    },
    {
        "name": "Barfi",
        "description": "Sweet fudge-like dessert made from condensed milk and sugar.",
        "slang": ["Barfi", "Burfi"],
        "search_terms": "barfi burfi indian street food"
    },
    {
        "name": "Peda",
        "description": "Sweet made from khoya (dried milk) and sugar, often flavored with cardamom.",
        "slang": ["Peda", "Milk Peda"],
        "search_terms": "peda indian street food"
    },
    {
        "name": "Modak",
        "description": "Sweet dumplings made from rice flour and coconut-jaggery filling.",
        "slang": ["Modak", "Ukadiche Modak"],
        "search_terms": "modak indian street food"
    },
    {
        "name": "Puran Poli",
        "description": "Sweet flatbread stuffed with sweetened lentil filling.",
        "slang": ["Puran Poli", "Bobbatlu"],
        "search_terms": "puran poli bobbatlu indian street food"
    },
    {
        "name": "Shrikhand",
        "description": "Sweet strained yogurt flavored with cardamom and saffron.",
        "slang": ["Shrikhand", "Srikhand"],
        "search_terms": "shrikhand srikhand indian street food"
    },
    {
        "name": "Basundi",
        "description": "Sweet thickened milk dessert flavored with cardamom and nuts.",
        "slang": ["Basundi", "Rabdi"],
        "search_terms": "basundi rabdi indian street food"
    },
    {
        "name": "Kheer",
        "description": "Rice pudding made with milk, sugar, and flavored with cardamom.",
        "slang": ["Kheer", "Payasam"],
        "search_terms": "kheer payasam indian street food"
    },
    
    # Drinks and Beverages
    {
        "name": "Lassi",
        "description": "Sweet or salty yogurt-based drink, often flavored with fruits or spices.",
        "slang": ["Lassi", "Sweet Lassi"],
        "search_terms": "lassi indian street food drink"
    },
    {
        "name": "Masala Chai",
        "description": "Spiced tea made with milk, ginger, cardamom, and other aromatic spices.",
        "slang": ["Chai", "Masala Tea"],
        "search_terms": "masala chai indian street food"
    },
    {
        "name": "Kulfi",
        "description": "Traditional Indian ice cream made with thickened milk and cardamom.",
        "slang": ["Kulfi", "Kulfi Falooda"],
        "search_terms": "kulfi indian street food"
    },
    {
        "name": "Falooda",
        "description": "Sweet dessert drink with vermicelli, rose syrup, and ice cream.",
        "slang": ["Falooda", "Faluda"],
        "search_terms": "falooda faluda indian street food"
    },
    
    # Regional Specialties
    {
        "name": "Gajar Ka Halwa",
        "description": "Sweet carrot pudding made with grated carrots, milk, and sugar.",
        "slang": ["Gajar Halwa", "Carrot Halwa"],
        "search_terms": "gajar halwa carrot halwa indian street food"
    },
    {
        "name": "Rasmalai",
        "description": "Soft cottage cheese patties soaked in sweetened, thickened milk.",
        "slang": ["Rasmalai", "Ras Malai"],
        "search_terms": "rasmalai indian street food"
    },
    {
        "name": "Misti Doi",
        "description": "Sweetened yogurt dessert, often served in earthen pots.",
        "slang": ["Misti Doi", "Sweet Curd"],
        "search_terms": "misti doi sweet curd indian street food"
    },
    {
        "name": "Bhapa Doi",
        "description": "Steamed sweet yogurt dessert, flavored with cardamom and saffron.",
        "slang": ["Bhapa Doi", "Steamed Yogurt"],
        "search_terms": "bhapa doi steamed yogurt indian street food"
    },
    {
        "name": "Chhena Poda",
        "description": "Baked sweet made from cottage cheese, sugar, and cardamom.",
        "slang": ["Chhena Poda", "Burnt Cheese"],
        "search_terms": "chhena poda burnt cheese indian street food"
    },
    {
        "name": "Chhena Gaja",
        "description": "Sweet made from cottage cheese and semolina, deep-fried and soaked in syrup.",
        "slang": ["Chhena Gaja", "Cheese Gaja"],
        "search_terms": "chhena gaja cheese gaja indian street food"
    },
    {
        "name": "Chhena Jhili",
        "description": "Sweet made from cottage cheese, deep-fried and soaked in sugar syrup.",
        "slang": ["Chhena Jhili", "Cheese Jhili"],
        "search_terms": "chhena jhili cheese jhili indian street food"
    },
    {
        "name": "Chhena Kheeri",
        "description": "Sweet rice pudding made with cottage cheese, milk, and sugar.",
        "slang": ["Chhena Kheeri", "Cheese Kheer"],
        "search_terms": "chhena kheeri cheese kheer indian street food"
    },
    {
        "name": "Chhena Pitha",
        "description": "Sweet dumplings made from cottage cheese and rice flour.",
        "slang": ["Chhena Pitha", "Cheese Pitha"],
        "search_terms": "chhena pitha cheese pitha indian street food"
    },
    {
        "name": "Chhena Tarkari",
        "description": "Sweet curry made from cottage cheese in sugar syrup.",
        "slang": ["Chhena Tarkari", "Cheese Curry"],
        "search_terms": "chhena tarkari cheese curry indian street food"
    },
    {
        "name": "Chhena Bara",
        "description": "Sweet fritters made from cottage cheese, deep-fried and soaked in syrup.",
        "slang": ["Chhena Bara", "Cheese Bara"],
        "search_terms": "chhena bara cheese bara indian street food"
    },
    {
        "name": "Chhena Chakuli",
        "description": "Sweet pancakes made from cottage cheese and rice flour.",
        "slang": ["Chhena Chakuli", "Cheese Chakuli"],
        "search_terms": "chhena chakuli cheese chakuli indian street food"
    },
    {
        "name": "Chhena Malpua",
        "description": "Sweet pancakes made from cottage cheese, flour, and sugar.",
        "slang": ["Chhena Malpua", "Cheese Malpua"],
        "search_terms": "chhena malpua cheese malpua indian street food"
    }
]

# Fusion foods for special rounds
FUSION_FOODS = [
    "Pizza Dosa",
    "Burger Samosa", 
    "Taco Puri",
    "Sushi Chaat",
    "Pasta Bhel",
    "Noodle Dosa",
    "Sandwich Chaat",
    "Wrap Tikki",
    "Burrito Pav",
    "Hot Dog Puri"
]

def get_food_count():
    """Return the total number of foods in the dataset"""
    return len(STREET_FOODS)

def get_food_by_category(category):
    """Get foods by category (savory, sweet, drinks, regional)"""
    categories = {
        'savory': STREET_FOODS[:25],  # First 25 are savory
        'sweet': STREET_FOODS[25:50],  # Next 25 are sweet
        'drinks': STREET_FOODS[50:54],  # Next 4 are drinks
        'regional': STREET_FOODS[54:]   # Rest are regional
    }
    return categories.get(category, STREET_FOODS)

def get_random_fusion_food():
    """Get a random fusion food for special rounds"""
    import random
    return random.choice(FUSION_FOODS)

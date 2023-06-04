'''
As you can see, this is a work in progress. It is perfectly functional, but it
isn't particularity clean.

I'd like to merge all three of these lists into a single, multi-dimensional
list. I'd deal less with less unrolling in for loops and what not. Plus, less
tag/keyword/exclusion addition management.

There are issues. If a keyword meets an exclusion, the entire recipe will be
skipped rather than going onto the other keyword. This will inevitably cause
Spatula to miss out on perfectly valid recipes. This'll have to be fixed.

For now, it works decently, even though it's too picky. I can spare a few missed
recipes (for now).
'''

def generateTags(String):
    counter = 0
    tag_string = ""

    tags = [
        "Appetizers and Snacks,,",
        "Breakfast and Brunch,,",
        "Desserts,,",
        "Dinner,,",
        "Drinks,,",
        "Breads,,",
        "Cakes,,",
        "Salads,,",
        "Smoothies,,",
        "Soup,,",
        "Beef,,",
        "Chicken,,",
        "Pasta,,",
        "Pork,,",
        "Salmon,,",
        "BBQ,,",
        "Quick,,",
        "Slow Cooker,,",
        "Vegan,,",
        "Vegetarian,,",
        "Diabetic,,",
        "Gluten,,",
        "Healthy,,",
        "Low Calorie,,",
        "Low Fat,,",
        "Asian,,",
        "Indian,,",
        "Italian,,",
        "Mexican,,",
        "Southern,,"
    ]

    keywords = [
        ["appetizer", "snack"],
        ["breakfast", "brunch"],
        ["cakes", "candies", "candy", "confectionery", "cookie", "custard", "doughnut", "ice cream", "pastry", "pasteries", "pie", "pies", "pudding", "tart"],
        ["dinner"],
        ["smoothie", "vodka", "whiskey", "liquor", "alcohol", "beer", "water", "juice", "gin", "rum", "tea", "coffee", "latte", "tequila"],
        ["bread"],
        ["cake"],
        ["salad"],
        ["smoothie"],
        ["soup", "stew", "chili", "goulash"],
        ["beef"],
        ["chicken"],
        ["agnolotti", "calamarata", "cannelloni", "caramelle", "conchiglie", "farfalle", "fettuccine", "fiori", "fusilli", "gemelli", "gnocchi", "gnudi", "linguine", "macaroni", "orecchiette", "pappardelle", "pasta", "penne", "pizzoccheri", "ravioli", "reginette", "rigatoni", "rotini", "spaghetti", "stelline", "tagliatelle", "tortellini", "trofie", "tufoli", "vermicelli", "ziti"],
        ["pork"],
        ["salmon"],
        ["bbq", "grill"],
        ["easy", "quick", "effortless", "simple", "low effort", "basic", "frill"],
        ["slow cooker", "charcoal"],
        ["vegan", "no-meat", "herbivorous", "herbivore", "meatless"],
        ["vegetarian", "vegetarianism", "no-meat", "herbivorous", "herbivore", "meatless"],
        ["diabetic", "diabetes", "low-sugar", "sugar-free", "low sugar", "sugar free"],
        ["gluten", "gluten free", "celiac", "gluten-free"],
        ["health", "mindful"],
        ["low calorie", "calorie"],
        ["fat", "low fat"],
        ["asia", "china", "chinese", "filip", "india", "japan", "philippines", "taiwan", "vietnam", "mongol", "korea", "burmese", "hong kong", "malay"],
        ["india", "bangladesh", "bengali"],
        ["italy", "italian"],
        ["mexican", "mexico"],
        ["southern", "florida", "georgia", "maryland", "north carolina", "south carolina", "virginia", "west virginia", "delaware", "alabama", "kentucky", "mississippi", "tennessee", "arkansas", "louisiana", "oklahoma", "texas"]
    ]

    exemptions = [
        [""],
        [""],
        [""],
        [""],
        ["beer batter"],
        ["gingerbread"],
        [""],
        [""],
        [""],
        [""],
        [""],
        [""],
        [""],
        [""],
        [""],
        [""],
        [""],
        [""],
        [""],
        [""],
        [""],
        [""],
        [""],
        [""],
        [""],
        [""],
        [""],
        [""],
        [""],
        [""] 
    ]

    for tag in tags:
        for keyword in keywords[counter]:
            for exemption in exemptions[counter]:
                if exemption:
                    if exemption in String.lower():
                        print(f"Exempting tag string: {exemption}")
                        return
            if keyword in String.lower() and not exemption:
                tag_string = tag_string + tag
                break
        counter = counter + 1

    if tag_string:
        print(f"Tags: {tag_string}")
        return tag_string
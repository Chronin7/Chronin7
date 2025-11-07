import util_functions
food_items={
    "main course":{
        "cheese":{
            "cost":67,
            "variations":{
                "american cheese":2,
                "asiago cheese":17,
                "blue cheese":18,
                "bocconcini cheese":14,
                "brie cheese":3,
                "burrata cheese":6,
                "camembert cheese":16,
                "cheddar cheese":14,
                "cheese curds":18,
                "colby cheese":12,
                "colby-jack cheese":12,
                "cold-pack cheese":13,
                "cotija cheese":19,
                "cottage cheese":13,
                "cream cheese":17,
                "emmental cheese":12,
                "farmer's cheese":5,
                "feta cheese":21,
                "fresh mozzarella cheese":15,
                "gorgonzola cheese":10,
                "gouda cheese":7132,
                "gruyere cheese":32,
                "halloumi cheese":12,
                "havarti cheese":16,
                "jarlsberg cheese":15,
                "limburger cheese":13,
                "mascarpone cheese":11,
                "monterey jack cheese":18,
                "mozzarella cheese":17,
                "muenster cheese":14,
                "neufchatel cheese":14,
                "paneer cheese":17,
                "parmesan cheese":14,
                "pepper jack cheese":21,
                "provolone cheese":18,
                "ricotta cheese":18,
                "romano cheese":15,
                "string cheese":11,
                "swiss cheese":10,
                "tetilla cheese":19,
                "white american cheese":12,
                "white cheddar cheese":14,
                "yellow american cheese":13,
                "yellow cheddar cheese":15
            }
        },
        "hamburger":{
            "cost":5,
            "variations":{
                "cheeseburger":4,
                "everything burger":8
            }
        },
        "chicken":{
            "cost":4,
            "variations":{
                "chicken nugets":3,
                "chicken wings":6,
                "chicken tikka masala":12
            }
        },
        "pho":{
            "cost":15,
            "variations":{
                None:None
            }
        },
        "squid":{
            "cost":21,
            "variations":{
                None:None
            }
        },
        "poutine":{
            "cost":15,
            "variations":{
                None:None
            }
        },
        "clams":{
            "cost":15,
            "variations":{
                None:None
            }
        },
        "fish":{
            "cost":15,
            "variations":{
                "carp":15,
                "pike":12,
                "shehorse":17,
                "goldfish":10,
                "shark":72
            }
        },
        "other":{
            "cost":0,
            "variations":{
                "prime rib":0
            }
        }
    },
    "sides":{
        "computer parts":{
            "cost":150,
            "variations":{
                "cpu":75,
                "gpu":120,
                "ram":60,
                "motherboard":90,
                "power supply":50,
                "ssd":80,
                "hdd":70,
                "cooling fan":40,
                "case":55
            }
        },
        "fries":{
            "cost":15,
            "variations":{
                "curly fries":1,
                "waffle fries":4,
                "crinkle fries":7,
                "cactus frys":15
            }
        },
        "rice":{
            "cost":0.0000046,
            "variations":{
                None:None
            }
        },
        "mac & cheese":{
            "cost":15,
            "variations":{
                "extra cheese & mac":5,
                "bacon mac & cheese ":7
            }
        },
        "biscuits":{
            "cost":11,
            "variations":{
                "cheese biscuits":3,
                "herb biscuits":4
            }
        },
        "peta bread":{
            "cost":13,
            "variations":{
                None:None
            }
        },
        "cornbred":{
            "cost":11,
            "variations":{
                "honey cornbred":4,
                "cheese cornbred":5
            },
        "cheese":{
            "cost":67,
            "variations":{
                "american cheese":2,
                "asiago cheese":17,
                "blue cheese":18,
                "bocconcini cheese":14,
                "brie cheese":3,
                "burrata cheese":6,
                "camembert cheese":16,
                "cheddar cheese":14,
                "cheese curds":18,
                "colby cheese":12,
                "colby-jack cheese":12,
                "cold-pack cheese":13,
                "cotija cheese":19,
                "cottage cheese":13,
                "cream cheese":17,
                "emmental cheese":12,
                "farmer's cheese":5,
                "feta cheese":21,
                "fresh mozzarella cheese":15,
                "gorgonzola cheese":10,
                "gouda cheese":7132,
                "gruyere cheese":32,
                "halloumi cheese":12,
                "havarti cheese":16,
                "jarlsberg cheese":15,
                "limburger cheese":13,
                "mascarpone cheese":11,
                "monterey jack cheese":18,
                "mozzarella cheese":17,
                "muenster cheese":14,
                "neufchatel cheese":14,
                "paneer cheese":17,
                "parmesan cheese":14,
                "pepper jack cheese":21,
                "provolone cheese":18,
                "ricotta cheese":18,
                "romano cheese":15,
                "string cheese":11,
                "swiss cheese":10,
                "tetilla cheese":19,
                "white american cheese":12,
                "white cheddar cheese":14,
                "yellow american cheese":13,
                "yellow cheddar cheese":15
            }
        },
        },
        "chips":{
            "cost":15,
            "variations":{
                "potato chips":3,
                "tortilla chips":4,
                "veggie chips":5
            }
        },
        "corn":{
            "cost":15,
            "variations":{
                "buttered corn":3,
                "seasoned corn":4
            }
        },
        "the arcane arts":{
            "cost":15,
            "variations":{
                "dark magic":50,
                "light magic":45,
                "chaos magic":60,
                "nature magic":30,
                "blood magic":70,
                "spirit magic":40,
                "time magic":80,
                "space magic":90,
                "mind magic":55,
                "soul magic":65,
                "elemental magic":75,
                "ancient magic":100,
                "forbidden magic":120,
                "divine magic":110,
                "necromancy":130,
                "illusion magic":35,
                "transmutation magic":85,
                "enchantment magic":95,
                "summoning magic":105,
                "alchemy":115
            }
        },
        "lime":{
            "cost":15,
            "variations":{
                "key lime":4,
                "persian lime":5
            }
        },
        "meme":{
            "cost":15,
            "variations":{
                "dank meme":10,
                "wholesome meme":8,
                "surreal meme":12
            }
        },
    },
    "drinks":{
        "soda":{
            "cost":15,
            "variations":{
                "cola":3,
                "lemon-lime":4,
                "root beer":5,
                "orange soda":6,
                "grape soda":7,
                "cream soda":8,
                "ginger ale":9,
                "club soda":10,
                "sprite":11,
                "fanta":12,
                "mountain dew":13,
                "dr pepper":14
            }
        },
        "fruit juice":{
            "cost":15,
            "variations":{
                "apple juice":3,
                "orange juice":4,
                "grape juice":5,
                "cranberry juice":6,
                "pineapple juice":7,
                "mango juice":8,
                "pomegranate juice":9,
                "watermelon juice":10
            }
        },
        "water":{
            "cost":1,
            "variations":{
                "sparkling water":2,
                "mineral water":3,
                "flavored water":4
            }
        },
        "cheese":{
            "cost":67,
            "variations":{
                "american cheese":2,
                "asiago cheese":17,
                "blue cheese":18,
                "bocconcini cheese":14,
                "brie cheese":3,
                "burrata cheese":6,
                "camembert cheese":16,
                "cheddar cheese":14,
                "cheese curds":18,
                "colby cheese":12,
                "colby-jack cheese":12,
                "cold-pack cheese":13,
                "cotija cheese":19,
                "cottage cheese":13,
                "cream cheese":17,
                "emmental cheese":12,
                "farmer's cheese":5,
                "feta cheese":21,
                "fresh mozzarella cheese":15,
                "gorgonzola cheese":10,
                "gouda cheese":7132,
                "gruyere cheese":32,
                "halloumi cheese":12,
                "havarti cheese":16,
                "jarlsberg cheese":15,
                "limburger cheese":13,
                "mascarpone cheese":11,
                "monterey jack cheese":18,
                "mozzarella cheese":17,
                "muenster cheese":14,
                "neufchatel cheese":14,
                "paneer cheese":17,
                "parmesan cheese":14,
                "pepper jack cheese":21,
                "provolone cheese":18,
                "ricotta cheese":18,
                "romano cheese":15,
                "string cheese":11,
                "swiss cheese":10,
                "tetilla cheese":19,
                "white american cheese":12,
                "white cheddar cheese":14,
                "yellow american cheese":13,
                "yellow cheddar cheese":15
            }
        }
    }
}

def print_option(option_chosen, detail_depth):
    if detail_depth == 0:
        print(option_chosen)
    elif detail_depth == 1:
        print(f"{option_chosen}")
    elif detail_depth == 2:
        print(f"{option_chosen}:")
        for item, details in food_items[option_chosen].items():
            print(f"  {item} - Cost: {details['cost']}")
            if details['variations'] and next(iter(details['variations'])) is not None:
                print("   Variations:")
                for variation, variation_cost in details['variations'].items():
                    print(f"    {variation} - Additional Cost: {variation_cost}")
def main():
    print("Welcome to the Food Ordering System!")
    print("Here are the available food items:")
    order = []
    while True:
        valid_categories = list(food_items.keys())
        print("\nAvailable categories:")
        for i, category in enumerate(valid_categories, 1):
            print(f"{i}. {category}")
            
        category = None
        while category is None:
            user_input = input("\nPlease enter the exact name of the category you want to order from: ").strip()
            if user_input in valid_categories:
                category = user_input
            else:
                print("\nInvalid category. Please choose from:")
                for cat in valid_categories:
                    print(f"- {cat}")
        print(f"\nItems in {category}:")
        valid_items = list(food_items[category].keys())
        for i, item_name in enumerate(valid_items, 1):
            item_details = food_items[category][item_name]
            print(f"{i}. {item_name} - Base Cost: ${item_details['cost']}")
            variations = item_details['variations']
            if variations and next(iter(variations)) is not None:
                print("   Variations:")
                for var_name, var_cost in variations.items():
                    print(f"    - {var_name} (Additional Cost: ${var_cost})")
            
        item = None
        variation = None
        while item is None:
            user_input = input("\nPlease enter the exact name of the item you want to order: ").strip()
            if user_input in valid_items:
                item = user_input
                # Check if item has variations
                variations = food_items[category][item]['variations']
                if variations and next(iter(variations)) is not None:
                    print("\nAvailable variations for", item + ":")
                    for var_name, var_cost in variations.items():
                        print(f"- {var_name} (Additional Cost: ${var_cost})")
                    
                    while variation is None:
                        var_input = input("\nPlease enter the exact name of the variation you want (or press Enter for no variation): ").strip()
                        if not var_input:  # If user just presses Enter
                            break
                        if var_input in variations:
                            variation = var_input
                        else:
                            print("\nInvalid variation. Please choose from the list above or press Enter for no variation.")
            else:
                print("\nInvalid item. Please choose from:")
                for valid_item in valid_items:
                    print(f"- {valid_item}")
                    
        order.append((category, item, variation))
        
        while True:
            user_input = input("\nWould you like to order more items? (yes/no): ").strip().lower()
            if user_input in ['yes', 'no']:
                more = user_input
                break
            else:
                print("\nPlease enter either 'yes' or 'no'")
                
        if more == "no":
            break
    total_cost = 0
    print("\nYour order summary:")
    for category, item, variation in order:
        item_details = food_items[category][item]
        item_cost = item_details['cost']
        variation_cost = 0
        
        if variation:
            variation_cost = item_details['variations'][variation]
            print(f"{item} ({variation}) from {category} - Base Cost: ${item_cost}, Variation Cost: ${variation_cost}")
        else:
            print(f"{item} from {category} - Cost: ${item_cost}")
            
        total_cost += item_cost + variation_cost
    print(f"\nTotal Cost of your order: ${total_cost}")
if __name__=="__main__":
    main()
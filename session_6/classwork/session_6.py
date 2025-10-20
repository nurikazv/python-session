# # Dictionary

# d = {}

# d['test'] = "test_word"

# d["test2"] = 'hello_world'

# d.pop('test')

# print(d.values())

# functions: add value to dictionary 
# del 
# values()
# items()
# keys()


product_data = {
    "store": "TechNova",
    "location": {
        "city": "San Francisco",
        "country": "USA"
    },
    "products": [
        {
            "id": "P1001",
            "name": "Wireless Mouse",
            "brand": "LogiTech",
            "price": 29.99,
            "currency": "USD",
            "stock": 134,
            "specs": {
                "color": "Black",
                "connectivity": "Bluetooth",
                "battery_life": "12 months"
            },
            "ratings": {
                "average": 4.5,
                "count": 240
            }
        },
        {
            "id": "P1002",
            "name": "Mechanical Keyboard",
            "brand": "KeyChron",
            "price": 79.99,
            "currency": "USD",
            "stock": 57,
            "specs": {
                "color": "White",
                "switch_type": "Gateron Brown",
                "backlight": "RGB"
            },
            "ratings": {
                "average": 4.7,
                "count": 145
            }
        },
        {
            "id": "P1003",
            "name": "Sony Wireless Noise-Canceling Headphones",
            "brand": "Sony",
            "price": 199.99,
            "currency": "USD",
            "stock": 23,
            "specs": {
                "color": "Black",
                "connectivity": "Bluetooth",
                "noise_cancellation": "Active",
                "battery_life": "30 hours"
            },
            "ratings": {
                "average": 4.8,
                "count": 529
            }
        }
    ]
}


# for product in product_data["products"]:
#     if product["price"] > 50 and product["ratings"]["average"] > 4.5:
#         print(product["name"], product["price"], product["ratings"]["average"], sep=" - ")


# task 1
# for product in product_data["products"]:
#     print(f"{product_data['store']} has the following items available: ")
#     print (product['name'])

# task 2

# for product in product_data["products"]:
#     print(product["brand"], product["ratings"]["average"] ,sep=":")


# task 3

# print(product_data["products"][0]["specs"]["color"])

inp_col = input("Color: ")
count = 0

for product in product_data["products"]:
    if product["specs"]["color"] == inp_col:
        print(f"{product['name']} {product['brand']}")
        count += 1

if count == 0:
    print("nothing available")
print(count)


# if count:
#     for item in matches:
#         print(item)
# else:
#     print("nothing available")

# print(inp_col)
# print(f"{count}")


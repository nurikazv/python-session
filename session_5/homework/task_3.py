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
        },
        {
            "id": "P1001",
            "name": "Wireless charger",
            "brand": "LogiTech",
            "price": 29.99,
            "currency": "USD",
            "stock": 0,
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
            "id": "P1001",
            "name": "Bluetooth Speaker",
            "brand": "LogiTech",
            "price": 29.99,
            "currency": "USD",
            "stock": 0,
            "specs": {
                "color": "Black",
                "connectivity": "Bluetooth",
                "battery_life": "12 months"
            },
            "ratings": {
                "average": 4.5,
                "count": 240
            }
        }
    ]
}


# Task 3: List Products Over $50 with High Rating
# Print the name, price, and average rating of products where 
# the price is greater than $50 and the average rating is above 4.5.
# Example Output:
#  Mechanical Keyboard - $79.99 - Rating: 4.7
#  Noise-Canceling Headphones - $199.99 - Rating: 4.8

for product in product_data["products"]:
    if product["price"] > 50 and product["ratings"]["average"] > 4.5:
        print(product["name"], product["price"], product["ratings"]["average"], sep=" - ")
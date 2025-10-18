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
# Below are the tasks you need to complete using the data structure provided above.
# If you have any questions, please feel free to reach out. Good luck :akumosolutions:
# Task 1: Print this following message by getting values from the dictionary
# Message: Company TechNova is located in San Francisco, USA.


print(f"Company {product_data['store']} is located in {product_data['location']['city']}, {product_data['location']['country']}.")


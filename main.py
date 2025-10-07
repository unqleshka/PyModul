purchases = [
        {"item": "apple", "category": "fruit", "price": 1.2, "quantity": 10},
        {"item": "banana", "category": "fruit", "price": 0.5, "quantity": 5},
        {"item": "milk", "category": "dairy", "price": 1.5, "quantity": 2},
        {"item": "bread", "category": "bakery", "price": 2.0, "quantity": 3},
]

def total_revenue(d: list):
    total_sum = 0
    for item in d:
        total_sum += item["price"]* item["quantity"]
    print(f"Общая выручка: {total_sum}")

def items_by_category(d: list):
    dict_items_by_category = dict()
    for item in d:
        if item["category"] in dict_items_by_category:
            if item["item"] not in dict_items_by_category[item["category"]]:
                dict_items_by_category[item["category"]].append(item["item"])
        else:
            dict_items_by_category[item["category"]] = [item["item"]]
    print(f"Товары по категориям: {dict_items_by_category}")

def expensive_purchases(d: list, min_price: float):
    exp_purchases = list()
    for item in d:
        if item["price"] > min_price:
            exp_purchases.append(item)
    print(f"Покупки дороже {min_price}: {exp_purchases}")

def average_price_by_category(d: list):
    dict_avg = dict()
    result = dict()
    for item in d:
        if item["category"] in dict_avg:
            if item["price"] not in dict_avg[item["category"]]:
                dict_avg[item["category"]].append(item["price"])
        else:
            dict_avg[item["category"]] = [item["price"]]
    for category, prices in dict_avg.items():
        avg_price = sum(prices) / len(prices)
        result[category] = avg_price
    print(f"Средняя цена по категориям: {result}")

def most_frequent_category(d:list):
    max_quantity = float("-inf")
    category = ''
    for item in d:
        if item["quantity"] > max_quantity:
            max_quantity = item["quantity"]
            category = item["category"]
    print(f"Категория с наибольшим количеством проданных товаров: {category}")

total_revenue(purchases)
items_by_category(purchases)
expensive_purchases(purchases, 1)
average_price_by_category(purchases)
most_frequent_category(purchases)
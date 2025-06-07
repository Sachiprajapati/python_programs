# The following company details are given for analysis: customer acc no, customer 
# name, purchased product no, product category, unit price. Marketing is interested 
# in understanding customer purchase patterns. Find the answers of following 
# questions:  
# How many customers have purchased bread?  
# How many customers have purchased butter? 
# How many customers have purchased bread and butter? 
# Who has purchased bread but not butter? 
# Which customers have purchased bread, butter and milk? 
# Print the name of the most valuable customers who have 
#  purchased all three items. 


from collections import defaultdict

data = [
    {"acc_no": 1, "name": "Alice", "product_no": 101, "category": "bread", "unit_price": 2.0},
    {"acc_no": 1, "name": "Alice", "product_no": 102, "category": "butter", "unit_price": 3.0},
    {"acc_no": 2, "name": "Bob", "product_no": 101, "category": "bread", "unit_price": 2.0},
    {"acc_no": 2, "name": "Bob", "product_no": 103, "category": "milk", "unit_price": 1.5},
    {"acc_no": 3, "name": "Charlie", "product_no": 102, "category": "butter", "unit_price": 3.0},
    {"acc_no": 3, "name": "Charlie", "product_no": 103, "category": "milk", "unit_price": 1.5},
    {"acc_no": 4, "name": "David", "product_no": 101, "category": "bread", "unit_price": 2.0},
    {"acc_no": 4, "name": "David", "product_no": 102, "category": "butter", "unit_price": 3.0},
    {"acc_no": 4, "name": "David", "product_no": 103, "category": "milk", "unit_price": 1.5},
    {"acc_no": 5, "name": "Eva", "product_no": 101, "category": "bread", "unit_price": 2.0},
    {"acc_no": 5, "name": "Eva", "product_no": 102, "category": "butter", "unit_price": 3.0},
]

customer_purchases = defaultdict(set)
customer_spending = defaultdict(float)

for entry in data:
    acc_no = entry["acc_no"]
    name = entry["name"]
    category = entry["category"]
    unit_price = entry["unit_price"]
    
    customer_purchases[acc_no].add(category)
    customer_spending[acc_no] += unit_price

customers_bread = {acc_no for acc_no, products in customer_purchases.items() if "bread" in products}
customers_butter = {acc_no for acc_no, products in customer_purchases.items() if "butter" in products}
customers_milk = {acc_no for acc_no, products in customer_purchases.items() if "milk" in products}

customers_bread_butter = customers_bread & customers_butter
customers_bread_butter_milk = customers_bread & customers_butter & customers_milk
customers_bread_not_butter = customers_bread - customers_butter

acc_to_name = {entry["acc_no"]: entry["name"] for entry in data}

print("Customers who purchased bread:", len(customers_bread))
print("Customers who purchased butter:", len(customers_butter))
print("Customers who purchased bread and butter:", len(customers_bread_butter))
print("Customers who purchased bread but not butter:", [acc_to_name[acc] for acc in customers_bread_not_butter])
print("Customers who purchased bread, butter, and milk:", [acc_to_name[acc] for acc in customers_bread_butter_milk])

most_valuable_customers = sorted(customers_bread_butter_milk, key=lambda acc: customer_spending[acc], reverse=True)

print("Most valuable customers who purchased bread, butter, and milk:", [acc_to_name[acc] for acc in most_valuable_customers])

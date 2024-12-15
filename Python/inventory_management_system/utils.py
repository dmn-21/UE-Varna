def calculate_total_value(inventory):
    return sum(int(item["Quantity"]) * float(item["Price"]) for item in inventory)

def generate_category_summary(inventory):
    summary = {}
    for item in inventory:
        category = item["Category"]
        quantity = int(item["Quantity"])
        summary[category] = summary.get(category, 0) + quantity
    return summary
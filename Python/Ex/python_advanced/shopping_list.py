def shopping_list(budget, **kwargs):
    if budget < 100:
        return "You do not have enough budget."

    bought_products = 0
    result = ''
    for product, value in kwargs.items():
        total_cost = float(value[0]) * int(value[1])
        if total_cost <= budget:
            bought_products += 1
            budget -= total_cost
            result += f"You bought {product} for {total_cost:.2f} leva.\n"

        if bought_products >= 5:
            break
    return result


print(shopping_list(100,
                    microwave=(70, 2),
                    skirts=(15, 4),
                    coffee=(1.50, 10),
                    ))


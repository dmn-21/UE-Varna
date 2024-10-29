from collections import deque

pizza_orders = deque([int(x) for x in input().split(', ')])
employees = [int(x) for x in input().split(', ')]
total_pizza_count = 0

while pizza_orders and employees:
    current_pizza = pizza_orders.popleft()
    if current_pizza <= 0 or current_pizza > 10 :
        continue

    current_employee = employees.pop()

    if current_pizza > current_employee:
        total_pizza_count += current_employee
        pizza_orders.appendleft(current_pizza - current_employee)
        continue

    total_pizza_count += current_pizza

if not pizza_orders:
    print(f"All orders are successfully completed!\n"
          f"Total pizzas made: {total_pizza_count}\n"
          f"Employees: {', '.join([str(x) for x in employees])}")
else:
    print(f"Not all orders are completed.\n"
          f"Orders left: {', '.join([str(x) for x in pizza_orders])}")

basic_salary = 1500
bonus_rate = 200
commission_rate = 0.02

number_of_items_sold = int(input("Enter the number of Items sold: "))
individual_sales_price = float(input("Enter the sales price of Item: "))
bonus = (bonus_rate * number_of_items_sold)

monthly_sales_total = individual_sales_price * number_of_items_sold
commission = (commission_rate * number_of_items_sold * monthly_sales_total)

print("Basic rate   = %6.2f" % basic_salary)
print("Bonus        = %6.2f" % bonus)
print("Commision    = %6.2f" % commission)
print("Gross salary = %6.2f" % (basic_salary + bonus + commission))

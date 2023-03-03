#A SALES AND OPERATIONS PLANNING PROJECT
#ask the user for the following
#the initial stock level for the product

initial_stock_level= int(input("Please enter an initial stock level: "))
#the number of months to plan
print("")
month_plan = int(input("Please enter the number of months to plan: "))
print("")
#the planned sales quantity for each month. This question will be asked based on the month the user inputs
monthly_planned_sales=[]
for i in range(month_plan):
    each_month =int(input(f"Please enter the planned sales quantity for month {i+1}: "))
    print("")
    monthly_planned_sales.append(each_month)
print(f"The planned sales quantity of each of the {month_plan} month is {monthly_planned_sales}")
#based on the data given, calculate the required production quantity as follows:
#if the sales quantity is smaller than than stock level of the previous month, the production quantity is 0
#if the sales quantity is larger than than stock level of the previous month, the production quantity is the difference
production_quantity =[]
new_stock_level= initial_stock_level
for j in range(len(monthly_planned_sales)):
    if monthly_planned_sales[j] > new_stock_level:
        resulting_stock_level =monthly_planned_sales[j]-new_stock_level
        new_stock_level=0
        production_quantity.append(resulting_stock_level)
    else:
        new_stock_level= new_stock_level - monthly_planned_sales[j]
        production_quantity.append(0)
#print the resulting production quantities of each month   
print("")
print("The resulting production quantities are:\n")
for i in range(len(production_quantity)):
    print(f"Production quantity month {i+1} - {production_quantity[i]}")
print("")
print(f"The resulting production quantities of each of the {month_plan} month is {production_quantity}") 







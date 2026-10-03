#Expense Tracker job

expenses=[] # list of all expense

print("Welcome to Expense Tracker  💸")



while True:
    print ("\n===== MENU =====")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View Total Spending ")
    print("4. Exist")
    number=int(input("Enter your choice:"))
    # add expenses
    if (number==1):
        date=input("Enter Date (DD-MM-YYYY):",)
        category=input("Enter the Category like clothes,food,studies,Travel etc:")
        amount=float(input("Enter the amount you spend:"))
        expenses.append({"date":date,"category":category,"amount":amount,"date":date})

    #view all expenses
    elif (number ==2):
        if len(expenses) ==0:
            print("First add expense to view expenses")
        else:
            print("==== This is all your expenses ====")
            print("No  Date  Category  Amount")
            count=1
            for expense in expenses:
                print(f"{count}  {expense["date"]}  {expense["category"]}  {expense["amount"]}")
                count+=1

    # view total expending
    elif (number == 3):
        total_spending=0
        for expense in expenses:
            print(expense)
            total_spending=total_spending+expense["amount"]
        print("\nyour total spend is:",total_spending)
    # exist        
    elif (number == 4):
        print("\nThank you for choosing us!")
        break
    else:
        print("\n don't use you whole brain keep some for your exam")

    

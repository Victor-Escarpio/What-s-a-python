expenses = []
ans = ()
total = 0
print("Welcome to the Expense Planner!")
print("1. Add Expense")
print("2. View Expenses")
print("3. Total Cost Summary")
print("4. Add Funds")
print("5. Quit")
while ans != "5":
    ans = input("Choose 1-5: ")
    if ans == "1":
        expense_name = input("Expense Title: ")
        expense_amount = float(input("Expense Amount: $"))
        expense_date = input("Expense Date (XX/XX/XXXX): ")
        expense = (expense_name,"/", "$",expense_amount,"/", expense_date)
        
        expense = {
            "name": expense_name,
            "amount": expense_amount,
            "date": expense_date,
        }

        expenses.append(expense)
        total -= expense_amount
        print("Expense added!")
    elif ans == "2":
        if not expenses:
            print("No expenses yet")
        else:
            for exp in expenses:
                print(f"{exp['name']} - ${exp['amount']} on {exp['date']}")
    
    elif ans == "3":
    
            print(f"Current Balance: ${total}")
    elif ans == "4":
         deposit = float(input("How much are you depositing? : $"))
         total += deposit
         print(f"New Balance: ${total}")
    elif ans == "5":
        print("Thanks for using The Expense Planner by: Victor Escarpio")
        print("Thanks for using The Expense Planner by: Victor Escarpio")

    else:
        print("Invalid Option.. Try Again")
                  

    

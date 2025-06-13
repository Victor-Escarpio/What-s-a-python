

todo = []
choice = "choose"
while choice != "quit":
    choice = input("Do you want to add a task, remove a task, or quit?: ")
    if choice == "add":
        for i, task in enumerate(todo, start=1):
            print(f"{i}. {task}")
        new = input("Enter your task: ")
        todo.append(new)
    elif choice == "remove":
        for i, task in enumerate(todo, start=1):
            print(f"{i}. {task}")
        removal = input("Which task? (the number of the task or back)")
        if removal == "back":
            continue
        try:
            removal = float(removal)
            if removal.is_integer():
                removal = int(removal)
                if 1 <= removal <= len(todo):
                    del todo[removal - 1]
                    print("Task removed.")
                else:
                    print("Invalid number")
            else:
                print("Incorrect input broski!")

        except ValueError:
            print("Invalid number!")
            
print("See ya!")



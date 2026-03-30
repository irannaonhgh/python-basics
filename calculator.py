while True:
    print("\nCalculator")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == "5":
        print("Bye 👋")
        break

    if choice not in {"1", "2", "3", "4"}:
        print("Invalid choice")
        continue

    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
    except ValueError:
        print("Please enter valid numbers")
        continue

    if choice == "1":
        print("Result:", a + b)
    elif choice == "2":
        print("Result:", a - b)
    elif choice == "3":
        print("Result:", a * b)
    elif choice == "4":
        if b == 0:
            print("Error: division by zero")
        else:
            print("Result:", a / b)

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def main():
    print("Simple Calculator (Addition and Subtraction)")
    while True:
        print("\nSelect operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Exit")
        choice = input("Enter choice (1/2/3): ")
        if choice == '3':
            print("Exiting calculator.")
            break
        if choice not in ('1', '2'):
            print("Invalid choice. Please try again.")
            continue
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            continue
        if choice == '1':
            print(f"Result: {num1} + {num2} = {add(num1, num2)}")
        elif choice == '2':
            print(f"Result: {num1} - {num2} = {subtract(num1, num2)}")

if __name__ == "__main__":
    main()


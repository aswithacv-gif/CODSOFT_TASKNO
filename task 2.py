def calculator():
    print("Simple Calculator")
    print("Operations: + , - , * , /")

    while True:
        try:
            num1 = float(input("\nEnter first number: "))
            op = input("Enter operation (+, -, *, /): ")
            num2 = float(input("Enter second number: "))

            if op == '+':
                result = num1 + num2
            elif op == '-':
                result = num1 - num2
            elif op == '*':
                result = num1 * num2
            elif op == '/':
                if num2 == 0:
                    print("Error: Cannot divide by zero.")
                    continue
                result = num1 / num2
            else:
                print("Invalid operation. Please choose +, -, *, or /.")
                continue

            print(f"Result: {num1} {op} {num2} = {result}")

        except ValueError:
            print("Invalid input. Please enter numeric values.")

        again = input("\nDo you want to perform another calculation? (yes/no): ").lower()
        if again != 'yes':
            print("Thank you for using the calculator!")
            break

if __name__ == "__main__":
    calculator()

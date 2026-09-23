def calculator():
    print("\n--- Basic Calculator ---")
    print("Choose operation: +, -, *, /")

    while True:
        try:
            num1 = float(input("Enter first number: "))
            operator = input("Enter operator (+, -, *, /): ")
            num2 = float(input("Enter second number: "))

            if operator == "+":
                result = num1 + num2
            elif operator == "-":
                result = num1 - num2
            elif operator == "*":
                result = num1 * num2
            elif operator == "/":
                if num2 == 0:
                    print("Cannot divide by zero.")
                    continue
                result = num1 / num2
            else:
                print("Invalid operator. Please try again.")
                continue

            print("Result:", result)
            break

        except ValueError:
            print("Invalid input. Please enter numbers only.")


def unit_converter():
    print("\n--- Unit Converter ---")
    print("1. Kilometers to Miles")
    print("2. Celsius to Fahrenheit")

    while True:
        choice = input("Choose conversion (1 or 2): ")

        try:
            value = float(input("Enter value: "))

            if choice == "1":
                miles = value * 0.621371
                print(f"{value} km = {miles:.2f} miles")
                break

            elif choice == "2":
                fahrenheit = (value * 9 / 5) + 32
                print(f"{value}°C = {fahrenheit:.2f}°F")
                break

            else:
                print("Invalid choice. Please enter 1 or 2.")

        except ValueError:
            print("Invalid input. Please enter a number.")


def main():
    while True:
        print("\n===== Interactive Calculator & Unit Converter =====")
        print("1. Calculator")
        print("2. Unit Converter")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            calculator()
        elif choice == "2":
            unit_converter()
        elif choice == "3":
            print("Thank you for using the program!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

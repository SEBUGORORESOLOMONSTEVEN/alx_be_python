
    
try:
        # Prompt for the first number and convert to float
        num1 = float(input("Enter the first number: "))
        # Prompt for the second number and convert to float
        num2 = float(input("Enter the second number: "))

        # Prompt for the desired operation
        operation = input("Choose the operation (+, -, *, /): ")

        result = None # Initialize result to None

        # Use a match-case statement to perform the chosen operation
        match operation:
            case '+':
                result = num1 + num2
                print(f"The result is {result}.")
            case '-':
                result = num1 - num2
                print(f"The result is {result}.")
            case '*':
                result = num1 * num2
                print(f"The result is {result}.")
            case '/':
                # Handle division by zero
                if num2 != 0:
                    result = num1 / num2
                    print(f"The result is {result}.")
                else:
                    print("Cannot divide by zero.")
            case _:
                # Handle invalid operation input
                print("Invalid operation. Please choose from +, -, *, /.")

except ValueError:
        # Handle cases where input is not a valid number
        print("Invalid input. Please enter valid numbers.")
except Exception as e:
        # Catch any other unexpected errors
        print("An unexpected error occurred: {e}")


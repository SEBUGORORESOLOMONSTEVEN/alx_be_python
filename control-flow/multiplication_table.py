try:
    number = int(input("Enter a number to see its multiplication table: "))

    print(f"Multiplication table for {number}:")

    for i in range(1, 11):
        product = number * i
        # CHANGE THIS LINE:
        print(f"{number} * {i} = {product}") # Use an f-string here

except ValueError:
    print("Invalid input. Please enter a whole number.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

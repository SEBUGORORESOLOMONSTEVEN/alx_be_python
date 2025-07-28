try:
        size = int(input("Enter the size of the pattern: "))

        if size <= 0:
            print("Please enter a positive integer for the pattern size.")
            

        row_count = 0
        while row_count < size:
            for _ in range(size):
                print("*", end="")
            print()
            row_count += 1

except ValueError:
        print("Invalid input. Please enter a whole number.")
except Exception as e:
        print(f"An unexpected error occurred: {e}")


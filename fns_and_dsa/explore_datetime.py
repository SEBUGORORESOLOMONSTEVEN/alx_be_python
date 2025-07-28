from datetime import datetime, timedelta

def display_current_datetime():
    
    # Get the current date and time
    current_date = datetime.now()

    # Format and print the current date and time
    # %Y: Year with century (e.g., 2024)
    # %m: Month as a zero-padded decimal number (e.g., 03)
    # %d: Day of the month as a zero-padded decimal number (e.g., 25)
    # %H: Hour (24-hour clock) as a zero-padded decimal number (e.g., 15)
    # %M: Minute as a zero-padded decimal number (e.g., 30)
    # %S: Second as a zero-padded decimal number (e.g., 45)
    formatted_current_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_current_date}")

def calculate_future_date():
    
    # Get the current date (we'll use this as the base for calculation)
    current_date = datetime.now()

    while True:
        try:
            # Prompt the user to enter a number of days
            days_to_add_str = input("Enter the number of days to add to the current date: ")
            days_to_add = int(days_to_add_str)
            break # Exit loop if input is a valid integer
        except ValueError:
            print("Invalid input. Please enter an integer for the number of days.")

    # Calculate the future date using timedelta
    # timedelta represents a duration, and we're adding 'days_to_add' days
    future_date = current_date + timedelta(days=days_to_add)

    # Format and print the future date
    # %Y: Year with century
    # %m: Month as a zero-padded decimal number
    # %d: Day of the month as a zero-padded decimal number
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    print(f"Future date: {formatted_future_date}")

def main():
    """
    Main function to run the datetime exploration script.
    """
    display_current_datetime()
    calculate_future_date()

if __name__ == "__main__":
    main()

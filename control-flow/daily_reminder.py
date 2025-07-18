task = input("Enter your task: ")

priority = input("Priority (high/medium/low): ").lower()

time_bound = input("Is it time-bound? (yes/no): ").lower()

time_sensitive_message = ""
if time_bound == "yes":
        time_sensitive_message = " that requires immediate attention today!"
elif time_bound == "no":
        pass
else:
        print("Invalid input for 'Is it time-bound?'. Please answer 'yes' or 'no'.")
        

match priority:
        case "high":
            reminder = f"Reminder: '{task}' is a high priority task{time_sensitive_message}"
        case "medium":
            reminder = f"Reminder: '{task}' is a medium priority task{time_sensitive_message}"
        case "low":
            if time_bound == "no":
                reminder = f"Note: '{task}' is a low priority task. Consider completing it when you have free time."
            else:
                reminder = f"Reminder: '{task}' is a low priority task{time_sensitive_message}"
        case _:
            print("Invalid priority. Please choose from high, medium, or low.")
            

print(reminder)
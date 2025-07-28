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
        

    # Initialize a base message without the "Reminder:" or "Note:" prefix
base_message_content = ""
is_note_case = False # Flag to distinguish the "Note:" specific output

match priority:
        case "high":
            base_message_content = f"'{task}' is a high priority task{time_sensitive_message}"
        case "medium":
            base_message_content = f"'{task}' is a medium priority task{time_sensitive_message}"
        case "low":
            if time_bound == "no":
                base_message_content = f"'{task}' is a low priority task. Consider completing it when you have free time."
                is_note_case = True # Set flag for the "Note:" case
            else:
                base_message_content = f"'{task}' is a low priority task{time_sensitive_message}"
        case _:
            print("Invalid priority. Please choose from high, medium, or low.")
            

    # Now, print the final reminder with the correct prefix
if is_note_case:
        print(f"Note: {base_message_content}")
else:
        # This print statement now explicitly starts with f"Reminder:"
        print(f"Reminder: {base_message_content}")
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

match priority:
    case "high":
            print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")

    case "medium":
            print(f"Reminder: '{task}' is a medium priority task that needs to be done today!")

    case "low":
            print(f"Reminder: '{task}' is a low priority task, but it needs to be done today!")
if time_bound == 'yes':
    print(f'That requires a immediate action today!') 
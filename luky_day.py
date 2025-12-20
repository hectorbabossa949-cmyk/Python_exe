import random
import datetime
def lucky_day_picker():
    print("☘Lucky Day Picker!")
    print("=" *30)
    days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
    to_do ={"Monday": "Sleep",
            "Tuesday": "Read novel",
            "Wednesday":"Eat snacks",
            "Thursday":"Go for a walk",
            "Friday": "Watch movie",
            "Saturday": "Meet up with friends",
            "Sunday": "Lay in the bed"
            }
    lucky_day = random.choice(days)
    print(f"Your lucky day is: {lucky_day}")
    print(f"Suggested activity is: {to_do[lucky_day]}")
    today = datetime.datetime.now().strftime("%A")
    print(f"Today is : {today}")
    if (today == lucky_day):
        print("WOW! Today is your lucky day! ✨")
    else:
        print(f"🎃Your lucky day is: {lucky_day}")
        print(f"Your lucky day is on {lucky_day}, so hang in there! 💪")

while True:
    user_input = input("\nPress 1 to pick again or 0 to exit: ")
    if user_input == "1":
        lucky_day_picker()
    elif user_input == "0":
        print("Thank you for using Lucky Day Picker! Goodbye! 👋")
        break
    else:
        print("Invalid input. Please try again.")
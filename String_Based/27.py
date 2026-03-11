# Q27: Determine the Season from a Month Name

def get_season(month):
    month = month.strip().capitalize()
    spring = ["March", "April", "May"]
    summer = ["June", "July", "August"]
    autumn = ["September", "October", "November"]
    winter = ["December", "January", "February"]

    if month in spring:
        return "Spring"
    elif month in summer:
        return "Summer"
    elif month in autumn:
        return "Autumn"
    elif month in winter:
        return "Winter"
    else:
        return "Invalid month"

month = input("Enter a month name: ")
print(f"Season: {get_season(month)}")

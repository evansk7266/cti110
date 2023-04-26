# Define your function here.

def days_in_feb(user_year):
    if user_year % 4 == 0:
        if user_year % 100 == 0:
            if user_year % 400 == 0:
                return 29
            else:
                return 28
        else:
            return 29
    else:
        return 28

if __name__ == '__main__':
    user_year = int(input())
    num_days = days_in_feb(user_year)
    print(f"{user_year} has {num_days} days in February.")
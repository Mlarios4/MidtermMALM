def days_passed_since_birthday(birthday):
    day, month, year = map(int, birthday.split('-'))
    current_date = (26, 2, 2024)
    days_passed_in_birth_year = 365 - sum([31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][:month - 1]) + day
    days_passed_in_current_year = sum([31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][:current_date[1] - 1]) + \
                                  current_date[0]
    total_days_passed = (current_date[2] - year - 1) * 365 + days_passed_in_birth_year + days_passed_in_current_year
    return total_days_passed
birthday = "22-06-2004"

print("Days passed since birthday:", days_passed_since_birthday(birthday))

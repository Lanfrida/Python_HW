def is_year_leap(year):
    if year % 4 == 0:
        return True
    else:
        False

year_china = 2024
result = is_year_leap(year_china)

print(f"год{year_china}:{result}")
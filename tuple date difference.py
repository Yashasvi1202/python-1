from datetime import date
def calculate_days(d1, d2):
  date1 = date(d1[2], d1[1], d1[0])
  date2 = date(d2[2], d2[1], d2[0])
  delta = abs(date2 - date1)
  return delta.days
date_a = (15, 8, 2023)
date_b = (1, 1, 2024)

result = calculate_days(date_a, date_b)

print(f"Days between {date_a} and {date_b}: {result} days")

def is_leap(year):
  leap = False
  if 1990 <= year <= pow(10,5):
    return year % 4 == 0 and (year % 400 == 0 or year % 100 != 0) 
   # Write your logic here
    
  return leap

year = int(raw_input())
print is_leap(year)

# put your python code here

year_number = int(input())

if (year_number % 4) == 0 and (year_number % 100) != 0 or (year_number % 400) == 0:
    print("Leap")
else:
    print("Ordinary")

first_number = int(input())
second_number = int(input())

if first_number > second_number:
    print(first_number)
    print(second_number)
else:
    if second_number > first_number:
        print(second_number)
        print(first_number)
    else:
        if first_number == second_number:
            print(first_number)
            print(second_number)

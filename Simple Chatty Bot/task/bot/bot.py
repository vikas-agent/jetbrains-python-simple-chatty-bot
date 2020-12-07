print("Hello! My name is Vikas.")
print("I was created in 2020.")
print("Please, remind me your name.")
user_name = input("> ")
print("What a great name you have, {}".format(user_name))
print("Let me guess your age.")
print("Enter remainders of dividing your age by 3, 5 and 7.")
remainder3 = int(input())
remainder5 = int(input())
remainder7 = int(input())
user_age = (remainder3 * 70 + remainder5 * 21 + remainder7 * 15) % 105
print("Your age is {user_age}; that's a good time to start programming!".format(user_age=user_age))
print("Now I will prove to you that I can count to any number you want.")
user_given_number = int(input())
initial_number = 0
while initial_number <= user_given_number:
    print("{} !".format(initial_number))
    initial_number += 1

print("Let's test your programming knowledge.")
print("Why do we use methods?")
print("""
1. To repeat a statement multiple times.
2. To decompose a program into several small subroutines.
3. To determine the execution time of a program.
4. To interrupt the execution of a program.
""")


def get_users_answer():
    users_answer = int(input("> "))
    check_users_input(users_answer)


def check_users_input(users_answers):
    if users_answers != 2:
        print("Please, try again.")
        get_users_answer()
    else:
        print("Completed, have a nice day!")
        print("Congratulations, have a nice day!")

get_users_answer()

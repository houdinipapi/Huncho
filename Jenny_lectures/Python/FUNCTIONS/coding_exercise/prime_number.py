def prime_checker(number):
    is_prime = True
    if number == 1:
        is_prime = False
    for i in range(2, number):  # for i in range(2, (math.ceil((number / 2) + 1))) ---> Time complexity will reduce
        if number % i == 0:
            is_prime = False
    if is_prime:
        print("Prime Number")
    else:
        print("Not a prime number")

user_num = int(input("Number: "))

prime_checker(user_num)
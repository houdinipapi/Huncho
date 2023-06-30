def addition(*args):  # Arbitrary positional
    total_sum = 0
    for i in args:
        total_sum += i
    return total_sum

print(addition(4, 5, 6))
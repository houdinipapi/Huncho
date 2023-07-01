import statistics

def mean_median_mode(list1):
    return statistics.mean(list1), statistics.median(list1), statistics.mode(list1)

print(mean_median_mode([3, 4, 5, 5, 67, 7, 43]))
mean, median, mode = mean_median_mode([3, 4, 5, 5, 67, 7, 43])
print(f"Mean: {mean}\nMedian: {median}\nMode: {mode}")


def addition(a, b):
    if a == 0 and b == 0:
        return "Both numbers are 0."
    else:
        return a + b

num1 = int(input("First Number: "))
num2 = int(input("Second Number: "))
print(addition(num1, num2))
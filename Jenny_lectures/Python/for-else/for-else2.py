#!/usr/bin/python3

'''
for/else
'''

nums = [2, 4, 6, 8, 24]

for i in nums:
    print(i)
    if i % 3:
        break
else:
    print("Successfully Iterated")

print("Terminated Iteration")

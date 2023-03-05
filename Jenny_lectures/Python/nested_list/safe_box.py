#!/usr/bin/python3

'''replace a number with a letter X'''

row1 = [1, 1, 1]
row2 = [2, 2, 2]
row3 = [3, 3, 3]

print(f"{row1}\n{row2}\n{row3}")

row_col_num = input("Pick a row and column number: ")
#print(row_col_num)

row_num = int(row_col_num[0])
col_num = int(row_col_num[1])
print(f"Row: {row_num}")
print(f"Column: {col_num}")

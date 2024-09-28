ton = input()  # Taking the input as a string
ton = list(ton)  # Converting the input string to a list of characters

ans = []  # Initializing the list to store the answers
a = 0  # Initializing the position of 'a'
b = 0  # Initializing the position of 'b'

# Finding the position of 'a' in the list
if "a" in ton:
    a = ton.index("a")
    a += 1  # Incrementing to match the 1-based index

# Finding the position of 'b' in the list
if "b" in ton:
    b = ton.index("b")
    b += 1  # Incrementing to match the 1-based index

# Iterating through the possible values of a1, b1, and c
try:
    for a1 in range(a, b):  # a1 ranges from a to b-1
        for b1 in range(b, len(ton) + 1):  # b1 ranges from b to len(ton)
            for c in range(b, len(ton) + 1):  # c ranges from b to len(ton)
                if 1 <= a1 < b1 < c <= len(ton)+1:  # Checking the conditions
                    ans.append((a1, b1, c))  # Storing the result

except Exception as e:
    pass  # Printing the error if any occurs

# Checking if the length of the answer list is even or odd
if len(ans) % 2 == 0:
    print("DuckDuck 2")  # Even length
else:
    print("DuckDuck 1")  # Odd length

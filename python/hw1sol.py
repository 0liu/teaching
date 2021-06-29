# Problem 1

# Given a list list1 = [10, 20, 30, 40, 50], write code to build a new list “list2” using a loop that reverses list1, such that list2 is like [50, 40, 30, 20, 10]. Print out your list2.

list1 = [10, 20, 30, 40, 50]

# Solution 1
list2 = []
for i in range(5):
    list2.append(list1[5-i-1])
print(list2)

# Solution 2
list2 = []
for i in range(4, -1, -1):
    list2.append(list1[i])
print(list2)

# Solution 3
list2 = []
for i in reversed(range(5)):
    list2.append(list1[i])
print(list2)

# Solution 4
list2 = list1[::-1]
print(list2)

# Solution 5
list2 = list(reversed(list1))
print(list2)


# ---------------------------------
# Probem 2

#Given a list A = [11, 45, 8, 11, 23, 45, 23, 45, 89], write code to build a dictionary that counts the occurrences of each value. Print out your dictionary. It should look like:
#{45: 3, 11: 2, 23: 2, 8: 1, 89: 1}

A = [11, 45, 8, 11, 23, 45, 23, 45, 89]
counts = {}

for key in A:  # i = 0, ..., 8
    if key not in counts:  # set the count to 1 when we see this key for the 1st time
        counts[key] = 1
    else:  # condition to check element in counts
        counts[key] += 1

print(counts)
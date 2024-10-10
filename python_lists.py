# 1. Python List Transformation
grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
grades.sort()
grades.reverse()
print(grades)

average = 0
for i in grades:
    average += i
average /= len(grades)
print(average)

# 2. Advanced List Methods and Identity Operators
submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]
if "Alice" in submitted and "Alice" in attended:
    print("Alice went to class and submitted her assignment")
else:
    print("alice did not do one of those things")

# 3. Advanced Sliding Techniques
temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]
segment = temperatures[7:14]
print(segment)

over100 = []
for i in temperatures:
    if i > 100:
        over100.append(i)
print(over100)
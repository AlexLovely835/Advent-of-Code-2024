
left_list = []
right_list = []

with open("day1/input.txt") as input:
    for line in input:
        left, right = line.split("   ")
        left_list.append(int(left))
        right_list.append(int(right))

left_list.sort()
right_list.sort()

total = 0
for i in range(0, len(left_list)):
    total += abs(left_list[i] - right_list[i])

print(total)
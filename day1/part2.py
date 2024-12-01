from collections import Counter

left_list = []
right_list = []

with open("day1/input.txt") as input:
    for line in input:
        left, right = line.split("   ")
        left_list.append(int(left))
        right_list.append(int(right))

left_count = Counter(left_list)
right_count = Counter(right_list)

total = 0

for k,v in left_count.items():
    r = right_count.get(k)
    if r:
        total += (k*r*v)

print(total)






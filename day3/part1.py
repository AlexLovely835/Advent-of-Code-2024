import re

with open("day3/input.txt") as input:
    mem = "\n".join(input.readlines())

instructions = re.findall(r'mul\([\d]{1,3},[\d]{1,3}\)', mem)

total = 0

for mul in instructions:
    nums = re.findall(r'[\d]{1,3}', mul)
    total += (int(nums[0]) * int(nums[1]))

print(total)





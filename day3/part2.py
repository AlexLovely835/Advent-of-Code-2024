import re

with open("day3/input.txt") as input:
    mem = "\n".join(input.readlines())

instructions = re.findall(r"mul\([\d]{1,3},[\d]{1,3}\)|don't\(\)|do\(\)", mem)

total = 0
do = True
for inst in instructions:
    if inst == "do()":
        do = True
    elif inst == "don't()":
        do = False
    else:
        if do:
            nums = re.findall(r'[\d]{1,3}', inst)
            total += (int(nums[0]) * int(nums[1]))

print(total)

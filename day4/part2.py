with open("day4/input.txt") as input:
    search = input.readlines()

total = 0

for x in range(1, len(search)-1):
    for y in range(1, len(search[0])-1):
        if search[x][y] == "A":
            opposites = [search[x+1][y+1], search[x-1][y-1], search[x+1][y-1], search[x-1][y+1]]
            if "X" not in opposites and "\n" not in opposites and "A" not in opposites and opposites[0] != opposites[1] and opposites[2] != opposites[3]:
                total += 1

print(total)
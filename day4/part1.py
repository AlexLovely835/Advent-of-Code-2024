with open("day4/input.txt") as input:
    search = input.readlines()

def getCoords(x, y, dir):
    dirs = [(x+1, y+1, "SE"), 
            (x+1, y, "S"),
            (x+1, y-1, "SW"),
            (x, y-1, "W"),
            (x-1, y-1, "NW"),
            (x-1, y, "N"),
            (x-1, y+1, "NE"),
            (x, y+1, "E")]

    for x1, y1, dir1 in dirs:
        if dir == dir1:
            return (x1, y1)

def probe(x, y, letter):
    found = []
    dirs = [(x+1, y+1, "SE"), 
            (x+1, y, "S"),
            (x+1, y-1, "SW"),
            (x, y-1, "W"),
            (x-1, y-1, "NW"),
            (x-1, y, "N"),
            (x-1, y+1, "NE"),
            (x, y+1, "E")]
    
    for x1, y1, dir in dirs:
        if x1 >= 0 and y1 >= 0 and not x1 >= len(search) and not y1 >= len(search[0]) and search[x1][y1] == letter:
            found.append((x1, y1, dir))
            
    return found

total = 0

for x in range(len(search)):
    for y in range(len(search[0])):
        if search[x][y] == "X":
            found = probe(x, y, "M")
            temp = []
            for x1, y1, dir in found:
                x2, y2 = getCoords(x1, y1, dir)
                if x2 >= 0 and y2 >= 0 and not x2 >= len(search) and not y2 >= len(search[0]) and search[x2][y2] == "A":
                    temp.append((x2, y2, dir))
            found = temp
            for x1, y1, dir in found:
                x2, y2 = getCoords(x1, y1, dir)
                if x2 >= 0 and y2 >= 0 and not x2 >= len(search) and not y2 >= len(search[0]) and search[x2][y2] == "S":
                    total += 1

print(total)
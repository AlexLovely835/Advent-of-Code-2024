
reports = []

with open("day2/input.txt") as input:
    for line in input:
        report = []
        for val in line.split(" "):
            report.append(int(val))
        reports.append(report)


safe = 0

for report in reports:
    dir = ""
    problems = 0
    for i in range(len(report)-1):
        if report[i] > report[i+1]:
            if not dir:
                dir = "down"
            elif dir == "up":
                break
        elif report[i] < report[i+1]:
            if not dir:
                dir = "up"
            elif dir == "down":
                break
        else:
            break
        
        dist = abs(report[i] - report[i+1])
        if dist > 3:
            break

        if i == len(report) - 2:
            safe += 1

print(safe)
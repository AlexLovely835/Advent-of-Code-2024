import copy 

reports = []

with open("day2/input.txt") as input:
    for line in input:
        report = []
        for val in line.split(" "):
            report.append(int(val))
        reports.append(report)


safe = 0

for report in reports:
    sub_reports = []
    sub_reports.append(report)
    for i in range(len(report)):
        new = copy.deepcopy(report)
        del new[i]
        sub_reports.append(new)

    for sub_report in sub_reports:
        dir = ""
        problems = 0
        safe_sub = False
        for i in range(len(sub_report)-1):
            if sub_report[i] > sub_report[i+1]:
                if not dir:
                    dir = "down"
                elif dir == "up":
                    break
            elif sub_report[i] < sub_report[i+1]:
                if not dir:
                    dir = "up"
                elif dir == "down":
                    break
            else:
                break
            
            dist = abs(sub_report[i] - sub_report[i+1])
            if dist > 3:
                break

            if i == len(sub_report) - 2:
                safe_sub = True
                break

        if safe_sub:
            safe += 1
            break


print(safe)
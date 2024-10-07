from path_finding_algo import knightPaths
from more_itertools import unique_everseen
import csv

# set maximum path to 3rd parameter arbitratily to prevent huge running time
"""THESE ARE IN THE FORMAT [COLUMN, ROW]"""
a1tof6Paths, a1tof6VisitedCells = knightPaths([0,0],[5,5],12)
a6tof1Paths, a6tof1VisitedCells = knightPaths([5,0],[0,5],12)

# a1 to f6 
with open('a1tof6AllRoutes.csv', 'w+') as f:
    for line in a1tof6Paths:
        f.write(",".join(line))
        f.write("\n")

with open('a1tof6AllRoutes.csv', 'r') as f1, open('a1tof6UniqueRoutes.csv', 'w+') as f2:
    f2.writelines(unique_everseen(f1))

with open('a1tof6AllRouteCells.csv', 'w+', newline='') as f:
    writer = csv.writer(f)

    for line in a1tof6VisitedCells:
        writer.writerow([str(t) for t in line])


# a6 to f1
with open('a6tof1AllRoutes.csv', 'w+') as f:
    for line in a6tof1Paths:
        f.write(",".join(line))
        f.write("\n")

with open('a6tof1AllRoutes.csv', 'r') as f1, open('a6tof1UniqueRoutes.csv', 'w+') as f2:
    f2.writelines(unique_everseen(f1))

with open('a6tof1AllRouteCells.csv', 'w+', newline='') as f:
    writer = csv.writer(f)

    for line in a6tof1VisitedCells:
        writer.writerow([str(t) for t in line])
from path_finding_algo import knightPaths
import csv

# call routes from csv
a1tof6 = []
a6tof1 = []
with open("a1tof6UniqueRoutes.csv", "r") as f:
    reader = csv.reader(f)
    a1tof6 = list(reader)

with open("a6tof1UniqueRoutes.csv", "r") as f:
    reader = csv.reader(f)
    a6tof1 = list(reader)

# call all routes from csv, purely to print correct path.
alla1tof6 = []
alla6tof1 = []

with open("a1tof6AllRoutes.csv", "r") as f:
    reader = csv.reader(f)
    alla1tof6 = list(reader)

with open("a6tof1AllRoutes.csv", "r") as f:
    reader = csv.reader(f)
    alla6tof1 = list(reader)

# call cell steps from csv
a1tof6Cells = []
a6tof1Cells = []

with open("a1tof6AllRouteCells.csv", "r") as f:
    reader = csv.reader(f)
    a1tof6Cells = list(reader)

with open("a6tof1AllRouteCells.csv", "r") as f:
    reader = csv.reader(f)
    a6tof1Cells = list(reader)


def functionFromPath(path, vars):
    a, b, c = vars
    values = {"A": a, "B": b, "C": c}
    total = values[path[0]]
    # set square to value not in the grid
    oldSquare = 'D'
    for square in path:
        if square == oldSquare:
            total += values[square]
        else:
            total *= values[square]
        oldSquare = square
    # constraint function, so this needs to equal 0
    return (total - 2024)

# we know solution can be less than 50 
currentMin = 51
bestPaths = []
abcValues = []


# iterate through a1 path, find all values for a, b and c that work, iterate through next path.
workingValuesAndPaths = []
for a1path in a1tof6:
    for a in range(1,26):
        for b in range(1,26):
            if b == a:
                continue
            for c in range(1,26):
                if c == b or c == a or a+b+c > 50:
                    continue
                if functionFromPath(a1path, (a,b,c)) == 0:
                    workingValuesAndPaths.append([a,b,c,a1path])

for a6path in a6tof1:
    for valueSet in workingValuesAndPaths:
        if functionFromPath(a6path, (valueSet[0],valueSet[1],valueSet[2]))==0:
            result = valueSet[0] + valueSet[1] + valueSet[2]
            if result < currentMin:
                currentMin = result
                bestPaths = []
                bestPaths.append(valueSet[3])
                bestPaths.append(a6path)
                abcValues = [valueSet[0],valueSet[1],valueSet[2]]


alphabet = "abcdef"
firstRoute = []
for num, cell in enumerate(a1tof6Cells[alla1tof6.index(bestPaths[0])]):
    number = int(cell[1])+1
    letter = alphabet[int(cell[4])]
    firstRoute.append(f"{letter}{number}")

secondRoute = []
for num, cell in enumerate(a6tof1Cells[alla6tof1.index(bestPaths[1])]):
    number = int(cell[1])+1
    letter = alphabet[int(cell[4])]
    secondRoute.append(f"{letter}{number}")

print(f"Minimum value of A, B, C values = {currentMin}\nA, B, C values = {abcValues}")
print(f"Paths are: \n{firstRoute}\n{secondRoute}")

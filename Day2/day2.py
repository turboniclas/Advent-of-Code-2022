data =  open("Day2/input.txt", "r").read().split('\n')

# X = rock
rock = 1
# Y = paper
paper = 2
# z = scissors
scissors= 3
loose = 0
draw = 3
win = 6
total_score = 0

# Part One

for i in range(len(data)):
    #opponent rock
    if data[i][0] == "A":
        if data[i][2] == "X":
            total_score += (rock + draw)
        elif data[i][2] == "Y":
            total_score += (paper + win)
        elif data[i][2] == "Z":
            total_score += (scissors + loose)
    #opponent paper
    elif data[i][0] == "B":
        if data[i][2] == "X":
            total_score += (rock + loose)
        elif data[i][2] == "Y":
            total_score += (paper + draw)
        elif data[i][2] == "Z":
            total_score += (scissors + win)
    #opponent scissors
    elif data[i][0] == "C":
        if data[i][2] == "X":
            total_score += (rock + win)
        elif data[i][2] == "Y":
            total_score += (paper + loose)
        elif data[i][2] == "Z":
            total_score += (scissors + draw)

print(f"Part One: {total_score}")

# Part Two

total_score = 0

for i in range(len(data)):
    #opponent rock
    if data[i][0] == "A":
        if data[i][2] == "X":
            total_score += (scissors + loose)
        elif data[i][2] == "Y":
            total_score += (rock + draw)
        elif data[i][2] == "Z":
            total_score += (paper + win)
    #opponent paper
    elif data[i][0] == "B":
        if data[i][2] == "X":
            total_score += (rock + loose)
        elif data[i][2] == "Y":
            total_score += (paper + draw)
        elif data[i][2] == "Z":
            total_score += (scissors + win)
    #opponent scissors
    elif data[i][0] == "C":
        if data[i][2] == "X":
            total_score += (paper + loose)
        elif data[i][2] == "Y":
            total_score += (scissors + draw)
        elif data[i][2] == "Z":
            total_score += (rock + win)
    
print(f"Part Two: {total_score}")
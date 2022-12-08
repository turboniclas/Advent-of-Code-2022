with open("Day8/input.txt", "r") as input:


    data = []
    for line in input:
        data.append([int(elem) for elem in line.rstrip()])



total_rows = len(data)
total_cols = len(data[0])

# Part One

def visible(row,col):

    tree = data[row][col]

    # direction above
    for k in range(row-1,-1,-1):
        if data[k][col] >= tree:
            break
    else:
        return True
    
    # direction below
    for k in range(row +1, total_rows):
        if data[k][col] >= tree:
            break
    else:
        return True
    
    # direction left
    for k in range(col-1, -1, -1):
        if data[row][k] >= tree:
            break
    else:
        return True

    # direction right
    for k in range(col +1, total_cols):
        if data[row][k] >= tree:
            break
    else:
        return True

    return False

visible_trees = (total_cols + total_rows) *2 -4

for row in range(1,total_rows-1):
    for col in range(1,total_cols-1):
        if visible(row, col):
            visible_trees += 1


#Part Two

def seeing_trees(row,col):

    tree = data[row][col]
    above_trees = 0
    below_trees = 0
    right_trees = 0
    left_trees = 0
    # direction above
    for k in range(row-1,-1,-1):
        above_trees += 1
        if data[k][col] >= tree:
            break
    
    # direction below
    for k in range(row +1, total_rows):
        below_trees += 1
        if data[k][col] >= tree:
            break
    
    
    # direction left
    for k in range(col-1, -1, -1):
        left_trees += 1
        if data[row][k] >= tree:
            break
    

    # direction right
    for k in range(col +1, total_cols):
        right_trees += 1
        if data[row][k] >= tree:
            break
    
    
    seeing_trees = above_trees * below_trees * left_trees * right_trees
    return seeing_trees

best_tree = 0

for row in range(1, total_rows-1):
    for col in range(1, total_cols-1):
        current_tree = seeing_trees(row, col)
        if current_tree > best_tree:
            best_tree = current_tree



print(f"Part One: {visible_trees}")
print(f"Part Two: {best_tree}")
#Solution by raxomus

with open("Day9/input.txt") as f:
    lines = f.read().splitlines()

adjacent = lambda p1, p2: all([abs((p1[i]) - p2[i]) <= 1 for i in range(2)])


directions = {"R" : (1, 0),
            "L" : (-1, 0),
            "U" : (0, 1),
            "D" : (0, -1)}

grid = [[0] * 2 for _ in range(10)]

seen_positions = {(0, 0)}
seen_positions9 = {(0, 0)}

for move in lines:
    d = directions[move[0]]
    for i in range(int(move[2:])):
        for j in range(2): grid[0][j] += d[j]
        for k in range(9):
            h, t = grid[k:k+2]
            if not adjacent(h ,t):
                for i in range(2): t[i] += (h[i] != t[i]) * (2*(h[i] >t[i]) -1)
        seen_positions.add(tuple(grid[1]))
        seen_positions9.add(tuple(grid[9]))

print(len(seen_positions ))
print(len(seen_positions9 ))
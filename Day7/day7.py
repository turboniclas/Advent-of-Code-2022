from collections import defaultdict

path = []
folders = defaultdict(int)

with open('Day7/input.txt', 'r') as f:
    for line in f:
        if line[:7] == '$ cd ..':
            path.pop()
        elif line[:4] == '$ cd':
            path.append(line.strip()[5:])
        elif line[0].isdigit():
            size, _ = line.split()
            for i in range(len(path)):
                folders['/'.join(path[:i + 1])] += int(size)

print('Part 1:', sum(f for f in folders.values() if f < 100_000))
print('Part 2:', min([f for f in folders.values() if folders['/'] - f <= 40_000_000]))
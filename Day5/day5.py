data =  open("Day5/input.txt", "r").read().split("\n")


stack = [[],
    ["Z", "P", "B", "Q", "M", "D", "N"],
    ["V", "H", "D", "M", "Q", "Z", "L", "C"],
    ["G", "Z" ,"F", "V", "D", "R", "H", "Q"],
    [ "N", "F","D", "G", "H"],
    ["Q", "F", "N"],
    ["T", "B", "F", "Z", "V", "Q", "D"],
    ["H", "S", "V", "D", "Z", "T", "M", "Q"],
    [ "Q" ,"N" ,"P", "F", "G", "M"],
    ["M","R","W","B"]
]

for i in range(len(stack)):
    stack[i] = list(reversed(stack[i]))

for i in range(10, len(data)):
    data[i] = data[i].split(" ")
    
# Part One    

def get_crates(crates):
    for step in range(10, len(crates)):
        moved_crates = int(crates[step][1])
        target_crate = int(crates[step][3])
        goal_crate = int(crates[step][5])
        for _ in range(moved_crates):
            if not stack[target_crate]:
                break
            else:
                crate = stack[target_crate].pop()
                stack[goal_crate].append(crate)
                
    for i in range(len(stack)):
        stack[i] = list(reversed(stack[i]))

    return "".join([s[0] for s in stack if len(s)>0])





print(get_crates(data))
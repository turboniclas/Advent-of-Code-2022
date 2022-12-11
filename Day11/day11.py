#data =  open("Day11/test_input.txt", "r").read().split("\n")
data =  open("Day11/input.txt", "r").read().strip().split("\n\n")


monkeys = []
operations = []
tests = []
true_to = []
false_to = []
for i in data:
    id, items, op, test, true, false = i.split("\n")
    monkeys.append([int(i) for i in items.split(":")[1].split(",")])
    operations.append(op.split()[4:])
    tests.append(int(test[19:]))
    true_to.append(int(true[25:]))
    false_to.append(int(false[26:]))

inspected = {}

for i in range(20):
    for monkey in range(len(monkeys)):
        curr_monkey = monkeys[monkey]
        
        while len(curr_monkey) != 0:
            curr = curr_monkey.pop(0)
            inspected[monkey] = inspected.get(monkey, 0) +1
            if not "old" in operations[monkey]:
                if "*" in operations[monkey]:
                    new = curr * int(operations[monkey][1])
                    new //= 3
                    if new % tests[monkey] == 0:
                        monkeys[true_to[monkey]].append(new)
                    else:
                        monkeys[false_to[monkey]].append(new)
                        
                elif "+" in operations[monkey]:
                    new = curr + int(operations[monkey][1])
                    new //= 3
                    if new % tests[monkey] == 0:
                        monkeys[true_to[monkey]].append(new)
                    else:
                        monkeys[false_to[monkey]].append(new)
            else:
                if "*" in operations[monkey]:
                    new = curr * curr
                    new //= 3
                    if new % tests[monkey] == 0:
                        monkeys[true_to[monkey]].append(new)
                    else:
                        monkeys[false_to[monkey]].append(new)
                        
                elif "+" in operations[monkey]:
                    new = curr + curr
                    new //= 3
                    if new % tests[monkey] == 0:
                        monkeys[true_to[monkey]].append(new)
                    else:
                        monkeys[false_to[monkey]].append(new)
    #print(f"round {i}{monkeys}")      
                    
max = max(inspected.values())

max2 = 0
for v in inspected.values():
    if(v>max2 and v<max):
        max2 = v

# Part One
print(max * max2)



   
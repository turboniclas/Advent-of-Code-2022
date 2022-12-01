data =  open("Day 1/input.txt", "r").read().split('\n')



sum = 0
calories_per_elf = []
for value in data:
    if value == "":
        calories_per_elf.append(sum)
        sum = 0
    else:
        sum += int(float(value))

"Part 1"
print(max(calories_per_elf))

"Part 2"
sorted_calories  = sorted(calories_per_elf)
sum = 0
for i in range(len(sorted_calories)-3, len(sorted_calories)):
    sum += sorted_calories[i]
print(sum)

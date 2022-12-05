data =  open("Day3/input.txt", "r").read().split('\n')

priorities = {}

def setPriority():
    for i in range(97, 123):
        priorities[chr(i)] = 0

    for i in range(65, 91):
        priorities[chr(i)] = 0

    temp = 1
    for key,value in priorities.items():
        priorities[key] = temp
        temp += 1
    return priorities


def getPriority(letter):
    return priorities[letter]

# Part One


def day3_part1(items):
    sum_of_priorities = 0
    for item in items:
        half = len(item) // 2
        first_half = item[:half]
        second_half = item[half:]
        for letter in first_half:
            if letter in second_half:
                sum_of_priorities += getPriority(letter)
                break
    return sum_of_priorities


# Part Two


def day3_part2(items):
    sum_of_prorities = 0
    for item in range(0, len(items), 3):
        for letter in items[item]:
            if letter in items[item + 1] and letter in items[item+2]:
                sum_of_prorities += getPriority(letter)
                break
    return sum_of_prorities

setPriority()
print(day3_part1(data))
print(day3_part2(data))






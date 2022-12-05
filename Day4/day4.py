data =  open("Day4/input.txt", "r").read().split("\n")
for d in range(len(data)):

    data[d] = data[d].replace("-" ," ")
    data[d] = data[d].replace(",", " ")
    data[d] = data[d].split(" ")

# Part One

def fully_contain(sections):
    fully_contain_sections = 0
    for i in sections:
        i[0],i[1],i[2],i[3] = [int(x) for x in [i[0],i[1],i[2],i[3]]]

        if i[2] >= i[0] and i[3] <= i[1] or i[0] >= i[2] and i[1] <= i[3]:
            fully_contain_sections += 1
    return fully_contain_sections

#Part 2

def full_overlap(sections):
    full_overlap_sections = 0
    for i in sections:
        i[0],i[1],i[2],i[3] = [int(x) for x in [i[0],i[1],i[2],i[3]]]

        if not(i[1] < i[2] or i[3] < i[0]):
            full_overlap_sections += 1
    return  full_overlap_sections


print(fully_contain(data))
print(full_overlap(data))
data =  open("Day7/test_input.txt", "r").read().split("\n")

for i in range(len(data)):
    if data[i] == "$ cd ..":
        data[i] = ""


directory = {}
l = []
def find_sum_over_100000(data):
    a= 0
    directory = {}
    for i in range(len(data)):
        if "$ cd" in data[i] and "$ ls" == data[i+1]:
            data[i] = data[i].split()
            directory[data[i][2]] = 0
            data[i] = data[i+2]
            while not "$ cd" in data[i]:
                if type(data[i][0]) == int:
                    directory[[data[i][2]]] = directory.get() + data[i][0]
                i +=1
    return directory
print(find_sum_over_100000(data))
data =  open("Day6/input.txt", "r").read()

# Part One

def first_packet_marker(message):
    for i in range(len(message)-3):
        temp = []
        temp.append(message[i])
        if not message[i+1] in temp:
            temp.append(message[i+1])
            if not message[i+2] in temp:
                temp.append(message[i+2])
                if not message[i+3] in temp:
                    return i+4
        else:
            temp = []

# Part Two

def first_message_marker(message):
    for i in range(len(message)-13):
        temp = []
        temp.append(message[i])
        for j in range(i+1,i+14):
            if not message[j] in temp:
                temp.append(message[j])
            else:
                temp = []
                break
        if len(temp) == 14:
            return i+14 


print(first_packet_marker(data))
print(first_message_marker(data))

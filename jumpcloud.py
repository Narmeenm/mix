

def min_num_of_jump(steps,mysteps):
    index = 0
    jumps = [] * steps
    for index,step in enumerate(mysteps):
        if step == 0:
            jumps.append(index)
    print(jumps)
    i = 0
    min_steps = 0
    while i + 1 != len(jumps)-1:
        if jumps[i]+2 == jumps[i+2]:
            min_steps += 1
            i = i +2
        else:
            min_steps += 1
            i = i +1
    if i+1 == len(jumps) - 1:
        min_steps += 1

    return min_steps



steps= input("Enter the number of the clouds:")

steps = int(steps)

list_binary = input("Enter a list of binary steps 0 or 1: ")
userlist = list_binary.split()
array = list(map(int,userlist))
print(min_num_of_jump(steps,array))

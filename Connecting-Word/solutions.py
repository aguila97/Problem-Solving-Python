#Connecting Words

'''
Write a function that connects each previous word to the next word by the shared 
letters. Return the resulting string (removing duplicate characters in the overlap) 
and the minimum number of shared letters across all pairs of strings.

'''


def join(lst):
    counter = 0
    counter_list = []
    word = ""
    final_string = []
    index1 = 0
    index2 = 0
    for i in range(len(lst)-1):
        while True:
            if index2 == len(lst[i]):
                counter_list.append(counter)
                counter = 0

                if i == len(lst)-2:
                    word += lst[len(lst)-1][index1:]
                final_string.append(word)
                word = ""
                index2 = 0
                index1 = 0
                break

            if lst[i][index2] == lst[i+1][index1]:
                word += lst[i][index2]
                index1+=1
                index2+=1
                counter+=1
            else:
                word += lst[i][index2]
                index2+=1
    

    #print(final_string)
    #final_string.append()
    if len(final_string) != 1:
        return join(final_string)
    return final_string


print(join(["oven", "envier", "erase", "serious"]))
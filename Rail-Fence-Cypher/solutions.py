





def check_if_exists(key_depth,encrpyt_data,message,index):
    if key_depth in encrpyt_data.keys():
        encrpyt_data[key_depth].append(message[index])
    
    else:
        encrpyt_data[key_depth] = []
        encrpyt_data[key_depth].append(message[index])
    

    return encrpyt_data




# Rail fence cipher
# https://edabit.com/challenge/3RuQwqfrzSR6afAgz
def rail_fence_cipher(message, rails):
    
    depth = 0
    initial_encrytion = {}
    increment_switch = True 

    for i in range(len(message)):
        if depth < rails and increment_switch:
            initial_encrytion = check_if_exists(depth,initial_encrytion,message,i)
            if depth == (rails-1):
                increment_switch = False
                continue
            depth +=1
        else:
            depth -= 1
            initial_encrytion = check_if_exists(depth,initial_encrytion,message,i)
            if depth == 0:
                increment_switch = True
                depth +=1

    final_result = ""
    for item in initial_encrytion.values():
        for letter in item:
            final_result += letter

    
    return final_result



message = "WEWILLALLDIEONEDAY"
rails = 3

print(rail_fence_cipher(message, rails))




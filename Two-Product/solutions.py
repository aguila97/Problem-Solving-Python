
# Naive Approach
def two_product_naiveWay(lst,N):
    # list out the divisible number for N
    res = []
    for i in range(1,N+1):
        if N % i == 0:
                res.append(i)
        else:
                continue

    # to get the possible multiples of N              
    start = 0
    end = len(res) - 1
    multiples = []
    while start < end:
        gg = []
        if res[start] * res[end] == N:
                gg.append(res[start])
                gg.append(res[end])
        start = start + 1
        end = end -1
        multiples.append(gg)
            

    #print(multiples)
    # To verify if the lst has multiples of N
    for i in multiples:
        if i[0] in lst:
                if i[1] in lst:
                    return i
        else:
                return None
        



# Best Approach
def two_product(lst,N):
    
    prev = {}

    result = []
    for i in range(len(lst)):
        current_number = lst[i]
        other_pair = N // current_number

        try:
            test_pair = prev[other_pair]
            return [test_pair,i]
        except:
            prev[current_number] = i
    
    return result


#print(two_product([1, 2, -1, 4, 5], 20))
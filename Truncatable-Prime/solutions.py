import math
def prime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    if n > 2 and n % 2 == 0:
        return False
    max_divisor = math.floor(math.sqrt(n))
    for d in range(3,1 + max_divisor,2):
        if n % d == 0:
            return False
    return True





def truncatable(n):
    a = str(n)

    b = len(a)
    left = []
    right = []
    if "0" in a:
        return False
    #print("left")
    for i in range(b):
        aa = a[i:]
        s1 = prime(int(aa))
        if s1 == True:
            left.append(s1)


        #print(f"{aa} | {s1}")

    #print("right")
    for i in range(b,0,-1):
        bb = a[:i]
        s2 = prime(int(bb))
        if s2 == True:
            right.append(s2)


        #print(f"{bb} | {s2}")

    if len(left) == b and len(right) == b:
        return "both"
    elif len(left) == b:
        return "left"
    elif len(right) == b:
        return "right"
    else:
        return False

       

#print(prime(593))
##print(truncatable(347))
##print(truncatable(47))
##
##print(truncatable(9137))
##print(truncatable(5939))
##print(truncatable(317))
##print(truncatable(5))
##print(truncatable(139))
##print(truncatable(103))
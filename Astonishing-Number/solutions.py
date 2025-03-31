def is_astonishing(num):
    a = str(num)
    if len(a) % 2 == 0:
        b = len(a)
        f = []
        for i in range(b-1):
            c = a[i+1:]
            d = a[:i+1]
            #print(f"{d}|{c}")
            f.append(int(d))
            f.append(int(c))
        for i in range(len(f)-1):
            if f[i] > f[i+1]:
                gg = []
                for j in range(f[i+1],f[i]+1):
                        gg.append(j)
                if sum(gg) != num:
                        continue
                else:
                        return "It's BA-Astonishing"
            else:
                hh = []
                for h in range(f[i],f[i+1]+1):
                        hh.append(h)
                if sum(hh) != num:
                        continue                                  
                else:
                        return "It's AB-Astonishing"
        return False
                    
                    
                    
    else:
            b = int(round(len(a) / 2,0))
            f = []
            for i in range(b):
                    c = a[i+1:]
                    d = a[:i+1]
                    #print(f"{d}|{c}")
                    f.append(int(d))
                    f.append(int(c))
            for i in range(len(f)-1):
                    if f[i] > f[i+1]:
                        gg = []
                        for j in range(f[i+1],f[i]+1):
                                gg.append(j)
                        if sum(gg) != num:
                                
                                continue
                        else:
                                return "It's BA-Astonishing"
                    else:
                        gg = []
                        for j in range(f[i],f[i+1]+1):
                                gg.append(j)
                        if sum(gg) != num:
                                
                                continue
                        else:
                                return "It's AB-Astonishing"
            return False
                                   
                            






#print(is_astonishing(2002077))
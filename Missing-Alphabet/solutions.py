def missing_alphabets(txt):
       if len(txt) == len(set(txt)):
              a = "abcdefghijklmnopqrstuvwxyz"
              for i in txt:
                     if i in a:
                            a = a.replace(i,"")
              return a
       else:
              a = "abcdefghijklmnopqrstuvwxyz"
              b = {}
              for i in a:
                     b[i] = 0

              for i in txt:
                     if i in b.keys():
                            b[i] +=1
              final = ""
              mul = 0
              for k,v in b.items():
                     if v > 0:
                            mul = v
                     elif v == 0:
                            c = k * mul
                            final += c
              return final
                     
                     
              

##print(missing_alphabets("edabit"))
##print(missing_alphabets("abcdefghijklmnopqrstuvwxy"))
##print(missing_alphabets("aaaa"))
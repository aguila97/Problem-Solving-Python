def final_countdown(lst):
       a = len(lst) - 1

       b = 0
       c = []
       start = 0
       for i in range(a):
              d = []

              end = 0
              if lst[i+1] == lst[i] - 1:
                     if lst[i+1] == 1:
                            end = i + 1
                            c.append(lst[start:end+1])
                            start = end
              elif (lst[i] == 1 and lst[i-1] != lst[i] + 1):
                     d.append(lst[i])
                     c.append(d)
                     start+=1
              elif (lst[i+1] == 1 and lst[i+1] != lst[i] - 1):
                     d.append(lst[i+1])
                     c.append(d)
                     start+=1
              else:
                     start+=1
       final = []
       gg = len(c)
       final.append(gg)
       final.append(c)




##print(final_countdown([4, 3, 2, 1, 3, 2, 1, 1]))
##print(final_countdown([2,3,2,1,4,3,2,1]))
##print(final_countdown([1,2,1,1]))
##print(final_countdown([3,2,1,5,5,3,2,1,5,5]))
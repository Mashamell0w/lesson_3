Сюда пишем сортировки свои:

#Alimaskina
def cnt_sort(lst, mx):
    hlp = [0 for i in range(mx+1)]
    for elem in lst:
        hlp[elem] += 1
    res = []
    for i in range(mx+1):
        res += [i for j in range(hlp[i])]
        
    return res


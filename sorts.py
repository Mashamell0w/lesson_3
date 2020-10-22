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


#Koldubaeva:
def bubble_sort(lst):
	for i in range(len(lst)):
    		for j in range(len(lst) - 1):
        		if lst[j] > lst[j + 1]:
            			lst[j], lst[j+1] = lst[j+1], lst[j]
	return lst


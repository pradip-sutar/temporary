a = ['pr','a','dip']
lst = []
obj = 0
for i in a:
    obj=len(i)
    for j in a:
        if obj<len(i):
            lst.append(i)
        else:
            pass
print(lst)
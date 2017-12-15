list1 = [int(x) for x in input().split()]

list2 = [int(x) for x in input().split()]

common =list(set(list1).intersection(list2))

print(common)
l1ntl2 = []

for i in list1:
	if i not in(common):
		l1ntl2.append(i)
print(l1ntl2)
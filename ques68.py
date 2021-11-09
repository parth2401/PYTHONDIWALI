def sub_lists (l):
	lists = [[]]
	for i in range(len(l) + 1):
		for j in range(i):
			lists.append(l[j: i])
	return lists

l1 = [1, 2, 3]
print(sub_lists(l1))

Output: 
[[], [1], [2], [1, 2], [3], [2, 3], [1, 2, 3]]

"""
Input : a = [1, 2, 3, 4]
		b = [5, 6, 7, 8, 9, "gautam"]
Output : c = [1,5,2,6,3,7,4,8,9,"gautam"]
"""
a = [1, 2, 3, 4]
b = [5, 6, 7, 8, 9, "gautam"]
c = []

for i in range(len(b)):
	if len(a) > i:
		c.append(a[i])
		c.append(b[i])
	else:
		c.append(b[i])
print(c)

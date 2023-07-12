def map(func,iter):
	ls = []
	for i in iter:
		ls.append(func(i))
	yield ls


ls = [15.5,78.8]
res = map(lambda x: x/2,ls)
print(list(res))
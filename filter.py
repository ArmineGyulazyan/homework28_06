def fun(variable):
    letters = ['a', 'e', 'i', 'o', 'u']
    if (variable in letters):
        return variable


def filter(func, sequence):
	ls = []
	for i in sequence:
		f = func(i)
		if f:
			ls.append(f)
	return ls


seq = ['b', 'a', 'e', 'l', 'i', 'm', 'c', 'o']
res = filter(fun, seq)
print(res)	
	
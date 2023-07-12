def zip(item1,item2):
	d = {}
	for i in item1:
		for j in item2:
			if item1.index(i) == item2.index(j):
				d[i] = j
	t_pairs = d.items()	
	zip_tuple = tuple(t_pairs)
	yield zip_tuple



a = [1,2,3]
b = ["Mia","Lia","Ina"]
x = zip(a,b)
print(list(x))

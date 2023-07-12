def enumerate(sequence,start = 0):
	ch_start = start
	ls = []
	for i in range(len(sequence)):
		pairs = (ch_start, sequence[i])
		ch_start += 1
		ls.append(pairs)
	yield ls



seq = ["book1","book2","book3","book4","book5"]
res = list(enumerate(seq))
print(res)

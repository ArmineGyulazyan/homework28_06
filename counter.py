def counter():
	count = 0
	def cl():
		nonlocal count
		count += 1
		
		return "the function was called", count, "time"
	return cl

c = counter()
print(str(c()))
print(str(c()))
print(str(c()))
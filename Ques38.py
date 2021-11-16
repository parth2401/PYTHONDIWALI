def swap(string):
	
	start = string[1]
	
	end = string[-1]
	
	swapped_string = end + string[2:-1] + start
	print(swapped_string)

swap("GeeksforGeeks")
swap("Python")

OUTPUT :-

seksforGeeke
nthoy

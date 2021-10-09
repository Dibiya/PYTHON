strings=[]
myStr =  input('Enter the string : ')
k = int(input('Enter k  (value for accepting string) : '))

words = myStr.split(" ")
for word in words:
	if len(word) > k:
		strings.append(word)
		

print( strings)
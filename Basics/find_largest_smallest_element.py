'''number=[54,67,43,89,21,34]

print("largest elements is: ",max(number))
print("Smallest elements is: ",min(number))'''


lst=[]
num=int(input('Enter the total numbers:'))
for n in range(num):
    numbers=int(input('Enter the number:'))
    lst.append(numbers)
print("largest elements is: ",max(lst))
print("Smallest elements is: ",min(lst))

'''def countdown(n):
    while n >= 0:
         print(n)
         n -= 1
print(countdown(5))'''


def recursive_fibonnacci(n):
   
   if n <= 1:
       return n
   else:
        return(recursive_fibonnacci(n-1) + recursive_fibonnacci(n-2))

num = 10
if num <= 0:
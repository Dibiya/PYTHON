'''def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("Recursion value")
tri_recursion(10)'''

def factorial_recursive(n):
    
    if n == 1:
        return 1
    else:
        return n * factorial_recursive(n-1)

print(factorial_recursive(5))
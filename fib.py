def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

n = int(input("Enter terms: "))
a, b = 0, 1

print("Non-recursive:")
for i in range(n):
    print(a, end=" ")
    a, b = b, a+b

print("\nRecursive:")
for i in range(n):
    print(fib(i), end=" ")
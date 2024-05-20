def fibonacci():
    x,y=0,1
    while True:
        yield x
        x,y=y,x+y
n=int(input("No.of Elements to generate:"))
print("Number of Elements are:",n,"\nFibnocci numbers:")
fib=fibonacci()
for _ in range(n):
    print(next(fib),end="   ")
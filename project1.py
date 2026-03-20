"""The fibnacci series is a sequence where each number is
the sum of the two preceding numbers, defined by a mathematical recurrence relationship."""

def fib():
    a,b=0,1
    while True:
        yield a
        a,b=b,a+b
        
n=int(input("Enter total fibonacci number:"))       
f=fib()

for i in range(n):
  print(next(f))
  





        

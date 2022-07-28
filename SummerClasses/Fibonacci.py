from tracemalloc import start


end = int(input("Enter the end point: "))
a = 0
b = 1
start = 0
while(start <end):
    print(a)
    c = b+a
    a=b
    b=c
    start += 1

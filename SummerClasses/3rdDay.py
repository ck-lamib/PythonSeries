#list[accessing element, replace, insert, sort,  pop, loop]
#code to generate two different user inputed matrix and also adding them.
#i.e. element at row1[0][0] will be added to only row2[0][0]

m = int(input("Enter row: "))
n = int(input("Enter column: "))
print("it will be "+ "["+ str(m)+"]"+"["+ str(n)+"] matrix")
row1 = []
print("Enter details for first "+ "["+ str(m)+"]"+"["+ str(n)+"] matrix")
for i in range(m):
    column = []
    for j in range(n):
        a= int(input("enter number for "+"["+ str(i)+"]"+"["+ str(j)+"] :"))
        column.append(a)
    row1.append(column)

row2 = []
print("Enter details for second "+ "["+ str(m)+"]"+"["+ str(n)+"] matrix")
for i in range(m):
    column = []
    for j in range(n):
        a= int(input("enter number for "+"["+ str(i)+"]"+"["+ str(j)+"] :"))
        column.append(a)
    row2.append(column)

sum =[]
for i in range(m):
    sumCol = []
    for j in range(n):
        a = row1[i][j]
        b = row2[i][j]
        c = a+b
        sumCol.append(c)
    sum.append(sumCol)

print("first matrix is : ")
for i in range(m):
    for j in range(n):
        print(row1[i][j], " ", end="")
    print()

print("second matrix is : ")
for i in range(m):
    for j in range(n):
        print(row2[i][j], " ", end="")
    print()

print("sum matrix is : ")
for i in range(m):
    for j in range(n):
        print(sum[i][j], " ", end="")
    print()

n, m = map(int, input("Enter number of rows and columns: ").split())
matrix = []
for i in range(1, n+1):
    tempRow = list(
        map(int, input(f'Please enter {m} elements for row {i}: ').split()))
    matrix.append(tempRow)
k = int(input("Enter value of k: "))
if k > m:
    print("Invalid value of k")
elif k == m:
    columnToReverse = []
    for i in range(0, n):
        columnToReverse.append(matrix[i][m-1])
    reversedColumn = columnToReverse[::-1]
    for i in range(0, n):
        matrix[i][m-1] = reversedColumn[i]
    for i in matrix:
        print(i)
else:
    a = k
    for i in range(1, (m//k)+1):
        newColumnToReverse = []
        for j in range(0, n):
            newColumnToReverse.append(matrix[j][k-1])
        newReversedColumn = newColumnToReverse[::-1]
        for j in range(0, n):
            matrix[j][k-1] = newReversedColumn[j]
        k += a
    for i in matrix:
        print(i)

n1, m1 = map(int, input("Enter number of rows and columns: ").split())
matrix1 = []
for i in range(1, n1+1):
    tempRow = list(
        map(int, input(f'Enter {m1} elements for row {i}: ').split()))
    matrix1.append(tempRow)
nonZeroElementsOfMatrix1 = []
for i in range(0, n1):
    for j in range(0, m1):
        if matrix1[i][j] != 0:
            nonZeroElementsOfMatrix1.append((i, j, matrix1[i][j]))
        else:
            continue
n2, m2 = map(int, input("Enter rows and columns for matrix: ").split())
matrix2 = []
for i in range(1, n2+1):
    tempRow2 = list(
        map(int, input(f'Enter {m2} elements for row {i}: ').split()))
    matrix2.append(tempRow2)
nonZeroElementsOfMatrix2 = []
for i in range(0, n2):
    for j in range(0, m2):
        if matrix2[i][j] != 0:
            nonZeroElementsOfMatrix2.append((i, j, matrix2[i][j]))
        else:
            continue
if len(nonZeroElementsOfMatrix1) == len(nonZeroElementsOfMatrix2):

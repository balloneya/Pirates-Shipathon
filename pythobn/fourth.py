def rotate_layers_clockwise(matrix):
    n = len(matrix)
    layers = n // 2  # Number of layers

    for layer in range(layers):
        top = layer
        bottom = n - layer - 1
        left = layer
        right = n - layer - 1

        # Extract the elements in the current layer
        elements = []

        # Top row (left to right)
        for i in range(left, right + 1):
            elements.append(matrix[top][i])

        # Right column (top+1 to bottom-1)
        for i in range(top + 1, bottom):
            elements.append(matrix[i][right])

        # Bottom row (right to left)
        for i in range(right, left - 1, -1):
            elements.append(matrix[bottom][i])

        # Left column (bottom-1 to top+1)
        for i in range(bottom - 1, top, -1):
            elements.append(matrix[i][left])

        # Rotate the layer clockwise by one position
        elements = [elements[-1]] + elements[:-1]

        # Put the rotated elements back
        idx = 0

        # Top row
        for i in range(left, right + 1):
            matrix[top][i] = elements[idx]
            idx += 1

        # Right column
        for i in range(top + 1, bottom):
            matrix[i][right] = elements[idx]
            idx += 1

        # Bottom row
        for i in range(right, left - 1, -1):
            matrix[bottom][i] = elements[idx]
            idx += 1

        # Left column
        for i in range(bottom - 1, top, -1):
            matrix[i][left] = elements[idx]
            idx += 1

    return matrix


n = int(input("Enter number for nxn matrix: "))
matrix = []
for i in range(1, n+1):
    tempRow = list(
        map(int, input(f'Please enter {n} elements for row {i}: ').split()))
    matrix.append(tempRow)

rotatedMatrix = rotate_layers_clockwise(matrix)
for i in rotatedMatrix:
    print(i)

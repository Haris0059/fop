import math

try:
    moves = {}
    for i in range(1, 3):
        x = int(input(f'Enter x{i} coordinate (1–8): '))
        y = int(input(f'Enter y{i} coordinate (1–8): '))

        if x < 1 or x > 8 or y < 1 or y > 8:
            raise ValueError(f'Input value for point {i} is out of range (1–8).')

        moves[f'x{i}'] = x
        moves[f'y{i}'] = y

    # Calculate Euclidean distance
    d = math.sqrt(pow(moves['x2'] - moves['x1'], 2) + pow(moves['y2'] - moves['y1'], 2))

    if d < 2:
        print('YES')
    else:
        print('NO')

except ValueError as err:
    print(err)

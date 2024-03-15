with open('input.txt', 'r') as file:
    k = int(file.readline())
    coordinates = [list(map(int, file.readline().split())) for _ in range(k)]

min_x = min(c[0] for c in coordinates)
min_y = min(c[1] for c in coordinates)
max_x = max(с[0] for с in coordinates)
max_y = max(с[1] for с in coordinates)

with open('output.txt', 'w') as file:
    file.write(f"{min_x} {min_y} {max_x} {max_y}")

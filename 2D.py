N = int(input())  
cells = set() 
perimeter = 0 

for i in range(N):
    row, col = map(int, input().split())
    cells.add((row, col))

for row, col in cells:
    for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        neighbor = (row + dr, col + dc)
        if neighbor not in cells:
            perimeter += 1 

print(perimeter)  

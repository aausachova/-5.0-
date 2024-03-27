from collections import defaultdict

def read_matches(n):
    matches = []
    for _ in range(n):
        x1, y1, x2, y2 = map(int, input().split())
        if (x2, y2) < (x1, y1):
            x1, y1, x2, y2 = x2, y2, x1, y1
        matches.append(((x1, y1), (x2, y2)))
    return matches

def compare_matches(matches_A, matches_B):
    offset = defaultdict(int)
    for i in range(len(matches_A)):  
        for j in range(len(matches_B)): 
            dx = matches_B[j][0][0] - matches_A[i][0][0]
            dy = matches_B[j][0][1] - matches_A[i][0][1]
            left = (dx, dy)
            dx2 = matches_B[j][1][0] - matches_A[i][1][0]
            dy2 = matches_B[j][1][1] - matches_A[i][1][1]
            right = (dx2, dy2)
            result = (left, right)
            if (dx, dy) != (dx2, dy2):
                continue
            offset[result] += 1
    return offset

def main():
    n = int(input())
    matches_A = read_matches(n)
    matches_B = read_matches(n)
    
    offset = compare_matches(matches_A, matches_B)
    
    maxMatches = max(offset.values(), default=0)
    print(n - maxMatches)

if __name__ == "__main__":
    main()

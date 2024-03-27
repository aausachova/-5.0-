from collections import Counter

n = int(input())
playlists = []
for _ in range(n):
    k = int(input())
    playlist = set(input().split())
    playlists.append(playlist)

intersection = set.intersection(*playlists)
sorted_intersection = sorted(intersection)

print(len(sorted_intersection))
print(" ".join(sorted_intersection))

n1 = int(input())
list1 = set(map(int, input().split()))
n2 = int(input())
list2 = set(map(int, input().split()))
n3 = int(input())
list3 = set(map(int, input().split()))
result = list(list1.intersection(list2).union(list1.intersection(list3), list2.intersection(list3)))
result.sort()
for num in result:
    print(num, end=' ')

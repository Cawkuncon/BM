n = input()
a = list(map(lambda x: int(x), input().split()))
m = input()
b = list(map(lambda x: int(x), input().split()))
c = list(set(a) & set(b))
print(c.sort())
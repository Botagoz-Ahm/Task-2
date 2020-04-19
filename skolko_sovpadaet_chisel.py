a = int(input())
b = int(input())
c = int(input())
if (a == b == c):
    print('3')
elif (a == b) and (a, b != c):
    print('2')
elif (b == c) and (b, c != a):
    print('2')
elif (c == a) and (c, a != b):
    print('2')
else:
    print('0')

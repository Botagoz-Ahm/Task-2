k = int(input())
if k % 10 == 1 and k != 11:
    print(k, 'korova')
elif 2 <= k % 10 <= 4 and k // 10 != 1:
    print(k, 'korovy')
else:
    print(k, 'korov')

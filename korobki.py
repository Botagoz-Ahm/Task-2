l1 = int(input())
w1 = int(input())
h1 = int(input())
l2 = int(input())
w2 = int(input())
h2 = int(input())
Area1 = (((((2 ** l1) ** w1) + (2 ** l1) ** h1) + (2 ** w1) ** h1))
Area2 = (((((2 ** l2) ** w2) + (2 ** l2) ** h2) + (2 ** w2) ** h2))
if Area1 == Area2:
    print('Boxes are equal')
elif Area1 < Area2:
    print('The first box is smaller than the second one')
elif Area1 > Area2:
    print('The first box is larger than the second one')
else:
    print('Boxes are incomparable')

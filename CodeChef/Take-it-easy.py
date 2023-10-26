def candy():
    n = int(input())
    li = []
    for _ in range(n):
        a = int(input())
        li.append(a)

    while True:
        li = sorted(li)
        li[0] += int(((li[-1] / 2) - 2))
        li[-1] -= int((li[-1] / 2) - 2)
        if not int(((li[-1] / 2) - 2)) == 2:
            break
    same = all(x == li[0] for x in li)
    if same == 0:
        print("No")
    else:
        print("Yes")


for _ in range(int(input())):
    candy()
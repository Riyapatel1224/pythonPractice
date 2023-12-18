def candy():
    n = int(input())
    li = list(map(int, input().split()))
    s = sum(li)
    if s % n:
        print("No")
    else:
        need = 0
        avg = s // n
        for i in li:
            if abs(avg - i) % 2:
                need = 1
                break
            need += avg - i
        if need:
            print("No")
        else:
            print("Yes")


for _ in range(int(input())):
    candy()

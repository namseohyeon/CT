import sys
S = []
N = int(sys.stdin.readline().strip())

for i in range(N):
    command = sys.stdin.readline().strip()
    c=command.split()
    if (c[0] == '1'):
        S.append(int(c[-1]))
    elif (c[0] == '2'):
        if S:
            print(S.pop(-1))
        else:
            print(-1)
    elif (c[0]=='3'):
        print(len(S))
    elif (c[0] == '4'):
        if len(S) == 0:
            print(1)
        else:
            print(0)
    elif (c[0] == '5'):
        if S:
            print(S[-1])
        else:
            print(-1)
            
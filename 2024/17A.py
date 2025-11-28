A = int(input()[12:])
B = int(input()[12:])
C = int(input()[12:])
input()
arr = [int(i) for i in input()[9:].split(",")]

combo = lambda x: x if x < 4 else {4: A, 5: B, 6: C}[x]

i, n = 0, len(arr)
ans = []
while i < n - 1:
    code, op = arr[i], arr[i + 1]
    i += 2
    match code:
        case 0:
            A //= pow(2, combo(op))
        case 1:
            B ^= op
        case 2:
            B = combo(op) % 8
        case 3:
            i = op if A != 0 else i
        case 4:
            B ^= C
        case 5:
            ans.append(combo(op) % 8)
        case 6:
            B = A // pow(2, combo(op))
        case 7:
            C = A // pow(2, combo(op))
print(*ans, sep=",")

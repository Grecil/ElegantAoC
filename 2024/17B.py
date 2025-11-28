A = int(input()[12:])
B = int(input()[12:])
C = int(input()[12:])
input()
arr = [int(i) for i in input()[9:].split(",")]
n = len(arr)


def run(a):
    combo = lambda x: x if x < 4 else {4: a, 5: b, 6: c}[x]
    i = b = c = 0
    out = []
    while i < n - 1:
        code, op = arr[i], arr[i + 1]
        i += 2
        match code:
            case 0:
                a //= pow(2, combo(op))
            case 1:
                b ^= op
            case 2:
                b = combo(op) % 8
            case 3:
                i = op if a != 0 else i
            case 4:
                b ^= c
            case 5:
                out.append(combo(op) % 8)
            case 6:
                b = a // pow(2, combo(op))
            case 7:
                c = a // pow(2, combo(op))
    return out


ans = [0]
for i in range(len(arr)):
    ans = [n * 8 + a for n in ans for a in range(8) if arr[-i - 1 :] == run(n * 8 + a)]
print(ans[0])

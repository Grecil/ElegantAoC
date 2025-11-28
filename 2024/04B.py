import sys

arr = sys.stdin.read().splitlines()
print(
    sum(
        arr[i][j] + arr[i + 1][j + 1] + arr[i + 2][j + 2] in ("MAS", "SAM")
        and arr[i + 2][j] + arr[i + 1][j + 1] + arr[i][j + 2] in ("MAS", "SAM")
        for i in range(len(arr) - 2)
        for j in range(len(arr[0]) - 2)
    )
)

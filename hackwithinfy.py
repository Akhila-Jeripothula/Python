t = int(input())

for _ in range(t):

    # Read M, x, y
    m, x, y = map(int, input().split())

    # Read the houses where cops are present
    cops = list(map(int, input().split()))

    # Distance each cop can cover
    distance = x * y

    # Assume all houses are safe initially
    safe = [True] * 101   # Index 1 to 100

    # Mark unsafe houses
    for cop in cops:

        start = max(1, cop - distance)
        end = min(100, cop + distance)

        for house in range(start, end + 1):
            safe[house] = False

    # Count safe houses
    count = 0

    for house in range(1, 101):
        if safe[house]:
            count += 1

    print(count)
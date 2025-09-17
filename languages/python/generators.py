def factors(n: int):
    results = []

    for i in range(1, n + 1):
        if n % i == 0:
            results.append(i)

    return results

def new_factors(n: int):
    for i in range(1, n + 1):
        if n % i == 0:
            yield i


n = int(input("Enter the value for factor n: "))

print(f"Old Factors {factors(n)}")

print(f"Using Yield in Factors {new_factors(n)}")

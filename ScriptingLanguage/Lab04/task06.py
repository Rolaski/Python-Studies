def binomial_coefficient(n, k):
    # Warunek bazowy
    if k == 0 or k == n:
        return 1
    # Warunek rekurencyjny
    return binomial_coefficient(n - 1, k - 1) + binomial_coefficient(n - 1, k)


n = 10
k = 2
result = binomial_coefficient(n, k)
print(f"Wartosc symbolu Newtona dla n={n} i k={k} wynosi: {result}")

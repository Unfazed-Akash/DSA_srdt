# Q7: Find Factors of a Number

n = int(input("Enter a number: "))

print(f"\nFactors of {n}:")
factors = [i for i in range(1, n + 1) if n % i == 0]
print(*factors)

# Q4: Equation Solver
# Evaluate: a^3 + a^2*b + 2*a^2*b + 2*a*b^2 + a*b^2 + b^3
# Simplifies to: (a + b)^3

a = float(input("Enter value of a: "))
b = float(input("Enter value of b: "))
c = float(input("Enter value of c: "))

result = a**3 + a**2 * b + 2 * a**2 * b + 2 * a * b**2 + a * b**2 + b**3

print(f"Result of the equation = {result}")
print(f"Verification (a+b)^3   = {(a + b) ** 3}")

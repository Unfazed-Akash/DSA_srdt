# Q2: Pythagorean Triplets
# Accept a perimeter value and find all Pythagorean triplets (a, b, c)
# where a + b + c = perimeter and a^2 + b^2 = c^2

p = int(input("Enter the perimeter: "))

found = False
for a in range(1, p):
    for b in range(a, p - a):
        c = p - a - b
        if c > 0 and a * a + b * b == c * c:
            print(f"Pythagorean triplet: {a}, {b}, {c}")
            found = True

if not found:
    print("No Pythagorean triplet found for the given perimeter")

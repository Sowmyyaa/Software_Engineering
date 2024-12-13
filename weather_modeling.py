import math


with open("SE_exp-01.txt", "r") as file:
    for line in file:
        if not line.strip():
            continue
        a, b, c = map(float, line.split())

      
        discriminant = b**2 - 4*a*c
        if discriminant >= 0:
            root1 = (-b + math.sqrt(discriminant)) / (2 * a)
            root2 = (-b - math.sqrt(discriminant)) / (2 * a)
            print(f"Roots for {a}x² + {b}x + {c} = 0: {root1:.2f}, {root2:.2f}")
            temperature = root1
            print(f"Modeled Temperature: {temperature:.2f}°C")
        else:
            print(f"No real roots for {a}x² + {b}x + {c} = 0")

OUTPUT:

Roots for 1.0x² + -3.0x + 2.0 = 0: 2.00, 1.00
Modeled Temperature: 2.00°C
Roots for 2.0x² + -4.0x + 1.0 = 0: 1.71, 0.29
Modeled Temperature: 1.71°C
Roots for 1.0x² + -2.0x + -3.0 = 0: 3.00, -1.00
Modeled Temperature: 3.00°C

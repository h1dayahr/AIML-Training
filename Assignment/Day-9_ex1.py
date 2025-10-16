def find_greatest(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3


# Main Program
print("=" * 45)
print(f"{'Find the Greatest of Three Numbers':^45}")
print("=" * 45)

n1 = float(input("Enter first number:  "))
n2 = float(input("Enter second number: "))
n3 = float(input("Enter third number:  "))

greatest = find_greatest(n1, n2, n3)

print("\n" + "=" * 45)
print(f"{'Number 1':<15} | {'Number 2':<15} | {'Number 3':<10}")
print("-" * 45)
print(f"{n1:<15} | {n2:<15} | {n3:<10}")
print("=" * 45)
print(f"{'Greatest Number':<30}: {greatest}")
print("=" * 45)

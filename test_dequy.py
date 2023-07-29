def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        print(n)
        return n * factorial(n-1)

# Ví dụ sử dụng hàm đệ quy tính giai thừa của 5
result = factorial(5)
print("Giai thừa của 5 là:", result)
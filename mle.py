def print_pascals_triangle(n):
    # Function to calculate factorial
    def factorial(num):
        if num == 0 or num == 1:
            return 1
        else:
            return num * factorial(num - 1)

    # Function to calculate binomial coefficient
    def binomial_coefficient(n, r):
        return factorial(n) // (factorial(r) * factorial(n - r))

    # Creating Pascal's Triangle as a 2D list
    pascals_triangle = [[0] * (i + 1) for i in range(n)]
    for i in range(n):
        for j in range(i + 1):
            pascals_triangle[i][j] = binomial_coefficient(i, j)

    # Printing Pascal's Triangle in a right-angled format
    for row in pascals_triangle:
        print(" ".join(map(str, row)))

# Taking input from the user
row_number = int(input())
print_pascals_triangle(row_number)
#!/usr/bin/python3
def pascal_triangle(n):
    """
    pascal_triangle - Returns a list of lists of integers
                      representing Pascal’s triangle of n.

    @n: number of rows of Pascal's triangle to generate

    Return: A list of lists where each sublist represents
            a row in Pascal's triangle. If n <= 0, returns
            an empty list.
    """
    if n <= 0:
        return []
    triangle = [[1]]  # Initialize the first row of Pascal's triangle

    for i in range(1, n):
        prev_row = triangle[-1]  # Get the previous row
        new_row = [1]  # Each row starts with 1
        # Generate the middle elements by summing adjacent elements
        for j in range(1, len(prev_row)):
            new_row.append(prev_row[j - 1] + prev_row[j])
        new_row.append(1)  # Each row ends with 1
        triangle.append(new_row)  # Append the new row to the triangle
    return triangle

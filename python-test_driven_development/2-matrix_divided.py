#!/usr/bin/python3
def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by div.
    
    Args:
        matrix: A list of lists of integers or floats.
        div: A number (int/float) to divide by.
        
    Returns:
        A new matrix with values rounded to 2 decimal places.
    """
    
    # Check if div is a number (int or float)
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Check for division by zero
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Check if matrix is a list of lists and not empty
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Get the length of the first row to compare with others
    if not isinstance(matrix[0], list):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    row_size = len(matrix[0])
    new_matrix = []

    for row in matrix:
        # Check if the row is a list
        if not isinstance(row, list):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        
        # Check if all rows have the same size
        if len(row) != row_size:
            raise TypeError("Each row of the matrix must have the same size")
        
        new_row = []
        for element in row:
            # Check if each element is an integer or float
            if not isinstance(element, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            
            # Divide and round to 2 decimal places
            new_row.append(round(element / div, 2))
        
        new_matrix.append(new_row)

    return new_matrix

def matrix_mul(m_a, m_b):
    """
    Multiplies two matrices.

    Args:
        m_a (list): Matrix A represented as a list of lists of integers or floats.
        m_b (list): Matrix B represented as a list of lists of integers or floats.

    Returns:
        list: The product of matrix multiplication.

    Raises:
        TypeError: If m_a or m_b is not a list, not a list of lists, or contains non-numeric elements.
        ValueError: If m_a or m_b is empty or if matrices cannot be multiplied due to incompatible dimensions.
    """
    # Validate m_a and m_b
    for matrix, name in [(m_a, 'm_a'), (m_b, 'm_b')]:
        if not isinstance(matrix, list):
            raise TypeError(f"{name} must be a list")
        if not matrix or (len(matrix) == 1 and not matrix[0]):
            raise ValueError(f"{name} can't be empty")
        if not all(isinstance(row, list) for row in matrix):
            raise TypeError(f"{name} must be a list of lists")
        if not all(isinstance(num, (int, float)) for row in matrix for num in row):
            raise TypeError(f"{name} should contain only integers or floats")
        if not all(len(row) == len(matrix[0]) for row in matrix):
            raise TypeError(f"Each row of {name} must be of the same size")

    # Validate compatibility for matrix multiplication
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    # Perform matrix multiplication
    result = [[sum(a * b for a, b in zip(row_a, col_b)) for col_b in zip(*m_b)] for row_a in m_a]
    return result

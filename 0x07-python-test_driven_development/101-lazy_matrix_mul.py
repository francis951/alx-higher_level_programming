#!/usr/bin/python3
"""
Module for lazy_matrix_mul.
Contains a function that multiplies 2 matrices using NumPy.
"""

import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies 2 matrices using NumPy.

    Args:
        m_a (list): The first matrix.
        m_b (list): The second matrix.

    Returns:
        numpy.ndarray: The product of the multiplication.

    Raises:
        ValueError: If matrices are not valid for multiplication.
    """
    try:
        result = np.dot(np.array(m_a), np.array(m_b))
        return result
    except ValueError as e:
        raise ValueError("Matrix shapes are not aligned for multiplication") from e

if __name__ == "__main__":
    m_a = [[1, 2], [3, 4]]
    m_b = [[1, 2], [3, 4]]
    print(lazy_matrix_mul(m_a, m_b))

    m_a = [[1, 2]]
    m_b = [[3, 4], [5, 6]]
    print(lazy_matrix_mul(m_a, m_b))


# Issue: https://github.com/sharminshanta/mathematics-python/issues/2 - Linear Algebra Basic #2

# Scalar: is like a point, literally anything that is a single numeric value
s = 12
# print(s)

# Vector: Vectors are lines with direction.
# Vector are built from components,
# which are ordinary numbers. We can think of a vector as a list of numbers,
# and vector algebra as operations performed
# on the numbers in the list. In other words vector is the numpy 1-D array.
# Vectors are matrices with either 1 row OR 1 column depending on
# whether we have row vector OR column vector. It occupies the elements in a similar manner as that of a Python list.
# Syntax: numpy.array(list) // Numpy: Numerical Python

'''
NumPy is a general-purpose array-processing package. It provides a high-performance multidimensional array object, 
and tools for working with these arrays. It is the fundamental package for scientific computing with Python. 
Numpy is basically used for creating array of n dimensions.
'''
import numpy as np

v = [10, 20, 30, 40, 50]
v = np.array(v)
v = np.array(v)

# print("Vector created from a list:")
# print(v)

'''
Matrices: Collection of numbers ordered in rows and columns.
A matrix is a collection of numbers arranged in a rectangular array in rows and columns. 
In the fields of engineering, physics, statistics, and graphics, matrices are widely used to 
express picture rotations and other types of transformations.
The matrix is referred to as an m by n matrix, denoted by the symbol “m x n” if there are m rows and n columns.
'''
m = np.array(
    [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
    ]
)

# print("Matrix =", m)

'''
Tensor: Although tensors appear to be complex objects, they can be understood as a collection of vectors and matrices. 
Understanding vectors and matrices is essential to understanding tensors. The subscript indicates the (row, column). 
Another way to think about a matrix is a vector with vectors as its elements.
'''

m1 = np.array(
    [
        [1, 2, 3, 4],
        [5, 6, 7, 8]
    ]
)

m2 = np.array(
    [
        [4, 3, 2, 1],
        [8, 7, 6, 5]
    ]
)

tensor = np.array([m1, m2])
print(tensor)

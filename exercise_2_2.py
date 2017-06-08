#!/usr/bin/env python
from __future__ import print_function
import numpy as np

import qml
from qml.kernels import gaussian_kernel
from qml.kernels import laplacian_kernel

from tutorial_data import compounds

if __name__ == "__main__":

    # Import QM7, already parsed to QML
    from tutorial_data import compounds

    from qml.kernels import gaussian_kernel
    
    # For every compound generate a coulomb matrix or BoB
    for mol in compounds:

        mol.generate_coulomb_matrix(size=23, sorting="row-norm")
        # mol.generate_bob(size=23, asize={"O":3, "C":7, "N":3, "H":16, "S":1})

    # Make a big 2D array with all the representations
    X = np.array([mol.coulomb_matrix for mol in compounds])
    # X = np.array([mol.bob for mol in compounds])

    # Print all representations
    print("Representations:")
    print(X)

    # Run on only a subset of the first 100 (for speed)
    X = X[:100]

    # Define the kernel width
    sigma = 1000.0

    # K is also a Numpy array
    K = gaussian_kernel(X, X, sigma)
    
    # Print the kernel
    print("Gaussian kernel:")
    print(K)

#!/usr/bin/env python
import numpy as np

import qml
from qml.kernels import gaussian_kernel
from qml.kernels import laplacian_kernel

from tutorial_data import compounds

if __name__ == "__main__":

    # For every compound generate a coulomb matrix
    for mol in compounds:

        mol.generate_coulomb_matrix(size=23, sorting="row-norm")

        # Or generate 
        # mol.generate_bob(size=23, asize={"O":3, "C":7, "N":3, "H":16, "S":1})

    # Make a big 2D array with all the 
    X = np.array([mol.coulomb_matrix for mol in compounds])
    # X = np.array([mol.bob for mol in compounds])

    # Print all the representations
    print X

   
    # Calculate and print a Gaussian kernel for QM7
    sigma = 800.0
    K1 = gaussian_kernel(X, X, sigma)
    print K1

    # Calculate and print a Lapacian kernel for QM7
    sigma = 4000.0
    K2 = laplacian_kernel(X, X, sigma)
    print K2

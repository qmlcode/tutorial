#!/usr/bin/env python
from __future__ import print_function
import numpy as np

import qml
from qml.kernels import gaussian_kernel
from qml.kernels import laplacian_kernel
from qml.math import cho_solve

from tutorial_data import compounds
from tutorial_data import energy_pbe0

if __name__ == "__main__":

    # Import QM7, already parsed to QML
    from tutorial_data import compounds

    from qml.kernels import gaussian_kernel
    
    # For every compound generate a coulomb matrix or BoB
    for mol in compounds:

        mol.generate_coulomb_matrix(size=23, sorting="row-norm")
        # mol.generate_bob(size=23, asize={"O":3, "C":7, "N":3, "H":16, "S":1})

    # Make a big 2D array with all the representations
    X = np.array([mol.representation for mol in compounds])
    # X = np.array([mol.bob for mol in compounds])

    # Print all representations
    print("Representations:")
    print(X)


    # Assign 1000 first molecules to the training set
    X_training = X[:1000]
    Y_training = energy_pbe0[:1000]
   
    sigma = 4000.0
    K = gaussian_kernel(X_training, X_training, sigma)
    print("Gaussian kernel:")
    print(K)

    # Add a small lambda to the diagonal of the kernel matrix
    K[np.diag_indices_from(K)] += 1e-8

    # Use the built-in Cholesky-decomposition to solve
    alpha = cho_solve(K, Y_training) 

    print("Alphas:")
    print(alpha)


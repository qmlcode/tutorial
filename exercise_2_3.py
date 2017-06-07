#!/usr/bin/env python
from __future__ import print_function
import numpy as np

import qml
from qml.kernels import gaussian_kernel
from qml.math import cho_solve

from tutorial_data import compounds
from tutorial_data import energy_pbe0

if __name__ == "__main__":

    # For every compound generate a coulomb matrix
    for mol in compounds:

        mol.generate_coulomb_matrix(size=23, sorting="row-norm")

    # Make a big 2D array with all the 
    X = np.array([mol.coulomb_matrix for mol in compounds])

    print(energy_pbe0)

    # Assign 1000 first molecules to the training set
    X_training = X[:1000]
    Y_training = energy_pbe0[:1000]

   
    sigma = 700.0
    K = gaussian_kernel(X_training, X_training, sigma)
    print(K)

    # Add a small lambda to the diagonal of the kernel matrix
    K[np.diag_indices_from(K)] += 1e-8

    # Use the built-in Cholesky-decomposition to solve
    alpha = cho_solve(K, Y_training) 

    print(alpha)

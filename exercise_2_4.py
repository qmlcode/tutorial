#!/usr/bin/env python
from __future__ import print_function
import numpy as np

import qml
from qml.kernels import gaussian_kernel
from qml.math import cho_solve

from tutorial_data import compounds
from tutorial_data import energy_pbe0
from tutorial_data import energy_delta

if __name__ == "__main__":

    # For every compound generate a coulomb matrix
    for mol in compounds:

        mol.generate_coulomb_matrix(size=23, sorting="row-norm")
        # mol.generate_bob(size=23, asize={"O":3, "C":7, "N":3, "H":16, "S":1})
            

    # Make a big 2D array with all the 
    X = np.array([mol.coulomb_matrix for mol in compounds])
    # X = np.array([mol.bob for mol in compounds])

    print(energy_pbe0)

    # Assign 1000 first molecules to the training set
    X_training = X[:1000]
    Y_training = energy_pbe0[:1000]
    # Y_training = energy_delta[:1000]

    # Assign 1000 first molecules to the training set
    X_test = X[-1000:]
    Y_test = energy_pbe0[-1000:]
    # Y_test = energy_delta[-1000:]
   
    # Calculate the Gaussian kernel
    sigma = 700.0
    K = gaussian_kernel(X_training, X_training, sigma)
    print(K)

    # Add a small lambda to the diagonal of the kernel matrix
    K[np.diag_indices_from(K)] += 1e-8

    # Use the built-in Cholesky-decomposition to solve
    alpha = cho_solve(K, Y_training) 

    print(alpha)

    # calculate a kernel matrix between test and training data, using the same sigma
    Ks = gaussian_kernel(X_test, X_training, sigma)

    # Make the predictions
    Y_predicted = np.dot(Ks, alpha)

    # Calculate MAE
    print(np.mean(np.abs(Y_predicted - Y_test)))



#!/usr/bin/env python
from __future__ import print_function
import qml

if __name__ == "__main__":

    # Create the molecule from the file qm7/0001.xyz
    mol = qml.Compound(xyz="qm7/0001.xyz")

    # Generate and print a coulomb matrix for the structure
    mol.generate_coulomb_matrix(size=5, sorting="row-norm")
    print(mol.coulomb_matrix)

    # Generate and print a bag of bonds representation
    # mol.generate_bob(size=5, asize={"C":2, "H":5})
    # print(mol.bob)


    # Print other properties stored in the object
    print(mol.coordinates)
    print(mol.atomtypes)
    print(mol.nuclear_charges)
    print(mol.name)
    print(mol.unit_cell)

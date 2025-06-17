#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        if not row:  # boş sətir varsa, çap etmə
            continue
        print(" ".join("{:d}".format(i) for i in row))


#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    # Əgər matrix boşdursa və ya matrix tək boş siyahıdan ibarətdirsə,
    # heç nə çap etmirik
    if matrix == [[]] or matrix == []:
        return

    for row in matrix:
        # boş satır varsa, çap etmə
        if not row:
            continue
        print(" ".join("{:d}".format(i) for i in row))

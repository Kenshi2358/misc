# multiprocessing example.

import multiprocessing
from multiprocessing import Process


def print_cube(num):
    """function to print cube of given num  """
    print(f"Cube: {num * num * num}")


def print_square(num):
    """function to print square of given num"""
    print(f"Square: {num * num}")


def print_pokemon(names, process_name):

    for each_name in names:
        print(f"{process_name} - {each_name}")


if __name__ == "__main__":

    # Creating an object from the Process class.
    # Target is the function to be executed by the Process class.
    # args is the arguments to be passed to the target function.

    p1 = multiprocessing.Process(target=print_square, args=(3, ))
    p2 = multiprocessing.Process(target=print_cube, args=(3, ))

    p1.start()
    p2.start()
    p1.join()
    p2.join()

    names_list = [['Charmander'], ['Squirtle'], ['Bulbasaur']]
    num_names = len(names_list)

    process_name_list = []
    for i, each_name in enumerate(names_list, start=1):

        process_name = f"p{i}"
        p = Process(name=process_name, target=print_pokemon, args=(each_name, process_name))
        # print(f"i: {i}")
        p.start()
        process_name_list.append(p)

    # Wait for all processes to complete.
    for each_process in process_name_list:
        each_process.join()

    print("Done!")

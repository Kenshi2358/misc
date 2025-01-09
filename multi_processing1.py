# multiprocessing example.

from multiprocessing import Process, Pool

def print_cube(num): 
    """function to print cube of given num  """
    print(f"Cube: {num * num * num}") 


def print_square(num): 
    """function to print square of given num"""
    print(f"Square: {num * num}") 


def print_pokemon(names, process_name):

    for each_name in names:
        print(f"{process_name} - {each_name}")

# # with Pool(2) as p:
# #     print(p.map(print_pokemon, names1))

if __name__ == "__main__": 

    # Creating an object from the Process class.
    # Target is the function to be executed by .Process
    # args is the arguments to be passed to the target function.

    # p1 = multiprocessing.Process(target=print_square, args=(10, ))     
    # p2 = multiprocessing.Process(target=print_cube, args=(10, )) 

    # name1 = ['Charmander']
    # name2 = ['Squirtle']
    # name3 = ['Bulbasaur']

    # for i in range(5):
    #     p1 = Process(target=print_pokemon, args=(name1,))
    #     p2 = Process(target=print_pokemon, args=(name2,))
    #     p3 = Process(target=print_pokemon, args=(name3,))

    #     p1.start()
    #     p2.start()
    #     p3.start()

    # # wait until each process is finished.
    # p1.join()
    # p2.join()
    # p3.join()

    # # both processes finished 
    # print("Done!") 

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


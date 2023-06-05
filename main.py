from random import randint

from bubble import bubble
from selection import selection
from insertion import insertion
from merge import sort_mg
import time as tm


def main():
    num_list = [randint(0, 100) for x in range(10)]
    print(f"List before sort: {num_list}")

    bubble_start = tm.time()
    bubble_list = bubble(num_list)
    bubble_finish = tm.time()

    selection_start = tm.time()
    selection_list = selection(num_list)
    selection_finish = tm.time()

    insertion_start = tm.time()
    insertion_list = insertion(num_list)
    insertion_finish = tm.time()

    merge_start = tm.time()
    merge_list = sort_mg(num_list)
    merge_finish = tm.time()


    print(f"Bubble sort: {bubble_list} \n Execution time: {bubble_finish - bubble_start}seconds\n")
    print(f"Selection sort: {selection_list} \n Execution time: {selection_finish - selection_start}seconds\n")
    print(f"Insertion sort: {insertion_list} \n Execution time: {insertion_finish - insertion_start}seconds\n")
    print(f"Merge sort: {merge_list} \n Execution time: {merge_finish - merge_start} seconds\n")



if __name__ == "__main__":
    main()

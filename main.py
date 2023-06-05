from random import randint

from bubble import bubble
from selection import selection
from insertion import insertion
from merge import sort_mg
import datetime as dt


def main():
    num_list = [randint(0, 5000) for x in range(5000)]
    print(f"List before sort: {num_list}")

    b_st = dt.datetime.now()
    bubble_list = bubble(num_list)
    b_et = dt.datetime.now()

    s_st = dt.datetime.now()
    selection_list = selection(num_list)
    s_et = dt.datetime.now()

    i_st = dt.datetime.now()
    insertion_list = insertion(num_list)
    i_et = dt.datetime.now()

    m_st = dt.datetime.now()
    merge_list = sort_mg(num_list)
    m_et = dt.datetime.now()


    print(f"Bubble sort: {bubble_list} \n Execution time: {(b_et - b_st).total_seconds()} seconds\n")
    print(f"Selection sort: {selection_list} \n Execution time: {(s_et - s_st).total_seconds()} seconds\n")
    print(f"Insertion sort: {insertion_list} \n Execution time: {(i_et - i_st).total_seconds()} seconds\n")
    print(f"Merge sort: {merge_list} \n Execution time: {(m_et - m_st).total_seconds()} seconds\n")



if __name__ == "__main__":
    main()

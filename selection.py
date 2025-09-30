# General Idea: 
# split list into sorted and unsorted portion
# Find the smallest value in the unsorted portion and swap with first unsorted element
def selection(my_list):
    unsorted_index = 0
    while unsorted_index < len(my_list):
        min = my_list[unsorted_index]
        min_index = unsorted_index
        # Iterate through unsorted portion of array to find minimum
        for i in range(unsorted_index, len(my_list), 1):
            if (my_list[i] < min): 
                min_index = i
                min = my_list[i]
        # Swap with first entry in array
        temp = my_list[unsorted_index]
        my_list[unsorted_index] = my_list[min_index]
        my_list[min_index] = temp
        unsorted_index = unsorted_index+1

def main():
    my_list = [5, 4, 2, 6, 3, 1]
    selection(my_list)
    print("result of sorting: ", my_list)

if __name__ == "__main__":
    main()
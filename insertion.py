# General Idea: 
# split list into sorted and unsorted portion
# consider the first item in the list to be sorted
# retrieve the first item of the unsorted list 
# iterate through sorted list until value that is greater than current item is encountered
# shift all items to the right and insert the value 

def insertion(my_list):
    # no-op if the list is quite small 
    if len(my_list) <= 1:
        return

    for i in range(1, len(my_list)):
        item = my_list[i];
        
        j = i - 1
        while j >= 0 and my_list[j] > item: 
            my_list[j+1] = my_list[j]
            j = j - 1

        my_list[j + 1] = item
        print("ith iteration of sorting: ", i, my_list)


def main():
    my_list = [5, 4, 2, 6, 3, 1]
    insertion(my_list)
    print("result of sorting: ", my_list)

if __name__ == "__main__":
    main()
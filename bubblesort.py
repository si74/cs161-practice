# General idea:
# Iterate through array and swap neighboring entries if j > i
# until no swaps have been done 
def bubblesort(my_list):
    length = len(my_list)
    swapped = True;
    while swapped: 
        swapped = False;
        for i in range(length-1):
            if my_list[i] > my_list[i+1]:
                temp = my_list[i]
                my_list[i] = my_list[i+1]
                my_list[i+1] = temp
                swapped = True

def main():
    my_list = [5, 4, 2, 6, 3, 1]
    bubblesort(my_list)
    print("result of sorting: ", my_list)

if __name__ == "__main__":
    main()
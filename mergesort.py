# Note: This is not an in-place merge sort 
def mergesort(my_list):
    # Base-case
    if (len(my_list) <= 1): 
        return my_list
    
    mid = len(my_list)//2
    
    list1 = my_list[0:mid]
    list2 = my_list[mid:]

    list1 = mergesort(list1)
    list2 = mergesort(list2)

    return merge(list1,list2)

def merge(list1, list2):
    newlist = []; 

    len1 = len(list1)
    len2 = len(list2)

    i = 0
    j = 0

    while (i < len1 and j < len2):
        if list1[i] <= list2[j]:
            newlist.append(list1[i])
            i += 1
        else: 
            newlist.append(list2[j])
            j += 1

    if i >= len1: 
        newlist.extend(list2[j:])
    
    if j >= len2: 
        newlist.extend(list1[i:])

    return newlist

def main():
    my_list = [5, 4, 2, 6, 3, 1]
    sorted_list = mergesort(my_list)
    print("result of sorting: ", sorted_list)

if __name__ == "__main__":
    main()
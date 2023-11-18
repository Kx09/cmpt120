"""

Sorting 

Recusion: defining a solution to the problem in terms of the solutions of the sub-problems. 

Factorial is a recursive function, defined recursively.

Recursive function: function keeps calling itself wihtin itself.

f(N) = ?

How many times does the function run the critical function 

3 x 4 = 3 + 3 + 3 + 3
15/4 = ((15-4)-4)-4

log2(64) = 6
64/2/2/2/2/2/2 = log2(64)

I learned the binary powers of 2 but not the times tables, retarded asf.

hence f(n) = log2(n) + 1
log base 2 because we are dividing by 2 and + 1 which is apporximate to the next integer. Rounding it up.

Do it untill you can no longer do so.


For a billion entries, a sequential search it would take a billion seconds to get it done
Using bogo-sort it takes ~ 30 operations of the function.

Bogo sort,
/2 and see left and right of the ordered list

Binary search: 

"""

""""""
def selection_sort(arr):
    n = len(arr)
    # Traverse through all array elements
    for i in range(n):
        # Find the minimum element in remaining unsorted array
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        # Swap the found minimum element with the first element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

# Example usage:

"""
my_list = [64, 25, 12, 22, 11]
selection_sort(my_list)
print("Sorted array is:", my_list)
"""









def bubble_sort(arr):
    n = len(arr)
    # Traverse through all array elements
    for i in range(n-1):
        # Last i elements are already in place
        for j in range(0, n-i-1):
            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Example usage:

"""
my_list = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(my_list)
print("Sorted array is:", my_list)
"""

"""
Redoing all algorithms at home.
The algorithms were:

Sequential search(slowest one, goes through the list n times for every element)
Binary search(searches from one half and creates further halfs)
Bubble sort(finds smallest of first 2 and then keeps going down the list)
Selection sort(finds smallest element in the list starting from 1 and sets it at one, then does the same down the list)
Insertion sort(finds the first two then goes down the list looking for the position to insert into)

"""

def SeqS(lis,to_find):
    for i in range(len(lis)):
        if lis[i] == to_find:
            return i
    return -1




def BubbleSort(a):

    end = len(a)

    for i in range(end):
        for i in range(1,end):
            if a[i-1] > a[i]:
                (a[i-1],a[i]) = (a[i],a[i-1])
            print(a[i],a[i-1])
            print(a)
        
        end = end - 1 

        
        


def BinSearch(a,find):

    end = len(a)-1
    start = 0

    while end >= start:
        middle = int((start + end)/2)
        print(middle, end, start)

        if middle == find:
            return [middle]
        elif middle > find:
            end = middle -1
        else:
            start = middle + 1
        
    return - 1
        


def selction_sort(a):


    for start in range(len(a)-start):
        smallest = a[start]
        for i in range(len(a)):
            
            if a[i+1] < smallest:
                smallest = a[i+1]
        start += 1 
    

def insertionsort(a):

    for i in range(1,len(a)):
    
        first = i-1
        second = i

        while first >= 0 and a[first] > a[second]:
            a[first + 1] = a[second]
            print(a[first])
            print(a[second])
            second = second - 1 
        
        a[first+1] == second 
            




def smallest(a):

    smallest = a[0]
    for i in range(len(a)):
        if smallest > a[i]:
            smallest = a[i]

    print(f"the smallest element is{smallest}")

a = [4,5,1,8,3,2,7,0,6]
print(a)
find = 0

selection_sort(a)

print(f"the sorted list is {a}")



#output = BinSearch(a,5)

"""
if output == -1:
    print(f"the element {find} was not found")
else:
    print("the element is at position",output)
"""


""""
Home work questions. 
Computing the maximum element of a list.


set maximum to the first element
Iterate through every item of the list,
check if item in list is > max, if it is then set max to that new element,
do it through all elements.
prints the max.

PSUEDO-CODE:

arr = [1,3,5,6]

max = arr[0]

for i in range(0,len(arr)-1):

    if arr[i] > max:
        max = arr[i]

ouput(arr[i])


Critical operation of this function is comparison 

O(n)



"""
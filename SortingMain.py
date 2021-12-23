def selection_sort(to_sort, sorted_ind, min_ind):
    sorted_ind = 0
    min_ind = 0
    for j in range(len(to_sort)):
        min_ind = j
        for i in range(j, len(to_sort)):
            if to_sort[i] < to_sort[min_ind]:
                min_ind = i

        # tuple swapping
        to_sort[j], to_sort[min_ind] = to_sort[min_ind], to_sort[j]


def merge_sort(to_sort):
    if len(to_sort) > 1:
        mid = len(to_sort) // 2
        first_half = to_sort[:mid]
        second_half = to_sort[mid:]
        merge_sort(first_half)
        merge_sort(second_half)

        i = j = k = 0

        while i < len(first_half) and j < len(second_half):
            if first_half[i] <= second_half[j]:
                # The value from the left half has been used
                to_sort[k] = first_half[i]
                # Increase iterator
                i += 1
            else:
                to_sort[k] = second_half[j]
                j += 1
            # Move to the next index
            k += 1

        # Remaining values
        while i < len(first_half):
            to_sort[k] = first_half[i]
            i += 1
            k += 1

        while j < len(second_half):
            to_sort[k] = second_half[j]
            j += 1
            k += 1


def insertion_sort(to_sort):
    for i in range(1, len(to_sort) ):
        j = i
        while j > 0 and to_sort[j - 1] > to_sort[j]:
            to_sort[j], to_sort[j - 1] = to_sort[j - 1], to_sort[j]
            j = j - 1

def bubble_sort(to_sort):
    for i in range(1, len(to_sort)):
        for j in range(0, len(to_sort) - 1):
            if to_sort[j] > to_sort[j+1]:
                to_sort[j], to_sort[j+1] = to_sort[j+1], to_sort[j]

# main
number_elem = int(input("Enter the amount of numbers to sort -> "))
if number_elem == 0:
    print("Enter valid amount")
    n = int(input("Enter the amount of numbers to sort -> "))

need_sort = []

for i in range(0, number_elem):
    element = int(input())
    need_sort.append(element)

sortAlgo = int(input("Choose sorting algorithm (1-#): \n 1. Selection Sort \n 2. Merge Sort \n "
                     "3. Insertion Sort \n 4. Bubble Sort \n -> "))

if sortAlgo == 1:
    selection_sort(need_sort, 0, 0)
    print("Results:")
    for i in need_sort:
        print(i)

# also print how fast it worked
elif sortAlgo == 2:
    merge_sort(need_sort)
    print("Results:")
    for i in need_sort:
        print(i)

elif sortAlgo == 3:
    insertion_sort(need_sort)
    print("Results:")
    for i in need_sort:
        print(i)

elif sortAlgo == 4:
    bubble_sort(need_sort)
    print("Results:")
    for i in need_sort:
        print(i)

elif (sortAlgo > 4):
    print("coming soon!")
    sortAlgo = int(input("Choose sorting algorithm (1-#): \n 1. Selection Sort \n 2. Merge Sort \n "
                     "3. Insertion Sort \n 4. Bubble Sort \n-> "))

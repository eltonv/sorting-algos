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


# main
number_elem = int(input("Enter the amount of numbers to sort -> "))
if number_elem == 0:
    print("Enter valid amount")
    n = int(input("Enter the amount of numbers to sort -> "))

need_sort = []

for i in range(0, number_elem):
    element = int(input())
    need_sort.append(element)

sortAlgo = int(input("Choose sorting algorithm (1-#): \n 1. Selection Sort \n -> "))

if (sortAlgo == 1):
    selection_sort(need_sort, 0, 0)
    print("Results:")
    for i in need_sort:
        print(i)

# also print how fast it worked

elif (sortAlgo > 1):
    print("coming soon!")
    sortAlgo = int(input("Choose sorting algorithm (1-#): \n 1. Selection Sort \n -> "))

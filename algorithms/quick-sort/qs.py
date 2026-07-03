# This is a standard implementation of Nic Lomuto's quick-sort

# finding final index:
# if a[j] <= p
#     increment i
#     swap a[i] and a[j]

def quicksort(array:list):
    if len(array) <= 1:
        return array

    pivot = array[-1]
    i = -1
    
    # bring pivot to final resting position:
    for j in range(len(array)-1):
        if array[j] <= pivot:
            i += 1 #increment
            array[i], array[j] = array[j], array[i]

    i += 1 # move pivot to final place
    array[i], array[-1] = array[-1], array[i]

    left:list = quicksort(array[:i])
    right:list = quicksort(array[i+1:])

    return left + [array[i]] + right



def main() -> None:
    array: list = [3,2,1]
    print(quicksort(array))

if __name__ == "__main__":
    main()


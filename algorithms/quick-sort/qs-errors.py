# This is a standard implementation of Nic Lomuto's quick-sort

# finding final index:
# if a[j] <= p
#     increment i
#     swap a[i] and a[j]

def quicksort(array:list):
    if len(array) <= 1:
        return array

    low:int = -1
    high:int = 0
    pivot = array[len(array)-1]
    
    # bring pivot to final resting position:
    while high < len(array):
        if array[high] <= pivot:
            low += 1 #increment
            tmp = array[low] #swap low and high
            array[low] = array[high]
            array[high] = tmp
        high+=1

    left:list = quicksort(array[:low])
    right:list = quicksort(array[low+1:])

    return left + [array[low]] + right



def main() -> None:
    array: list = [3,2,1]
    print(quicksort(array))

if __name__ == "__main__":
    main()

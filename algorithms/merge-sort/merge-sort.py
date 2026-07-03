from timeit import default_timer as timer

def mergesort(array: list) -> list:
    if (array == [] or array == None):
        return []
    # already sorted
    if (len(array) <= 1):
        return array

    pivot: int = len(array) // 2
    left: list = mergesort(array[:pivot])
    right: list = mergesort(array[pivot:])

    def merge(left: list, right: list):
        merged: list = []

        idx_left: int = 0
        idx_right: int = 0

        # idx_left tracks the left most index
        while (idx_left < len(left) and idx_right < len(right)):
            value_left: int = left[idx_left]
            value_right: int = right[idx_right]

            if value_left == value_right:
                merged.append(value_left)
                merged.append(value_right)
                idx_let += 1
                idx_right += 1
            elif value_left < value_right:
                merged.append(value_left)
                idx_left += 1
            else:
                merged.append(value_right)
                idx_right += 1

        if idx_left == len(left):
            for i in right[idx_right:]:
                merged.append(i)
        elif idx_right == len(right):
            for i in left[idx_left:]:
                merged.append(i)

        return merged
    return merge(left, right)


def main():
    # array: list = [1,6,2,5,3,9,7,0,8,4]
    array: list = [1, 2, 3, 5, 8, 3, 6, 2, 436, 7, 4, 2, 3, 7, 8, 6, 4, 2, 1, 7, 8,
                   9, 7, 56, 43, 3, 7, 7, 4, 5, 6, 2, 67, 9, 7, 5, 56, 2, 34, 5, 6, 8, 5] * 1000000
    print(f"before: {array}")
    start: float = timer()
    print(f"after: {mergesort(array)}")
    print(f"time elapsed: {(timer() - start)}")
if __name__ == "__main__":
    main()

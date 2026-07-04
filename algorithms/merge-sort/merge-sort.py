from timeit import default_timer as timer

def mergesort(array: list) -> list:
    # watch out for empty input:
    if (array == [] or array == None):
        return []

    # already sorted
    if (len(array) <= 1):
        return array

    middle: int = len(array) // 2
    left: list = mergesort(array[:middle])
    right: list = mergesort(array[middle:])

    return merge(left, right)

def merge(left: list, right: list):
    merged: list = []

    idx_left: int = 0
    idx_right: int = 0

    while (idx_left < len(left) and idx_right < len(right)):
        if left[idx_left] < right[idx_right]:
            merged.append(left[idx_left])
            idx_left += 1
        else:
            merged.append(right[idx_right])
            idx_right += 1

    merged.extend(left[idx_left:])
    merged.extend(right[idx_right:])

    return merged


def main():
    array: list = [1,6,2,5,3,9,7,0,8,4]
    print(f"before: {array}")
    start: float = timer()
    print(f"after: {mergesort(array)}")
    print(f"time elapsed: {(timer() - start)}")
if __name__ == "__main__":
    main()

from typing import List


def append_elements(arr1: List[int], arr2: List[int]) -> List[int]:
    for i, n in enumerate(arr2):
        arr1.append(arr2[i])

    return arr1
  

def remove_elements(arr1: List[int], arr2: List[int]) -> List[int]:
    for i, n in enumerate(arr2):
        if arr2[i] in arr1:
                 arr1.remove(arr2[i])

    return arr1


# do not modify below this line
print(append_elements([1, 2, 3], [4, 5, 6]))
print(append_elements([4, 3], [4, 5, 3]))

print(remove_elements([1, 2, 3, 4, 5], [2, 4, 6]))
print(remove_elements([1, 2, 3, 4, 5], [2, 3, 4, 5, 5]))
print(remove_elements([1, 7, 2, 3, 4, 5], [6, 7, 8, 2]))

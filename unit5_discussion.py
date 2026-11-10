"""
=====================================================
UNIT 5 DISCUSSION: SEARCH ALGORITHMS (LINEAR vs BINARY)
=====================================================

INSTRUCTIONS:
In this assignment, you will implement and analyze two
fundamental search algorithms: linear search and binary search.

You will demonstrate your understanding by modifying the
provided code, running experiments on different dataset sizes,
and clearly explaining your results through code comments
and program output.
"""
import time


def linear_search(lst, target):
    """
    TODO (Student):
    Implement a linear search algorithm.

    Requirements:
    - Search the list from beginning to end.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining why linear search
      has O(n) time complexity.
    """
    # Linear search checks each element one by one from index 0 to n-1.
    # Time Complexity is O(n) because in the worst-case scenario (target is at the
    # end or completely missing), the algorithm must perform n comparisons,
    # making execution time grow linearly with dataset size.
    for index in range(len(lst)):
        if lst[index] == target:
            return index
    return -1


def binary_search(lst, target):
    """
    TODO (Student):
    Implement a binary search algorithm.

    Requirements:
    - Assume the list is already sorted.
    - Repeatedly reduce the search space by half.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining how each iteration
      reduces the search space.
    """
    low = 0
    high = len(lst) - 1

    while low <= high:
        mid = (low + high) // 2

        # Each iteration calculates a new midpoint and compares it to the target.
        # By ruling out half of the remaining elements based on the sorted order,
        # the search space is cut in half every time, giving it O(log n) efficiency.
        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            low = mid + 1  # Target is in the upper half; eliminate the lower half.
        else:
            high = mid - 1  # Target is in the lower half; eliminate the upper half.

    return -1


def main():
    print("=== UNIT 5: SEARCH ALGORITHMS ===")

    # ===============================
    # TODO (Student): SMALL DATASET
    # ===============================
    #
    # Requirements:
    # 1. Create a small sorted dataset.
    # 2. Test both linear search and binary search.
    # 3. Search for:
    #    - a value that exists
    #    - a value that does not exist
    # 4. Use comments to clearly explain the results.

    print("\n=== SMALL DATASET TEST ===")
    small_list = [5, 12, 23, 34, 45, 56, 67, 78, 89, 90]
    print(f"Dataset: {small_list}")

    # Case A: Value exists (34)
    print("\nTesting Existing Value (34):")
    print(f"Linear Search Index: {linear_search(small_list, 34)}")
    print(f"Binary Search Index: {binary_search(small_list, 34)}")

    # Case B: Value does not exist (50)
    print("\nTesting Non-Existing Value (50):")
    print(f"Linear Search Index: {linear_search(small_list, 50)}")
    print(f"Binary Search Index: {binary_search(small_list, 50)}")

    # Analysis Comment:
    # For small datasets, both algorithms execute near-instantaneously. The
    # overhead of setting up binary search pointers yields no noticeable
    # speed advantage over linear iteration when elements are sparse.

    # ===============================
    # TODO (Student): LARGE DATASET
    # ===============================
    #
    # Requirements:
    # 1. Create a much larger sorted dataset.
    # 2. Test both search algorithms.
    # 3. Compare the results.
    # 4. Use comments to explain why binary search becomes more
    #    efficient as datasets grow larger.

    print("\n=== LARGE DATASET TEST ===")
    large_list = list(range(1, 10000001))  # 10 million elements
    target_value = 9999999  # Worst-case scenario near the very end

    print(f"Dataset Size: {len(large_list):,} elements")
    print(f"Searching for target: {target_value:,}")

    # Time Linear Search
    start_time = time.perf_counter()
    lin_res = linear_search(large_list, target_value)
    lin_time = time.perf_counter() - start_time
    print(f"Linear Search Index: {lin_res} | Time taken: {lin_time:.6f} seconds")

    # Time Binary Search
    start_time = time.perf_counter()
    bin_res = binary_search(large_list, target_value)
    bin_time = time.perf_counter() - start_time
    print(f"Binary Search Index: {bin_res} | Time taken: {bin_time:.6f} seconds")

    # Analysis Comment:
    # Binary search scales logarithmically, O(log n). For 10 million elements,
    # it needs a maximum of ~24 comparisons. Linear search scales at O(n) and
    # must check nearly all 10 million elements, taking significantly longer.

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    # Explain what happens in each case.

    print("\n=== EDGE CASE TESTS ===")

    # Edge Case 1: Empty List
    empty_list = []
    print("Edge Case 1: Empty List")
    print(f"Linear Search: {linear_search(empty_list, 10)}")
    print(f"Binary Search: {binary_search(empty_list, 10)}")
    # Explanation: Both safely loop 0 times and return -1 without throwing errors.

    # Edge Case 2: Target at the exact first position
    single_element_list = [42]
    print("\nEdge Case 2: Target at First Position of Single-Element List")
    print(f"Linear Search: {linear_search(single_element_list, 42)}")
    print(f"Binary Search: {binary_search(single_element_list, 42)}")
    # Explanation: Linear search succeeds on its first loop iteration. Binary search
    # evaluates mid=0 on the first pass, matches the target, and breaks instantly.


if __name__ == "__main__":
    main()
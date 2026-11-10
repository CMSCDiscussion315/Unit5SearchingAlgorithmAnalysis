# Unit 5 Discussion: Search Algorithms

## Overview

This assignment compares linear search and binary search.

## Learning Objectives

- Implement linear search
- Implement binary search
- Compare performance
- Analyze algorithm efficiency

## Requirements

1. Test both algorithms on a small dataset.
2. Test both algorithms on a large dataset.
3. Demonstrate edge cases.
4. Analyze performance.
5. Create a real-world search scenario.


## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Explain when to use linear versus binary search, including tradeoffs in real-world scenarios.

     Markdown
# Unit 5 Discussion: Search Algorithms

## Overview
This assignment compared linear search and binary search.

## Learning Objectives
- Implemented linear search
- Implemented binary search
- Compared performance
- Analyzed algorithm efficiency

## Requirements
1. Tested both algorithms on a small dataset.
2. Tested both algorithms on a large dataset.
3. Demonstrated edge cases.
4. Analyzed performance.
5. Created a real-world search scenario.

## Code Implementation Summary
- **Linear Search:** I implemented a simple loop that iterated through the items sequentially. I documented within the comments why its worst-case complexity results in an $O(n)$ footprint due to scanning every index.
- **Binary Search:** I developed a divide-and-conquer strategy using `low`, `high`, and `mid` boundary markers. I added commentary detailing how the search field dropped by exactly half at every step, yielding $O(\log n)$ performance.
- **Evaluation Framework:** I executed scripts comparing both approaches against a small array, an array of 10 million sorted items, empty arrays, and single-item inputs. The experimental runtime benchmarks proved the overwhelming speed advantage of binary search at high scale.


   Discussion Reflection

1. Concepts and Skills Learned
   While completing this assignment, I reinforced my practical understanding of algorithmic time complexities by moving from abstract big-O theories to tangible execution benchmarks. Implementing linear search highlighted the architectural simplicity of sequential data scanning, while coding the index logic for binary search strengthened my grasp of divide-and-conquer patterns. Additionally, I learned how to utilize Python's time.perf_counter() to collect accurate performance data for algorithm comparison.
2. Challenges Encountered and Overcome
   My primary challenge involved preventing off-by-one errors while updating the pointer boundaries (low = mid + 1 and high = mid - 1) in the binary search implementation. If handled incorrectly, these pointers can prompt infinite loops or skip values. I overcame this by dry-running the loop states on paper using a 3-element list array until the terminating logic conditions became clear.
3. Application and Real-World Tradeoffs
   Linear search should be used when data collections are completely unsorted or dynamically changing, or when the dataset is small enough that organization overhead is unjustified. Binary search is best reserved for massive, relatively static datasets where the data is sorted.
   In a real-world application like a smartphone music player app, storing tracks in an unorganized playlist forces a linear scan (O(n)) to find a track. However, indexing the entire master library alphabetically enables instant search speeds (O(log n)). The trade-off is clear: binary search requires an upfront time investment to organize data, but it delivers massive runtime dividends if that data is searched frequently.
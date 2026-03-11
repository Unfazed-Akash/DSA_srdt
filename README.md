# DSA Questions - Python Solutions

A complete collection of **42 Data Structures & Algorithms** problems solved in Python, organized into 4 categories. Each question has its own `.py` file with clean, readable code and interactive input.

> The original question sheet is included as [`DSA Questions.pdf`](./DSA%20Questions.pdf) for reference.

---

## Folder Structure

```
DSA_srdt/
├── Number_System/        # Q1  – Q7
├── Array_Based/          # Q8  – Q25
├── String_Based/         # Q26 – Q38
├── Linked_List/          # Q39 – Q42
└── DSA Questions.pdf     # Original question sheet
```

---

## How to Run Any Solution

```bash
python Number_System/1.py
python Array_Based/8.py
# ... and so on
```

> Requires **Python 3.x**. Each file reads input interactively from the terminal.

---

## Category 1 — Number System (`Number_System/`)

| File | Question | Description |
|------|----------|-------------|
| `1.py` | Check if a Number is Prime | Reads a number and prints whether it is prime or not |
| `2.py` | Pythagorean Triplets | Accepts a perimeter value and finds all triplets (a, b, c) where a²+b²=c² |
| `3.py` | Maximum Marks per Semester | Accepts total marks for each student and calculates marks per semester (6 semesters) |
| `4.py` | Equation Solver | Evaluates a³ + a²b + 2a²b + 2ab² + ab² + b³ (simplifies to (a+b)³) |
| `5.py` | Tyres in Dealerships | Calculates total and mean tyres for motorbikes (2), cars (4), and trucks (10) |
| `6.py` | Minimum Discount Item | Finds the item with the minimum absolute discount (Clothing 20%, Shoe 10%, Laptop 5%) |
| `7.py` | Find Factors of a Number | Prints all factors of a given number |

---

## Category 2 — Array Based (`Array_Based/`)

| File | Question | Description |
|------|----------|-------------|
| `8.py` | Matrix Rotation by 90° | Rotates an N×N matrix 90 degrees clockwise in-place (transpose + reverse rows) |
| `9.py` | Binary Search | Searches for a target in a sorted array using binary search |
| `10.py` | Count Occurrences | Counts how many times a given integer appears in a list |
| `11.py` | Spiral Matrix Traversal | Traverses and prints all elements of a matrix in spiral order |
| `12.py` | Second Smallest & Largest | Finds the second smallest and second largest elements in an array |
| `13.py` | Merge Intervals | Merges all overlapping intervals from a given list |
| `14.py` | Matrix Identity Check | Checks if a given square matrix is an identity matrix |
| `15.py` | Reverse an Array | Reverses an array in-place using two pointers |
| `16.py` | Kth Largest Element | Finds the Kth largest element in an array |
| `17.py` | Missing Number | Finds the missing number in an array containing values from 0 to n |
| `18.py` | Find Duplicate Number | Detects the duplicate number using Floyd's Cycle Detection |
| `19.py` | Merge Two Sorted Arrays | Merges two sorted arrays into a single sorted array |
| `20.py` | Rotate Array | Rotates an array to the right by K positions |
| `21.py` | Maximum Product Subarray | Finds the subarray with the maximum product (Kadane's variant) |
| `22.py` | Count Pairs with Given Sum | Counts all pairs in an array that add up to a target sum |
| `23.py` | Move Zeros to End | Moves all zeros to the end while maintaining order of non-zero elements |
| `24.py` | Majority Element | Finds the element that appears more than n/2 times (Boyer-Moore Voting) |
| `25.py` | Intersection of Two Arrays | Returns the sorted list of unique common elements between two arrays |

---

## Category 3 — String Based (`String_Based/`)

| File | Question | Description |
|------|----------|-------------|
| `26.py` | Move '#' to Front | Moves all `#` characters to the beginning of the string |
| `27.py` | Season from Month | Returns the season (Spring/Summer/Autumn/Winter) for a given month name |
| `28.py` | Counting Valleys | Counts valleys in a hiking path described by U (up) and D (down) steps |
| `29.py` | String Compression | Run-length encodes a string (e.g., `"aaabbb"` → `"a3b3"`) |
| `30.py` | Reverse a String | Reverses a string using Python slicing |
| `31.py` | Valid Anagram Check | Checks if two strings are anagrams of each other |
| `32.py` | First Unique Character | Returns the index of the first non-repeating character in a string |
| `33.py` | First Non-Repeated Character | Returns the first character that does not repeat in the string |
| `34.py` | Palindrome Check | Checks whether a given string is a palindrome |
| `35.py` | Longest Palindromic Substring | Finds the longest palindromic substring using expand-around-center |
| `36.py` | Longest Common Prefix | Finds the longest common prefix among a list of strings |
| `37.py` | String Rotation Check | Checks if one string is a rotation of another |
| `38.py` | Longest Substring Without Repeating Characters | Finds the length of the longest substring with all unique characters (sliding window) |

---

## Category 4 — Linked List (`Linked_List/`)

| File | Question | Description |
|------|----------|-------------|
| `39.py` | Reverse a Linked List | Reverses a singly linked list iteratively using three pointers |
| `40.py` | Detect Loop | Detects a cycle in a linked list using Floyd's Cycle Detection Algorithm |
| `41.py` | Find Middle Node | Finds the middle node using the slow/fast pointer (tortoise and hare) technique |
| `42.py` | Merge Two Sorted Linked Lists | Merges two sorted linked lists into one sorted linked list |

---

## Algorithms & Techniques Used

| Technique | Used In |
|-----------|---------|
| Two Pointers | `15.py`, `39.py`, `41.py` |
| Binary Search | `9.py` |
| Sliding Window | `38.py` |
| Floyd's Cycle Detection | `18.py`, `40.py` |
| Boyer-Moore Voting | `24.py` |
| Expand Around Center | `35.py` |
| Kadane's Algorithm (variant) | `21.py` |
| Sorting + Greedy | `13.py`, `12.py` |
| Hash Map / Frequency Count | `22.py`, `32.py`, `33.py` |
| Matrix In-place Manipulation | `8.py`, `14.py` |

---

## Requirements

- Python 3.6 or higher
- No external libraries required (only Python standard library)

---

## Verification & Testing

All 42 solution files were executed with representative sample inputs to verify correctness. The table below summarizes the results.

| Category | Files | Tested | Passed | Failed |
|---|---|---|---|---|
| Number System | `1.py` – `7.py` | 7 | 7 | 0 |
| Array Based | `8.py` – `25.py` | 18 | 18 | 0 |
| String Based | `26.py` – `38.py` | 13 | 13 | 0 |
| Linked List | `39.py` – `42.py` | 4 | 4 | 0 |
| **Total** | | **42** | **42** | **0** |

**Result: 42 / 42 files execute without errors and produce the expected output.**

### Input Format Notes

Some files accept a **size/count on the first line** followed by the elements; others read all elements as a **single space-separated line**. The table below clarifies which files use which format.

| Input Format | Files |
|---|---|
| Size first, then elements per line | `8.py`, `9.py`, `11.py`, `13.py`, `36.py` |
| Space-separated elements on one line (no size) | `10.py`, `12.py`, `15.py`, `16.py`, `18.py` – `25.py`, `39.py` – `42.py` |
| One value per line (multiple prompts) | `3.py`, `4.py`, `5.py`, `6.py` |

---

## Academic Context

These solutions are submitted as part of a **DSA homework assignment** given by a training company associated with my college. This repository is uploaded for academic review and learning reference only.

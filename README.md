# Lab: Linked Lists and Recursion  
**Lab GitHub Repo**: [Linked Lists and Recursion](https://github.com/learn-co-curriculum/Linked-Lists-and-Recursion)

---

## Overview
In this lab, we’ll apply **linked lists** and **recursion** to build a small prototype for managing a list of data. Imagine a junior developer assigned to maintain a simple employee roster, where IDs are stored in a linked list. You’ve been asked to implement **recursive** functionalities such as summing IDs, reversing the list in-place, and searching for a particular ID.

By focusing on **linked lists** (for dynamic insertion/deletion) and **recursion** (for elegant traversal), you’ll gain hands-on experience with node-based data structures—common in many low-level or performance-sensitive applications.

---

## Task 1: Define the Problem

1. **Load or create** an initial linked list of integer IDs.  
2. **Enable recursive functionality** to:
   - **Sum** all node data in the list.  
   - **Reverse** the list in-place.  
   - **Search** for a given ID.  
3. **Present** or print the result for each operation in a user-friendly format.

**The Challenge**: Demonstrate your understanding of linked lists while using recursion to solve day-to-day tasks such as searching and reversing data.

---

## Task 2: Determine the Design

### Linked List Structure

- **App / Main**  
  Drive the creation and manipulation of the linked list.  

- **Node Class**  
  Each node stores an **integer data** and a pointer/reference to `next`.  

- **LinkedList Class**  
  - `head` references the first node.  
  - Methods to **insert**, **sum**, **reverse**, and **search**.  

---

## Task 3: Develop, Test, and Refine the Code

### Set Up

#### Fork and Clone
1. Go to the provided **GitHub repository link**.  
2. Fork the repository to your GitHub account.  
3. Clone the forked repository to your local machine.  

#### Open and Run
1. Open the project in your preferred Python-friendly environment (VSCode, PyCharm, etc.).  

### Implementation Details

1. **Create a feature branch** (e.g., `feature/linked-list-lab`).  
2. **Create the `Node` and `LinkedList` classes**:
   - **Node** class with `data` and `next`.  
   - **LinkedList** class to house `head` and methods.
3. **Manage Linked List Insertion**:
   - `insert_at_front(data)` → O(1).  
   - *(Optional)* `insert_at_end(data)` → O(n) to traverse to the end.
4. **Use Recursion**:
   - **Sum**: Returns `0` if node is `None`, otherwise `node.data + recurse(node.next)`.  
   - **Reverse**: Re-point each node’s `next` to the **previous** node until the list is reversed.  
   - **Search**: Returns `True` if a node’s `data` matches the target; stops if it hits `None`.
5. **Run Tests** (if provided) or manually test:
   - Insert some sample data, then call each recursive method.  
   - Print the list or results to confirm correctness.
6. **Push feature branch** and open a PR on GitHub.
7. **Merge** to `main` once reviewed.

---

## Task 4: Document and Maintain

### Best Practice Documentation Steps

- **Add Comments**: Clarify logic for recursion, highlight base vs. recursive cases.  
- **Explain Intent**: Make it clear why you’re using recursion in a particular method (e.g., elegance, clarity, demonstration).  
- **README**: Update with instructions on how to run the code, test, and interpret results.  
- **Clean Up**:
  - Remove any debugging prints or stale branches.  
  - Ensure your `.gitignore` is updated to exclude unnecessary files.

## Submission
Once the lab is complete, all tests are passing, and you've pushed the completed code to 
your forked repo on GitHub, submit your GitHub repo through Canvas using CodeGrade.

---

## How to Run

Requires Python 3.8+.

```bash
python3 main.py              # demo: build a roster, sum, search, reverse
python3 -m pytest            # run the test suite (or: python3 -m unittest -v)
```

### Sample output

```
Employee ID roster:
100 -> 101 -> 102 -> 103 -> None

Sum of all IDs: 406
Is ID 102 on the roster? Yes
Is ID 999 on the roster? No

Roster after reversing:
103 -> 102 -> 101 -> 100 -> None
```

### Interpreting results

- `display()` prints nodes from `head` to the end, with `None` marking the tail.
- `recursive_sum()` adds each node's value to the sum of the rest of the list (base case: `None` → `0`).
- `recursive_search(target)` returns `True` on the first match, `False` once it reaches `None`.
- `recursive_reverse()` flips each node's `next` pointer to the previous node, then sets `head` to the old tail.

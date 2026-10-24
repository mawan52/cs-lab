# cs-lab
The main goal behind this repository and book, if you can call it that, is to
help me gain deeper knowledge of computer science outside of school.

## Roadmap

### Foundations

- [ ] Logic (AND, OR, NOT, Implication, Truth Tables)
- [ ] Sets & Relations
- [ ] Functions (Injective, Surjective, Bijective)
- [ ] Proof Techniques
  - [ ] Induction
  - [ ] Contradiction
- [ ] Combinatorics (Permutations & Combinations)
- [ ] Number Theory (Modular Arithmetic, Primes)
- [ ] Asymptotic Analysis (Big O, Big Omega, Big Theta)

- [ ] The C Programming Language
  - [ ] Fundamentals
    - [ ] Variables and primitive types
    - [ ] Expressions and operators
    - [ ] Conditional Statements
    - [ ] Loops
    - [ ] Functions
    - [ ] Scope and storage duration
    - [ ] Type conversions
  - [ ] Memory and Data
    - [ ] Character arrays and strings
    - [ ] Pointers
    - [ ] Pointer arithmetic
    - [ ] Pointers and arrays
    - [ ] Pointers to pointers
    - [ ] Structs
    - [ ] Unions
    - [ ] Enums
    - [ ] Function pointers
  - [ ] Dynamic Memory
    - [ ] 'malloc'
    - [ ] 'calloc'
    - [ ] 'realloc'
    - [ ] 'free'
    - [ ] Memory ownership
    - [ ] Memory leaks
    - [ ] Dangling pointers
    - [ ] Double-free errors
  - [ ] Low-Level C
    - [ ] Bitwise operations
    - [ ] Memory alignment
    - [ ] Structure padding
    - [ ] Endianness
    - [ ] Undefined behaviour
    - [ ] Implementation-defined behaviour
    - [ ] Volatile objects
    - [ ] Basic file input and output
    - [ ] Error handling
---

### Data Structures

- [ ] Linear
  - [ ] Array
  - [ ] Linked List (Singly, Doubly)
  - [ ] Stack
  - [ ] Queue
  - [ ] Circular Queue
  - [ ] Circular Buffer
- [ ] Non-Linear
  - [ ] Hashmap (Collision handling)
  - [ ] Binary Tree
  - [x] Binary Search Tree (BST) ![bst.c](./datastructures/binary-search-tree/c/bst.c)
  - [ ] AVL Tree (Self-balancing)
  - [ ] Heap (Min/Max)
- [ ] Graph Representations
  - [ ] Adjacency Matrix
  - [ ] Adjacency List

---

### Algorithms
Important: Traversal vs. Pathfinding

- [ ] Techniques
  - [ ] Iteration
  - [ ] Recursion
  - [ ] Divide and conquer
  - [ ] Greedy algorithms
  - [ ] Backtracking
  - [ ] Heuristic

- [x] Tree Traversal
  - [x] BFS (Breadth First Search) ![bfs.py](./algorithms/bfs/bfs.py)
  - [x] DFS (Depth First Search) ![dfs.py](./algorithms/dfs/dfs.py)

- [x] Pathfinding
  - [x] Dijkstra ![dijkstra.py](./algorithms/dijkstra/dijkstra_pq.py)
  - [x] A\* ![a_star.py](./algorithms/a_star/a_star.py)

- [x] Sorting
  - [x] Merge Sort ![merge-sort.py](./algorithms/merge-sort/merge-sort.py)
  - [x] Quick Sort ![quick-sort.py](./algorithms/quick-sort/qs.py)

- [ ] Graph Theory Basics
  - [ ] Directed & Undirected Graphs
  - [ ] Weighted & Unweighted Graphs
  - [ ] Trees
  - [ ] Cycles
  - [ ] Connectivity

---

### Systems

- [ ] Data Representation
  - [ ] Bits and bytes
  - [ ] Machine words
  - [ ] Binary numbers
  - [ ] Hexadecimal numbers

- [ ] Memory Management
  - [ ] The Stack vs. The Heap
  - [ ] Virtual Memory & Paging
  - [ ] L1/L2/L3 Cache Locality

- [ ] Architecture
  - [ ] CPU Architecture (Registers, ALU, Control Unit)
  - [ ] Instruction Set Architecture (ISA)
  - [ ] x86 Assembly Basics
  - [ ] RISC-V Assembly basics
  - [ ] x86 vs RISC-V

- [ ] Operating Systems & Concurrency
  - [ ] Processes vs. Threads
  - [ ] Context Switching
  - [ ] Mutexes & Semaphores (Concurrency control)
  - [ ] System Calls

- [ ] Toolchain
  - [ ] Compilation Process (Source -> Binary)
  - [ ] Static vs. Dynamic Linking

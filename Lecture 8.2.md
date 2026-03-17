![Image](Lecture 8.2_artifacts/image_000000_bbaa640f2b7c7b6f18cdf441c797dcf1ce99e755b6ef0a9bbf7b581538bddcab.png)

## Module 37

Partha Pratim Das

Objectives &amp; Outline

Data Structure

Linear Data

Structures

Array

Linked List

Search

Linear Search

Binary Search

Module Summary

## Database Management Systems

Module 37: Algorithms and Data Structures/2: Data Structures

## Partha Pratim Das

Department of Computer Science and Engineering Indian Institute of Technology, Kharagpur ppd@cse.iitkgp.ac.in

Partha Pratim Das

![Image](Lecture 8.2_artifacts/image_000001_b551d1d039a350a56349b412170007d20638ad0732feb40b06cdb100cf6ab680.png)

## Module 37

Partha Pratim Das

## Objectives &amp; Outline

Data Structure

Linear Data

Structures

Array

Linked List

Search

Linear Search

Binary Search

Module Summary

## Module Recap

- Need for analyzing the running-time and space requirements of a program
- Asymptotic growth rate or order of the complexity of different algorithms
- Worst-case, average-case and best-case analysis

![Image](Lecture 8.2_artifacts/image_000002_0d9dfbde1de846c018eea32fe6aba21e8a9c7f3c69ef770101468a6cfb66a6e5.png)

## Module 37

Partha Pratim Das

## Objectives &amp; Outline

Data Structure

Linear Data Structures

Array

Linked List

Search

Linear Search

Binary Search

Module Summary

## Module Objectives

- Introduction to Data Structures
- Review of linear data structures - array, list, stack, queue
- Review of search - linear and binary

![Image](Lecture 8.2_artifacts/image_000003_0d9dfbde1de846c018eea32fe6aba21e8a9c7f3c69ef770101468a6cfb66a6e5.png)

## Module 37

Partha Pratim Das

## Objectives &amp; Outline

Data Structure

Linear Data Structures

Array

Linked List

Search

Linear Search

Binary Search

Module Summary

## Module Outline

- Linear data structures - array, list, stack, queue
- Search - linear and binary

![Image](Lecture 8.2_artifacts/image_000004_821f32da21a8bb9af0bddb9e2ff2419e915ba7e461f5dc4f05b60eaa6ed0b478.png)

## Module 37

Partha Pratim Das

Objectives &amp; Outline

## Data Structure

Linear Data

Structures

Array

Linked List

Search

Linear Search

Binary Search

Module Summary

## Data Structure

- Data structure : A data structure specifies the way of organizing and storing in-memory data that enables efficient access and modification of the data.
- Linear Data Structures
- Non-linear Data Structures
- Most data structure has a container for the data and typical operations that its needs to perform
- For applications relating to data management, the key operations are:
- Create
- Insert
- Delete
- Find / Search
- Close
- Efficiency is measured in terms of time and space taken for these operations

## Partha Pratim Das

![Image](Lecture 8.2_artifacts/image_000005_bbaa640f2b7c7b6f18cdf441c797dcf1ce99e755b6ef0a9bbf7b581538bddcab.png)

Module 37

Partha Pratim Das

Objectives &amp; Outline

Data Structure

Linear Data Structures

Array

Linked List

Search

Linear Search

Binary Search

Module Summary

## Linear Data Structures

## Linear Data Structures

![Image](Lecture 8.2_artifacts/image_000006_b551d1d039a350a56349b412170007d20638ad0732feb40b06cdb100cf6ab680.png)

Module 37

Partha Pratim Das

Objectives &amp; Outline

Data Structure

Linear Data Structures

Array

Linked List

Search

Linear Search

Binary Search

Module Summary

## Linear Data Structures

- A Linear data structure has data elements arranged in linear or sequential manner such that each member element is connected to its previous and next element.
- Since data elements are sequentially connected, each element is traversable through a single run.
- Examples of linear data structures are Array, Linked List, Queue, Stack, etc.

![Image](Lecture 8.2_artifacts/image_000007_b551d1d039a350a56349b412170007d20638ad0732feb40b06cdb100cf6ab680.png)

## Module 37

Partha Pratim Das

Objectives &amp; Outline

Data Structure

Linear Data Structures

Array

Linked List

Search

Linear Search

Binary Search

Module Summary

![Image](Lecture 8.2_artifacts/image_000008_4e9831be635a5b2027f4394a2cdec209eb3551c7604b4b2f8454fbf53232d662.png)

## Different examples of linear data structure:

- Array : The data elements are stored at contiguous locations in memory.
- Linked List : The data elements are not required to be stored at contiguous locations in memory. Rather each element stores a link (a pointer to a reference) to the location of the next element.
- Queue : It is a FIFO (First In First Out) data structure. The element that has been inserted first in the queue would be removed first. Thus, insert and removal of the elements in this take place in the same order.
- Stack : It is a LIFO (Last In First Out) data structure. The element that has been inserted last in the stack would be removed first. Thus, insert and removal of the elements in this take place in the reverse order.

![Image](Lecture 8.2_artifacts/image_000009_32155ccc63eaf8ac3b5d36be7560257f854d0b99536286a17a16546fbab339af.png)

## Module 37

Partha Pratim

Das

Objectives &amp;

Outline

Data Structure

Linear Data

Structures

Array

Linked List

Search

Linear Search

Binary Search

Module Summary

## Linear Data Structures (3): Array

- The elements are stored in contiguous memory locations.
- Simple access using indices. For example, let the array name be arr, we can access the element at position 5 as arr[5] .
- Array allows random access using its index which is fast (cost of O (1)). Useful for operations like sorting, searching.

![Image](Lecture 8.2_artifacts/image_000010_1b19d63029a573984c1507ae4af8c841be3caed1226da6a81303e0332da8a098.png)

![Image](Lecture 8.2_artifacts/image_000011_821f32da21a8bb9af0bddb9e2ff2419e915ba7e461f5dc4f05b60eaa6ed0b478.png)

## Module 37

Partha Pratim Das

Objectives &amp; Outline

Data Structure

Linear Data

Structures

Array

Linked List

Search

Linear Search

Binary Search

Module Summary

## Linear Data Structures (4): Array

- Have fixed sizes, not flexible . Since we do not know the number of elements to be stored in runtime, If we create it too large then it can be a waste of memory, if we create it too small then some elements may not be accommodated in the array.
- For example, suppose we create an array to store 8 elements. However, during execution of the program only 5 elements are available, which results in wastage of memory space.

![Image](Lecture 8.2_artifacts/image_000012_aaca1a1c0c88db6b56a99e4a6e8bdc796ffd232ab1f148a4c5aa77c3f4deb2d3.png)

![Image](Lecture 8.2_artifacts/image_000013_fde1132bf222cc20a3e76fd9bad23db921b22024804914407d2f2bc1b513e47e.png)

## Module 37

Partha Pratim Das

Objectives &amp; Outline

Data Structure

Linear Data

Structures

Array

Linked List

Search

Linear Search

Binary Search

Module Summary

## Linear Data Structures (5): Array

- Insertion and removal of elements from an array are costlier since the memory locations have to be consecutive.
- Insertion or removal of an element from the end of an array is easy.
- ▷ Insert at end:
- ▷ Remove from end:

![Image](Lecture 8.2_artifacts/image_000014_05513e8724ee6bda60003c4d3d375420d8db91fc8a9e45c7038ae0d1059509a9.png)

![Image](Lecture 8.2_artifacts/image_000015_bbaa640f2b7c7b6f18cdf441c797dcf1ce99e755b6ef0a9bbf7b581538bddcab.png)

Module 37

Partha Pratim

Das

Objectives &amp; Outline

Data Structure

Linear Data

Structures

Array

Linked List

Search

Linear Search

Binary Search

Module Summary

## Linear Data Structures (6): Array

- Insertion and removal of elements from an array are costlier since the memory locations have to be consecutive.
- Insert and remove elements at any arbitrary position is costly (cost is O ( n ))
- ▷ Insert at any arbitrary position:
- ▷ Remove from any arbitrary position:

![Image](Lecture 8.2_artifacts/image_000016_4967837750b83ffeccc49657f1dfa90e63598bfed9db7d3cf04391eaab374f5f.png)

![Image](Lecture 8.2_artifacts/image_000017_6deabdc54f3cf1bc0b9bf8285e824ff67388bc8e0ce95ef4334f3ef850f2fe3b.png)

## Database Management Systems

Partha Pratim Das

![Image](Lecture 8.2_artifacts/image_000018_bbaa640f2b7c7b6f18cdf441c797dcf1ce99e755b6ef0a9bbf7b581538bddcab.png)

## Module 37

Partha Pratim

Das

Objectives &amp; Outline

Data Structure

Linear Data

Structures

Array

Linked List

Search

Linear Search

Binary Search

Module Summary

## Linear Data Structures (7): Linked List

- Elements are not required to be stored at contiguous memory locations. A new element can be stored anywhere in the memory where free space is available. Thus, it provides better memory usage than arrays.
- For each new element allocated, a link (a pointer or a reference) is created for the new element using which the element can be added to the linked list.

![Image](Lecture 8.2_artifacts/image_000019_50e59e53b0febbd8701782d30f13f531db47e8c878f2d3d22f77795430836157.png)

Each element is stored in a node. A node has two parts:

- Info : stores the element.
- Link : stores the location of the next node.
- Header is a link to the first node of the linked list.

![Image](Lecture 8.2_artifacts/image_000020_0d2e8daa05c74407b310229f101057782122d2bf078613dc8c643ca2fdb280b5.png)

Module 37

Partha Pratim Das

Objectives &amp; Outline

Data Structure

Linear Data Structures

Array

Linked List

Search

Linear Search

Binary Search

Module Summary

## Linear Data Structures (8): Linked List

- Flexible in size . Size of a linked list grows or shrinks as and when new elements are inserted or deleted.
- Random access is not possible in linked lists. The elements will have to be accessed sequentially.
- Insertion or removal of an element at/from any arbitrary position is efficient as none of the elements are not required to be moved to new locations.

![Image](Lecture 8.2_artifacts/image_000021_bbaa640f2b7c7b6f18cdf441c797dcf1ce99e755b6ef0a9bbf7b581538bddcab.png)

## Module 37

Partha Pratim Das

Objectives &amp;

Outline

Data Structure

Linear Data

Structures

Array

Linked List

Search

Linear Search

Binary Search

Module Summary

## Linear Data Structures (9): Linked List

- Insertion or removal of an element at/from any arbitrary position is efficient.
- Insertion at front:
1. NewNode.Link = Header
2. Header = NewNode

![Image](Lecture 8.2_artifacts/image_000022_e4ab8ca46b1f69c1913071ef71d101db0e9eec8daeba46e9e4c2ff37f02ce033.png)

Partha Pratim Das

![Image](Lecture 8.2_artifacts/image_000023_bbaa640f2b7c7b6f18cdf441c797dcf1ce99e755b6ef0a9bbf7b581538bddcab.png)

Module 37

Partha Pratim

Das

Objectives &amp;

Outline

Data Structure

Linear Data

Structures

Array

Linked List

Search

Linear Search

Binary Search

Module Summary

## Linear Data Structures (10): Linked List

- Insertion or removal of an element at/from any arbitrary position is efficient.
- Remove from front:
1. Temp = Header
2. Header = Header.Link
3. Delete(Temp)

![Image](Lecture 8.2_artifacts/image_000024_461b090719ecf27385f27d15ec17af23fd1af8cdfb6c0d109d95bc42bdbe3c92.png)

Partha Pratim Das

Database Management Systems

![Image](Lecture 8.2_artifacts/image_000025_fde1132bf222cc20a3e76fd9bad23db921b22024804914407d2f2bc1b513e47e.png)

## Module 37

Partha Pratim

Das

Objectives &amp;

Outline

Data Structure

Linear Data

Structures

Array

Linked List

Search

Linear Search

Binary Search

Module Summary

## Linear Data Structures (11): Linked List

- Insertion or removal of an element at/from any arbitrary position is efficient.
- Insertion at end:
1. Node.Link = NewNode

![Image](Lecture 8.2_artifacts/image_000026_8ba64c8b59ed86d5fbf1a6a88f0620a4db9d5a5ebd7248b3f3b381bf151978cf.png)

![Image](Lecture 8.2_artifacts/image_000027_fde1132bf222cc20a3e76fd9bad23db921b22024804914407d2f2bc1b513e47e.png)

## Linear Data Structures (12): Linked List

![Image](Lecture 8.2_artifacts/image_000028_1d319ec13b66b4dc42b89e6a4cf59c0e8d4965106b7100e16b19844254a1c229.png)

![Image](Lecture 8.2_artifacts/image_000029_fde1132bf222cc20a3e76fd9bad23db921b22024804914407d2f2bc1b513e47e.png)

Module 37

Partha Pratim

Das

Objectives &amp;

Outline

Data Structure

Linear Data

Structures

Array

Linked List

Search

Linear Search

Binary Search

Module Summary

## Linear Data Structures (13): Linked List

- Insertion or removal of an element at/from any arbitrary position is efficient.
- Insertion at any intermediate position:
1. NewNode.Link = Node.Link
2. Node.Link = NewNode

![Image](Lecture 8.2_artifacts/image_000030_d7e8ab75ad6ed2983715357f2078e5f6843eddf88435a1248fd2ce0aeb6eff3b.png)

Partha Pratim Das

Database Management Systems

![Image](Lecture 8.2_artifacts/image_000031_bbaa640f2b7c7b6f18cdf441c797dcf1ce99e755b6ef0a9bbf7b581538bddcab.png)

Module 37

Partha Pratim

Das

Objectives &amp;

Outline

Data Structure

Linear Data

Structures

Array

Linked List

Search

Linear Search

Binary Search

Module Summary

## Linear Data Structures (14): Linked List

- Insertion or removal of an element at/from any arbitrary position is efficient.
- Remove from any intermediate position:
1. Temp = Node.Link
2. Node.Link = Node.Link.Link
3. Delete(Temp)

![Image](Lecture 8.2_artifacts/image_000032_2851771ecf106b39fe611e829215b5b8cf3a9c5cfa19e1bfb5e70195d2c436bb.png)

Partha Pratim Das

Database Management Systems

![Image](Lecture 8.2_artifacts/image_000033_bbaa640f2b7c7b6f18cdf441c797dcf1ce99e755b6ef0a9bbf7b581538bddcab.png)

## Module 37

Partha Pratim

Das

Objectives &amp;

Outline

Data Structure

Linear Data

Structures

Array

Linked List

Search

Linear Search

Binary Search

Module Summary

## Search

## Search

![Image](Lecture 8.2_artifacts/image_000034_32155ccc63eaf8ac3b5d36be7560257f854d0b99536286a17a16546fbab339af.png)

## Module 37

Partha Pratim Das

Objectives &amp; Outline

Data Structure

Linear Data

Structures

Array

Linked List

Search

Linear Search

Binary Search

Module Summary

## Linear Search

- The algorithm starts with the first element, compares with the given key value and returns yes if they match.
- If it does not match, then it proceeds sequentially comparing each element of the list with the given key until a match is found or the full list is traversed.

Let the given input list be inputArr = ['a','c','a','d','e','m','i','c','s'] and the search key be 'i'.

Figure: Linear Search Example

![Image](Lecture 8.2_artifacts/image_000035_b57f21957ff99e9d0ed235def9484b0634bcd29e87c5a104693cc9eb3f741d75.png)

Partha Pratim Das

## Database Management Systems

![Image](Lecture 8.2_artifacts/image_000036_bbaa640f2b7c7b6f18cdf441c797dcf1ce99e755b6ef0a9bbf7b581538bddcab.png)

Module 37

Partha Pratim Das

Objectives &amp; Outline

Data Structure

Linear Data Structures

Array

Linked List

Search

Linear Search

Binary Search

Module Summary

## Linear Search (2)

Python Code for Linear Search:

------------------------------------------------------ def linSearch(inputArr, k): for i in range(len(inputArr)): if inputArr[i] == k: return i return -1

inputArr = ['a','c','a','d','e','m','i','c','s']

k = 'i'

index = linsearch(inputArr,k)

if index != -1:

print("Element found at "+ index)

![Image](Lecture 8.2_artifacts/image_000037_bbaa640f2b7c7b6f18cdf441c797dcf1ce99e755b6ef0a9bbf7b581538bddcab.png)

## Module 37

Partha Pratim Das

Objectives &amp; Outline

Data Structure

Linear Data

Structures

Array

Linked List

Search

Linear Search

Binary Search

Module Summary

## Binary Search

- The input for the algorithm is a sorted list.
- The algorithm compares the key k with the middle element in the list.
- If the key matches, then it returns the index.
- If the key does not match and is greater than the middle element, then the new list is the list to the right of the middle element.
- If the key does not match and is less than the middle element, then the new list is the list to the left of the middle element.

Let the given input list be inputArr = ['a','a','c','c','d','e','i','m','s'] and the search key be 'i'.

![Image](Lecture 8.2_artifacts/image_000038_403876bb626157879f07d8385768b74437abeb02b7909caa5e75ac0c3116fdae.png)

![Image](Lecture 8.2_artifacts/image_000039_bbaa640f2b7c7b6f18cdf441c797dcf1ce99e755b6ef0a9bbf7b581538bddcab.png)

Module 37

Partha Pratim Das

Objectives &amp; Outline

Data Structure

Linear Data

Structures

Array

Linked List

Search

Linear Search

Binary Search

Module Summary

## Binary Search

Python Code for Binary Search:

------------------------------------------------------ def binSearch(inputArr, k): low = 0 high = len(inputArr) - 1 mid = 0 while low &lt;= high: mid = (high + low) // 2 # Division(floor) if inputArr[mid] &lt; k: # new list is to the right of k low = mid + 1 elif inputArr[mid] &gt; k: # new list is to the left of k high = mid 1 else: # means k is present at mid return mid return -1 # The element is not present

inputArr = ['a','a','c','c','d','e','i','m','s'] k = 'i' index = binSearch(inputArr, k) if index != -1: print("Element found at position "+ str(index+1)) else: print("Not found ")

Database Management Systems

![Image](Lecture 8.2_artifacts/image_000040_bbaa640f2b7c7b6f18cdf441c797dcf1ce99e755b6ef0a9bbf7b581538bddcab.png)

Module 37

Partha Pratim

Das

Objectives &amp;

Outline

Data Structure

Linear Data

Structures

Array

Linked List

Search

Linear Search

Binary Search

Module Summary

## Common Data Structure Operations

![Image](Lecture 8.2_artifacts/image_000041_16c554bf10c2efe1fb27fe1105244d49b860c8e041836bace727911cc09959ed.png)

|                        | Data Structure      | Time Complexity   | Time Complexity   | Time Complexity   | Time Complexity      | Time Complexity   | Time Complexity   | Time Complexity   | Time Complexity      | Space Complexity   |
|------------------------|---------------------|-------------------|-------------------|-------------------|----------------------|-------------------|-------------------|-------------------|----------------------|--------------------|
|                        |                     | Average           | Average           | Average           | Average              | Worst             | Worst             | Worst             | Worst                | Worst              |
|                        |                     | Access            | Search            |                   | Insertion   Deletion | Access            | Search            |                   | Insertion   Deletion |                    |
| Linear Data Structures | Array               | 0(1)              |                   |                   |                      | 0(1)              | O(n)              | O(n)              | O(n)                 | O(n)               |
| Linear Data Structures | Stack               | 0(n)              |                   | 0(1)              | 0(1)                 | O(n)              | O(n)              | 0(1)              | 0(1)                 | O(n)               |
| Linear Data Structures | [Queue              | 0(n)              |                   | 0(1)              | 0(1)                 | O(n)              | O(n)              | 0(1)              | 0(1)                 | O(n)               |
| Linear Data Structures | [singly-Linked List | 0(n)              | 0(n)              | 0(1)              | 0(1)                 | O(n)              | O(n)              | 0(1)              | 0(1)                 | O(n)               |
| Linear Data Structures | Doubly-Linked List  | 0(n)              | 0(n)              | 0(1)              | 0(1)                 | O(n)              | O(n)              | 0(1)              | 0(1)                 | O(n)               |
|                        | Skip List           | 0( log(n) )       | 0( log(n))        |                   | 0(log(n))            | O(n)              | O(n)              | O(n)              | O(n)                 | O(n log(n))        |
|                        | Hash Iable          |                   | 0(1)              | 0(1)              | 0(1)                 |                   | O(n)              | O(n)              | O(n)                 | O(n)               |
|                        | [Binary_Search Tree | 0( log(n) )       | 0( log(n))        | 0( log(n))        |                      | O(n)              | O(n)              | O(n)              | O(n)                 | O(n)               |
|                        | Cartesian Iree      | N/A               | 0( log(n)         | 0( log(n)         |                      | N/A               | O(n)              | O(n)              | O(n)                 | O(n)               |
|                        | B-Iree              | 0( log(n) )       | 0( log(n))        | O(log(n))         |                      |                   | O( log(n) )       | O( log(n) )       | O(log(n))            | O(n)               |
|                        | Red-Black Iree      |                   |                   |                   |                      | O(1og(n)          | 0(log(n)          | O(log(n)          | O(log(n))            | O(n)               |
|                        | Splay_Tree          | N/A               | O(log(n))         |                   |                      |                   | O(log(n))         | O(log(n))         | O(log(n))            | O(n)               |
|                        | AVL Iree            | @(log(n))         |                   | O(log(n)          | 0(1og(n)             | O(log(n))         | O(log(n)          | O(log(n)          | O(log(n)             | O(n)               |
|                        | KD Iree             |                   |                   |                   | O(log(n))            | O(n)              | O(n)              | O(n)              | O(n)                 | O(n)               |

Source

: Know Thy Complexities! (06-Apr-2021)

Database Management Systems

![Image](Lecture 8.2_artifacts/image_000042_0d9dfbde1de846c018eea32fe6aba21e8a9c7f3c69ef770101468a6cfb66a6e5.png)

Module 37

Partha Pratim Das

Objectives &amp; Outline

Data Structure

Linear Data Structures

Array

Linked List

Search

Linear Search

Binary Search

Module Summary

## Module Summary

- Introduced Data Structures
- Reviewed array, list, stack, queue
- Reviewed linear and binary search

Slides used in this presentation are borrowed from http://db-book.com/ with kind permission of the authors.

Edited and new slides are marked with 'PPD'.

Partha Pratim Das
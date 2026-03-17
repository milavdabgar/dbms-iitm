![Image](Lecture 9.3_artifacts/image_000000_bbaa640f2b7c7b6f18cdf441c797dcf1ce99e755b6ef0a9bbf7b581538bddcab.png)

## Module 43

Partha Pratim Das

Objectives &amp; Outline

B+-Tree Index Files

Simple B +

Tree

Index Files

Nodes

Observations

Query

Duplicates

Updates

Insertion

Deletion

File Organization

Non-Unique Keys

Relocation and Secondary Indices

Strings

B-Tree Index Files

Comparison

Module Summary

Database Management Systems

## Database Management Systems

Module 43: Indexing and Hashing/3: Indexing/3

## Partha Pratim Das

Department of Computer Science and Engineering Indian Institute of Technology, Kharagpur ppd@cse.iitkgp.ac.in

Partha Pratim Das

![Image](Lecture 9.3_artifacts/image_000001_0d9dfbde1de846c018eea32fe6aba21e8a9c7f3c69ef770101468a6cfb66a6e5.png)

## Module 43

Partha Pratim Das

Objectives &amp; Outline

B+-Tree Index Files

Simple B +

Tree

Index Files

Nodes

Observations

Query

Duplicates

Updates

Insertion

Deletion

File Organization

Non-Unique Keys

Relocation and Secondary Indices

Strings

B-Tree Index Files

Comparison

Module Summary

## Module Recap

- Recapitulated the notions of Balanced Binary Search Trees as options for optimal in-memory search data structures
- Understood the issues relating to external data structures for persistent data
- Explored 2-3-4 Tree in depth as a precursor to B/B+-Tree for an efficient external data structure for database and index tables

![Image](Lecture 9.3_artifacts/image_000002_b551d1d039a350a56349b412170007d20638ad0732feb40b06cdb100cf6ab680.png)

## Module 43

Partha Pratim Das

Objectives &amp; Outline

B+-Tree Index Files

Simple B +

Tree

Index Files

Nodes

Observations

Query

Duplicates

Updates

Insertion

Deletion

File Organization

Non-Unique Keys

Relocation and Secondary Indices

Strings

B-Tree Index Files

Comparison

Module Summary

## Module Objectives

- To understand the design of B + Tree Index Files as a generalization of 2-3-4 Tree
- To understand the fundamentals of B-Tree Index Files

![Image](Lecture 9.3_artifacts/image_000003_b551d1d039a350a56349b412170007d20638ad0732feb40b06cdb100cf6ab680.png)

## Module 43

Partha Pratim Das

Objectives &amp; Outline

B+-Tree Index

Files

Simple B +

Index Files

Nodes

Observations

Query

Duplicates

Updates

Insertion

Deletion

File Organization

Non-Unique Keys

Relocation and

Secondary Indices

Strings

B-Tree Index Files

Comparison

Module Summary

Tree

## Module Outline

- B + Tree Index Files
- B-Tree Index Files

![Image](Lecture 9.3_artifacts/image_000004_32155ccc63eaf8ac3b5d36be7560257f854d0b99536286a17a16546fbab339af.png)

## Module 43

Partha Pratim Das

Objectives &amp; Outline

B+-Tree Index Files

Simple B +

Tree

Index Files

Nodes

Observations

Query

Duplicates

Updates

Insertion

Deletion

File Organization

Non-Unique Keys

Relocation and

Secondary Indices

Strings

B-Tree Index Files

Comparison

Module Summary

## B + Tree Index Files

![Image](Lecture 9.3_artifacts/image_000005_bbaa640f2b7c7b6f18cdf441c797dcf1ce99e755b6ef0a9bbf7b581538bddcab.png)

## Module 43

Partha Pratim Das

Objectives &amp; Outline

B+-Tree Index Files

Simple B +

Tree

Index Files

Nodes

Observations

Query

Duplicates

Updates

Insertion

Deletion

File Organization

Non-Unique Keys

Relocation and

Secondary Indices

Strings

B-Tree Index Files

Comparison

Module Summary

## B + Tree

## The B + Tree

- Is a balanced binary search tree
- Follows a multi-level index format like 2-3-4 Tree
- Has the leaf nodes denoting actual data pointers
- Ensures that all leaf nodes remain at the same height (like 2-3-4 Tree)
- Has the leaf nodes are linked using a link list
- Can support random access as well as sequential access
- Example:

![Image](Lecture 9.3_artifacts/image_000006_89959b01921c6da9b628e8322c19b9c3cc90e9a07f26f3fe5c826b5fb880b4c5.png)

Source :

B

+

Tree

Database Management Systems

## Partha Pratim Das

![Image](Lecture 9.3_artifacts/image_000007_bbaa640f2b7c7b6f18cdf441c797dcf1ce99e755b6ef0a9bbf7b581538bddcab.png)

## Module 43

Partha Pratim

Das

Objectives &amp;

Outline

B+-Tree Index

Files

Simple B +

Index Files

Nodes

Observations

Query

Duplicates

Updates

Insertion

Deletion

File Organization

Non-Unique Keys

Relocation and

Secondary Indices

Strings

B-Tree Index Files

Comparison

Module Summary

Tree

![Image](Lecture 9.3_artifacts/image_000008_25fbbc447a3fc5b164f1fd70a7a4bbdfc2e5da77d22fc403fd57a0587222a1ae.png)

![Image](Lecture 9.3_artifacts/image_000009_3ee5dd4a26c1967e6e7654c2d655b1d2ce166236248a4a44705aaaccda1789c4.png)

- Internal node contains
- At least n 2 child pointers, except the root node
- At most n pointers
- Leaf node contains
- At least n 2 record pointers and n 2 key values
- At most n record pointer and n key values
- One block pointer P to point to next leaf node

![Image](Lecture 9.3_artifacts/image_000010_63d33d823cdab82aa5b664df8bcc75dfe5a34fdd86cad2409d6e110e52ec9c79.png)

## Source : B + Tree

Database Management Systems

Note: These are approximate values, we will discuss more precise values later in this lecture.

![Image](Lecture 9.3_artifacts/image_000011_bbaa640f2b7c7b6f18cdf441c797dcf1ce99e755b6ef0a9bbf7b581538bddcab.png)

## Module 43

Partha Pratim Das

Objectives &amp; Outline

B+-Tree Index Files

Simple B +

Tree

Index Files

Nodes

Observations

Query

Duplicates

Updates

Insertion

Deletion

File Organization

Non-Unique Keys

Relocation and

Secondary Indices

Strings

B-Tree Index Files

Comparison

Module Summary

## B + Tree (3): Search

- Suppose we have to search 55 in the B + tree below
- First, we will fetch for the intermediary node which will direct to the leaf node that can contain a record for 55
- So, in the intermediary node, we will find a branch between 50 and 75 nodes
- Then at the end, we will be redirected to the third leaf node
- Here DBMS will perform a sequential search to find 55

![Image](Lecture 9.3_artifacts/image_000012_fec748991f2f044f0b0c87831d9d618e8ad102936e9ae8e0a04082905eff0ed1.png)

B

+

Tree

Source :

![Image](Lecture 9.3_artifacts/image_000013_bbaa640f2b7c7b6f18cdf441c797dcf1ce99e755b6ef0a9bbf7b581538bddcab.png)

Module 43

Partha Pratim

Das

Objectives &amp;

Outline

B+-Tree Index

Files

Simple B +

Index Files

Nodes

Observations

Query

Duplicates

Updates

Insertion

Deletion

File Organization

Non-Unique Keys

Relocation and

Secondary Indices

Strings

B-Tree Index

Files

Comparison

Module Summary

Tree

## B + Tree (3): Insert

![Image](Lecture 9.3_artifacts/image_000014_01b812ae83dc5e2b7b1aebc9e7124b5aec6decfdc7d2d2a0fd91f36163e58ff2.png)

- Suppose we want to insert a record 60 that goes to 3 rd leaf node after 55
- The leaf node of this tree is already full, so we cannot insert 60 there
- So we have to split the leaf node, so that it can be inserted into tree without affecting the fill factor, balance and order
- The 3 rd leaf node has the values (50, 55, 60, 65, 70) and its current root node is 50
- We will split the leaf node of the tree in the middle so that its balance is not altered

## Source : B + Tree

Database Management Systems

## Partha Pratim Das

![Image](Lecture 9.3_artifacts/image_000015_bbaa640f2b7c7b6f18cdf441c797dcf1ce99e755b6ef0a9bbf7b581538bddcab.png)

Module 43

Partha Pratim

Das

Objectives &amp;

Outline

B+-Tree Index

Files

Simple B +

Index Files

Nodes

Observations

Query

Duplicates

Updates

Insertion

Deletion

File Organization

Non-Unique Keys

Relocation and

Secondary Indices

Strings

B-Tree Index

Files

Comparison

Module Summary

Tree

## B + Tree (4): Insert

![Image](Lecture 9.3_artifacts/image_000016_31ea633bb06cf4e617b693b290d200f4eff049eb7930ce9d5e7d434099b052e9.png)

- So we can group (50, 55) and (60, 65, 70) into 2 leaf nodes
- If these two has to be leaf nodes, the intermediate node cannot branch from 50
- It should have 60 added to it, and then we can have pointers to a new leaf node
- This is how we can insert an entry when there is overflow. In a normal scenario, it is very easy to find the node where it fits and then place it in that leaf node

Source :

![Image](Lecture 9.3_artifacts/image_000017_d73c026667f44cda001415f8490bb3f778066d52b7e3cd5f493a0ea3f0fafb54.png)

![Image](Lecture 9.3_artifacts/image_000018_bbaa640f2b7c7b6f18cdf441c797dcf1ce99e755b6ef0a9bbf7b581538bddcab.png)

Module 43

Partha Pratim

Das

Objectives &amp;

Outline

B+-Tree Index

Files

Simple B +

Index Files

Nodes

Observations

Query

Duplicates

Updates

Insertion

Deletion

File Organization

Non-Unique Keys

Relocation and

Secondary Indices

Strings

B-Tree Index

Files

Comparison

Module Summary

Tree

## B + Tree (5): Delete

![Image](Lecture 9.3_artifacts/image_000019_dcc7abbd561a61d67782c7ed0930e76005bdee657584ba895da1c8d574041bdf.png)

- To delete 60, we have to remove 60 from intermediate node as well as 4 th leaf node
- If we remove it from the intermediate node, then the tree will not remain a B+ tree
- So with deleting 60 we re-arranging the nodes:

![Image](Lecture 9.3_artifacts/image_000020_7e7bf43aac9cbe10338fa01cb49025022055965cf8eabc33215a39896befeedb.png)

Source

:

B

+

Tree

Database Management Systems

Partha Pratim Das

![Image](Lecture 9.3_artifacts/image_000021_0d9dfbde1de846c018eea32fe6aba21e8a9c7f3c69ef770101468a6cfb66a6e5.png)

## Module 43

Partha Pratim Das

Objectives &amp; Outline

B+-Tree Index Files

Simple B +

Tree

Index Files

Nodes

Observations

Query

Duplicates

Updates

Insertion

Deletion

File Organization

Non-Unique Keys

Relocation and Secondary Indices

Strings

B-Tree Index Files

Comparison

Module Summary

## B + Tree Index Files

- B + tree indices are an alternative to indexed-sequential files
- Disadvantage of ISAM files
- Performance degrades as file grows, since many overflow blocks get created
- Periodic reorganization of entire file is required
- Advantage of B + tree index files :
- Automatically reorganizes itself with small, local, changes, in the face of insertions and deletions
- Reorganization of entire file is not required to maintain performance
- (Minor) disadvantage of B + trees :
- Extra insertion and deletion overhead, space overhead
- Advantages of B + trees outweigh disadvantages
- B + trees are used extensively

![Image](Lecture 9.3_artifacts/image_000022_bbaa640f2b7c7b6f18cdf441c797dcf1ce99e755b6ef0a9bbf7b581538bddcab.png)

Module 43

Partha Pratim

Das

Objectives &amp;

Outline

B+-Tree Index

Files

Simple B +

Index Files

Nodes

Observations

Query

Duplicates

Updates

Insertion

Deletion

File Organization

Non-Unique Keys

Relocation and

Secondary Indices

Strings

B-Tree Index

Files

Comparison

Module Summary

Tree

## B + Tree Index Files (2): Example

![Image](Lecture 9.3_artifacts/image_000023_2c8ef269953d6158ebaa611ca34d81be86798856fa9b7b8570017994f32085fb.png)

Database Management Systems

Partha Pratim Das

![Image](Lecture 9.3_artifacts/image_000024_bbaa640f2b7c7b6f18cdf441c797dcf1ce99e755b6ef0a9bbf7b581538bddcab.png)

## Module 43

Partha Pratim Das

Objectives &amp; Outline

B+-Tree Index Files

Simple B + Tree

Index Files

Nodes

Observations

Query

Duplicates

Updates

Insertion

Deletion

File Organization

Non-Unique Keys

Relocation and Secondary Indices

Strings

B-Tree Index Files

Comparison

Module Summary

## B + Tree Index Files (3): Structure

A B + tree is a rooted tree satisfying the following properties:

- All paths from root to leaf are of the same length
- Each node that is not a root or a leaf has between glyph[ceilingleft] n 2 glyph[ceilingright] and n children
- A leaf node has between an glyph[ceilingleft] n -1 2 glyph[ceilingright] and n -1 values
- Special cases:
- If the root is not a leaf, it has at least 2 children.
- If the root is a leaf (that is, there are no other nodes in the tree), it can have between 0 and ( n -1) values.

![Image](Lecture 9.3_artifacts/image_000025_bbaa640f2b7c7b6f18cdf441c797dcf1ce99e755b6ef0a9bbf7b581538bddcab.png)

Module 43

Partha Pratim Das

Objectives &amp; Outline

B+-Tree Index

Files

Simple B +

Index Files

Nodes

Observations

Query

Duplicates

Updates

Insertion

Deletion

File Organization

Non-Unique Keys

Relocation and

Secondary Indices

Strings

B-Tree Index Files

Comparison

Module Summary

Tree

## B + Tree Index Files (4): Node Structure

- Typical node
- K i are the search-key values
- P i are pointers to children (for non-leaf nodes) or pointers to records or buckets of records (for leaf nodes).
- The search-keys in a node are ordered
- K 1 &lt; K 2 &lt; K 3 &lt; · · · &lt; K n -1 (Initially assume no duplicate keys, address duplicates later)

P1

K1

P2

Pn-1

Kn-1

Pn

![Image](Lecture 9.3_artifacts/image_000026_bbaa640f2b7c7b6f18cdf441c797dcf1ce99e755b6ef0a9bbf7b581538bddcab.png)

Module 43

Partha Pratim

Das

Objectives &amp;

Outline

B+-Tree Index

Files

Simple B +

Index Files

Nodes

Observations

Query

Duplicates

Updates

Insertion

Deletion

File Organization

Non-Unique Keys

Relocation and

Secondary Indices

Strings

B-Tree Index

Files

Comparison

Module Summary

Tree

## B + Tree Index Files (5): Leaf Nodes

## Properties of a leaf node

- For i = 1 , 2 , · · · , n -1, pointer P i points to a file record with search-key value K i ,
- If L i , L j are leaf nodes and i &lt; j , L i 's search-key values are less than or equal to L j 's search-key values
- P n points to next leaf node in search-key order

![Image](Lecture 9.3_artifacts/image_000027_50eeaf3797996ade356fac573425b3d53e1b2f8f730e0e7404ca322f5aacc8e1.png)

## Database Management Systems

Partha Pratim Das

![Image](Lecture 9.3_artifacts/image_000028_bbaa640f2b7c7b6f18cdf441c797dcf1ce99e755b6ef0a9bbf7b581538bddcab.png)

## Module 43

Partha Pratim Das

Objectives &amp; Outline

B+-Tree Index Files

Simple B + Tree Index Files

Nodes

Observations

Query

Duplicates

Updates

Insertion

Deletion

File Organization

Non-Unique Keys

Relocation and Secondary Indices

Strings

B-Tree Index Files

Comparison

Module Summary

## B + Tree Index Files (6): Non-Leaf Nodes

- Non leaf nodes form a multi-level sparse index on the leaf nodes. For a non-leaf node with m pointers:
- All the search-keys in the subtree to which P 1 points are less than K 1
- For 2 ≤ i ≤ n -1, all the search-keys in the subtree to which Pi points have values greater than or equal to K i -1 and less than K i
- All the search-keys in the subtree to which Pn points have values greater than or equal to K n -1

P1

K1

P2

Pn-1

Kn-1

Pn

![Image](Lecture 9.3_artifacts/image_000029_15c72944a9e2b3aecafbb80559a397829b0bbba1d53103de51f6517ce067a480.png)

![Image](Lecture 9.3_artifacts/image_000030_bbaa640f2b7c7b6f18cdf441c797dcf1ce99e755b6ef0a9bbf7b581538bddcab.png)

Module 43

Partha Pratim

Das

Objectives &amp;

Outline

B+-Tree Index

Files

Simple B +

Index Files

Nodes

Observations

Query

Duplicates

Updates

Insertion

Deletion

File Organization

Non-Unique Keys

Relocation and

Secondary Indices

Strings

B-Tree Index

Files

Comparison

Module Summary

Tree

## B + Tree Index Files (7): Example

![Image](Lecture 9.3_artifacts/image_000031_0a93e175bf36d6083556cc854d92bb0a6fd8fba0a7ebdd4eb2306809fae05e16.png)

- Leaf nodes must have between 3 and 5 values: glyph[ceilingleft] n -1 2 glyph[ceilingright] and n -1, with n = 6
- Non-leaf nodes other than root must have between 3 and 6 children: glyph[ceilingleft] n 2 glyph[ceilingright] and n with n = 6
- Root must have at least 2 children

![Image](Lecture 9.3_artifacts/image_000032_bbaa640f2b7c7b6f18cdf441c797dcf1ce99e755b6ef0a9bbf7b581538bddcab.png)

Module 43

Partha Pratim Das

Objectives &amp; Outline

B+-Tree Index Files

Simple B +

Tree

Index Files

Nodes

Observations

Query

Duplicates

Updates

Insertion

Deletion

File Organization

Non-Unique Keys

Relocation and Secondary Indices

Strings

B-Tree Index Files

Comparison

Module Summary

## B + Tree Index Files: Observations

- Since the inter-node connections are done by pointers, logically close blocks need not be physically close
- The non-leaf levels of the B + tree form a hierarchy of sparse indices
- The B + tree contains a relatively small number of levels
- Level below root has at least 2 ∗ ⌈ n ⌉ values
- Next level has at least 2 ∗ glyph[ceilingleft] n glyph[ceilingright] ∗ glyph[ceilingleft] n glyph[ceilingright] values
- 2
- 2 2
- ... etc.
- If there are K search-key values in the file, the tree height is no more than glyph[ceilingleft] log glyph[ceilingleft] n / 2 glyph[ceilingright] ( K ) glyph[ceilingright]
- thus searches can be conducted efficiently
- Insertions and deletions to the main file can be handled efficiently, as the index can be restructured in logarithmic time

Database Management Systems

Partha Pratim Das

43.19

![Image](Lecture 9.3_artifacts/image_000033_bbaa640f2b7c7b6f18cdf441c797dcf1ce99e755b6ef0a9bbf7b581538bddcab.png)

## Module 43

Partha Pratim Das

Objectives &amp; Outline

B+-Tree Index

Files

Simple B +

Index Files

Nodes

Observations

Query

Duplicates

Updates

Insertion

Deletion

File Organization

Non-Unique Keys

Relocation and

Secondary Indices

Strings

B-Tree Index Files

Comparison

Module Summary

Tree

## B + Tree Index Files: Queries

- Find record with search-key value V
- a) C = root
- b) While C is not a leaf node
- i) Let i be least value such that V ≤ K i
- ii) If no such exists, set C = last non-null pointer in C
- iii) Else { if ( V = K i ) Set C = P i +1 else set C = P i }
- c) Let i be least value s.t. K i = V
- d) If there is such a value i, follow pointer Pi to the desired record
- e) Else no record with search-key value k exists

![Image](Lecture 9.3_artifacts/image_000034_a7ce7bf6eab45de9836b45ab1f4b943f0215ec3640ae5982a28841207b350ec6.png)

Database Management Systems

Partha Pratim Das

![Image](Lecture 9.3_artifacts/image_000035_bbaa640f2b7c7b6f18cdf441c797dcf1ce99e755b6ef0a9bbf7b581538bddcab.png)

## Module 43

Partha Pratim Das

Objectives &amp; Outline

B+-Tree Index Files

Simple B +

Tree

Index Files

Nodes

Observations

Query

Duplicates

Updates

Insertion

Deletion

File Organization

Non-Unique Keys

Relocation and

Secondary Indices

Strings

B-Tree Index Files

Comparison

Module Summary

## B + Trees Index Files: Queries (2)

- If there are K search-key values in the file, the height of the tree is no more than ⌈ log glyph[ceilingleft] n 2 glyph[ceilingright] ( K ) ⌉
- A node is generally the same size as a disk block, typically 4 kilobytes
- and n is typically around 100 (40 bytes per index entry)
- With 1 million search key values and n = 100
- at most log 50 (1 , 000 , 000) = 4 nodes are accessed in a lookup
- Contrast this with a balanced binary tree with 1 million search key values - around 20 nodes are accessed in a lookup
- above difference is significant since every node access may need a disk I/O, costing around 20 milliseconds

![Image](Lecture 9.3_artifacts/image_000036_bbaa640f2b7c7b6f18cdf441c797dcf1ce99e755b6ef0a9bbf7b581538bddcab.png)

## Module 43

Partha Pratim Das

Objectives &amp; Outline

B+-Tree Index Files

Simple B +

Tree

Index Files

Nodes

Observations

Query

Duplicates

Updates

Insertion

Deletion

File Organization

Non-Unique Keys

Relocation and Secondary Indices

Strings

B-Tree Index Files

Comparison

Module Summary

## B + Tree Index Files: Handling Duplicates

- With duplicate search keys
- In both leaf and internal nodes,
- glyph[triangleright] we cannot guarantee that K 1 &lt; K 2 &lt; K 3 &lt; · · · &lt; K n -1
- glyph[triangleright] but can guarantee K 1 ≤ K 2 ≤ K 3 ≤ · · · ≤ K n -1
- Search-keys in the subtree to which P i points
- glyph[triangleright] are ≤ K i , but not necessarily &lt; K i ,
- glyph[triangleright] To see why, suppose same search key value V is present in two leaf node L i and L i +1 . Then in parent node K i must be equal to V

![Image](Lecture 9.3_artifacts/image_000037_bbaa640f2b7c7b6f18cdf441c797dcf1ce99e755b6ef0a9bbf7b581538bddcab.png)

## Module 43

Partha Pratim Das

Objectives &amp; Outline

B+-Tree Index Files

Simple B +

Tree

Index Files

Nodes

Observations

Query

Duplicates

Updates

Insertion

Deletion

File Organization

Non-Unique Keys

Relocation and Secondary Indices

Strings

B-Tree Index Files

Comparison

Module Summary

## B + Tree Index Files: Handling Duplicates (2)

- We modify find procedure as follows
- traverse P i even if V = K i
- As soon as we reach a leaf node C check if C has only search key values less than V glyph[triangleright] if so set C = right sibling of C before checking whether C contains V
- Procedure printAll
- uses modified find procedure to find first occurrence of V
- Traverse through consecutive leaves to find all occurrences of V

![Image](Lecture 9.3_artifacts/image_000038_0d9dfbde1de846c018eea32fe6aba21e8a9c7f3c69ef770101468a6cfb66a6e5.png)

## Module 43

Partha Pratim Das

Objectives &amp; Outline

B+-Tree Index Files

Simple B +

Tree

Index Files

Nodes

Observations

Query

Duplicates

Updates

Insertion

Deletion

File Organization

Non-Unique Keys

Relocation and Secondary Indices

Strings

B-Tree Index Files

Comparison

Module Summary

## Updates on B + Trees: Insertion

- Find the leaf node in which the search-key value would appear
- If the search-key value is already present in the leaf node
- Add record to the file
- If necessary add a pointer to the bucket
- If the search-key value is not present, then
- Add the record to the main file (and create a bucket if necessary)
- If there is room in the leaf node, insert (key-value, pointer) pair in the leaf node
- Otherwise, split the node (along with the new (key-value, pointer) entry) as discussed in the next slide

![Image](Lecture 9.3_artifacts/image_000039_0d9dfbde1de846c018eea32fe6aba21e8a9c7f3c69ef770101468a6cfb66a6e5.png)

## Module 43

Partha Pratim Das

Objectives &amp; Outline

B+-Tree Index Files

Simple B +

Tree

Index Files

Nodes

Observations

Query

Duplicates

Updates

Insertion

Deletion

File Organization

Non-Unique Keys

Relocation and

Secondary Indices

Strings

B-Tree Index Files

Comparison

Module Summary

## Updates on B + Trees: Insertion (2)

- Splitting a leaf node:
- take the n (search-key value, pointer) pairs (including the one being inserted) in sorted order. Place the first ⌈ n 2 ⌉ in the original node, and the rest in a new node
- let the new node be p , and let k be the least key value in p . Insert ( k , p ) in the parent of the node being split
- If the parent is full, split it and propagate the split further up
- Splitting of nodes proceeds upwards till a node that is not full is found
- In the worst case the root node may be split increasing the height of the tree by 1

![Image](Lecture 9.3_artifacts/image_000040_2075283719ce89602eb0456db75922abafde38b5e8aa0fc67dcc0d6edca6d6f4.png)

![Image](Lecture 9.3_artifacts/image_000041_bbaa640f2b7c7b6f18cdf441c797dcf1ce99e755b6ef0a9bbf7b581538bddcab.png)

## Module 43

Partha Pratim Das

Objectives &amp; Outline

B+-Tree Index

Files

Simple B +

Index Files

Nodes

Observations

Query

Duplicates

Updates

Insertion

Deletion

File Organization

Non-Unique Keys

Relocation and

Secondary Indices

Strings

B-Tree Index

Files

Comparison

Module Summary

Tree

## Updates on B + Trees: Insertion (3)

- Splitting a non-leaf node: when inserting ( k , p ) into an already full internal node N
- Copy N to an in-memory area M with space for n +1 pointers and n keys
- Insert ( k , p ) into M
- Copy P 1 , K 1 , · · · , K glyph[ceilingleft] n 2 glyph[ceilingright] -1 , P glyph[ceilingleft] n 2 glyph[ceilingright] from M back into node N
- Insert ( K glyph[ceilingleft] n 2 glyph[ceilingright] , N ′ ) into parent N
- Copy P glyph[ceilingleft] n 2 glyph[ceilingright] +1 , K glyph[ceilingleft] n 2 glyph[ceilingright] +1 , · · · , K n , P n +1 from M into newly allocated node N ′
- Read pseudocode in book!

![Image](Lecture 9.3_artifacts/image_000042_04ea81927341a9ec817ef053724a1028d638e9377f4d7a3951675017572b9857.png)

Database Management Systems

![Image](Lecture 9.3_artifacts/image_000043_d8837fc0013179df996be5d6752151fa0fb28de0768b46d5524993be088a6b53.png)

Partha Pratim Das

![Image](Lecture 9.3_artifacts/image_000044_bbaa640f2b7c7b6f18cdf441c797dcf1ce99e755b6ef0a9bbf7b581538bddcab.png)

Module 43

Partha Pratim

Das

Objectives &amp;

Outline

B+-Tree Index

Files

Simple B +

Index Files

Nodes

Observations

Query

Duplicates

Updates

Insertion

Deletion

File Organization

Non-Unique Keys

Relocation and

Secondary Indices

Strings

B-Tree Index

Files

Comparison

Module Summary

Tree

## Updates on B + Trees: Insertion Example

Morart

Einstein

Gold

Root node

Internal nodes

Leaf nodes

Brandt

Califieri

Crickl

Einstein

El Said

Katz

Kim

Morart

Singh

Srinivasan

Wu

![Image](Lecture 9.3_artifacts/image_000045_efd78f172111b8fe0f913491462f94586070632d764ee2286ec66f6974070754.png)

Database Management Systems

Partha Pratim Das

![Image](Lecture 9.3_artifacts/image_000046_bbaa640f2b7c7b6f18cdf441c797dcf1ce99e755b6ef0a9bbf7b581538bddcab.png)

## Updates on B + Trees: Insertion Example (2)

![Image](Lecture 9.3_artifacts/image_000047_0b7d476b739c8dcc485f908c22696829bc63d0856dcaf26c01d3f1ad091c45bf.png)

![Image](Lecture 9.3_artifacts/image_000048_0d9dfbde1de846c018eea32fe6aba21e8a9c7f3c69ef770101468a6cfb66a6e5.png)

## Module 43

Partha Pratim Das

Objectives &amp; Outline

B+-Tree Index Files

Simple B +

Tree

Index Files

Nodes

Observations

Query

Duplicates

Updates

Insertion

Deletion

File Organization

Non-Unique Keys

Relocation and Secondary Indices

Strings

B-Tree Index Files

Comparison

Module Summary

## Updates on B + Trees: Deletion

- Find the record to be deleted, and remove it from the main file and from the bucket (if present)
- Remove (search-key value, pointer) from the leaf node if there is no bucket or if the bucket has become empty
- If the node has too few entries due to the removal, and the entries in the node and a sibling fit into a single node, then merge siblings :
- Insert all the search-key values in the two nodes into a single node (the one on the left), and delete the other node.
- Delete the pair ( K i -1 , P i ), where P i is the pointer to the deleted node, from its parent, recursively using the above procedure.

![Image](Lecture 9.3_artifacts/image_000049_02038e7c09c1baf62d04727e732bfec243b50cc49a987d55147bfddbff5da435.png)

![Image](Lecture 9.3_artifacts/image_000050_0d9dfbde1de846c018eea32fe6aba21e8a9c7f3c69ef770101468a6cfb66a6e5.png)

## Module 43

Partha Pratim Das

Objectives &amp; Outline

B+-Tree Index Files

Simple B +

Tree

Index Files

Nodes

Observations

Query

Duplicates

Updates

Insertion

Deletion

File Organization

Non-Unique Keys

Relocation and Secondary Indices

Strings

B-Tree Index Files

Comparison

Module Summary

## Updates on B + Trees: Deletion (2)

- Otherwise, if the node has too few entries due to the removal, but the entries in the node and a sibling do not fit into a single node, then redistribute pointers :
- Redistribute the pointers between the node and a sibling such that both have more than the minimum number of entries
- Update the corresponding search-key value in the parent of the node
- The node deletions may cascade upwards till a node which has ⌈ n 2 ⌉ or more pointers is found
- If the root node has only one pointer after deletion, it is deleted and the sole child becomes the root

![Image](Lecture 9.3_artifacts/image_000051_bbaa640f2b7c7b6f18cdf441c797dcf1ce99e755b6ef0a9bbf7b581538bddcab.png)

Module 43

Partha Pratim

Das

Objectives &amp;

Outline

B+-Tree Index

Files

Simple B +

Index Files

Nodes

Observations

Query

Duplicates

Updates

Insertion

Deletion

File Organization

Non-Unique Keys

Relocation and

Secondary Indices

Strings

B-Tree Index

Files

Comparison

Module Summary

Tree

## Updates on B + Trees: Deletion Example

![Image](Lecture 9.3_artifacts/image_000052_22d6b431360330fda356ca3f2febbc1a9913e9e0fac0de709894eea8e5d88c03.png)

Database Management Systems

Partha Pratim Das

![Image](Lecture 9.3_artifacts/image_000053_bbaa640f2b7c7b6f18cdf441c797dcf1ce99e755b6ef0a9bbf7b581538bddcab.png)

Module 43

Partha Pratim

Das

Objectives &amp;

Outline

B+-Tree Index

Files

Simple B +

Index Files

Nodes

Observations

Query

Duplicates

Updates

Insertion

Deletion

File Organization

Non-Unique Keys

Relocation and

Secondary Indices

Strings

B-Tree Index

Files

Comparison

Module Summary

Tree

## Updates on B + Trees: Deletion Example (2)

![Image](Lecture 9.3_artifacts/image_000054_54122baea55d473324ad7365e6c09258ad38e5de178d8f5f1389ec8dae4fa704.png)

- Leaf containing Singh and Wu became underfull, and borrowed a value Kim from its left sibling
- Search-key value in the parent changes as a result

![Image](Lecture 9.3_artifacts/image_000055_bbaa640f2b7c7b6f18cdf441c797dcf1ce99e755b6ef0a9bbf7b581538bddcab.png)

Module 43

Partha Pratim

Das

Objectives &amp;

Outline

B+-Tree Index

Files

Simple B +

Index Files

Nodes

Observations

Query

Duplicates

Updates

Insertion

Deletion

File Organization

Non-Unique Keys

Relocation and

Secondary Indices

Strings

B-Tree Index

Files

Comparison

Module Summary

Tree

## Updates on B + Trees: Deletion Example (3)

![Image](Lecture 9.3_artifacts/image_000056_30d020224112c1af5f4493ef6597954b64fdbd1ee6377ee3dd916a1f24b2a55d.png)

- Node with 'Gold' and 'Katz' became underfull, and was merged with its sibling
- Parent node becomes underfull, and is merged with its sibling
- Value separating two nodes (at the parent) is pulled down when merging
- Root node then has only one child, and is delete Database Management Systems Partha Pratim Das

![Image](Lecture 9.3_artifacts/image_000057_bbaa640f2b7c7b6f18cdf441c797dcf1ce99e755b6ef0a9bbf7b581538bddcab.png)

## Module 43

Partha Pratim Das

Objectives &amp; Outline

B+-Tree Index Files

Simple B +

Tree

Index Files

Nodes

Observations

Query

Duplicates

Updates

Insertion

Deletion

File Organization

Non-Unique Keys

Relocation and Secondary Indices

Strings

B-Tree Index Files

Comparison

Module Summary

## B + Tree File Organization

- Index file degradation problem is solved by using B + Tree indices
- Data file degradation problem is solved by using B + Tree File Organization
- The leaf nodes in a B + tree file organization store records, instead of pointers
- Leaf nodes are still required to be half full
- Since records are larger than pointers, the maximum number of records that can be stored in a leaf node is less than the number of pointers in a non-leaf node
- Insertion and deletion are handled in the same way as insertion and deletion of entries in a B + tree index

![Image](Lecture 9.3_artifacts/image_000058_bbaa640f2b7c7b6f18cdf441c797dcf1ce99e755b6ef0a9bbf7b581538bddcab.png)

Module 43

Partha Pratim

Das

Objectives &amp;

Outline

B+-Tree Index

Files

Simple B +

Index Files

Nodes

Observations

Query

Duplicates

Updates

Insertion

Deletion

File Organization

Non-Unique Keys

Relocation and

Secondary Indices

Strings

B-Tree Index

Files

Comparison

Module Summary

Tree

## B + Tree File Organization: Example

![Image](Lecture 9.3_artifacts/image_000059_ade8204d7fc2362aa293a0554f3988e0823c0d0b0ef41be9b80ebd245858f48c.png)

- Good space utilization important since records use more space than pointers.
- To improve space utilization, involve more sibling nodes in redistribution during splits and merges
- Involving 2 siblings in redistribution (to avoid split / merge where possible) results in each node having at least ⌈ 2 n 3 ⌉ entries

Partha Pratim Das

![Image](Lecture 9.3_artifacts/image_000060_0d9dfbde1de846c018eea32fe6aba21e8a9c7f3c69ef770101468a6cfb66a6e5.png)

## Module 43

Partha Pratim Das

Objectives &amp; Outline

B+-Tree Index Files

Simple B + Tree Index Files

Nodes

Observations

Query

Duplicates

Updates

Insertion

Deletion

File Organization

Non-Unique Keys

Relocation and Secondary Indices

Strings

B-Tree Index Files

Comparison

Module Summary

## Non-Unique Search Keys

- Alternatives to scheme described earlier
- Buckets on separate block (bad idea)
- List of tuple pointers with each key
- glyph[triangleright] Extra code to handle long lists
- glyph[triangleright] Deletion of a tuple can be expensive if there are many duplicates on search key (why?)
- glyph[triangleright] Low space overhead, no extra cost for queries
- Make search key unique by adding a record-identifier
- glyph[triangleright] Extra storage overhead for keys
- glyph[triangleright] Simpler code for insertion/deletion
- glyph[triangleright] Widely used

![Image](Lecture 9.3_artifacts/image_000061_0d9dfbde1de846c018eea32fe6aba21e8a9c7f3c69ef770101468a6cfb66a6e5.png)

## Module 43

Partha Pratim Das

Objectives &amp; Outline

B+-Tree Index Files

Simple B +

Tree

Index Files

Nodes

Observations

Query

Duplicates

Updates

Insertion

Deletion

File Organization

Non-Unique Keys

Relocation and Secondary Indices

Strings

B-Tree Index Files

Comparison

Module Summary

## Record Relocation and Secondary Indices

- If a record moves, all secondary indices that store record pointers have to be updated
- Node splits in B + tree file organizations become very expensive
- Solution : Use primary-index search key instead of record pointer in secondary index
- Extra traversal of primary index to locate record
- Higher cost for queries, but node splits are cheap
- Add record-id if primary-index search key is non-unique

![Image](Lecture 9.3_artifacts/image_000062_0d9dfbde1de846c018eea32fe6aba21e8a9c7f3c69ef770101468a6cfb66a6e5.png)

## Module 43

Partha Pratim Das

Objectives &amp; Outline

B+-Tree Index Files

Simple B +

Tree

Index Files

Nodes

Observations

Query

Duplicates

Updates

Insertion

Deletion

File Organization

Non-Unique Keys

Relocation and Secondary Indices

Strings

B-Tree Index Files

Comparison

Module Summary

## Indexing Strings

- Variable length strings as keys
- Variable fanout
- Use space utilization as criterion for splitting, not number of pointers
- Prefix compression
- Key values at internal nodes can be prefixes of full key
- glyph[triangleright] Keep enough characters to distinguish entries in the subtrees separated by the key value
- -For example, 'Silas' and 'Silberschatz' can be separated by 'Silb'
- Keys in leaf node can be compressed by sharing common prefixes

![Image](Lecture 9.3_artifacts/image_000063_bbaa640f2b7c7b6f18cdf441c797dcf1ce99e755b6ef0a9bbf7b581538bddcab.png)

## Module 43

Partha Pratim Das

Objectives &amp; Outline

B+-Tree Index

Files

Simple B +

Index Files

Nodes

Observations

Query

Duplicates

Updates

Insertion

Deletion

File Organization

Non-Unique Keys

Relocation and

Secondary Indices

Strings

B-Tree Index Files

Comparison

Module Summary

Tree

## B-Tree Index Files

## B-Tree Index Files

![Image](Lecture 9.3_artifacts/image_000064_5c3857bb5086fd8f667b15c29d3e9b32b54e3373e7814ab5bccd73811d8a52c4.png)

![Image](Lecture 9.3_artifacts/image_000065_bbaa640f2b7c7b6f18cdf441c797dcf1ce99e755b6ef0a9bbf7b581538bddcab.png)

## Module 43

Partha Pratim Das

Objectives &amp; Outline

B+-Tree Index

Files

Simple B +

Index Files

Nodes

Observations

Query

Duplicates

Updates

Insertion

Deletion

File Organization

Non-Unique Keys

Relocation and

Secondary Indices

Strings

B-Tree Index Files

Comparison

Module Summary

Tree

## B-Tree Index Files

- Similar to B + tree, but B-tree allows search-key values to appear only once; eliminates redundant storage of search keys
- Search keys in non-leaf nodes appear nowhere else in the B-tree; an additional pointer field for each search key in a non-leaf node must be included
- Generalized B-tree leaf node
- Non-leaf node - pointers Bi are the bucket or file record pointers

![Image](Lecture 9.3_artifacts/image_000066_8bc4f0aa3a2528bb39a8861a65b5f9d9c6683b5c28f98a12fb4f99bc85c3b44b.png)

![Image](Lecture 9.3_artifacts/image_000067_bbaa640f2b7c7b6f18cdf441c797dcf1ce99e755b6ef0a9bbf7b581538bddcab.png)

Module 43

Partha Pratim

Das

Objectives &amp;

Outline

B+-Tree Index

Files

Simple B +

Index Files

Nodes

Observations

Query

Duplicates

Updates

Insertion

Deletion

File Organization

Non-Unique Keys

Relocation and

Secondary Indices

Strings

B-Tree Index

Files

Comparison

Module Summary

Tree

## B-Tree Index File (2): Example

![Image](Lecture 9.3_artifacts/image_000068_532b65a2b673175cb51bbeb78041a46d74635ed0a3f004e01ebeb52758c42a8d.png)

B-tree (above) and B + tree (below) on same data

![Image](Lecture 9.3_artifacts/image_000069_a27bbbcc8925dc865d19518ac2bc711102e326e3f52be3f548f05c6d49504c45.png)

Database Management Systems

Partha Pratim Das

![Image](Lecture 9.3_artifacts/image_000070_bbaa640f2b7c7b6f18cdf441c797dcf1ce99e755b6ef0a9bbf7b581538bddcab.png)

## Module 43

Partha Pratim Das

Objectives &amp; Outline

B+-Tree Index Files

Simple B +

Tree

Index Files

Nodes

Observations

Query

Duplicates

Updates

Insertion

Deletion

File Organization

Non-Unique Keys

Relocation and Secondary Indices

Strings

B-Tree Index Files

Comparison

Module Summary

## Comparison of B-Tree and B + Tree Index Files

- Advantages of B-Tree indices:
- May use less tree nodes than a corresponding B + Tree
- Sometimes possible to find search-key value before reaching leaf node
- Disadvantages of B-Tree indices:
- Only small fraction of all search-key values are found early
- Non-leaf nodes are larger, so fan-out is reduced. Thus, B-Trees typically have greater depth than corresponding B + Tree
- Insertion and deletion more complicated than in B + Trees
- Implementation is harder than B + Trees
- Typically, advantages of B-Trees do not outweigh disadvantages

![Image](Lecture 9.3_artifacts/image_000071_0d9dfbde1de846c018eea32fe6aba21e8a9c7f3c69ef770101468a6cfb66a6e5.png)

Module 43

Partha Pratim Das

Objectives &amp; Outline

B+-Tree Index Files

Simple B +

Tree

Index Files

Nodes

Observations

Query

Duplicates

Updates

Insertion

Deletion

File Organization

Non-Unique Keys

Relocation and Secondary Indices

Strings

B-Tree Index Files

Comparison

Module Summary

## Module Summary

- Understood the design of B + Tree Index Files in depth for database persistent store
- Familiarized with B-Tree Index Files

Slides used in this presentation are borrowed from http://db-book.com/ with kind permission of the authors. Edited and new slides are marked with 'PPD'.

43.43
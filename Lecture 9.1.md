![Image](Lecture 9.1_artifacts/image_000000_bbaa640f2b7c7b6f18cdf441c797dcf1ce99e755b6ef0a9bbf7b581538bddcab.png)

## Module 41

Partha Pratim Das

Week Recap

Objectives &amp;

Outline

Indexing

Metrics

Ordered Indices Dense Index Files Sparse Index Files Primary and Secondary Indices Multilevel Index Index Update

Module Summary

## Database Management Systems

Module 41: Indexing and Hashing/1: Indexing/1

## Partha Pratim Das

Department of Computer Science and Engineering Indian Institute of Technology, Kharagpur ppd@cse.iitkgp.ac.in

Partha Pratim Das

![Image](Lecture 9.1_artifacts/image_000001_bbaa640f2b7c7b6f18cdf441c797dcf1ce99e755b6ef0a9bbf7b581538bddcab.png)

Module 41

Partha Pratim Das

Week Recap

Objectives &amp; Outline

Indexing

Metrics

Ordered Indices

Dense Index Files

Sparse Index Files

Primary and Secondary Indices

Multilevel Index

Index Update

Module Summary

## Week Recap

- Need for algorithm analysis, Asymptotic complexity, and Worst-case, average-case and best-case analysis
- Reviewed Linear Data Structures; array, list, stack, queue; and linear and binary search
- Reviewed Non-linear Data Structures - graph, tree, hash table; Binary Search Tree; and compared Linear and Non-Linear Data Structures
- Understood the range of Physical Storage Media
- Studied about Magnetic Disks and Magnetic Tape
- Glimpsed through Other Storage and the Future of Storage
- Familiarized with the organization for database files
- Understood how records and relations are organized in files
- Learnt how databases keep their own information in Data-Dictionary Storage - the metadata database of a database
- Understood the mechanisms for fast access of a database store

Database Management Systems

## Partha Pratim Das

![Image](Lecture 9.1_artifacts/image_000002_821f32da21a8bb9af0bddb9e2ff2419e915ba7e461f5dc4f05b60eaa6ed0b478.png)

## Module 41

Partha Pratim Das

Week Recap

Objectives &amp; Outline

Indexing

Metrics

Ordered Indices Dense Index Files Sparse Index Files Primary and Secondary Indices Multilevel Index Index Update

Module Summary

## Module Objectives

- To understand the reasons for which we need to index database table
- To learn about the ordered indexes and Indexed Sequential Access Mechanism

![Image](Lecture 9.1_artifacts/image_000003_0d9dfbde1de846c018eea32fe6aba21e8a9c7f3c69ef770101468a6cfb66a6e5.png)

## Module 41

Partha Pratim Das

Week Recap

Objectives &amp; Outline

Indexing

Metrics

Ordered Indices Dense Index Files Sparse Index Files Primary and Secondary Indices Multilevel Index Index Update

Module Summary

## Module Outline

- Basic Concepts of Indexing
- Ordered Indices

![Image](Lecture 9.1_artifacts/image_000004_c66187055de285596be50032d73dadd82d2ef960cecf03026d68ecb78134d5c9.png)

## Module 41

Partha Pratim Das

Week Recap

Objectives &amp;

Outline

Indexing

Metrics

Ordered Indices

Dense Index Files

Sparse Index Files

Primary and

Secondary Indices

Multilevel Index

Index Update

Module Summary

## Concepts of Indexing

## Concepts of Indexing

![Image](Lecture 9.1_artifacts/image_000005_bbaa640f2b7c7b6f18cdf441c797dcf1ce99e755b6ef0a9bbf7b581538bddcab.png)

Module 41

Partha Pratim

Das

Week Recap

Objectives &amp;

Outline

Indexing

Metrics

Ordered Indices

Dense Index Files

Sparse Index Files

Primary and

Secondary Indices

Multilevel Index

Index Update

Module Summary

## Search Records

- Consider a table: Faculty(Name, Phone)
- How to search on Name?
- Get the phone number for 'Pabitra Mitra'
- Use 'Name' Index - sorted on 'Name', search 'Pabitra Mitra' and navigate on pointer (rec #)
- How to search on Phone?
- Get the name of the faculty having phone number = 84772
- Use 'Phone' Index - sorted on 'Phone', search '84772' and navigate on pointer (rec #)
- We can keep the records sorted on 'Name' or on 'Phone' (called the primary index), but not on both Database Management Systems Partha Pratim Das

| Index on 'Name"     | Index on 'Name"   |                    |       | Index on "Phone   | Index on "Phone   |
|---------------------|-------------------|--------------------|-------|-------------------|-------------------|
| Name                | Pointer           | Rec# Name          | Phone | Pointer           | Phone             |
| Anupam Basu         |                   | 1Partha Pratim Das | 81998 |                   | 81664             |
| Pabitra Mitra       |                   | 2Anupam Basu       | 82404 |                   | 81998             |
| Partha Pratim Das   |                   | 3Ranjan Sen        | 84624 |                   | 82404             |
| Prabir Kumar Biswas |                   | 4Sudeshna Sarkar   | 82432 |                   | 82432             |
| Rajib Mall          |                   | 5Rajib Mall        | 83668 |                   | 83668             |
| Ranjan Sen          |                   | 6Pabitra Mitra     | 81664 |                   | 84624             |
| Sudeshna Sarkar     |                   |                    |       |                   | 84772             |

![Image](Lecture 9.1_artifacts/image_000006_0d9dfbde1de846c018eea32fe6aba21e8a9c7f3c69ef770101468a6cfb66a6e5.png)

## Module 41

Partha Pratim Das

Week Recap

Objectives &amp; Outline

Indexing

Metrics

Ordered Indices

Dense Index Files

Sparse Index Files

Primary and Secondary Indices

Multilevel Index

Index Update

Module Summary

## Basic Concepts

- Indexing mechanisms used to speed up access to desired data.
- For example:
- glyph[triangleright] Name in a faculty table
- glyph[triangleright] author catalog in library
- Search Key - attribute to set of attributes used to look up records in a file
- An index file consists of records (called index entries ) of the form
- Index files are typically much smaller than the original file
- Two basic kinds of indices:
- Ordered indices : search keys are stored in sorted order
- Hash indices : search keys are distributed uniformly across buckets using a hash function

![Image](Lecture 9.1_artifacts/image_000007_259d2605693368d3fdf6d649074f1d4cd28e2e011d6f621df9aad7e45165cca5.png)

Database Management Systems

Partha Pratim Das

![Image](Lecture 9.1_artifacts/image_000008_0d9dfbde1de846c018eea32fe6aba21e8a9c7f3c69ef770101468a6cfb66a6e5.png)

## Module 41

Partha Pratim Das

Week Recap

Objectives &amp; Outline

Indexing

Metrics

Ordered Indices Dense Index Files Sparse Index Files Primary and Secondary Indices Multilevel Index Index Update

Module Summary

## Index Evaluation Metrics

- Access types supported efficiently. For example,
- records with a specified value in the attribute, or
- records with an attribute value falling in a specified range of values
- Access time
- Insertion time
- Deletion time
- Space overhead

![Image](Lecture 9.1_artifacts/image_000009_bbaa640f2b7c7b6f18cdf441c797dcf1ce99e755b6ef0a9bbf7b581538bddcab.png)

## Module 41

Partha Pratim Das

Week Recap

Objectives &amp;

Outline

Indexing

Metrics

Ordered Indices

Dense Index Files

Sparse Index Files

Primary and

Secondary Indices

Multilevel Index

Index Update

Module Summary

## Ordered Indices

## Ordered Indices

![Image](Lecture 9.1_artifacts/image_000010_0d9dfbde1de846c018eea32fe6aba21e8a9c7f3c69ef770101468a6cfb66a6e5.png)

## Module 41

Partha Pratim Das

Week Recap

Objectives &amp; Outline

Indexing

Metrics

## Ordered Indices

Dense Index Files

Sparse Index Files

Primary and Secondary Indices

Multilevel Index

Index Update

Module Summary

## Ordered Indices

- In an ordered index , index entries are stored sorted on the search key value. For example, author catalog in library
- Primary index : in a sequentially ordered file, the index whose search key specifies the sequential order of the file
- Also called clustering index
- The search key of a primary index is usually but not necessarily the primary key
- Secondary index : an index whose search key specifies an order different from the sequential order of the file
- Also called non-clustering index
- Index-sequential file : ordered sequential file with a primary index

![Image](Lecture 9.1_artifacts/image_000011_c66187055de285596be50032d73dadd82d2ef960cecf03026d68ecb78134d5c9.png)

## Module 41

Partha Pratim

Das

Week Recap

Objectives &amp;

Outline

Indexing

Metrics

Ordered Indices

Dense Index Files

Sparse Index Files

Primary and

Secondary Indices

Multilevel Index

Index Update

Module Summary

## Dense Index Files

- Dense index - Index record appears for every search-key value in the file.
- For example, index on ID attribute of instructor relation

![Image](Lecture 9.1_artifacts/image_000012_ccaa0e7dd6b83d02be0b3a45827f8bbd4556e260258fcb50bf2f3499c3f035d3.png)

## Partha Pratim Das

![Image](Lecture 9.1_artifacts/image_000013_bbaa640f2b7c7b6f18cdf441c797dcf1ce99e755b6ef0a9bbf7b581538bddcab.png)

## Module 41

Partha Pratim

Das

Week Recap

Objectives &amp;

Outline

Indexing

Metrics

Ordered Indices

Dense Index Files

Sparse Index Files

Primary and

Secondary Indices

Multilevel Index

Index Update

Module Summary

## Dense Index Files (2)

- Dense index on dept name , with instructor file sorted on dept name

![Image](Lecture 9.1_artifacts/image_000014_d08e883b56e5ebede24c7f49ba7d0cc4dc29c134177bb1e2e32d6aa6110ad0b7.png)

| Biology   |   76766 | Crick      | Biology   |   72000 |
|-----------|---------|------------|-----------|---------|
| Comp. Sci |   10101 | Srinivasan |           |   65000 |
| Elec. Eng |   45565 | Katz       | Comp Sci. |   75000 |
| Finance   |   83821 | Brandt     |           |   92000 |
| History   |   98345 | Kim        | Elec. Eng |   80000 |
| Music     |   12121 | Wu         | Finance   |   90000 |
| Physics   |   76543 | Singh      | Finance   |   80000 |
|           |   32343 | El Said    | History   |   60000 |
|           |   58583 | Califieri  | History   |   62000 |
|           |   15151 | Mozart     | Music     |   40000 |
|           |   22222 | Einstein   | Physics   |   95000 |
|           |   33465 | Gold       | Physics   |   87000 |

![Image](Lecture 9.1_artifacts/image_000015_bbaa640f2b7c7b6f18cdf441c797dcf1ce99e755b6ef0a9bbf7b581538bddcab.png)

## Module 41

Partha Pratim Das

Week Recap

Objectives &amp;

Outline

Indexing

Metrics

Ordered Indices

Dense Index Files

Sparse Index Files

Primary and

Secondary Indices

Multilevel Index

Index Update

Module Summary

## Sparse Index Files

- Sparse Index : contains index records for only some search-key values.
- Applicable when records are sequentially ordered on search-key
- To locate a record with search-key value K we:
- Find index record with largest search-key value &lt; K
- Search file sequentially starting at the record to which the index record points

![Image](Lecture 9.1_artifacts/image_000016_236d8f184448ca180331190b09c1983f1059efbc799b7048ff7e912561242200.png)

## Database Management Systems

Partha Pratim Das

![Image](Lecture 9.1_artifacts/image_000017_bbaa640f2b7c7b6f18cdf441c797dcf1ce99e755b6ef0a9bbf7b581538bddcab.png)

## Module 41

Partha Pratim Das

Week Recap

Objectives &amp; Outline

Indexing

Metrics

Ordered Indices

Dense Index Files

Sparse Index Files

Primary and

Secondary Indices

Multilevel Index

Index Update

Module Summary

## Sparse Index Files (2)

- Compared to dense indices:
- Less space and less maintenance overhead for insertions and deletions
- Generally slower than dense index for locating records
- Good tradeoff : sparse index with an index entry for every block in file, corresponding to least search-key value in the block

![Image](Lecture 9.1_artifacts/image_000018_bba5e5e4f70e932f1d11ff82a3ef33436b7a418157fec2882f04c51592fd31a1.png)

Partha Pratim Das

![Image](Lecture 9.1_artifacts/image_000019_bbaa640f2b7c7b6f18cdf441c797dcf1ce99e755b6ef0a9bbf7b581538bddcab.png)

## Secondary Indices Example

![Image](Lecture 9.1_artifacts/image_000020_42cd2bf3ef9560f31251c956daa747d78f6c07b58b4b2a85d14dbfb762ed4c84.png)

![Image](Lecture 9.1_artifacts/image_000021_0d9dfbde1de846c018eea32fe6aba21e8a9c7f3c69ef770101468a6cfb66a6e5.png)

## Module 41

Partha Pratim Das

Week Recap

Objectives &amp; Outline

Indexing

Metrics

Ordered Indices

Dense Index Files

Sparse Index Files

Primary and Secondary Indices

Multilevel Index

Index Update

Module Summary

## Primary and Secondary Indices

- Indices offer substantial benefits when searching for records
- BUT: Updating indices imposes overhead on database modification -when a file is modified, every index on the file must be updated
- Sequential scan using primary index is efficient, but a sequential scan using a secondary index is expensive
- Each record access may fetch a new block from disk
- Block fetch requires about 5 to 10 milliseconds, versus about 100 nanoseconds for memory access

![Image](Lecture 9.1_artifacts/image_000022_0d9dfbde1de846c018eea32fe6aba21e8a9c7f3c69ef770101468a6cfb66a6e5.png)

## Module 41

Partha Pratim Das

Week Recap

Objectives &amp; Outline

Indexing

Metrics

Ordered Indices

Dense Index Files

Sparse Index Files

Primary and Secondary Indices

Multilevel Index

Index Update

Module Summary

## Multilevel Index

- If primary index does not fit in memory, access becomes expensive
- Solution: treat primary index kept on disk as a sequential file and construct a sparse index on it
- outer index - a sparse index of primary index
- inner index - the primary index file
- If even outer index is too large to fit in main memory, yet another level of index can be created, and so on
- Indices at all levels must be updated on insertion or deletion from the file

![Image](Lecture 9.1_artifacts/image_000023_bbaa640f2b7c7b6f18cdf441c797dcf1ce99e755b6ef0a9bbf7b581538bddcab.png)

![Image](Lecture 9.1_artifacts/image_000024_895d9b9493f1faf22bbfd8ec98777793758937a9081be505611fa64490160db2.png)

![Image](Lecture 9.1_artifacts/image_000025_ff079708b8618ebf0a8a3ad3f1c206ec2c2ca07ff9b82b9c9fe89663a41596ba.png)

![Image](Lecture 9.1_artifacts/image_000026_0d9dfbde1de846c018eea32fe6aba21e8a9c7f3c69ef770101468a6cfb66a6e5.png)

## Module 41

Partha Pratim Das

Week Recap

Objectives &amp; Outline

Indexing

Metrics

Ordered Indices

Dense Index Files

Sparse Index Files

Primary and

Secondary Indices

Multilevel Index

Index Update

Module Summary

## Index Update: Deletion

- If deleted record was the only record in the file with its particular search-key value, the searchkey is deleted from the index also.
- Single-level index entry deletion :
- Dense indices - deletion of search-key is similar to file record deletion
- Sparse indices -
- glyph[triangleright] If an entry for the search key exists in the index, it is deleted by replacing the entry in the index with the next search-key value in the file (in search-key order)
- glyph[triangleright] If the next search-key value already has an index entry, the entry is deleted instead of being replaced

![Image](Lecture 9.1_artifacts/image_000027_6dc9e7a6958a8047057c3e42aa03629e3873b82fcb68fad0d6c3279550a9daea.png)

![Image](Lecture 9.1_artifacts/image_000028_0d9dfbde1de846c018eea32fe6aba21e8a9c7f3c69ef770101468a6cfb66a6e5.png)

## Module 41

Partha Pratim Das

Week Recap

Objectives &amp; Outline

Indexing

Metrics

Ordered Indices

Dense Index Files

Sparse Index Files

Primary and

Secondary Indices

Multilevel Index

Index Update

Module Summary

## Index Update (2): Insertion

- Single-level index insertion :
- Perform a lookup using the search-key value appearing in the record to be inserted
- Dense indices - if the search-key value does not appear in the index, insert it
- Sparse indices - if index stores an entry for each block of the file, no change needs to be made to the index unless a new block is created
- glyph[triangleright] If a new block is created, the first search-key value appearing in the new block is inserted into the index
- Multilevel insertion and deletion : algorithms are simple extensions of the single-level algorithms

![Image](Lecture 9.1_artifacts/image_000029_bbaa640f2b7c7b6f18cdf441c797dcf1ce99e755b6ef0a9bbf7b581538bddcab.png)

## Module 41

Partha Pratim Das

Week Recap

Objectives &amp; Outline

Indexing

Metrics

Ordered Indices Dense Index Files Sparse Index Files Primary and Secondary Indices

Multilevel Index

Index Update

Module Summary

## Secondary Indices

- Frequently, one wants to find all the records whose values in a certain field (which is not the search-key of the primary index) satisfy some condition
- Example 1: In the instructor relation stored sequentially by ID, we may want to find all instructors in a particular department
- Example 2: as above, but where we want to find all instructors with a specified salary or with salary in a specified range of values
- We can have a secondary index with an index record for each search-key value

![Image](Lecture 9.1_artifacts/image_000030_0d9dfbde1de846c018eea32fe6aba21e8a9c7f3c69ef770101468a6cfb66a6e5.png)

## Module 41

Partha Pratim Das

Week Recap

Objectives &amp; Outline

Indexing

Metrics

Ordered Indices Dense Index Files Sparse Index Files Primary and Secondary Indices Multilevel Index Index Update

Module Summary

## Module Summary

- Appreciated the reasons for indexing database tables
- Understood the ordered indexes

Slides used in this presentation are borrowed from http://db-book.com/ with kind permission of the authors. Edited and new slides are marked with 'PPD'.
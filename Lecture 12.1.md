<!-- image -->

## Module 56

Partha Pratim Das

Week Recap

Objectives &amp; Outline

Query Processing

Query Cost

Selection

Operation

Complex Selections

Sorting

External Sort-Merge

Join Operation

Other Operations

Module Summary

Database Management Systems

## Database Management Systems

Module 56: Query Processing and Optimization/1: Processing

## Partha Pratim Das

Department of Computer Science and Engineering Indian Institute of Technology, Kharagpur ppd@cse.iitkgp.ac.in

Partha Pratim Das

<!-- image -->

## Module 56

Partha Pratim Das

Week Recap

Objectives &amp; Outline

Query Processing

Query Cost

Selection

Operation

Complex Selections

Sorting

External Sort-Merge

Join Operation

Other Operations

Module Summary

## Week Recap

- Learnt the importance of backup an analysed different backup strategies
- Failures may be due to variety of sources - each needs a strategy for handling
- A proper mix and management of volatile, non-volatile and stable storage can guarantee recovery from failures and ensure Atomicity, Consistency and Durability
- Log-based recovery is efficient and effective
- Learnt how Hot backup of transaction log helps in recovering consistent database.
- Studied the recovery algorithms for concurrent transactions
- Recovery based on operation logging supplements log-based recovery
- Planning for Backup
- Understood RAID - array of redundant disks in parallel to enhance speed and reliability

## Partha Pratim Das

<!-- image -->

## Module 56

Partha Pratim Das

Week Recap

Objectives &amp; Outline

Query Processing

Query Cost

Selection

Operation

Complex Selections

Sorting

External Sort-Merge

Join Operation

Other Operations

Module Summary

## Module Objectives

- To understand the overall flow for Query Processing
- To define the Measures of Query Cost
- To understand the algorithms for processing Selection Operations, Sorting, Join Operations, and a few Other Operations

<!-- image -->

## Module 56

Partha Pratim Das

Week Recap

Objectives &amp; Outline

Query Processing

Query Cost

Selection Operation Complex Selections

Sorting

External Sort-Merge

Join Operation

Other Operations

Module Summary

## Module Outline

- Overview of Query Processing
- Measures of Query Cost
- Selection Operation
- Sorting
- Join Operation
- Other Operations

<!-- image -->

Module 56

Partha Pratim Das

Week Recap

Objectives &amp;

Outline

Query Processing

Query Cost

Selection

Operation

Complex Selections

Sorting

External Sort-Merge

Join Operation

Other Operations

Module Summary

## Overview of Query Processing

## Overview of Query Processing

<!-- image -->

Module 56

Partha Pratim

Das

Week Recap

Objectives &amp;

Outline

Query Processing

Query Cost

Selection

Operation

Complex Selections

Sorting

External Sort-Merge

Join Operation

Other Operations

Module Summary

## Basic Steps in Query Processing

- a) Parsing and translation
- b) Optimization
- c) Evaluation

Database Management Systems

<!-- image -->

Partha Pratim Das

<!-- image -->

Module 56

Partha Pratim Das

Week Recap

Objectives &amp; Outline

Query Processing

Query Cost

Selection

Operation

Complex Selections

Sorting

External Sort-Merge

Join Operation

Other Operations

Module Summary

## Basic Steps in Query Processing (2)

- Parsing and translation
- translate the query into its internal form
- glyph[triangleright] This is then translated into relational algebra
- Parser checks syntax, verifies relations
- Evaluation
- The query-execution engine takes a query-evaluation plan, executes that plan, and returns the answers to the query

<!-- image -->

## Module 56

Partha Pratim Das

Week Recap

Objectives &amp; Outline

Query Processing

Query Cost

Selection

Operation

Complex Selections

Sorting

External Sort-Merge

Join Operation

Other Operations

Module Summary

## Basic Steps in Query Processing (3): Optimization

- Consider the query

select salary from instructor where salary &lt; 75000;

which can be translated into either of the following relational-algebra expressions:

- σ salary &lt; 75000 (Π salary ( instructor ))
- Π salary ( σ salary &lt; 75000 ( instructor ))
- Each relational algebra operation can be evaluated using one of several different algorithms
- Correspondingly, a relational-algebra expression can be evaluated in many ways
- Annotated expression specifying detailed evaluation strategy is called an evaluation-plan .
- For example, can use an index on salary to find instructors with salary &lt; 75000, ◦ or can perform complete relation scan and discard instructors with salary ≥ 75000

## Partha Pratim Das

<!-- image -->

## Module 56

Partha Pratim Das

Week Recap

Objectives &amp; Outline

Query Processing

Query Cost

Selection

Operation

Complex Selections

Sorting

External Sort-Merge

Join Operation

Other Operations

Module Summary

## Basic Steps in Query Processing (4): Optimization

- Query Optimization : Amongst all equivalent evaluation plans choose the one with lowest cost
- Cost is estimated using statistical information from the database catalog
- glyph[triangleright] For example, number of tuples in each relation, size of tuples, etc.
- In this module we study
- How to measure query costs
- Algorithms for evaluating relational algebra operations
- How to combine algorithms for individual operations in order to evaluate a complete expression
- In the next module
- We study how to optimize queries, that is, how to find an evaluation plan with lowest estimated cost

## Partha Pratim Das

<!-- image -->

Module 56

Partha Pratim Das

Week Recap

Objectives &amp; Outline

Query Processing

Query Cost

Selection

Operation

Complex Selections

Sorting

External Sort-Merge

Join Operation

Other Operations

Module Summary

## Measures of Query Cost

## Measures of Query Cost

<!-- image -->

## Module 56

Partha Pratim Das

Week Recap

Objectives &amp; Outline

Query Processing

Query Cost

Selection

Operation

Complex Selections

Sorting

External Sort-Merge

Join Operation

Other Operations

Module Summary

## Measures of Query Cost

- Cost is generally measured as total elapsed time for answering query
- Many factors contribute to time cost
- glyph[triangleright] disk accesses, CPU, or even network communication
- Typically disk access is the predominant cost, and is also relatively easy to estimate
- Measured by taking into account
- Number of seeks * average-seek-cost
- Number of blocks read * average-block-read-cost
- Number of blocks written * average-block-write-cost
- glyph[triangleright] Cost to write a block is greater than cost to read a block
- -data is read back after being written to ensure that the write was successful

<!-- image -->

Module 56

Partha Pratim Das

Week Recap

Objectives &amp; Outline

Query Processing

Query Cost

Selection

Operation

Complex Selections

Sorting

External Sort-Merge

Join Operation

Other Operations

Module Summary

## Measures of Query Cost (2)

- For simplicity we just use the number of block transfers from disk and the number of seeks as the cost measures
- t T : time to transfer one block
- t S : time for one seek
- Cost for b block transfers plus S seeks

<!-- formula-not-decoded -->

- We ignore CPU costs for simplicity
- Real systems do take CPU cost into account
- We do not include cost to writing output to disk in our cost formulae

<!-- image -->

## Module 56

Partha Pratim Das

Week Recap

Objectives &amp; Outline

Query Processing

Query Cost

Selection Operation Complex Selections

Sorting

External Sort-Merge

Join Operation

Other Operations

Module Summary

## Measures of Query Cost (3)

- Several algorithms can reduce disk IO by using extra buffer space
- Amount of real memory available to buffer depends on other concurrent queries and OS processes, known only during execution
- glyph[triangleright] We often use worst case estimates, assuming only the minimum amount of memory needed for the operation is available
- Required data may be buffer resident already, avoiding disk I/O
- But hard to take into account for cost estimation

<!-- image -->

## Module 56

Partha Pratim Das

Week Recap

Objectives &amp; Outline

Query Processing

Query Cost

Selection Operation

Complex Selections

Sorting

External Sort-Merge

Join Operation

Other Operations

Module Summary

## Selection Operation

## Selection Operation

<!-- image -->

Module 56

Partha Pratim

Das

Week Recap

Objectives &amp;

Outline

Query Processing

Query Cost

Selection

Operation

Complex Selections

Sorting

External Sort-Merge

Join Operation

Other Operations

Module Summary

## Selection Operation: File / Index Scan

| A#   | Algorithm                 | Cost                            | Reason                                                                                                                                                                                                             |
|------|---------------------------|---------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| A1   | Linear Search             | tS + br × tT                    | One initial seek plus br block transfers                                                                                                                                                                           |
| A1   | Linear Search, Eq. on Key | Average case tS +( br / 2) × tT | Since at most one record satisfies condition, scan can be terminated as soon as the required record is found. br blocks transfers in worst case                                                                    |
| A2   | Prm. Index, Eq. on Key    | ( hi +1) × ( tT + tS )          | Index lookup traverses the height of the tree plus one I/O to fetch the record; each of these I/O operations requires a seek and a block transfer                                                                  |
| A3   | Prm. Index, Eq. on Nonkey | hi × ( tT + tS )+ b × tT        | One seek for each level of the tree, one seek for the first block. Here all of b are read. These blocks are leaf blocks assumed to be stored sequentially (for a primary index) and don't require additional seeks |
| A4   | Snd. Index, Eq. on Key    | ( hi +1) × ( tT + tS )          | This case is similar to primary index                                                                                                                                                                              |
| A4   | Snd. Index, Eq. on Nonkey | ( hi + n ) × ( tT + tS )        | Here, cost of index traversal is the same as for A 3, but each record may be on a different block, requiring a seek per record. Cost is potentially very high if n is large                                        |
| A5   | Prm. Index, Comparison    | hi × ( tT + tS )+ b × tT        | Identical to the case of A 3, equality on nonkey                                                                                                                                                                   |
| A6   | Snd. Index, Comparison    | ( hi + n ) × ( tT + tS )        | Identical to the case of A 4, equality on nonkey                                                                                                                                                                   |

- tT is time to transfer one block. tS is time for one seek
- br denotes the number of blocks in the file
- b denotes the number of blocks containing records with the specified search key
- hi denotes the height of the index. n is the number of records fetched

<!-- image -->

Module 56

Partha Pratim Das

Week Recap

Objectives &amp; Outline

Query Processing

Query Cost

Selection Operation

Complex Selections

Sorting

External Sort-Merge

Join Operation

Other Operations

Module Summary

## Complex Selections: Conjunction

- Conjunction :

σ θ 1 ∧ θ 2 ∧ ...θ n (r)

- A7 ( conjunctive selection using one index )
- Select a combination of θ i and algorithms A1 through A6 that results in the least cost for σ θ i (r)
- Test other conditions on tuple after fetching it into memory buffer
- A8 ( conjunctive selection using composite index )
- Use appropriate composite (multiple-key) index if available
- A9 ( conjunctive selection by intersection of identifiers )
- Requires indices with record pointers
- Use corresponding index for each condition, and take intersection of all the obtained sets of record pointers
- Then fetch records from file
- If some conditions do not have appropriate indices, apply test in memory

Partha Pratim Das

<!-- image -->

## Module 56

Partha Pratim Das

Week Recap

Objectives &amp; Outline

Query Processing

Query Cost

Selection Operation

Complex Selections

Sorting

External Sort-Merge

Join Operation

Other Operations

Module Summary

## Complex Selections: Disjunction

- Disjunction : σ θ 1 ∨ θ 2 ∨ ...θ n (r).
- A10 ( disjunctive selection by union of identifiers )
- Applicable if all conditions have available indices
- glyph[triangleright] Otherwise use linear scan
- Use corresponding index for each condition, and take union of all the obtained sets of record pointers
- Then fetch records from file
- Negation : σ ¬ θ (r)
- Use linear scan on file
- If very few records satisfy ¬ θ , and an index is applicable to θ
- glyph[triangleright] Find satisfying records using index and fetch from file

<!-- image -->

## Module 56

Partha Pratim

Das

Week Recap

Objectives &amp;

Outline

Query Processing

Query Cost

Selection

Operation

Complex Selections

Sorting

External Sort-Merge

Join Operation

Other Operations

Module Summary

## Sorting

## Sorting

<!-- image -->

Module 56

Partha Pratim Das

Week Recap

Objectives &amp; Outline

Query Processing

Query Cost

Selection

Operation

Complex Selections

Sorting

External Sort-Merge

Join Operation

Other Operations

Module Summary

## Sorting

- We may build an index on the relation , and then use the index to read the relation in sorted order
- May lead to one disk block access for each tuple
- For relations that fit in memory, techniques like quicksort can be used
- For relations that do not fit in memory, external sort-merge is a good choice

<!-- image -->

Module 56

Partha Pratim

Das

Week Recap

Objectives &amp;

Outline

Query Processing

Query Cost

Selection

Operation

Complex Selections

Sorting

External Sort-Merge

Join Operation

Other Operations

Module Summary

## External Sort-Merge: Example

Database Management Systems

<!-- image -->

Partha Pratim Das

<!-- image -->

Module 56

Partha Pratim Das

Week Recap

Objectives &amp; Outline

Query Processing

Query Cost

Selection

Operation

Complex Selections

Sorting

External Sort-Merge

Join Operation

Other Operations

Module Summary

## External Sort-Merge: Algorithm

- a) Create sorted runs . Let M denote the number of blocks in the main-memory buffer available for sorting. First, a number of sorted runs are created; each run is sorted, but contains only some of the records of the relation.

i =

0;

repeat or the rest of the relation, whichever is smaller;

read M blocks of the relation, sort the in-memory part of the relation; write the sorted data to run file Ri; i = i + 1;

until the end of the relation

- b) Merge the runs (N-way merge) : Now, the runs are merged. For the total number of runs, N &lt; M , so that we can allocate one block to each run and have space left to hold one block of output. The merge stage operates as follows:

read one block of each of the N files Ri into a buffer block in memory; repeat choose the first tuple (in sort order) among all buffer blocks; write the tuple to the output, and delete it from the buffer block; if the buffer block of any run Ri is empty and not end-of-file(Ri) then read the next block of Ri into the buffer block;

until all input buffer blocks are empty

- c) If N ≥ M , several merge passes are required
- In each pass, contiguous groups of M -1 runs are merged.
- A pass reduces the number of runs by a factor of M -1, and creates runs longer by the same factor
- For M =11 and 90 runs, one pass reduces the number of runs to 9, each 10 times the size of the initial runs
- Repeated passes are performed till all runs have been merged into one Database Management Systems Partha Pratim Das

<!-- image -->

## Module 56

Partha Pratim Das

Week Recap

Objectives &amp; Outline

Query Processing

Query Cost

Selection

Operation

Complex Selections

Sorting External Sort-Merge

Join Operation

Other Operations

Module Summary

## Join Operation

## Join Operation

<!-- image -->

<!-- image -->

## Module 56

Partha Pratim Das

Week Recap

Objectives &amp; Outline

Query Processing

Query Cost

Selection

Operation

Complex Selections

Sorting

External Sort-Merge

Join Operation

Other Operations

Module Summary

## Join Operation

- Several different algorithms to implement joins
- Nested-loop join
- Block nested-loop join
- Indexed nested-loop join
- Merge-join
- Hash-join
- Choice based on cost estimate
- Examples use the following information
- Number of records of student : n students = 5,000
- Number of records of takes : n takes = 10,000
- Number of blocks of student : b students = 100
- Number of blocks of takes : b takes = 400

<!-- image -->

## Module 56

Partha Pratim Das

Week Recap

Objectives &amp; Outline

Query Processing

Query Cost

Selection

Operation

Complex Selections

Sorting External Sort-Merge

Join Operation

Other Operations

Module Summary

## Nested-Loop Join

- To compute the theta join r glyph[triangleright] glyph[triangleleft] θ s for each tuple t r in r do begin for each tuple t s in s do begin test pair ( t r , t s ) to see if they satisfy the join condition θ if they do, add t r · t s to the result. end

end

- r is called the outer relation and s the inner relation of the join
- Requires no indices and can be used with any kind of join condition
- Expensive since it examines every pair of tuples in the two relations

<!-- image -->

Module 56

Partha Pratim Das

Week Recap

Objectives &amp; Outline

Query Processing

Query Cost

Selection Operation

Complex Selections

Sorting

External Sort-Merge

Join Operation

Other Operations

Module Summary

## Nested-Loop Join (2)

- In the worst case, if there is enough memory only to hold one block of each relation, the estimated cost is nr ∗ bs + br block transfers, plus nr + br seeks, where nr ( ns ) denotes the number of tuples in r ( s ) and br ( bs ) denotes the number of blocks containing tuples of in r ( s )
- If the smaller relation fits entirely in memory, use that as the inner relation.
- Reduces cost to br + bs block transfers and 2 seeks
- Example of join of students and takes : nstudents = 5,000, ntakes = 10,000, bstudents = 100, btakes = 400
- Assuming worst case memory availability cost estimate is
- with student as outer relation:
- 5000 * 400 + 100 = 2,000,100 block transfers,
- glyph[triangleright] glyph[triangleright] 5000 + 100 = 5100 seeks
- with takes as the outer relation
- glyph[triangleright] 10000 * 100 + 400 = 1,000,400 block transfers and 10,400 seeks
- If smaller relation ( student ) fits entirely in memory, the cost estimate will be 500 block transfers
- Block nested-loops algorithm is preferable

Database Management Systems

<!-- image -->

Module 56

Partha Pratim Das

Week Recap

Objectives &amp; Outline

Query Processing

Query Cost

Selection

Operation

Complex Selections

Sorting

External Sort-Merge

Join Operation

Other Operations

Module Summary

## Block Nested-Loop Join

- Variant of nested-loop join in which every block of inner relation is paired with every block of outer relation

for each block

B

r

of

r

do begin for each

block

B

s

of

s

do begin for each

tuple

t

r

in

B

r

do begin for each tuple t s in B s do begin

Check if (

t

r

,

t

s

) satisfy the join condition if they do, add

t

r

•

t

s

to the result.

end end

end end

<!-- image -->

Module 56

Partha Pratim Das

Week Recap

Objectives &amp; Outline

Query Processing

Query Cost

Selection

Operation

Complex Selections

Sorting

External Sort-Merge

Join Operation

Other Operations

Module Summary

## Block Nested-Loop Join (2)

- Worst case estimate: br ∗ bs + br block transfers + 2 * br seeks
- Each block in the inner relation s is read once for each block in the outer relation
- Best case: br + bs block transfers + 2 seeks.
- Improvements to nested loop and block nested loop algorithms:
- In block nested-loop, use M -2 disk blocks as blocking unit for outer relations, where M = memory size in blocks; use remaining two blocks to buffer inner relation and output
- glyph[triangleright] Cost = glyph[ceilingleft] br / ( M -2) glyph[ceilingright] ∗ bs + br block transfers +2 ∗ glyph[ceilingleft] br / ( M -2) glyph[ceilingright] seeks
- If equi-join attribute forms a key or inner relation, stop inner loop on first match
- Scan inner loop forward and backward alternately, to make use of the blocks remaining in buffer (with LRU replacement)
- Use index on inner relation, if available

<!-- image -->

## Module 56

Partha Pratim Das

Week Recap

Objectives &amp; Outline

Query Processing

Query Cost

Selection Operation

Complex Selections

Sorting

External Sort-Merge

Join Operation

Other Operations

Module Summary

## Indexed Nested-Loop Join

- Index lookups can replace file scans if
- join is an equi-join or natural join and
- an index is available on the inner relation's join attribute
- glyph[triangleright] Can construct an index just to compute a join.
- For each tuple tr in the outer relation r , use the index to look up tuples in s that satisfy the join condition with tuple tr .
- Worst case: buffer has space for only one page of r , and, for each tuple in r , we perform an index lookup on s .
- Cost of the join: br × ( t T + t S ) + nr ∗ c
- Where c is the cost of traversing index and fetching all matching s tuples for one tuple or r
- c can be estimated as cost of a single selection on s using the join condition.
- If indices are available on join attributes of both r and s , use the relation with fewer tuples as the outer relation.

<!-- image -->

## Module 56

Partha Pratim Das

Week Recap

Objectives &amp; Outline

Query Processing

Query Cost

Selection

Operation

Complex Selections

Sorting

External Sort-Merge

Join Operation

Other Operations

Module Summary

## Example of Nested-Loop Join Costs

- Compute student glyph[multicloseright] glyph[multicloseleft] takes , with student as the outer relation.
- Let takes have a primary B + -tree index on the attribute ID , which contains 20 entries in each index node.
- Since takes has 10,000 tuples, the height of the tree is 4, and one more access is needed to find the actual data
- student has 5000 tuples
- Cost of block nested loops join
- 400*100 + 100 = 40,100 block transfers + 2 * 100 = 200 seeks
- glyph[triangleright] assuming worst case memory
- glyph[triangleright] may be significantly less with more memory
- Cost of indexed nested loops join
- 100 + 5000 * 5 = 25,100 block transfers and seeks.
- CPU cost likely to be less than that for block nested loops join

<!-- image -->

## Module 56

Partha Pratim Das

Week Recap

Objectives &amp; Outline

Query Processing

Query Cost

Selection

Operation

Complex Selections

Sorting

External Sort-Merge

Join Operation

Other Operations

Module Summary

## Other Operations

## Other Operations

<!-- image -->

<!-- image -->

Module 56

Partha Pratim Das

Week Recap

Objectives &amp; Outline

Query Processing

Query Cost

Selection Operation Complex Selections

Sorting

External Sort-Merge

Join Operation

Other Operations

Module Summary

## Other Operations

- Duplicate Elimination
- Projection
- Aggregation
- Set Operations
- Outer Join

<!-- image -->

Module 56

Partha Pratim Das

Week Recap

Objectives &amp; Outline

Query Processing

Query Cost

Selection

Operation

Complex Selections

Sorting

External Sort-Merge

Join Operation

Other Operations

Module Summary

## Other Operations: Duplicate Elimination &amp; Projection

- Duplicate Elimination can be implemented via hashing or sorting
- On sorting duplicates will come adjacent to each other, and all but one set of duplicates can be deleted
- Optimization : duplicates can be deleted during run generation as well as at intermediate merge steps in external sort-merge
- Hashing is similar - duplicates will come into the same bucket

## · Projection :

- perform projection on each tuple
- followed by duplicate elimination

<!-- image -->

Module 56

Partha Pratim Das

Week Recap

Objectives &amp; Outline

Query Processing

Query Cost

Selection Operation Complex Selections

Sorting

External Sort-Merge

Join Operation

Other Operations

Module Summary

## Other Operations: Aggregation

- Aggregation can be implemented in a manner similar to duplicate elimination
- Sorting or hashing can be used to bring tuples in the same group together, and then the aggregate functions can be applied on each group
- Optimization : combine tuples in the same group during run generation and intermediate merges, by computing partial aggregate values
- glyph[triangleright] For count, min, max, sum: keep aggregate values on tuples found so far in the group
- -When combining partial aggregate for count, add up the aggregates
- glyph[triangleright] For avg, keep sum and count, and divide sum by count at the end

<!-- image -->

Module 56

Partha Pratim Das

Week Recap

Objectives &amp; Outline

Query Processing

Query Cost

Selection

Operation

Complex Selections

Sorting

External Sort-Merge

Join Operation

Other Operations

Module Summary

## Module Summary

- Understood the overall flow for Query Processing and defined the Measures of Query Cost
- Studied the algorithms for processing Selection Operations, Sorting, Join Operations and a few Other Operations

Slides used in this presentation are borrowed from http://db-book.com/ with kind permission of the authors.

Edited and new slides are marked with 'PPD'.

Database Management Systems

Partha Pratim Das

56.34
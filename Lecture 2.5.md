![Image](Lecture 2.5_artifacts/image_000000_bbaa640f2b7c7b6f18cdf441c797dcf1ce99e755b6ef0a9bbf7b581538bddcab.png)

## Module 10

Partha Pratim Das

Objectives &amp; Outline

Set Operations

Null Values

Three Valued Logic

Aggregate Functions

Group By

Having

Null Values

Module Summary

## Database Management Systems

Module 10: Introduction to SQL/3

## Partha Pratim Das

Department of Computer Science and Engineering Indian Institute of Technology, Kharagpur ppd@cse.iitkgp.ac.in

Partha Pratim Das

![Image](Lecture 2.5_artifacts/image_000001_821f32da21a8bb9af0bddb9e2ff2419e915ba7e461f5dc4f05b60eaa6ed0b478.png)

## Module 10

Partha Pratim Das

Objectives &amp; Outline

Set Operations

Null Values

Three Valued Logic

Aggregate

Functions

Group By

Having

Null Values

Module Summary

## Module Recap

- Completed the understanding of basic query structure

![Image](Lecture 2.5_artifacts/image_000002_821f32da21a8bb9af0bddb9e2ff2419e915ba7e461f5dc4f05b60eaa6ed0b478.png)

Module 10

Partha Pratim Das

Objectives &amp; Outline

Set Operations

Null Values

Three Valued Logic

Aggregate

Functions

Group By

Having

Null Values

Module Summary

## Module Objectives

- To familiarize with set operations, null values and aggregation

![Image](Lecture 2.5_artifacts/image_000003_0d9dfbde1de846c018eea32fe6aba21e8a9c7f3c69ef770101468a6cfb66a6e5.png)

## Module 10

Partha Pratim Das

## Objectives &amp; Outline

Set Operations

Null Values

Three Valued Logic

Aggregate Functions

Group By

Having

Null Values

Module Summary

## Module Outline

- Set Operations: union, intersect, except
- Null Values
- Aggregate Functions: avg, min, max, sum, and count
- Group By
- Having
- Null Values

![Image](Lecture 2.5_artifacts/image_000004_fde1132bf222cc20a3e76fd9bad23db921b22024804914407d2f2bc1b513e47e.png)

## Module 10

Partha Pratim Das

Objectives &amp; Outline

Set Operations

Null Values

Three Valued Logic

Aggregate Functions

Group By

Having

Null Values

Module Summary

## Set Operations

## Set Operations

![Image](Lecture 2.5_artifacts/image_000005_bbaa640f2b7c7b6f18cdf441c797dcf1ce99e755b6ef0a9bbf7b581538bddcab.png)

## Module 10

Partha Pratim Das

Objectives &amp; Outline

Set Operations

Null Values

Three Valued Logic

Aggregate Functions

Group By

Having

Null Values

Module Summary

## Set Operations

- Find courses that ran in Fall 2009 or in Spring 2010

( select course id from section where sem = 'Fall' and year = 2009) union

( select course id from section where sem = 'Spring' and year = 2010)

- Find courses that ran in Fall 2009 and in Spring 2010

( select course id from section where sem = 'Fall' and year = 2009) intersect

( select course id from section where sem = 'Spring' and year = 2010)

- Find courses that ran in Fall 2009 but not in Spring 2010

( select course id from section where sem = 'Fall' and year = 2009) except

( select course id from section where sem = 'Spring' and year = 2010)

## Partha Pratim Das

![Image](Lecture 2.5_artifacts/image_000006_bbaa640f2b7c7b6f18cdf441c797dcf1ce99e755b6ef0a9bbf7b581538bddcab.png)

## Module 10

Partha Pratim Das

Objectives &amp; Outline

Set Operations

Null Values

Three Valued Logic

Aggregate Functions

Group By

Having

Null Values

Module Summary

## Set Operations (2)

- Find the salaries of all instructors that are less than the largest salary
- select distinct T . salary from instructor as T , instructor as S where T . salary &lt; S . salary
- Find all the salaries of all instructors select distinct salary

from instructor

- Find the largest salary of all instructors
- ( select 'second query' ) except ( select 'first query')

![Image](Lecture 2.5_artifacts/image_000007_bbaa640f2b7c7b6f18cdf441c797dcf1ce99e755b6ef0a9bbf7b581538bddcab.png)

## Module 10

Partha Pratim Das

Objectives &amp; Outline

Set Operations

Null Values

Three Valued Logic

Aggregate Functions

Group By

Having

Null Values

Module Summary

## Set Operations (3)

- Set operations union , intersect , and except
- Each of the above operations automatically eliminates duplicates
- To retain all duplicates use the corresponding multiset versions union all , intersect all , and except all .
- Suppose a tuple occurs m times in r and n times in s , then, it occurs:
- m + n times in r union all s
- min( m , n ) times in r intersect all s
- max(0, m -n ) times in r except all s

![Image](Lecture 2.5_artifacts/image_000008_0d2e8daa05c74407b310229f101057782122d2bf078613dc8c643ca2fdb280b5.png)

## Module 10

Partha Pratim Das

Objectives &amp; Outline

Set Operations

Null Values

Three Valued Logic

Aggregate Functions

Group By

Having

Null Values

Module Summary

## Null Values

## Null Values

![Image](Lecture 2.5_artifacts/image_000009_0d9dfbde1de846c018eea32fe6aba21e8a9c7f3c69ef770101468a6cfb66a6e5.png)

## Module 10

Partha Pratim Das

Objectives &amp; Outline

Set Operations

Null Values

Three Valued Logic

Aggregate Functions

Group By

Having

Null Values

Module Summary

## Null Values

- It is possible for tuples to have a null value, denoted by null , for some of their attributes
- null signifies an unknown value or that a value does not exist
- The result of any arithmetic expression involving null is null
- Example: 5 + null returns null
- The predicate is null can be used to check for null values
- Example: Find all instructors whose salary is null
- select name from instructor

where salary is null

- It is not possible to test for null values with comparison operators, such as =, &lt; , or &lt;&gt; We need to use the is null and is not null operators instead

![Image](Lecture 2.5_artifacts/image_000010_0d9dfbde1de846c018eea32fe6aba21e8a9c7f3c69ef770101468a6cfb66a6e5.png)

## Module 10

Partha Pratim Das

Objectives &amp; Outline

Set Operations

Null Values

Three Valued Logic

Aggregate Functions

Group By

Having

Null Values

Module Summary

## Null Values (2): Three Valued Logic

- Three values true, false, unknown
- Any comparison with null returns unknown
- Example: 5 &lt; null or null &lt;&gt; null or null = null
- Three-valued logic using the value unknown:
- OR: ( unknown or true ) = true , ( unknown or false ) = unknown ( unknown or unknown ) = unknown
- AND: ( true and unknown ) = unknown , ( false and unknown ) = false , ( unknown and unknown ) = unknown
- NOT: ( not unknown ) = unknown
- ' P is unknown ' evaluates to true if predicate P evaluates to unknown
- Result of where clause predicate is treated as false if it evaluates to unknown

![Image](Lecture 2.5_artifacts/image_000011_fde1132bf222cc20a3e76fd9bad23db921b22024804914407d2f2bc1b513e47e.png)

## Module 10

Partha Pratim Das

Objectives &amp; Outline

Set Operations

Null Values

Three Valued Logic

Aggregate Functions

Group By

Having

Null Values

Module Summary

## Aggregate Functions

## Aggregate Functions

![Image](Lecture 2.5_artifacts/image_000012_6d6676798107c57180074306c98b4bdadd9bf0b823b5ad2520b501da94360fb4.png)

![Image](Lecture 2.5_artifacts/image_000013_0d9dfbde1de846c018eea32fe6aba21e8a9c7f3c69ef770101468a6cfb66a6e5.png)

## Module 10

Partha Pratim Das

Objectives &amp; Outline

Set Operations

Null Values

Three Valued Logic

Aggregate Functions

Group By

Having

Null Values

Module Summary

## Aggregate Functions

- These functions operate on the multiset of values of a column of a relation, and return a value

avg :

average value

min

: minimum value

max

: maximum value

sum :

sum of values

count

: number of values

![Image](Lecture 2.5_artifacts/image_000014_0d9dfbde1de846c018eea32fe6aba21e8a9c7f3c69ef770101468a6cfb66a6e5.png)

## Module 10

Partha Pratim Das

Objectives &amp; Outline

Set Operations

Null Values

Three Valued Logic

Aggregate Functions

Group By

Having

Null Values

Module Summary

## Aggregate Functions (2)

- Find the average salary of instructors in the Computer Science department
- select avg ( salary )
- from instructor where dept name = 'Comp. Sci';
- Find the total number of instructors who teach a course in the Spring 2010 semester select count (distinct ID )
- from teaches

where semester = 'Spring' and year = 2010;

- Find the number of tuples in the course relation
- select count (*)

from courses ;

![Image](Lecture 2.5_artifacts/image_000015_0d9dfbde1de846c018eea32fe6aba21e8a9c7f3c69ef770101468a6cfb66a6e5.png)

## Module 10

Partha Pratim Das

Objectives &amp; Outline

Set Operations

Null Values

Three Valued Logic

Aggregate

Functions

Group By

Having

Null Values

Module Summary

## Aggregate Functions (3): Group By

- Find the average salary of instructors in each department select dept name , avg ( salary ) as avg salary from instructor group by dept name ;

| ID    | name       | dept_name   |   salary |
|-------|------------|-------------|----------|
| 76766 | Crick      | Biology     |    72000 |
| 45565 | Katz       | Comp. Sci.  |    75000 |
| 10101 | Srinivasan | Comp. Sci.  |    65000 |
| 83821 | Brandt     | Sci.        |    92000 |
| 98345 | Kim        | Elec. Eng   |    80000 |
|       | Wu         | Finance     |    90000 |
| 76543 | Singh      | Finance     |    80000 |
| 32343 | El Said    | History     |    60000 |
| 58583 | Califieri  | History     |    62000 |
| 15151 | Mozart     | Music       |    40000 |
| 33456 | Gold       | Physics     |    87000 |
| 22222 | Einstein   | Physics     |    95000 |

| dept_name   | lavg_salary   |
|-------------|---------------|
| Biology     | 72000         |
| Sci. Comp.  | 77333         |
| Elec. Eng   |               |
| Finance     | 85000         |
| History     | 61000         |
| Music       | 40000         |
| Physics     | 91000         |

Database Management Systems

Partha Pratim Das

![Image](Lecture 2.5_artifacts/image_000016_0d2e8daa05c74407b310229f101057782122d2bf078613dc8c643ca2fdb280b5.png)

## Module 10

Partha Pratim Das

Objectives &amp; Outline

Set Operations

Null Values

Three Valued Logic

Aggregate Functions

Group By

Having

Null Values

Module Summary

## Aggregate Functions (4): Group By

- Attributes in select clause outside of aggregate functions must appear in group by list

/* erroneous query */ select dept name , ID , avg ( salary ) from instructor group by dept name ;

![Image](Lecture 2.5_artifacts/image_000017_0d9dfbde1de846c018eea32fe6aba21e8a9c7f3c69ef770101468a6cfb66a6e5.png)

## Module 10

Partha Pratim Das

Objectives &amp; Outline

Set Operations

Null Values

Three Valued Logic

Aggregate Functions

Group By

Having

Null Values

Module Summary

## Aggregate Functions (5): Having Clause

- Find the names and average salaries of all departments whose average salary is greater than 42000

select dept name , ID , avg ( salary ) from instructor group by dept name having avg ( salary ) &gt; 42000;

Note: predicates in the having clause are applied after the formation of groups whereas predicates in the where clause are applied before forming groups

![Image](Lecture 2.5_artifacts/image_000018_0d9dfbde1de846c018eea32fe6aba21e8a9c7f3c69ef770101468a6cfb66a6e5.png)

## Module 10

Partha Pratim Das

Objectives &amp; Outline

Set Operations

Null Values

Three Valued Logic

Aggregate Functions

Group By

Having

Null Values

Module Summary

## Null Values and Aggregates

- Total all salaries

select sum ( salary ) from instructor ;

- Above statement ignores null amounts
- Result is null if there is no non-null amount
- All aggregate operations except count(*) ignore tuples with null values on the aggregated attributes
- What if collection has only null values?
- count returns 0
- all other aggregates return null

![Image](Lecture 2.5_artifacts/image_000019_0d9dfbde1de846c018eea32fe6aba21e8a9c7f3c69ef770101468a6cfb66a6e5.png)

Module 10

Partha Pratim Das

Objectives &amp; Outline

Set Operations

Null Values

Three Valued Logic

Aggregate Functions

Group By

Having

Null Values

Module Summary

## Module Summary

- Completed the understanding of set operations, null values, and aggregation

Slides used in this presentation are borrowed from http://db-book.com/ with kind permission of the authors.

Edited and new slides are marked with 'PPD'.
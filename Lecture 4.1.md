![Image](Lecture 4.1_artifacts/image_000000_bbaa640f2b7c7b6f18cdf441c797dcf1ce99e755b6ef0a9bbf7b581538bddcab.png)

## Module 16

Partha Pratim Das

Week Recap

Objectives &amp;

Outline

Relational

Algebra

Select

Project

Union

Difference

Intersection

Cartesian Product

Rename

Division

Module Summary

## Database Management Systems

Module 16: Formal Relational Query Languages/1

## Partha Pratim Das

Department of Computer Science and Engineering Indian Institute of Technology, Kharagpur ppd@cse.iitkgp.ac.in

Partha Pratim Das

![Image](Lecture 4.1_artifacts/image_000001_bbaa640f2b7c7b6f18cdf441c797dcf1ce99e755b6ef0a9bbf7b581538bddcab.png)

## Module 16

Partha Pratim Das

Week Recap

Objectives &amp; Outline

Relational Algebra

Select

Project

Union

Difference

Intersection

Cartesian Product

Rename

Division

Module Summary

## Week Recap

- SQL Examples have been practiced for basic query structures
- Nested Subquery in SQL
- Data Modification
- SQL expressions for Join and Views
- Transactions
- Integrity Constraints
- More data types in SQL
- Authorization in SQL
- Functions and Procedures in SQL
- Triggers

![Image](Lecture 4.1_artifacts/image_000002_821f32da21a8bb9af0bddb9e2ff2419e915ba7e461f5dc4f05b60eaa6ed0b478.png)

## Module 16

Partha Pratim Das

Week Recap

Objectives &amp; Outline

Relational

Algebra

Select

Project

Union

Difference

Intersection

Cartesian Product

Rename

Division

Module Summary

## Module Objectives

- To understand formal query language through relational algebra

![Image](Lecture 4.1_artifacts/image_000003_821f32da21a8bb9af0bddb9e2ff2419e915ba7e461f5dc4f05b60eaa6ed0b478.png)

## Module 16

Partha Pratim Das

Week Recap

Objectives &amp; Outline

Relational

Algebra

Select

Project

Union

Difference

Intersection

Cartesian Product

Rename

Division

Module Summary

## Module Outline

- Relational Algebra

![Image](Lecture 4.1_artifacts/image_000004_0d9dfbde1de846c018eea32fe6aba21e8a9c7f3c69ef770101468a6cfb66a6e5.png)

## Module 16

Partha Pratim Das

Week Recap

Objectives &amp; Outline

Relational Algebra

Select

Project

Union

Difference

Intersection

Cartesian Product

Rename

Division

Module Summary

## Formal Relational Query Language

- Relational Algebra
- Procedural and Algebra based
- Tuple Relational Calculus
- Non-Procedural and Predicate Calculus based
- Domain Relational Calculus
- Non-Procedural and Predicate Calculus based

![Image](Lecture 4.1_artifacts/image_000005_bbaa640f2b7c7b6f18cdf441c797dcf1ce99e755b6ef0a9bbf7b581538bddcab.png)

## Module 16

Partha Pratim Das

Week Recap

Objectives &amp; Outline

Relational Algebra

Select

Project

Union

Difference

Intersection

Cartesian Product

Rename

Division

Module Summary

## Relational Algebra

![Image](Lecture 4.1_artifacts/image_000006_0d9dfbde1de846c018eea32fe6aba21e8a9c7f3c69ef770101468a6cfb66a6e5.png)

## Module 16

Partha Pratim Das

Week Recap

Objectives &amp; Outline

Relational Algebra

Select

Project

Union

Difference

Intersection

Cartesian Product

Rename

Division

Module Summary

## Relational Algebra

- Created by Edgar F Codd at IBM in 1970
- Procedural language
- Six basic operators
- select: σ
- project: Π
- union: ∪
- set difference: -
- Cartesian product:

x

- rename: ρ
- The operators take one or two relations as inputs and produce a new relation as a result

![Image](Lecture 4.1_artifacts/image_000007_bbaa640f2b7c7b6f18cdf441c797dcf1ce99e755b6ef0a9bbf7b581538bddcab.png)

## Module 16

Partha Pratim Das

Week Recap

Objectives &amp; Outline

Relational Algebra

Select

Project

Union

Difference

Intersection

Cartesian Product

Rename

Division

Module Summary

## Select Operation

- Notation: σ p ( r )
- p is called the selection predicate
- Defined as:

σ p ( r ) = { t | t ∈ r and p ( t ) }

where p is a formula in propositional calculus consisting of terms connected by : ∧ ( and ), ∨ ( or ), ¬ ( not ) Each terms is one of:

&lt; attribute &gt; op &lt; attribute &gt; or &lt; constant &gt;

glyph[negationslash]

where op is one of: = , = , &gt;, ≥ . &lt; . ≤

- Example of selection:

σ dept name = 'Physics' ( instructor )

Database Management Systems

Partha Pratim Das

![Image](Lecture 4.1_artifacts/image_000008_8bd0c132939c9c9432fa01f7f21c841624569c388ec538d991147639c511a717.png)

![Image](Lecture 4.1_artifacts/image_000009_dc3e0bf4c8911633b01552a93fd9e95fb1167c884db1c471e28d0d4d0c4ed4f0.png)

^ D &gt; 5 (r)

![Image](Lecture 4.1_artifacts/image_000010_0d9dfbde1de846c018eea32fe6aba21e8a9c7f3c69ef770101468a6cfb66a6e5.png)

## Module 16

Partha Pratim Das

Week Recap

Objectives &amp; Outline

Relational

Algebra

Select

Project

Union

Difference

Intersection

Cartesian Product

Rename

Division

Module Summary

## Project Operation

- Notation: Π A 1 , A 2 ,... Ak (r) where A 1 , A 2 are attribute names and r is a relation
- The result is defined as the relation of k columns obtained by erasing the columns that are not listed
- Duplicate rows removed from result, since relations are sets
- Example: To eliminate the dept name attribute of instructor

Π ID , name , salary ( instructor )

![Image](Lecture 4.1_artifacts/image_000011_6a0c098e7b31195aa84520d7039b6525ca83a024cccbf60196ff2c7fdaf2ebca.png)

![Image](Lecture 4.1_artifacts/image_000012_bbaa640f2b7c7b6f18cdf441c797dcf1ce99e755b6ef0a9bbf7b581538bddcab.png)

## Module 16

Partha Pratim Das

Week Recap

Objectives &amp; Outline

Relational Algebra

Select

Project

Union

Difference

Intersection

Cartesian Product

Rename

Division

Module Summary

## Union Operation

- Notation: r ∪ s
- Defined as: r ∪ s = { t | t ∈ r or t ∈ s }
- For r ∪ s to be valid.
- a) r, s must have the same arity (same number of attributes)
- b) The attribute domains must be compatible (example: 2nd column of r deals with the same type of values as does the 2nd column of s )
- c) Example: to find all courses taught in the Fall 2009 semester, or in the Spring 2010 semester, or in both

![Image](Lecture 4.1_artifacts/image_000013_7e6a5e6920b2185c32aa5d692fc71f9f03a3da861caf3bdc38dd7d032695fa8f.png)

Π course id ( σ semester =' Fall ' ∧ year =2009 ( section )) ∪ Π course id ( σ semester =' Spring ' ∧ year =2010 ( section ))

![Image](Lecture 4.1_artifacts/image_000014_bbaa640f2b7c7b6f18cdf441c797dcf1ce99e755b6ef0a9bbf7b581538bddcab.png)

## Module 16

Partha Pratim Das

Week Recap

Objectives &amp; Outline

Relational Algebra

Select

Project

Union

Difference

Intersection

Cartesian Product

Rename

Division

Module Summary

## Difference Operation

- Notation r -s
- Defined as: r -s = { t | t ∈ r and t / ∈ s }
- Set differences must be taken between compatible relations
- r and s must have the same arity
- attribute domains of r and s must be compatible
- Example: to find all courses taught in the Fall 2009 semester, but not in the Spring 2010 semester

Π course id ( σ semester =' Fall ' ∧ year =2009 ( section )) -Π course id ( σ semester =' Spring ' ∧ year =2010 ( section ))

![Image](Lecture 4.1_artifacts/image_000015_c0f778ae37df2a5b1c2ee72f19aed5a2035bccb52d2b02a8f0ed4db2b82ad234.png)

![Image](Lecture 4.1_artifacts/image_000016_0d9dfbde1de846c018eea32fe6aba21e8a9c7f3c69ef770101468a6cfb66a6e5.png)

## Module 16

Partha Pratim Das

Week Recap

Objectives &amp; Outline

Relational Algebra

Select

Project

Union

Difference

Intersection

Cartesian Product

Rename

Division

Module Summary

## Intersection Operation

- Notation: r ∩ s
- Defined as:

<!-- formula-not-decoded -->

- Assume:
- r, s have the same arity
- attributes of r and s are compatible
- Note: r ∩ s = r - ( r -s )

![Image](Lecture 4.1_artifacts/image_000017_90c395d58973a3011baf8e41acd9df71b9d3df7ce99b2f348bbc15e1d321df5e.png)

![Image](Lecture 4.1_artifacts/image_000018_93a3933842ea1fa6829d8ade18a27923860180dab714b4a4165c3de635462234.png)

![Image](Lecture 4.1_artifacts/image_000019_bbaa640f2b7c7b6f18cdf441c797dcf1ce99e755b6ef0a9bbf7b581538bddcab.png)

## Module 16

Partha Pratim Das

Week Recap

Objectives &amp; Outline

Relational Algebra

Select

Project

Union

Difference

Intersection

Cartesian Product

Rename

Division

Module Summary

## Cartesian-Product Operation

- Notation r × s
- Defined as:

r × s = { t q | t ∈ r and q ∈ s }

- Assume that attributes of r ( R ) and s ( S ) are disjoint. (That is, R ∩ S = φ )
- If attributes of r(R) and s(S) are not disjoint, then renaming must be used

![Image](Lecture 4.1_artifacts/image_000020_39834c8affc9fb57b4befce878a5a1fa12cda74a86de3d0728c6d46caf601301.png)

![Image](Lecture 4.1_artifacts/image_000021_0d9dfbde1de846c018eea32fe6aba21e8a9c7f3c69ef770101468a6cfb66a6e5.png)

## Module 16

Partha Pratim

Das

Week Recap

Objectives &amp;

Outline

Relational

Algebra

Select

Project

Union

Difference

Intersection

Cartesian Product

Rename

Division

Module Summary

## Rename Operation

- Allows us to name, and therefore to refer to, the results of relational-algebra expressions.
- Allows us to refer to a relation by more than one name.
- Example:

ρ x ( E ) returns the expression E under the name X

- If a relational-algebra expression E has arity n , then

<!-- formula-not-decoded -->

returns the result of expression E under the name X , and with the attributes renamed to

<!-- formula-not-decoded -->

.

Database Management Systems

16.14

![Image](Lecture 4.1_artifacts/image_000022_fde1132bf222cc20a3e76fd9bad23db921b22024804914407d2f2bc1b513e47e.png)

## Module 16

Partha Pratim Das

Week Recap

Objectives &amp; Outline

Relational Algebra

Select

Project

Union

Difference

Intersection

Cartesian Product

Rename

Division

Module Summary

## Division Operation

- The division operation is applied to two relations
- R(Z) ÷ S(X), where X subset Z. Let Y = Z - X (and hence Z = X ∪ Y); that is, let Y be the set of attributes of R that are not attributes of S
- The result of DIVISION is a relation T(Y) that includes a tuple t if tuples t R appear in R with t R [Y] = t, and with
- t R [ X ] = ts for every tuple ts in S.
- For a tuple t to appear in the result T of the DIVISION, the values in t must appear in R in combination with every tuple in S
- Division is a derived operation and can be expressed in terms of other operations
- r ÷ s ≡ Π R -S ( r ) -Π R -S ((Π R -S ( r ) × s ) -Π R -S , S ( r ))

![Image](Lecture 4.1_artifacts/image_000023_fde1132bf222cc20a3e76fd9bad23db921b22024804914407d2f2bc1b513e47e.png)

## Module 16

Partha Pratim

Das

Week Recap

Objectives &amp;

Outline

Relational

Algebra

Select

Project

Union

Difference

Intersection

Cartesian Product

Rename

Division

Module Summary

## Division Examples

## R

| Broun   | Compilers   |
|---------|-------------|
| Brown   | Dalabases   |
| Leuis   | Proloe      |
| Smith   |             |

5

![Image](Lecture 4.1_artifacts/image_000024_420cf06f245ae4cca4614707e947c000783e1313ecd6562cc6e25469f50c4563.png)

![Image](Lecture 4.1_artifacts/image_000025_6f8c738645e65586a57fe1bcd4389fa011dfbb8517333af68bfa592e18699336.png)

![Image](Lecture 4.1_artifacts/image_000026_c66187055de285596be50032d73dadd82d2ef960cecf03026d68ecb78134d5c9.png)

## Module 16

Partha Pratim

Das

Week Recap

Objectives &amp;

Outline

Relational

Algebra

Select

Project

Union

Difference

Intersection

Cartesian Product

Rename

Division

Module Summary

## Division Examples (2)

R

5

RIs

![Image](Lecture 4.1_artifacts/image_000027_2c316faaeddf57b9ceaec6bcf29b748b3bad0bb3f25ab7a04aab9cfb41d1ad79.png)

|                                     | Module                                                | Subject   | Lecnrer   |
|-------------------------------------|-------------------------------------------------------|-----------|-----------|
| Broun Broun Green Green Levis Suuth | Compilers Dalabases Prolog Databases Prolog Databases | Darabases | Green     |

![Image](Lecture 4.1_artifacts/image_000028_32155ccc63eaf8ac3b5d36be7560257f854d0b99536286a17a16546fbab339af.png)

## Division Examples (3)

![Image](Lecture 4.1_artifacts/image_000029_daabb652c0df64782e685580632cb39fca9accc154c89b4b4a074d7ce2cd180b.png)

![Image](Lecture 4.1_artifacts/image_000030_32155ccc63eaf8ac3b5d36be7560257f854d0b99536286a17a16546fbab339af.png)

Module 16

Partha Pratim

Das

Week Recap

Objectives &amp;

Outline

Relational

Algebra

Select

Project

Union

Difference

Intersection

Cartesian Product

Rename

Division

Module Summary

## Division Example (4)

- Relations r, s :

![Image](Lecture 4.1_artifacts/image_000031_a2f3aa8c48d35291a629b69175ff76d4542006a682dd71f25de6b14fa1177518.png)

![Image](Lecture 4.1_artifacts/image_000032_c277774fa8f1038bffc31d9c5ac59588b1e3bc295c46abe0b4034a3cf56a36c8.png)

![Image](Lecture 4.1_artifacts/image_000033_88e31967ef8e397ed1ae7f55f08d6404427ab710d6231e94bbb4e0a70a0c21eb.png)

e.g. A is customer name B is branch-name 1 and 2 here show two specific branch-names (Find customers who have an account in all branches of the bank)

## Partha Pratim Das

![Image](Lecture 4.1_artifacts/image_000034_32155ccc63eaf8ac3b5d36be7560257f854d0b99536286a17a16546fbab339af.png)

Module 16

Partha Pratim

Das

Week Recap

Objectives &amp;

Outline

Relational

Algebra

Select

Project

Union

Difference

Intersection

Cartesian Product

Rename

Division

Module Summary

## Division Example (5)

- Relations r, s :

![Image](Lecture 4.1_artifacts/image_000035_f7e0c53d4904413b2e47c9899d5047057aa7b20b28933dec7bcf5d6328a4d948.png)

Source: db.fcngroup.nl/silberslides/Divsion Database Management Systems

![Image](Lecture 4.1_artifacts/image_000036_1bd621acd99697e107e46af0cfa832a2796cceb634c185d95673839c66d38e6f.png)

- e.g. Students who have taken both 'a' and 'b' courses, with instructor '1'

(Find students who have taken all courses given by instructor 1)

## Partha Pratim Das

![Image](Lecture 4.1_artifacts/image_000037_0d9dfbde1de846c018eea32fe6aba21e8a9c7f3c69ef770101468a6cfb66a6e5.png)

Module 16

Partha Pratim Das

Week Recap

Objectives &amp; Outline

Relational Algebra

Select

Project

Union

Difference

Intersection

Cartesian Product

Rename

Division

Module Summary

## Module Summary

- Discussed relational algebra with examples

Slides used in this presentation are borrowed from http://db-book.com/ with kind permission of the authors.

Edited and new slides are marked with 'PPD'.
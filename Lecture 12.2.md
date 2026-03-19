<!-- image -->

## Module 57

Partha Pratim Das

Objectives &amp; Outline

Query Optimization Equivalent Expressions Evaluation Plan Cost

Transformation of Relational Expressions

Equivalence Rules

Example

Plan Generation

Module Summary

## Database Management Systems

Module 57: Query Processing and Optimization/2: Optimization

## Partha Pratim Das

Department of Computer Science and Engineering Indian Institute of Technology, Kharagpur ppd@cse.iitkgp.ac.in

Partha Pratim Das

<!-- image -->

## Module 57

Partha Pratim Das

Objectives &amp; Outline

Query Optimization Equivalent Expressions

Evaluation Plan

Cost

Transformation of Relational Expressions

Equivalence Rules

Example

Plan Generation

Module Summary

## Module Recap

- Understood the overall flow for Query Processing and defined the Measures of Query Cost
- Studied the algorithms for processing Selection Operations, Sorting, Join Operations and a few Other Operations

<!-- image -->

## Module 57

Partha Pratim Das

Objectives &amp; Outline

Query Optimization Equivalent Expressions Evaluation Plan Cost

Transformation of Relational Expressions

Equivalence Rules

Example

Plan Generation

Module Summary

## Module Objectives

- To understand the basic issues for optimizing queries
- To understand how transformation of Relational Expressions can create alternates for optimization

<!-- image -->

## Module 57

Partha Pratim Das

Objectives &amp; Outline

Query

Optimization

Equivalent

Expressions

Evaluation Plan

Cost

Transformation of Relational Expressions

Equivalence Rules

Example

Plan Generation

Module Summary

## Module Outline

- Introduction to Query Optimization
- Transformation of Relational Expressions

<!-- image -->

Module 57

Partha Pratim Das

Objectives &amp; Outline

Query Optimization

Equivalent

Expressions

Evaluation Plan

Cost

Transformation of Relational Expressions

Equivalence Rules

Example

Plan Generation

Module Summary

## Introduction to Query Optimization

## Introduction to Query Optimization

<!-- image -->

## Module 57

Partha Pratim Das

Objectives &amp;

Outline

Query

Optimization

Equivalent

Expressions

Evaluation Plan

Cost

Transformation of

Relational

Expressions

Equivalence Rules

Example

Plan Generation

Module Summary

## Query Optimization

- Alternative ways of evaluating a given query
- Equivalent expressions
- Different algorithms for each operation

<!-- image -->

## Database Management Systems

course(course id, title; dept name; credits) teaches(lD, course id; sec id, semester; year)

name, title dept\_name

instructor

## Partha Pratim Das

Music teaches

course

<!-- image -->

Module 57

Partha Pratim

Das

Objectives &amp;

Outline

Query

Optimization

Equivalent

Expressions

Evaluation Plan

Cost

Transformation of

Relational

Expressions

Equivalence Rules

Example

Plan Generation

Module Summary

## Query Optimization (2)

<!-- image -->

<!-- image -->

## Module 57

Partha Pratim Das

Objectives &amp; Outline

Query

Optimization

Equivalent

Expressions

Evaluation Plan

Cost

Transformation of Relational Expressions

Equivalence Rules

Example

Plan Generation

Module Summary

## Query Optimization (3)

- Cost difference between evaluation plans for a query can be enormous
- For example, seconds vs. days in some cases
- Steps in cost-based query optimization
- a) Generate logically equivalent expressions using equivalence rules
- b) Annotate resultant expressions to get alternative query plans
- c) Choose the cheapest plan based on estimated cost
- Estimation of plan cost based on:
- Statistical information about relations.
- glyph[triangleright] Examples: number of tuples, number of distinct values for an attribute
- Statistics estimation for intermediate results
- glyph[triangleright] to compute cost of complex expressions
- Cost formulae for algorithms, computed using statistics

<!-- image -->

Module 57

Partha Pratim Das

Objectives &amp; Outline

Query

Optimization

Equivalent

Expressions

Evaluation Plan

Cost

Transformation of Relational Expressions

Equivalence Rules

Example

Plan Generation

Module Summary

## Transformation of Relational Expressions

## Transformation of Relational Expressions

<!-- image -->

## Module 57

Partha Pratim Das

Objectives &amp; Outline

Query

Optimization

Equivalent

Expressions

Evaluation Plan

Cost

## Transformation of Relational Expressions

Equivalence Rules

Example

Plan Generation

Module Summary

## Transformation of Relational Expressions

- Two relational algebra expressions are said to be equivalent if the two expressions generate the same set of tuples on every legal database instance
- Note: order of tuples is irrelevant
- We do not care if they generate different results on databases that violate integrity constraints
- In SQL, inputs and outputs are multisets of tuples
- Two expressions in the multiset version of the relational algebra are said to be equivalent if the two expressions generate the same multiset of tuples on every legal database instance.
- An equivalence rule says that expressions of two forms are equivalent
- Can replace expression of first form by second, or vice versa

<!-- image -->

Module 57

Partha Pratim Das

Objectives &amp; Outline

Query Optimization Equivalent Expressions Evaluation Plan Cost

Transformation of Relational Expressions

Equivalence Rules

Example

Plan Generation

Module Summary

## Equivalence Rules

- 1 Conjunctive selection operations can be deconstructed into a sequence of individual selections

<!-- formula-not-decoded -->

- 2 Selection operations are commutative

<!-- formula-not-decoded -->

- 3 Only the last in a sequence of projection operations is needed, the others can be omitted

<!-- formula-not-decoded -->

- 4 Selections can be combined with Cartesian products and theta joins

<!-- formula-not-decoded -->

Database Management Systems

σ θ 1 ( E 1 glyph[multicloseright] glyph[multicloseleft] θ 2 E 2 ) = E 1 glyph[multicloseright] glyph[multicloseleft] θ 1 ∧ θ 2 E 2 Partha Pratim Das

57.11

<!-- image -->

## Module 57

Partha Pratim Das

Objectives &amp; Outline

Query

Optimization

Equivalent

Expressions

Evaluation Plan

Cost

Transformation of Relational Expressions

Equivalence Rules

Example

Plan Generation

Module Summary

## Equivalence Rules (2)

- 5 Theta-join operations (and natural joins) are commutative

<!-- formula-not-decoded -->

- 6 a. Natural join operations are associative:

<!-- formula-not-decoded -->

- b. Theta joins are associative in the following manner:

<!-- formula-not-decoded -->

where θ 2 involves attributes from E 2 and E 3 only

<!-- image -->

## Equivalence Rules (3): Pictorial Depiction

<!-- image -->

<!-- image -->

## Module 57

Partha Pratim Das

Objectives &amp; Outline

Query

Optimization

Equivalent

Expressions

Evaluation Plan

Cost

Transformation of Relational Expressions

Equivalence Rules

Example

Plan Generation

Module Summary

## Equivalence Rules (4)

- 7 The selection operation distributes over the theta join operation under the following two conditions:
- a. When all the attributes in θ 0 involve only the attributes of one of the expressions ( E 1 ) being joined

<!-- formula-not-decoded -->

- b. When θ 1 involves only the attributes of E 1 and θ 2 involves only the attributes of E 2 .

<!-- formula-not-decoded -->

<!-- image -->

## Module 57

Partha Pratim Das

Objectives &amp; Outline

Query

Optimization

Equivalent

Expressions

Evaluation Plan

Cost

Transformation of Relational Expressions

Equivalence Rules

Example

Plan Generation

Module Summary

## Equivalence Rules (5)

- 8 The projection operation distributes over the theta join operation as follows:
- a. if θ involves only attributes from L 1 ∪ L 2 :

∏ L 1 ∪ L 2 ( E 1 glyph[multicloseright] glyph[multicloseleft] θ E 2 ) = ∏ L 1 ( E 1 ) glyph[multicloseright] glyph[multicloseleft] θ ∏ L 2 ( E 2 )

- b. Consider a join E 1 glyph[multicloseright] glyph[multicloseleft] θ E 2
- Let L 1 and L 2 be sets of attributes from E 1 and E 2 , respectively
- Let L 3 be attributes of E 1 that are involved in join condition θ , but are not in L 1 ∪ L 2 , and
- Let L 4 be attributes of E 2 that are involved in join condition θ , but are not in L 1 ∪ L 2 .

<!-- formula-not-decoded -->

<!-- image -->

Module 57

Partha Pratim Das

Objectives &amp; Outline

Query

Optimization

Equivalent

Expressions

Evaluation Plan

Cost

Transformation of Relational Expressions

Equivalence Rules

Example

Plan Generation

Module Summary

## Equivalence Rules (6)

- 9 The set operations union and intersection are commutative.

E 1 ∪ E 2 = E 2 ∪ E 1

E 1 ∩ E 2 = E 2 ∩ E 1

- (set difference is not commutative).
- 10 Set union and intersection are associative.
- ( E 1 ∪ E 2) ∪ E 3 = E 1 ∪ ( E 2 ∪ E 3)
- ( E 1 ∩ E 2) ∩ E 3 = E 1 ∩ ( E 2 ∩ E 3)
- 11 The selection operation distributes over ∪ , ∩ , -
- σ θ ( E 1 -E 2 ) = σ θ ( E 1 ) -σ θ ( E 2 )
- and similarly for ∪ and ∩ in place of -

Also: σ θ ( E 1 -E 2 ) = σ θ ( E 1 ) -E 2

and similarly for ∩ in place of -, but not for ∪

- 12 The projection operation distributes over union
- π L ( E 1 ∪ E 2 ) = ( π L ( E 1 )) ∪ ( π L ( E 2 ))

Database Management Systems

Partha Pratim Das

<!-- image -->

## Module 57

Partha Pratim Das

Objectives &amp; Outline

Query

Optimization

Equivalent

Expressions

Evaluation Plan

Cost

Transformation of Relational Expressions

Equivalence Rules

Example

Plan Generation

Module Summary

## Exercise

- Create equivalence rules involving
- The group by/aggregation operation
- Left outer join operation

<!-- image -->

## Module 57

Partha Pratim

Das

Objectives &amp; Outline

Query

Optimization

Equivalent

Expressions

Evaluation Plan

Cost

Transformation of

Relational

Expressions

Equivalence Rules

Example

Plan Generation

Module Summary

## Transformation Example: Pushing Selections

- Query: Find the names of all instructors in the Music department, along with the titles of the courses that they teach
- π name , title ( σ dept name =' Music ' ( instructor glyph[multicloseright] glyph[multicloseleft] ( teaches glyph[multicloseright] glyph[multicloseleft] π course id , title ( course ))))
- Transformation using rule 7a
- π name , title (( σ dept name =' Music ' ( instructor )) glyph[multicloseright] glyph[multicloseleft] ( teaches glyph[multicloseright] glyph[multicloseleft] π course id , title ( course )))
- Performing the selection as early as possible reduces the size of the relation to be joined

courselcourse\_id , title, dept name, credits) course id, sec id, semester, year)

<!-- image -->

## Database Management Systems

## Partha Pratim Das

57.18

<!-- image -->

Module 57

Partha Pratim Das

Objectives &amp; Outline

Query

Optimization

Equivalent

Expressions

Evaluation Plan

Cost

Transformation of

Relational

Expressions

Equivalence Rules

Example

Plan Generation

Module Summary

## Multiple Transformations

- Query: Find the names of all instructors in the Music department who have taught a course in 2009, along with the titles of the courses that they taught
- π name , title ( σ dept name =' Music ' ∧ year =2009 ( instructor glyph[multicloseright] glyph[multicloseleft] ( teaches glyph[multicloseright] glyph[multicloseleft] π course id , title ( course ))))
- Transformation using join associatively (Rule 6a):
- π name , title ( σ dept name =' Music ' ∧ year =2009 (( instructor glyph[multicloseright] glyph[multicloseleft] teaches ) glyph[multicloseright] glyph[multicloseleft] π course id , title ( course )))
- Second form provides an opportunity to apply the 'perform selections early' rule, resulting in the subexpression
- σ dept name =' Music ' ( instructor ) glyph[multicloseright] glyph[multicloseleft] σ year =2009 ( teaches )

<!-- image -->

<!-- image -->

Module 57

Partha Pratim

Das

Objectives &amp;

Outline

Query

Optimization

Equivalent

Expressions

Evaluation Plan

Cost

Transformation of

Relational

Expressions

Equivalence Rules

Example

Plan Generation

Module Summary

## Multiple Transformations (2)

<!-- image -->

<!-- image -->

## Module 57

Partha Pratim Das

Objectives &amp; Outline

Query

Optimization

Equivalent

Expressions

Evaluation Plan

Cost

Transformation of Relational Expressions

Equivalence Rules

Example

Plan Generation

Module Summary

## Transformation Example: Pushing Projections

- Consider:
- π name , title (( σ dept name =' Music ' ( instructor )) glyph[multicloseright] glyph[multicloseleft] ( teaches glyph[multicloseright] glyph[multicloseleft] π course id , title ( course )))
- When we compute
- σ dept name =' Music ' ( instructor glyph[multicloseright] glyph[multicloseleft] teaches )

we obtain a relation whose schema is:

- ( ID , name , dept name , salary , course id , sec id , semester , year )
- Push projections using equivalence rules 8a and 8b; eliminate unneeded attributes from intermediate results to get:
- π name , title ( π name , course id ( σ dept name =' Music ' ( instructor ) glyph[multicloseright] glyph[multicloseleft] teaches )) glyph[multicloseright] glyph[multicloseleft] π course id , title ( course )
- Performing the projection as early as possible reduces the size of the relation to be joined

courselcourse\_id, title dept name, credits) instructorllD, name, dept name, salary)

∏ L 1 ∪ L 2 ( E 1 glyph[multicloseright] glyph[multicloseleft] θ E 2 ) = ∏ L 1 ( E 1 ) glyph[multicloseright] glyph[multicloseleft] θ ∏ L 2 ( E 2 ) ∏ L 1 ∪ L 2 ( E 1 glyph[multicloseright] glyph[multicloseleft] θ E 2 ) = ∏ L 1 ∪ L 2 ( ( ∏ L 1 ∪ L 3 ( E 1 )) glyph[multicloseright] glyph[multicloseleft] θ ( ∏ L 2 ∪ L 4 ( E 2 )) )

Database Management Systems

Partha Pratim Das

<!-- image -->

## Module 57

Partha Pratim Das

Objectives &amp; Outline

Query

Optimization

Equivalent

Expressions

Evaluation Plan

Cost

Transformation of Relational Expressions

Equivalence Rules

Example

Plan Generation

Module Summary

## Join Ordering Example

- For all relations r 1 , r 2 , and r 3 , ( r 1 glyph[multicloseright] glyph[multicloseleft] r 2 ) glyph[multicloseright] glyph[multicloseleft] r 3 = r 1 glyph[multicloseright] glyph[multicloseleft] ( r 2 glyph[multicloseright] glyph[multicloseleft] r 3 ) (Join Associativity)
- •
- If r 2 glyph[multicloseright] glyph[multicloseleft] r 3 is quite large and r 1 glyph[multicloseright] glyph[multicloseleft] r 2 is small, we choose ( r 1 glyph[multicloseright] glyph[multicloseleft] r 2 ) glyph[multicloseright] glyph[multicloseleft] r 3 so that we compute and store a smaller temporary relation

<!-- image -->

## Module 57

Partha Pratim Das

Objectives &amp; Outline

Query

Optimization

Equivalent

Expressions

Evaluation Plan

Cost

Transformation of Relational Expressions

Equivalence Rules

Example

Plan Generation

Module Summary

## Join Ordering Example (2)

- Consider the expression
- π name , title ( σ dept name =' Music ' ( instructor ) glyph[multicloseright] glyph[multicloseleft] teaches ) glyph[multicloseright] glyph[multicloseleft] π course id , title ( course )
- Could compute teaches glyph[multicloseright] glyph[multicloseleft] π course id , title ( course ) first, and join result with σ dept name =' Music ' ( instructor )
- but the result of the first join is likely to be a large relation
- Only a small fraction of the university's instructors are likely to be from the Music department
- it is better to compute
- σ dept name =' Music ' ( instructor ) glyph[multicloseright] glyph[multicloseleft] ( teaches ) first

course(course id, title; dept name, credits) instructorlID; name; dept name; salary) teaches(lD; course id, sec id, semester; year)

<!-- image -->

## Module 57

Partha Pratim Das

Objectives &amp; Outline

Query

Optimization

Equivalent

Expressions

Evaluation Plan

Cost

Transformation of Relational Expressions

Equivalence Rules

Example

Plan Generation

Module Summary

## Enumeration of Equivalent Expressions

- Query optimizers use equivalence rules to systematically generate expressions equivalent to the given expression
- Can generate all equivalent expressions as follows:
- Repeat
- glyph[triangleright] apply all applicable equivalence rules on every subexpression of every equivalent expression found so far
- glyph[triangleright] add newly generated expressions to the set of equivalent expressions
- Until no new equivalent expressions are generated above
- The above approach is very expensive in space and time
- Two approaches
- glyph[triangleright] Optimized plan generation based on transformation rules
- glyph[triangleright] Special case approach for queries with only selections, projections and joins

<!-- image -->

## Module 57

Partha Pratim Das

Objectives &amp; Outline

Query Optimization Equivalent Expressions Evaluation Plan Cost

Transformation of Relational Expressions

Equivalence Rules

Example

Plan Generation

Module Summary

## Implementing Transformation Based Optimization

- Space requirements reduced by sharing common sub-expressions:
- when E1 is generated from E2 by an equivalence rule, usually only the top level of the two are different, subtrees below are the same and can be shared using pointers glyph[triangleright] E.g. when applying join commutativity
- Same sub-expression may get generated multiple times
- glyph[triangleright] Detect duplicate sub-expressions and share one copy
- Time requirements are reduced by not generating all expressions
- Dynamic programming

<!-- image -->

<!-- image -->

## Module 57

Partha Pratim Das

Objectives &amp; Outline

Query Optimization Equivalent Expressions Evaluation Plan Cost

Transformation of Relational Expressions

Equivalence Rules

Example

Plan Generation

Module Summary

## Module Summary

- Understood the basic issues for optimizing queries
- For every relational expression, usually there are a number of equivalent expressions that can be created by simple transformations
- Final execution plan can be created by choose the estimated least cost expression from the alternates

Slides used in this presentation are borrowed from http://db-book.com/ with kind permission of the authors.

Edited and new slides are marked with 'PPD'. Database Management Systems Partha Pratim Das
![Image](Lecture 2.2_artifacts/image_000000_bbaa640f2b7c7b6f18cdf441c797dcf1ce99e755b6ef0a9bbf7b581538bddcab.png)

## Module 07

Partha Pratim Das

Objectives &amp; Outline

Relational Operators

Aggregation Operators

Module Summary

## Database Management Systems

Module 07: Introduction to Relational Model/2

## Partha Pratim Das

Department of Computer Science and Engineering Indian Institute of Technology, Kharagpur ppd@cse.iitkgp.ac.in

Partha Pratim Das

![Image](Lecture 2.2_artifacts/image_000001_0d9dfbde1de846c018eea32fe6aba21e8a9c7f3c69ef770101468a6cfb66a6e5.png)

## Module 07

Partha Pratim Das

Objectives &amp; Outline

Relational Operators

Aggregation Operators

Module Summary

## Module Recap

- Basic notions of modeling introduced
- Attributes and their Types
- Schema and Instance
- Keys and their Categorization
- Languages for Relation Model introduced

![Image](Lecture 2.2_artifacts/image_000002_0d9dfbde1de846c018eea32fe6aba21e8a9c7f3c69ef770101468a6cfb66a6e5.png)

## Module 07

Partha Pratim Das

Objectives &amp; Outline

Relational Operators

Aggregation Operators

Module Summary

## Module Objectives

- To understand relational algebra
- To familiarize with the operators of relational algebra

![Image](Lecture 2.2_artifacts/image_000003_b551d1d039a350a56349b412170007d20638ad0732feb40b06cdb100cf6ab680.png)

## Module 07

Partha Pratim Das

## Objectives &amp; Outline

Relational Operators

Aggregation Operators

Module Summary

## Module Outline

- Operations
- Select
- Project
- Union
- Difference
- Intersection
- Cartesian Product
- Natural Join
- Aggregate Operations

![Image](Lecture 2.2_artifacts/image_000004_0d2e8daa05c74407b310229f101057782122d2bf078613dc8c643ca2fdb280b5.png)

Module 07

Partha Pratim Das

Objectives &amp; Outline

Relational Operators

Aggregation Operators

Module Summary

## Relational Operators

## Relational Operators

![Image](Lecture 2.2_artifacts/image_000005_bbaa640f2b7c7b6f18cdf441c797dcf1ce99e755b6ef0a9bbf7b581538bddcab.png)

## Module 07

Partha Pratim Das

Objectives &amp; Outline

Relational

Operators

Aggregation Operators

Module Summary

## Basic Properties of Relations

- A relation is set . Hence,
- Ordering of rows / tuples is inconsequential

| A   | B              | A   | B   |
|-----|----------------|-----|-----|
| a1  | b1             | a1  | b1  |
| a1  | b2 is same as: | a2  | b1  |
| a2  | b1             | a2  | b2  |
| a2  | b2             | a1  | b2  |

## · All rows / tuples must be distinct

A

B

a1

a1

a1

b1

b2

b2

a1

b1

Database Management Systems

A

a1

a1

is not valid

B

b1

b2

is

## Partha Pratim Das

![Image](Lecture 2.2_artifacts/image_000006_bbaa640f2b7c7b6f18cdf441c797dcf1ce99e755b6ef0a9bbf7b581538bddcab.png)

## Module 07

Partha Pratim

Das

Objectives &amp;

Outline

Relational Operators

Aggregation Operators

Module Summary

## Select Operation - selection of rows (tuples)

- Relation r

1

5

7

7

3

B

B

![Image](Lecture 2.2_artifacts/image_000007_5bbbab4ed5988d9e24e35c2bbc52c80ff2e35316200ed543c7f176a7956c9e39.png)

- σ A = B ∧ D &gt; 5 ( r )

ß

![Image](Lecture 2.2_artifacts/image_000008_bbaa640f2b7c7b6f18cdf441c797dcf1ce99e755b6ef0a9bbf7b581538bddcab.png)

Module 07

Partha Pratim

Das

Objectives &amp;

Outline

Relational

Operators

Aggregation

Operators

Module Summary

## Project Operation - selection of columns (Attributes)

- Relation r
- π A , C ( r )

Database Management Systems

![Image](Lecture 2.2_artifacts/image_000009_ef40dbcd1acaa14719c70cb972cfcd6b7251322f75d269e4d9d0e9d379bdc4af.png)

Partha Pratim Das

![Image](Lecture 2.2_artifacts/image_000010_fde1132bf222cc20a3e76fd9bad23db921b22024804914407d2f2bc1b513e47e.png)

Module 07

Partha Pratim

Das

Objectives &amp;

Outline

Relational

Operators

Aggregation

Operators

Module Summary

## Union of two relations

- Relation r , s
- r ∪ s

![Image](Lecture 2.2_artifacts/image_000011_ce3c882bf595af49413e64554f8e692b0660ac980729f9fd01fc3b81af84eabc.png)

## Partha Pratim Das

![Image](Lecture 2.2_artifacts/image_000012_bbaa640f2b7c7b6f18cdf441c797dcf1ce99e755b6ef0a9bbf7b581538bddcab.png)

Module 07

Partha Pratim

Das

Objectives &amp;

Outline

Relational

Operators

Aggregation

Operators

Module Summary

## Set difference of two relations

- Relation r , s
- r -s

![Image](Lecture 2.2_artifacts/image_000013_32ed706f37d3f77c48bdc975c14057082a5f70e984274b910b15cf6fe87b52fa.png)

![Image](Lecture 2.2_artifacts/image_000014_bbaa640f2b7c7b6f18cdf441c797dcf1ce99e755b6ef0a9bbf7b581538bddcab.png)

Module 07

Partha Pratim

Das

Objectives &amp;

Outline

Relational

Operators

Aggregation

Operators

Module Summary

## Set intersection of two relations

- Relation r , s
- r ∩ s

![Image](Lecture 2.2_artifacts/image_000015_04bf9ac366dd968ba53eae566267cab1d15aaeedac1fbc52dc8be7b3c89ca01a.png)

![Image](Lecture 2.2_artifacts/image_000016_15d95ea4e70710d011a079244a377aea53615af9fa15981ddc78842b00daab83.png)

Note:

r ∩ s = r -( r -s )

![Image](Lecture 2.2_artifacts/image_000017_bbaa640f2b7c7b6f18cdf441c797dcf1ce99e755b6ef0a9bbf7b581538bddcab.png)

Module 07

Partha Pratim

Das

Objectives &amp;

Outline

Relational

Operators

Aggregation

Operators

Module Summary

## Joining two relations - Cartesian-product

- Relation r , s

![Image](Lecture 2.2_artifacts/image_000018_a0176a3313262ecd1e9727a86ddb08333c0ec42f560f01141d35b77826a18d31.png)

![Image](Lecture 2.2_artifacts/image_000019_b277e58487b771d787ee36eb0221179f9d51ada48639e6bf8c4c7c48de92009b.png)

Partha Pratim Das

- r × s

![Image](Lecture 2.2_artifacts/image_000020_fde1132bf222cc20a3e76fd9bad23db921b22024804914407d2f2bc1b513e47e.png)

Module 07

Partha Pratim

Das

Objectives &amp;

Outline

Relational

Operators

Aggregation

Operators

Module Summary

## Cartesian-product - naming issue

- Relation r , s
- r × s

![Image](Lecture 2.2_artifacts/image_000021_c73eaa300396c98eb55b9d3b095f52f96b9fc31a7a8ab837d64fad7590978c98.png)

![Image](Lecture 2.2_artifacts/image_000022_0d9dfbde1de846c018eea32fe6aba21e8a9c7f3c69ef770101468a6cfb66a6e5.png)

Module 07

Partha Pratim

Das

Objectives &amp; Outline

Relational Operators

Aggregation Operators

Module Summary

## Renaming a Table

- Allows us to refer to a relation, (say E ) by more than one name.
- ρ X ( E )

returns the expression E under the name X

- Relations r

![Image](Lecture 2.2_artifacts/image_000023_66d8a128dead735d13b126ab41f2f705e07fc2d88c78a5598f3565df723660a6.png)

![Image](Lecture 2.2_artifacts/image_000024_720123ba8fc85f8bba37b5663ae12cf72bfeebcf36a00f1cf3af6dcb0e144a13.png)

Partha Pratim Das

- r × ρ s ( r )

![Image](Lecture 2.2_artifacts/image_000025_0d2e8daa05c74407b310229f101057782122d2bf078613dc8c643ca2fdb280b5.png)

## Module 07

Partha Pratim Das

Objectives &amp; Outline

Relational Operators

Aggregation Operators

Module Summary

## Composition of Operations

- Can build expressions using multiple operations
- Example: σ A = C ( r × s )
- r × s

· σ A = C ( r × s )

![Image](Lecture 2.2_artifacts/image_000026_23455047d65674637cb49ce6e93c50ef3a92b6858608443a823a4a4c62b5b976.png)

![Image](Lecture 2.2_artifacts/image_000027_f8e78888f2e234ee0ab433fdb9c07aad883112c63f8b6c2fdae9868c12b2880f.png)

Partha Pratim Das

![Image](Lecture 2.2_artifacts/image_000028_bbaa640f2b7c7b6f18cdf441c797dcf1ce99e755b6ef0a9bbf7b581538bddcab.png)

## Module 07

Partha Pratim Das

Objectives &amp; Outline

Relational Operators

Aggregation Operators

Module Summary

## Joining two relations - Natural Join

- Let r and s be relations on schemas R and S respectively. Then, the 'natural join' of relations R and S is a relation on schema R ∪ S obtained as follows:
- Consider each pair of tuples t r from r and t s from s .
- If t r and t s have the same value on each of the attributes in R ∩ S , add a tuple t to the result, where
- glyph[triangleright] t has the same value as t r on r
- glyph[triangleright] t has the same value as t s on s

![Image](Lecture 2.2_artifacts/image_000029_0d9dfbde1de846c018eea32fe6aba21e8a9c7f3c69ef770101468a6cfb66a6e5.png)

Module 07

Partha Pratim

Das

Objectives &amp;

Outline

Relational

Operators

Aggregation

Operators

Module Summary

## Natural Join Example

- Relations r , s :
- Natural Join

◦

r

glyph[triangleright]

glyph[triangleleft]

s

π A , r . B , C , r . D , E ( σ r . B = s . B ∧ r . D = s . D ( r × s ))

![Image](Lecture 2.2_artifacts/image_000030_14420a552c73d01aa3cfe279ebe7805a78819bd21daae47055aa0f6d6fabfe86.png)

![Image](Lecture 2.2_artifacts/image_000031_86be300d71262d993051503e2a6480fa1234ca96d1f31c8c64194b777b530802.png)

![Image](Lecture 2.2_artifacts/image_000032_35687e3f5ebada05f6fa62971d6dc0630bd5fb3952a7f7a0c2a6e1b466d30538.png)

Partha Pratim Das

![Image](Lecture 2.2_artifacts/image_000033_0d2e8daa05c74407b310229f101057782122d2bf078613dc8c643ca2fdb280b5.png)

Module 07

Partha Pratim Das

Objectives &amp; Outline

Relational Operators

Aggregation Operators

Module Summary

## Aggregation Operators

## Aggregation Operators

![Image](Lecture 2.2_artifacts/image_000034_b551d1d039a350a56349b412170007d20638ad0732feb40b06cdb100cf6ab680.png)

## Module 07

Partha Pratim Das

Objectives &amp; Outline

Relational Operators

Aggregation Operators

Module Summary

## Aggregate Operators

- Can we compute:
- SUM
- AVG
- MAX
- MIN

![Image](Lecture 2.2_artifacts/image_000035_0d9dfbde1de846c018eea32fe6aba21e8a9c7f3c69ef770101468a6cfb66a6e5.png)

## Module 07

Partha Pratim Das

Objectives &amp; Outline

Relational Operators

Aggregation Operators

Module Summary

## Notes about Relational Languages

- Each query input is a table (or set of tables)
- Each query output is a table
- All data in the output table appears in one of the input tables
- Relational Algebra is not Turing complete

![Image](Lecture 2.2_artifacts/image_000036_fde1132bf222cc20a3e76fd9bad23db921b22024804914407d2f2bc1b513e47e.png)

Module 07

Partha Pratim

Das

Objectives &amp;

Outline

Relational

Operators

Aggregation

Operators

Module Summary

## Summary of Relational Algebra Operators

| Symbol (Name)      | Example of Use                                                                                                        |
|--------------------|-----------------------------------------------------------------------------------------------------------------------|
| (Selection)        | 85000 salary                                                                                                          |
| (Selection)        | Return rows of the input relation that the predicate. satisfy                                                         |
| (Projection)       | ID (instructor) salary                                                                                                |
| (Projection)       | Output specified attributes from all rows of the input relation. Remove duplicate tuples from the output.             |
| Cartesian Product) | instructor X department                                                                                               |
| Cartesian Product) | Output all possible combinations of rows in instructor = department. and                                              |
| (Union)            | name (student)                                                                                                        |
| (Union)            | Output the union of tuples from the two input relations                                                               |
| Set Difference)    | (student)                                                                                                             |
| Set Difference)    | Output the set difference of tuples from the two input relations.                                                     |
| (Natural Join)     | instructor % department                                                                                               |
| (Natural Join)     | Output pairs of rows from the two input relations that have the same value on all attributes that have the same name. |

## Partha Pratim Das

![Image](Lecture 2.2_artifacts/image_000037_0d9dfbde1de846c018eea32fe6aba21e8a9c7f3c69ef770101468a6cfb66a6e5.png)

## Module 07

Partha Pratim Das

Objectives &amp; Outline

Relational Operators

Aggregation Operators

Module Summary

## Module Summary

- Introduced relational algebra
- Familiarized with the operators of relational algebra

Slides used in this presentation are borrowed from http://db-book.com/ with kind permission of the authors. Edited and new slides are marked with 'PPD'.
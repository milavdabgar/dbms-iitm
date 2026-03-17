![Image](Lecture 5.2_artifacts/image_000000_bbaa640f2b7c7b6f18cdf441c797dcf1ce99e755b6ef0a9bbf7b581538bddcab.png)

## Module 22

Partha Pratim Das

Objectives &amp; Outline

Functional Dependencies Closure of FDs

Module Summary

## Database Management Systems

Module 22: Relational Database Design/2

## Partha Pratim Das

Department of Computer Science and Engineering Indian Institute of Technology, Kharagpur ppd@cse.iitkgp.ac.in

![Image](Lecture 5.2_artifacts/image_000001_821f32da21a8bb9af0bddb9e2ff2419e915ba7e461f5dc4f05b60eaa6ed0b478.png)

## Module 22

Partha Pratim Das

Objectives &amp; Outline

Functional Dependencies Closure of FDs

Module Summary

## Module Recap

- Identified the features of good relational design
- Familiarized with the First Normal Form

![Image](Lecture 5.2_artifacts/image_000002_0d2e8daa05c74407b310229f101057782122d2bf078613dc8c643ca2fdb280b5.png)

Module 22

Partha Pratim Das

Objectives &amp; Outline

Functional Dependencies Closure of FDs

Module Summary

## Module Objectives

- To Introduce Functional Dependencies

![Image](Lecture 5.2_artifacts/image_000003_0d2e8daa05c74407b310229f101057782122d2bf078613dc8c643ca2fdb280b5.png)

Module 22

Partha Pratim Das

Objectives &amp; Outline

Functional Dependencies Closure of FDs

Module Summary

## Module Outline

- Functional Dependencies

![Image](Lecture 5.2_artifacts/image_000004_bbaa640f2b7c7b6f18cdf441c797dcf1ce99e755b6ef0a9bbf7b581538bddcab.png)

Module 22

Partha Pratim Das

Objectives &amp; Outline

Functional Dependencies

Closure of FDs

Module Summary

## Functional Dependencies

![Image](Lecture 5.2_artifacts/image_000005_bbaa640f2b7c7b6f18cdf441c797dcf1ce99e755b6ef0a9bbf7b581538bddcab.png)

## Module 22

Partha Pratim Das

Objectives &amp; Outline

Functional Dependencies

Closure of FDs

Module Summary

## Goal: Devise a Theory for Good Relations

- Decide whether a particular relation R is in 'good' form.
- In the case that a relation R is not in 'good' form, decompose it into a set of relations { R 1 , R 2 , . . . , R n } such that
- each relation is in good form
- the decomposition is a lossless-join decomposition
- The theory is based on:
- Functional dependencies
- Multivalued dependencies
- Other dependencies

![Image](Lecture 5.2_artifacts/image_000006_0d9dfbde1de846c018eea32fe6aba21e8a9c7f3c69ef770101468a6cfb66a6e5.png)

## Module 22

Partha Pratim Das

Objectives &amp; Outline

Functional Dependencies

Closure of FDs

Module Summary

## Functional Dependencies

- Constraints on the set of legal relations
- Require that the value for a certain set of attributes determines uniquely the value for another set of attributes
- A functional dependency is a generalization of the notion of a key

![Image](Lecture 5.2_artifacts/image_000007_bbaa640f2b7c7b6f18cdf441c797dcf1ce99e755b6ef0a9bbf7b581538bddcab.png)

Module 22

Partha Pratim Das

Objectives &amp; Outline

Functional Dependencies

Closure of FDs

Module Summary

## Functional Dependencies (2)

- Let R be a relation schema α ⊆ R and β ⊆ R
- The functional dependency or FD
- α → β

holds on R if and only if for any legal relations r ( R ), whenever any two tuples t 1 and t 2 of r agree on the attributes α , they also agree on the attributes β . That is,

<!-- formula-not-decoded -->

- Example: Consider r ( A , B ) with the following instance of r .
- On this instance, A → B does NOT hold, but B → A does hold. So we cannot have tuples like (2, 4), or (3, 5), or (4, 7) added to the current instance. Database Management Systems Partha Pratim Das

![Image](Lecture 5.2_artifacts/image_000008_161ab532df317073b117f157affb71c084307781898c1de51bc4b57e61d763d9.png)

![Image](Lecture 5.2_artifacts/image_000009_0d9dfbde1de846c018eea32fe6aba21e8a9c7f3c69ef770101468a6cfb66a6e5.png)

## Module 22

Partha Pratim Das

Objectives &amp; Outline

Functional Dependencies

Closure of FDs

Module Summary

## Functional Dependencies (3)

- K is a superkey for relation schema R if and only if K → R
- K is a candidate key for R if and only if
- K → R and
- for no α ⊂ K , α → R
- Functional dependencies allow us to express constraints that cannot be expressed using superkeys. Consider the schema:

inst dept(ID, name, salary, dept name, building, budget)

- We expect these functional dependencies to hold:

dept name → building dept name → budget

ID → budget but would not expect the following to hold: dept name → salary

![Image](Lecture 5.2_artifacts/image_000010_0d9dfbde1de846c018eea32fe6aba21e8a9c7f3c69ef770101468a6cfb66a6e5.png)

## Module 22

Partha Pratim Das

Objectives &amp; Outline

Functional Dependencies

Closure of FDs

Module Summary

## Functional Dependencies (4)

- We use functional dependencies to:
- test relations to see if they are legal under a given set of functional dependencies.
- glyph[triangleright] If a relation r is legal under a set F of functional dependencies, we say that r satisfies F
- specify constraints on the set of legal relations
- glyph[triangleright] We say that F holds on R if all legal relations on R satisfy the set of functional dependencies F
- Note : A specific instance of a relation schema may satisfy a functional dependency even if the functional dependency does not hold on all legal instances
- For example, a specific instance of instructor may, by chance, satisfy name → ID
- In such cases we do not say that F holds on R

![Image](Lecture 5.2_artifacts/image_000011_0d2e8daa05c74407b310229f101057782122d2bf078613dc8c643ca2fdb280b5.png)

## Module 22

Partha Pratim Das

Objectives &amp; Outline

Functional Dependencies

Closure of FDs

Module Summary

## Functional Dependencies (5)

- A functional dependency is trivial if it is satisfied by all instances of a relation
- ◦
- Example:
- glyph[triangleright] ID , name → ID
- glyph[triangleright] name → name
- In general, α → β is trivial if β ⊆ α .

![Image](Lecture 5.2_artifacts/image_000012_0d2e8daa05c74407b310229f101057782122d2bf078613dc8c643ca2fdb280b5.png)

## Module 22

Partha Pratim

Das

Objectives &amp;

Outline

Functional

Dependencies

Closure of FDs

Module Summary

## Functional Dependencies (6)

- Functional dependencies are:
- StudentID → Semester
- StudentID , Lecture → TA
- { StudentID , Lecture } → { TA , Semester }

|   StudentID | Semester   | Lecture           | TA    |
|-------------|------------|-------------------|-------|
|        1234 |            | Numerical Methods | John  |
|        1221 |            | Numerical Methods | Smith |
|        1234 |            | Visual Computing  | Bob   |
|        1201 |            | Numerical Methods | Peter |
|        1201 |            | Physics II        | Simon |

![Image](Lecture 5.2_artifacts/image_000013_821f32da21a8bb9af0bddb9e2ff2419e915ba7e461f5dc4f05b60eaa6ed0b478.png)

## Module 22

Partha Pratim

Das

Objectives &amp;

Outline

Functional

Dependencies

Closure of FDs

Module Summary

## Functional Dependencies (7)

## · Functional dependencies are:

|   Employee ID | Employee Name   | Department ID   | Department Name   |
|---------------|-----------------|-----------------|-------------------|
|          0001 | John Doe        |                 | Human Resources   |
|          0002 | Jane Doe        |                 | Marketing         |
|          0003 | John Smith      |                 | Human Resources   |
|          0004 | Jane Goodall    |                 | Sales             |

- EmployeeID → EmployeeName
- EmployeeID → DepartmentID
- DepartmentID → DepartmentName

![Image](Lecture 5.2_artifacts/image_000014_0d2e8daa05c74407b310229f101057782122d2bf078613dc8c643ca2fdb280b5.png)

## Module 22

Partha Pratim Das

Objectives &amp; Outline

Functional Dependencies Closure of FDs

Module Summary

## Functional Dependencies (9): Closure of a Set of FDs

- F = { A → B , B → C }
- F + = { A → B , B → C , A → C }

![Image](Lecture 5.2_artifacts/image_000015_0d9dfbde1de846c018eea32fe6aba21e8a9c7f3c69ef770101468a6cfb66a6e5.png)

Module 22

Partha Pratim Das

Objectives &amp; Outline

Functional Dependencies Closure of FDs

Module Summary

## Module Summary

- Introduced the notion of Functional Dependencies

Slides used in this presentation are borrowed from http://db-book.com/ with kind permission of the authors.

Edited and new slides are marked with 'PPD'.
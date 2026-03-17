![Image](Lecture 6.2_artifacts/image_000000_bbaa640f2b7c7b6f18cdf441c797dcf1ce99e755b6ef0a9bbf7b581538bddcab.png)

## Module 27

Partha Pratim Das

Objectives &amp; Outline

Decomposition to 3NF

Test

Algorithm

Practice Problem

Decomposition to

BCNF

Test

Algorithm

Practice Problem

Comparison

Module Summary

## Database Management Systems

Module 27: Relational Database Design/7: Normal Forms

## Partha Pratim Das

Department of Computer Science and Engineering Indian Institute of Technology, Kharagpur ppd@cse.iitkgp.ac.in

Partha Pratim Das

![Image](Lecture 6.2_artifacts/image_000001_821f32da21a8bb9af0bddb9e2ff2419e915ba7e461f5dc4f05b60eaa6ed0b478.png)

Module 27

Partha Pratim Das

Objectives &amp; Outline

Decomposition to

3NF

Test

Algorithm

Practice Problem

Decomposition to

BCNF

Test

Algorithm

Practice Problem

Comparison

Module Summary

## Module Recap

- Studied the Normal Forms and their Importance in Relational Design - how progressive increase of constraints can minimize redundancy in a schema

![Image](Lecture 6.2_artifacts/image_000002_0d2e8daa05c74407b310229f101057782122d2bf078613dc8c643ca2fdb280b5.png)

## Module 27

Partha Pratim Das

Objectives &amp; Outline

Decomposition to

3NF

Test

Algorithm

Practice Problem

Decomposition to

BCNF

Test

Algorithm

Practice Problem

Comparison

Module Summary

## Module Objectives

- To Learn the Decomposition Algorithm for a Relation to 3NF
- To Learn the Decomposition Algorithm for a Relation to BCNF

![Image](Lecture 6.2_artifacts/image_000003_0d2e8daa05c74407b310229f101057782122d2bf078613dc8c643ca2fdb280b5.png)

Module 27

Partha Pratim Das

Objectives &amp; Outline

Decomposition to

3NF

Test

Algorithm

Practice Problem

Decomposition to

BCNF

Test

Algorithm

Practice Problem

Comparison

Module Summary

## Module Outline

- Decomposition to 3NF
- Decomposition to BCNF

![Image](Lecture 6.2_artifacts/image_000004_fde1132bf222cc20a3e76fd9bad23db921b22024804914407d2f2bc1b513e47e.png)

## Module 27

Partha Pratim Das

Objectives &amp; Outline

Decomposition to 3NF

Test

Algorithm

Practice Problem

Decomposition to

BCNF

Test

Algorithm

Practice Problem

Comparison

Module Summary

## Decomposition to 3NF

## Decomposition to 3NF

![Image](Lecture 6.2_artifacts/image_000005_bbaa640f2b7c7b6f18cdf441c797dcf1ce99e755b6ef0a9bbf7b581538bddcab.png)

## Module 27

Partha Pratim Das

Objectives &amp; Outline

Decomposition to 3NF

Test

Algorithm

Practice Problem

Decomposition to BCNF

Test

Algorithm

Practice Problem

Comparison

Module Summary

## 3NF Decomposition: Motivation

- There are some situations where
- BCNF is not dependency preserving, and
- Efficient checking for FD violation on updates is important
- Solution: define a weaker normal form, called Third Normal Form (3NF)
- Allows some redundancy (with resultant problems; as seen above)
- But functional dependencies can be checked on individual relations without computing a join
- There is always a lossless-join, dependency-preserving decomposition into 3NF

![Image](Lecture 6.2_artifacts/image_000006_bbaa640f2b7c7b6f18cdf441c797dcf1ce99e755b6ef0a9bbf7b581538bddcab.png)

## Module 27

Partha Pratim Das

Objectives &amp; Outline

Decomposition to 3NF

Test

Algorithm

Practice Problem

Decomposition to BCNF

Test

Algorithm

Practice Problem

Comparison

Module Summary

## 3NF Decomposition (2): 3NF Definition

- A relational schema R is in 3NF if for every FD X → A associated with R either
- A ⊆ X (that is, the FD is trivial) or
- X is a superkey of R or
- A is part of some candidate key (not just superkey!)
- A relation in 3NF is naturally in 2NF

![Image](Lecture 6.2_artifacts/image_000007_bbaa640f2b7c7b6f18cdf441c797dcf1ce99e755b6ef0a9bbf7b581538bddcab.png)

## Module 27

Partha Pratim Das

Objectives &amp; Outline

Decomposition to 3NF

Test

Algorithm

Practice Problem

Decomposition to BCNF

Test

Algorithm

Practice Problem

Comparison

Module Summary

## 3NF Decomposition (3): Testing for 3NF

- Optimization: Need to check only FDs in F , need not check all FDs in F + .
- Use attribute closure to check for each dependency α → β , if α is a superkey.
- If α is not a superkey, we have to verify if each attribute in β is contained in a candidate key of R
- This test is rather more expensive, since it involve finding candidate keys
- Testing for 3NF has been shown to be NP-hard
- Decomposition into 3NF can be done in polynomial time

![Image](Lecture 6.2_artifacts/image_000008_bbaa640f2b7c7b6f18cdf441c797dcf1ce99e755b6ef0a9bbf7b581538bddcab.png)

## Module 27

Partha Pratim Das

Objectives &amp; Outline

Decomposition to 3NF

Test

Algorithm

Practice Problem

Decomposition to BCNF

Test

Algorithm

Practice Problem

Comparison

Module Summary

## 3NF Decomposition (4): Algorithm

- Given: relation R , set F of functional dependencies
- Find: decomposition of R into a set of 3NF relation R i
- Algorithm:
- a) Eliminate redundant FDs, resulting in a canonical cover F c of F
- b) Create a relation R i = XY for each FD X → Y in F c
- c) If the key K of R does not occur in any relation R i , create one more relation R i = K

![Image](Lecture 6.2_artifacts/image_000009_bbaa640f2b7c7b6f18cdf441c797dcf1ce99e755b6ef0a9bbf7b581538bddcab.png)

Module 27

Partha Pratim Das

Objectives &amp; Outline

Decomposition to

3NF

Test

Algorithm

Practice Problem

Decomposition to

BCNF

Test

Algorithm

Practice Problem

Comparison

Module Summary

## 3NF Decomposition (5): Algorithm

Let Fc be a canonical cover for F ; i := 0; for each functional dependency α → β in Fc do if none of the schemas Rj , 1 ≤ j ≤ i contains αβ then begin i := i +1; Ri := αβ end if none of the schemas Rj , 1 ≤ j ≤ i contains a candidate key for R then begin i := i +1; Ri := any candidate key for R ; end /* Optionally, remove redundant relations */ repeat if any schema Rj is contained in another schema Rk then /* delete Rj */ Rj = R ; i = i -1; return ( R 1 , R 2 , · · · , Ri ) Database Management Systems Partha Pratim Das

![Image](Lecture 6.2_artifacts/image_000010_bbaa640f2b7c7b6f18cdf441c797dcf1ce99e755b6ef0a9bbf7b581538bddcab.png)

## Module 27

Partha Pratim Das

Objectives &amp; Outline

Decomposition to 3NF

Test

Algorithm

Practice Problem

Decomposition to BCNF

Test

Algorithm

Practice Problem

Comparison

Module Summary

## 3NF Decomposition (6): Algorithm

- Upon decomposition:
- Each relation schema R i is in 3NF
- Decomposition is
- glyph[triangleright] Dependency Preserving
- glyph[triangleright] Lossless Join
- Prove these properties

![Image](Lecture 6.2_artifacts/image_000011_bbaa640f2b7c7b6f18cdf441c797dcf1ce99e755b6ef0a9bbf7b581538bddcab.png)

## Module 27

Partha Pratim Das

Objectives &amp; Outline

Decomposition to 3NF

Test

Algorithm

Practice Problem

Decomposition to BCNF

Test

Algorithm

Practice Problem

Comparison

Module Summary

## 3NF Decomposition (7): Example

- Relation schema:

cust banker branch = (customer id, employee id, branch name, type)

- The functional dependencies for this relation schema are:
- a) customer id, employee id → branch name, type
- b) employee id → branch name
- c) customer id, branch name → employee id
- We first compute a canonical cover
- branch name is extraneous in the RHS of the 1 st dependency
- No other attribute is extraneous, so we get F c = customer id, employee id → type employee id → branch name customer id, branch name → employee id

![Image](Lecture 6.2_artifacts/image_000012_bbaa640f2b7c7b6f18cdf441c797dcf1ce99e755b6ef0a9bbf7b581538bddcab.png)

## Module 27

Partha Pratim Das

Objectives &amp; Outline

Decomposition to 3NF

Test

Algorithm

Practice Problem

Decomposition to BCNF

Test

Algorithm

Practice Problem

Comparison

Module Summary

## 3NF Decomposition (8): Example

- The for
- loop generates following 3NF schema:

(customer id, employee id, type) (employee id, branch name) (customer id, branch name, employee id)

- Observe that (customer id, employee id, type) contains a candidate key of the original schema, so no further relation schema needs be added
- At end of for loop, detect and delete schemas, such as (employee id, branch name) , which are subsets of other schemas
- result will not depend on the order in which FDs are considered
- •
- The resultant simplified 3NF schema is: (customer id, employee id, type) (customer id, branch name, employee id)

![Image](Lecture 6.2_artifacts/image_000013_bbaa640f2b7c7b6f18cdf441c797dcf1ce99e755b6ef0a9bbf7b581538bddcab.png)

## Module 27

Partha Pratim Das

Objectives &amp; Outline

Decomposition to

3NF

Test

Algorithm

Practice Problem

Decomposition to

BCNF

Test

Algorithm

Practice Problem

Comparison

Module Summary

## Practice Problem for 3NF Decomposition (1)

- R = ABCDEFGH
- FDs = { A → B , ABCD → E , EF → GH , ACDF → EG }

Solution is given in the next slide (hidden from presentation - check after you have solved

![Image](Lecture 6.2_artifacts/image_000014_bbaa640f2b7c7b6f18cdf441c797dcf1ce99e755b6ef0a9bbf7b581538bddcab.png)

## Module 27

Partha Pratim Das

Objectives &amp; Outline

Decomposition to

3NF

Test

Algorithm

Practice Problem

Decomposition to

BCNF

Test

Algorithm

Practice Problem

Comparison

Module Summary

## Practice Problem for 3NF Decomposition (2)

- R = CSJDPQV
- FDs = { C → CSJDPQV , SD → P , JP → C , J → S }

Solution is given in the next slide (hidden from presentation - check after you have solved)

![Image](Lecture 6.2_artifacts/image_000015_0d9dfbde1de846c018eea32fe6aba21e8a9c7f3c69ef770101468a6cfb66a6e5.png)

## Module 27

Partha Pratim Das

Objectives &amp; Outline

Decomposition to 3NF

Test

Algorithm

Practice Problem

Decomposition to BCNF

Test

Algorithm

Practice Problem

Comparison

Module Summary

## Practice Problem for 3NF Decomposition (3)

## Decompose the following schema to 3NF in the following steps

- Compute all keys for R
- Compute a Canonical Cover Fc for F Put the FDs into alphabetical order.
- Using Fc , employ the 3NFdecom algorithm to obtain a lossless and dependency preserving decomposition of relation R into a collection of relations that are in 3NF
- Does your schema allow redundancy?
- R ( ABCDEFGH
- ): F = { A → CD , ACF → G , AD → BEF , BCG → D , CF → AH , CH → G , D → B , H → DEG
- R ( ABCDE
- }
- ): F = { A → B , A → C , C → D , A → E
- R ( ABCDE ): F = { A → BC , CD → E , B → D , E → A
- }
- R ( ABCD
- ): F = { A → D , AB → C , AD → C , B → C , D → AB
- }

}

![Image](Lecture 6.2_artifacts/image_000016_fde1132bf222cc20a3e76fd9bad23db921b22024804914407d2f2bc1b513e47e.png)

Module 27

Partha Pratim Das

Objectives &amp; Outline

Decomposition to

3NF

Test

Algorithm

Practice Problem

Decomposition to BCNF

Test

Algorithm

Practice Problem

Comparison

Module Summary

## Decomposition to BCNF

## Decomposition to BCNF

![Image](Lecture 6.2_artifacts/image_000017_0d9dfbde1de846c018eea32fe6aba21e8a9c7f3c69ef770101468a6cfb66a6e5.png)

## Module 27

Partha Pratim Das

Objectives &amp; Outline

Decomposition to 3NF

Test

Algorithm

Practice Problem

Decomposition to BCNF

Test

Algorithm

Practice Problem

Comparison

Module Summary

## BCNF Decomposition: BCNF Definition

- A relation schema R is in BCNF with respect to a set F of FDs if for all FDs in F + of the form

α → β , where α ⊆ R and β ⊆ R ◦ α → β is trivial (that is, β ⊆ α ) ◦ α is a superkey for R

at least one of the following holds:

![Image](Lecture 6.2_artifacts/image_000018_bbaa640f2b7c7b6f18cdf441c797dcf1ce99e755b6ef0a9bbf7b581538bddcab.png)

Module 27

Partha Pratim Das

Objectives &amp; Outline

Decomposition to 3NF

Test

Algorithm

Practice Problem

Decomposition to BCNF

Test

Algorithm

Practice Problem

Comparison

Module Summary

## BCNF Decomposition (2): Testing for BCNF

- To check if a non-trivial dependency α → β causes a violation of BCNF
- a) Compute α + (the attribute closure of α ), and
- b) Verify that it includes all attributes of R , that is, it is a superkey of R .
- Simplified test: To check if a relation schema R is in BCNF, it suffices to check only the dependencies in the given set F for violation of BCNF, rather than checking all dependencies in F + .
- If none of the dependencies in F causes a violation of BCNF, then none of the dependencies in F + will cause a violation of BCNF either.
- However, simplified test using only F is incorrect when testing a relation in a decomposition of R
- Consider R = ( A , B , C , D , E ), with F = { A → B , BC → D }
- glyph[triangleright] Decompose R into R 1 = ( A , B ) and R 2 = ( A , C , D , E )
- glyph[triangleright] Neither of the dependencies in F contain only attributes from ( A , C , D , E ) so we might be mislead into thinking R 2 satisfies BCNF.
- glyph[triangleright] In fact, dependency AC → D in F + shows R 2 is not in BCNF.

Database Management Systems

Partha Pratim Das

![Image](Lecture 6.2_artifacts/image_000019_bbaa640f2b7c7b6f18cdf441c797dcf1ce99e755b6ef0a9bbf7b581538bddcab.png)

## Module 27

Partha Pratim Das

Objectives &amp; Outline

Decomposition to 3NF

Test

Algorithm

Practice Problem

Decomposition to BCNF

Test

Algorithm

Practice Problem

Comparison

Module Summary

## BCNF Decomposition (3): Testing for BCNF Decomposition

- To check if a relation R i in a decomposition of R is in BCNF,
- Either test R i for BCNF with respect to the restriction of F to R i (that is, all FDs in F + that contain only attributes from R i )
- Or use the original set of dependencies F that hold on R , but with the following test:
- glyph[triangleright] for every set of attributes α ⊆ R i , check that α + (the attribute closure of α ) either includes no attribute of R i -α , or includes all attributes of R i .
- glyph[triangleright] If the condition is violated by some α → β in F , the dependency α → ( α + -α ) ∩ R i
- can be shown to hold on R i , and R i violates BCNF.
- glyph[triangleright] We use above dependency to decompose Ri

![Image](Lecture 6.2_artifacts/image_000020_bbaa640f2b7c7b6f18cdf441c797dcf1ce99e755b6ef0a9bbf7b581538bddcab.png)

Module 27

Partha Pratim Das

Objectives &amp; Outline

Decomposition to

3NF

Test

Algorithm

Practice Problem

Decomposition to BCNF

Test

Algorithm

Practice Problem Comparison

Module Summary

## BCNF Decomposition (4): Testing Dependency Preservation: Using Closure Set of FD (Exp. Algo.): Module 25

Consider the example given below, we will apply both the algorithms to check dependency preservation and will discuss the results.

- R ( A, B, C, D )
- F = { A → B , B → C , C → D , D → A }
- Decomposition:
- R1 (A, B) R2 (B, C) R3 (C, D)
- A → B is preserved on table R1
- B → C is preserved on table R2
- C → D is preserved on table R3
- We have to check whether the one remaining FD: D → A is preserved or not.
- F ′ = F 1 ∪ F 2 ∪ F 3.
- Checking for:
- D → A in F ′ +
- glyph[triangleright] D → C (from R3), C → B (from R2), B → A (from R1) : D → A (By Transitivity) Hence all dependencies are preserved .

| R1                       | R2                       | R3                       |
|--------------------------|--------------------------|--------------------------|
| F 1= { A → AB , B → BA } | F 2= { B → BC , C → CB } | F 3= { C → CD , D → DC } |

Database Management Systems

Partha Pratim Das

27.21

![Image](Lecture 6.2_artifacts/image_000021_32155ccc63eaf8ac3b5d36be7560257f854d0b99536286a17a16546fbab339af.png)

Module 27

Partha Pratim Das

Objectives &amp; Outline

Decomposition to

3NF

Test

Algorithm

Practice Problem

Decomposition to BCNF

Test

Algorithm

Practice Problem

Comparison

Module Summary

## BCNF Decomposition (4): Testing Dependency Preservation: Using Closure of Attributes (Poly. Algo.): Module 25

- R ( ABCD ) :. F = { A → B , B → C , C → D , D → A }
- Decomp = { AB , BC , CD }
- On projections:

| RI    | R2   | R3   |
|-------|------|------|
| F1    | F2   | F3   |
| A ~ B |      |      |

In this algo F1, F2, F3 are not the closure sets, rather the set of dependencies directly applicable on R1, R2, R3 respectively.

- Need to check for: A → B , B → C , C → D , D → A
- ( D ) + / F 1 = D . ( D ) + / F 2 = D . ( D ) + / F 3 = D . So, D → A could not be preserved.
- In the previous method we saw the dependency was preserved. In reality also it is preserved. Therefore the polynomial time algorithm may not work in case of all examples. To prove preservation Algo 2 is sufficient but not necessary whereas Algo 1 is both sufficient as well as necessary.

Note: This difference in result can occur in any example where a functional dependency of one decomposed table uses another functional dependency in its closure which is not applicable on any of the decomposed table because of absence of all attributes in the table.

Partha Pratim Das

![Image](Lecture 6.2_artifacts/image_000022_0d9dfbde1de846c018eea32fe6aba21e8a9c7f3c69ef770101468a6cfb66a6e5.png)

## Module 27

Partha Pratim Das

Objectives &amp; Outline

Decomposition to 3NF

Test

Algorithm

Practice Problem

Decomposition to BCNF

Test

Algorithm

Practice Problem

Comparison

Module Summary

## BCNF Decomposition (4): Algorithm

- a) For all dependencies A → B in F + , check if A is a superkey
- By using attribute closure
- b) If not, then
- Choose a dependency in F + that breaks the BCNF rules, say A → B
- Create R 1 = AB
- Create R 2 = ( R -( B -A ))
- Note that: R 1 ∩ R 2 = A and A → AB (= R 1), so this is lossless decomposition
- c) Repeat for R 1, and R 2
- By defining F 1 + to be all dependencies in F that contain only attributes in R 1
- Similarly F 2 +

![Image](Lecture 6.2_artifacts/image_000023_bbaa640f2b7c7b6f18cdf441c797dcf1ce99e755b6ef0a9bbf7b581538bddcab.png)

Module 27

Partha Pratim Das

Objectives &amp; Outline

Decomposition to 3NF

Test

Algorithm

Practice Problem

Decomposition to BCNF

Test

Algorithm

Practice Problem

Comparison

Module Summary

## BCNF Decomposition (5): Algorithm

result := { R } ; done := false ; compute F + ; while (not done) do if (there is a schema R i in result that is not in BCNF) then begin let α → β be a nontrivial functional dependency that holds on R i such that α → β is not in F + , and α ∩ β = φ ; result := ( result - R i ) ∪ ( R i - β ) ∪ ( α, β ); end

else done := true ;

Note: each R i is in BCNF, and decomposition is lossless-join.

Database Management Systems

Partha Pratim Das

![Image](Lecture 6.2_artifacts/image_000024_bbaa640f2b7c7b6f18cdf441c797dcf1ce99e755b6ef0a9bbf7b581538bddcab.png)

Module 27

Partha Pratim Das

Objectives &amp; Outline

Decomposition to 3NF

Test

Algorithm

Practice Problem

Decomposition to

BCNF

Test

Algorithm

Practice Problem

Comparison

Module Summary

## BCNF Decomposition (6): Example

- R = ( A , B , C ) F = { A → B B → C } Key = { A }
- R is not in BCNF ( B → C but B is not superkey)
- Decomposition
- R 1 = ( B , C )
- R 2 = ( A , B )

![Image](Lecture 6.2_artifacts/image_000025_bbaa640f2b7c7b6f18cdf441c797dcf1ce99e755b6ef0a9bbf7b581538bddcab.png)

Module 27

Partha Pratim Das

Objectives &amp; Outline

Decomposition to 3NF

Test

Algorithm

Practice Problem

Decomposition to BCNF

Test

Algorithm

Practice Problem

Comparison

Module Summary

## BCNF Decomposition (7): Example

- class (course id, title, dept name, credits, sec id, semester, year, building, room number, capacity, time slot id)
- Functional dependencies:
- course id → title, dept name, credits
- building, room number → capacity
- course id, sec id, semester, year → building, room number, time slot id
- A candidate key course id, sec id, semester, year .
- BCNF Decomposition:
- course id → title, dept name, credits holds
- glyph[triangleright] but course id is not a superkey
- We replace class by:
- glyph[triangleright] course(course id, title, dept name, credits)
- glyph[triangleright] class-1 (course id, sec id, semester, year, building, room number, capacity, time slot id)

Partha Pratim Das

![Image](Lecture 6.2_artifacts/image_000026_bbaa640f2b7c7b6f18cdf441c797dcf1ce99e755b6ef0a9bbf7b581538bddcab.png)

## Module 27

Partha Pratim Das

Objectives &amp; Outline

Decomposition to 3NF

Test

Algorithm

Practice Problem

Decomposition to BCNF

Test

Algorithm

Practice Problem

Comparison

Module Summary

## BCNF Decomposition (8): Example

- course is in BCNF
- How do we know this?
- building, room number → capacity holds on
- class-1(course id, sec id, semester, year, building, room number, capacity, time slot id)
- But { building, room number } is not a superkey for class-1 .
- We replace class-1 by:
- glyph[triangleright] classroom (building, room number, capacity)
- glyph[triangleright] section (course id, sec id, semester, year, building, room number, time slot id)
- classroom and section are in BCNF.

![Image](Lecture 6.2_artifacts/image_000027_0d9dfbde1de846c018eea32fe6aba21e8a9c7f3c69ef770101468a6cfb66a6e5.png)

Module 27

Partha Pratim Das

Objectives &amp; Outline

Decomposition to 3NF

Test

Algorithm

Practice Problem

Decomposition to BCNF

Test

Algorithm

Practice Problem

Comparison

Module Summary

## BCNF Decomposition (8): Dependency Preservation

- It is not always possible to get a BCNF decomposition that is dependency preserving
- R = ( J , K , L )
- F = { JK → L L → K }

Two candidate keys = JK and JL

- R is not in BCNF
- Any decomposition of R will fail to preserve

JK → L

This implies that testing for JK → L requires a join

![Image](Lecture 6.2_artifacts/image_000028_0d9dfbde1de846c018eea32fe6aba21e8a9c7f3c69ef770101468a6cfb66a6e5.png)

## Module 27

Partha Pratim Das

Objectives &amp; Outline

Decomposition to 3NF

Test

Algorithm

Practice Problem

Decomposition to BCNF

Test

Algorithm

Practice Problem

Comparison

Module Summary

## Practice Problem for BCNF Decomposition

## Decompose the following schema to BCNF

- R = ABCDE . F = { A → B , BC → D }
- R = ABCDEH . F = { A → BC , E → HA }
- R = CSJDPQV . F = { C → CSJDPQV , SD → P , JP → C , J → S }
- R = ABCD . F = { C → D , C → A , B → C }

![Image](Lecture 6.2_artifacts/image_000029_de9fe6c76df380f60438ed658b199586d6f3470997f8a8b07f4706bc06dbdbc4.png)

![Image](Lecture 6.2_artifacts/image_000030_fde1132bf222cc20a3e76fd9bad23db921b22024804914407d2f2bc1b513e47e.png)

Module 27

Partha Pratim

Das

Objectives &amp; Outline

Decomposition to

3NF

Test

Algorithm

Practice Problem

Decomposition to

BCNF

Test

Algorithm

Practice Problem

Comparison

Module Summary

## Comparison of BCNF and 3NF

- It is always possible to decompose a relation into a set of relations that are in 3NF such that:
- the decomposition is lossless
- the dependencies are preserved
- It is always possible to decompose a relation into a set of relations that are in BCNF such that:
- the decomposition is lossless
- it may not be possible to preserve dependencies.

|   S# | 3NF                                                                                 | BCNF                                              |
|------|-------------------------------------------------------------------------------------|---------------------------------------------------|
|    1 | It concentrates on Primary Key                                                      | It concentrates on Candidate Key                  |
|    2 | Redundancy is high as compared to BCNF                                              | 0% redundancy                                     |
|    3 | It preserves all the dependencies                                                   | It may not preserve the dependencies              |
|    4 | A dependency X → Y is allowed in 3NF if X is a super key or Y is a part of some key | A dependency X → Y is allowed if X is a super key |

![Image](Lecture 6.2_artifacts/image_000031_0d9dfbde1de846c018eea32fe6aba21e8a9c7f3c69ef770101468a6cfb66a6e5.png)

Module 27

Partha Pratim Das

Objectives &amp; Outline

Decomposition to 3NF

Test

Algorithm

Practice Problem

Decomposition to

BCNF

Test

Algorithm

Practice Problem

Comparison

Module Summary

## Module Summary

- Learnt how to decompose a schema into 3NF while preserving dependency and lossless join
- Learnt how to decompose a schema into BCNF with lossless join

Slides used in this presentation are borrowed from http://db-book.com/ with kind permission of the authors. Edited and new slides are marked with 'PPD'.
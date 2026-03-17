![Image](Lecture 5.3_artifacts/image_000000_bbaa640f2b7c7b6f18cdf441c797dcf1ce99e755b6ef0a9bbf7b581538bddcab.png)

## Module 23

Partha Pratim Das

Objectives &amp; Outline

FD Theory Armstrong's Axioms Closure of FDs Closure of Attributes

Decomposition using FDs

BCNF

3NF

Normalization

Module Summary

## Database Management Systems

Module 23: Relational Database Design/3

## Partha Pratim Das

Department of Computer Science and Engineering Indian Institute of Technology, Kharagpur ppd@cse.iitkgp.ac.in

![Image](Lecture 5.3_artifacts/image_000001_821f32da21a8bb9af0bddb9e2ff2419e915ba7e461f5dc4f05b60eaa6ed0b478.png)

## Module 23

Partha Pratim Das

Objectives &amp; Outline

FD Theory

Armstrong's Axioms

Closure of FDs

Closure of Attributes

Decomposition using FDs

BCNF

3NF

Normalization

Module Summary

## Module Recap

- Introduced the notion of Functional Dependencies

![Image](Lecture 5.3_artifacts/image_000002_0d9dfbde1de846c018eea32fe6aba21e8a9c7f3c69ef770101468a6cfb66a6e5.png)

## Module 23

Partha Pratim Das

Objectives &amp; Outline

FD Theory

Armstrong's Axioms

Closure of FDs

Closure of Attributes

Decomposition using FDs

BCNF

3NF

Normalization

Module Summary

## Module Objectives

- To develop the theory of functional dependencies
- To understand how a schema can be decomposed for a 'good' design using functional dependencies

![Image](Lecture 5.3_artifacts/image_000003_0d9dfbde1de846c018eea32fe6aba21e8a9c7f3c69ef770101468a6cfb66a6e5.png)

## Module 23

Partha Pratim Das

Objectives &amp; Outline

FD Theory

Armstrong's Axioms

Closure of FDs

Closure of Attributes

Decomposition using FDs

BCNF

3NF

Normalization

Module Summary

## Module Outline

- Functional Dependency Theory
- Decomposition Using Functional Dependencies

![Image](Lecture 5.3_artifacts/image_000004_821f32da21a8bb9af0bddb9e2ff2419e915ba7e461f5dc4f05b60eaa6ed0b478.png)

## Module 23

Partha Pratim Das

Objectives &amp; Outline

FD Theory

Armstrong's Axioms

Closure of FDs

Closure of Attributes

Decomposition using FDs

BCNF

3NF

Normalization

Module Summary

## Functional Dependency Theory

## Functional Dependency Theory

![Image](Lecture 5.3_artifacts/image_000005_0d9dfbde1de846c018eea32fe6aba21e8a9c7f3c69ef770101468a6cfb66a6e5.png)

Module 23

Partha Pratim Das

Objectives &amp; Outline

FD Theory

Armstrong's Axioms

Closure of FDs

Closure of Attributes

Decomposition using FDs

BCNF

3NF

Normalization

Module Summary

## Functional Dependencies: Armstrong's Axioms

- Given a set of Functional Dependencies F , we can infer new dependencies by the Armstrong's Axioms :
- These axioms can be repeatedly applied to generate new FDs and added to F
- A new FD obtained by applying the axioms is said to the logically implied by F
- The process of generations of FDs terminate after finite number of steps and we call it the Closure Set F + for FDs F . This is the set of all FDs logically implied by F
- Clearly, F ⊆ F +
- These axioms are
- Sound (generate only functional dependencies that actually hold), and
- Complete (eventually generate all functional dependencies that hold)
- Prove the axioms from definitions of FDs
- Prove the soundness and completeness of the axioms Database Management Systems Partha Pratim Das

- Reflexivity : if β ⊆ α , then α → β

- Augmentation : if α → β , then γα → γβ

- Transitivity : if α → β and β → γ , then α → γ

![Image](Lecture 5.3_artifacts/image_000006_0d2e8daa05c74407b310229f101057782122d2bf078613dc8c643ca2fdb280b5.png)

## Module 23

Partha Pratim Das

Objectives &amp; Outline

FD Theory Armstrong's Axioms

Closure of FDs

Closure of Attributes

Decomposition using FDs

BCNF

3NF

Normalization

Module Summary

## Functional Dependencies (2): Closure of a Set FDs

- F = { A → B , B → C }
- F + = { A → B , B → C , A → C }

![Image](Lecture 5.3_artifacts/image_000007_bbaa640f2b7c7b6f18cdf441c797dcf1ce99e755b6ef0a9bbf7b581538bddcab.png)

Module 23

Partha Pratim

Das

Objectives &amp; Outline

FD Theory

Armstrong's Axioms

Closure of FDs

Closure of Attributes

Decomposition using FDs

BCNF

3NF

Normalization

Module Summary

## Functional Dependencies (3): Closure of a Set FDs

- R = ( A , B , C , G , H , I )
- F = { A → B A → C CG → H CG → I B → H }
- Some members of F +
- A → H
- glyph[triangleright] by transitivity from A → B and B → H
- AG → I
- glyph[triangleright] by augmenting A → C with G , to get AG → CG and then transitivity with CG → I
- CG → HI

glyph[triangleright]

by augmenting with

I

to infer

Database Management Systems

CG

CGI

→

→

I

with

HI

CG

to infer

CG

→

, and then transitivity

Partha Pratim Das

CGI

, and augmenting

CG

→

H

![Image](Lecture 5.3_artifacts/image_000008_32155ccc63eaf8ac3b5d36be7560257f854d0b99536286a17a16546fbab339af.png)

## Module 23

Partha Pratim Das

Objectives &amp; Outline

FD Theory Armstrong's Axioms

Closure of FDs

Closure of Attributes

Decomposition using FDs

BCNF

3NF

Normalization

Module Summary

## Functional Dependencies (4): Closure of a Set FDs: Computing F +

- To compute the closure of a set of functional dependencies F : F + ← F

repeat for each functional dependency f in F + apply reflexivity and augmentation rules on f add the resulting functional dependencies to F + for each pair of functional dependencies f 1 and f 2 in F + if f 1 and f 2 can be combined using transitivity then add the resulting functional dependency to F +

until F + does not change any further

- Note : We shall see an alternative procedure for this task later

![Image](Lecture 5.3_artifacts/image_000009_0d9dfbde1de846c018eea32fe6aba21e8a9c7f3c69ef770101468a6cfb66a6e5.png)

## Module 23

Partha Pratim Das

Objectives &amp; Outline

FD Theory Armstrong's Axioms

Closure of FDs

Closure of Attributes

Decomposition using FDs

BCNF

3NF

Normalization

Module Summary

## Functional Dependencies (5): Armstrong's Axioms: Derived Rules

- Additional Derived Rules:
- Union : if α → β holds and α → γ holds, then α → βγ holds
- Decomposition : if α → βγ holds, then α → β holds and α → γ holds
- Pseudotransitivity : if α → β holds and γβ → δ holds, then αγ → δ holds
- The above rules can be inferred from basic Armstrong's axioms (and hence are not included in the basic set). They can be proven independently too
- Reflexivity : if β ⊆ α , then α → β
- Augmentation : if α → β , then γα → γβ
- Transitivity : if α → β and β → γ , then α → γ
- Prove the Rules from:
- Basic Axioms
- The definitions of FDs

![Image](Lecture 5.3_artifacts/image_000010_0d9dfbde1de846c018eea32fe6aba21e8a9c7f3c69ef770101468a6cfb66a6e5.png)

## Module 23

Partha Pratim Das

Objectives &amp; Outline

FD Theory

Armstrong's Axioms

Closure of FDs

Closure of Attributes

Decomposition using FDs

BCNF

3NF

Normalization

Module Summary

## Functional Dependencies (6): Closure of Attribute Sets

- Given a set of attributes α , define the closure of α under F (denoted by α + ) as the set of attributes that are functionally determined by α under F
- Algorithm to compute α + , the closure of α under F
- result ← α

while

(changes to result

)

do for each β → γ in F do

begin if β ⊆ result then result ← result ∪ γ

end

![Image](Lecture 5.3_artifacts/image_000011_bbaa640f2b7c7b6f18cdf441c797dcf1ce99e755b6ef0a9bbf7b581538bddcab.png)

Module 23

Partha Pratim Das

Objectives &amp; Outline

FD Theory

Armstrong's Axioms

Closure of FDs

Closure of Attributes

Decomposition using FDs

BCNF

3NF

Normalization

Module Summary

## Functional Dependencies (7): Closure of Attribute Sets: Example

- R = ( A , B , C , G , H , I )
- F = { A → B , A → C , CG → H , CG → I , B → H }
- ( AG ) +
- a) result = AG
- b) result = ABCG ( A → C and A → B )
- c) result = ABCGH ( CG → H and CG ⊆ AGBC )
- d) result = ABCGHI ( CG → I and CG ⊆ AGBCH )
- Is AG a candidate key?
- a) Is AG a super key?
- i) Does AG → R ? == Is ( AG ) + ⊇ R
- b) Is any subset of AG a superkey?
- i) Does A → R ? == Is ( A ) + ⊇ R
- ii) Does G → R ? == Is ( G ) + ⊇ R

![Image](Lecture 5.3_artifacts/image_000012_0d9dfbde1de846c018eea32fe6aba21e8a9c7f3c69ef770101468a6cfb66a6e5.png)

## Module 23

Partha Pratim Das

Objectives &amp; Outline

FD Theory

Armstrong's Axioms

Closure of FDs

Closure of Attributes

Decomposition using FDs

BCNF

3NF

Normalization

Module Summary

## Functional Dependencies (7): Closure of Attribute Sets: Use

There are several uses of the attribute closure algorithm:

- Testing for superkey:
- To test if α is a superkey, we compute α + , and check if α + contains all attributes of R .
- Testing functional dependencies
- To check if a functional dependency α → β holds (or, in other words, is in F + ), just check if β ⊆ α +
- That is, we compute α + by using attribute closure, and then check if it contains β .
- Is a simple and cheap test, and very useful
- Computing closure of F
- For each γ ⊆ R , we find the closure γ + , and for each S ⊆ γ + , we output a functional dependency γ → S .

![Image](Lecture 5.3_artifacts/image_000013_fde1132bf222cc20a3e76fd9bad23db921b22024804914407d2f2bc1b513e47e.png)

## Module 23

Partha Pratim Das

Objectives &amp; Outline

FD Theory

Armstrong's Axioms

Closure of FDs

Closure of Attributes

Decomposition using FDs

BCNF

3NF

Normalization

Module Summary

## Decomposition using Functional Dependencies

Decomposition using Functional Dependencies

![Image](Lecture 5.3_artifacts/image_000014_0d9dfbde1de846c018eea32fe6aba21e8a9c7f3c69ef770101468a6cfb66a6e5.png)

## Module 23

Partha Pratim Das

Objectives &amp; Outline

FD Theory

Armstrong's Axioms

Closure of FDs

Closure of Attributes

Decomposition using FDs

BCNF

3NF

Normalization

Module Summary

## BCNF: Boyce-Codd Normal Form

- A relation schema R is in BCNF with respect to a set F of FDs if for all FDs in F + of the form

α → β , where α ⊆ R and β ⊆ R at least one of the following holds:

◦ α → β is trivial (that is, β ⊆ α )

- α is a superkey for R
- Example schema not in BCNF:

instr dept (ID, name, salary, dept name, building, budget)

- because the non-trivial dependency dept name → building, budget holds on instr dept , but dept name is not a superkey

![Image](Lecture 5.3_artifacts/image_000015_0d9dfbde1de846c018eea32fe6aba21e8a9c7f3c69ef770101468a6cfb66a6e5.png)

## Module 23

Partha Pratim Das

Objectives &amp; Outline

FD Theory

Armstrong's Axioms

Closure of FDs

Closure of Attributes

Decomposition using FDs

BCNF

3NF

Normalization

Module Summary

## BCNF (2): Decomposition

- If in schema R and a non-trivial dependency α → β causes a violation of BCNF, we decompose R into:
- α ∪ β
- ( R -( β -α ))
- In our example,
- α = dept name
- β = building , budget
- dept name → building, budget
- inst dept is replaced by
- ( α ∪ β ) = ( dept name, building, budget )
- glyph[triangleright] dept name → building, budget
- ( R -( β -α )) = (ID, name, salary, dept name)
- glyph[triangleright] ID → name, salary, dept name

![Image](Lecture 5.3_artifacts/image_000016_bbaa640f2b7c7b6f18cdf441c797dcf1ce99e755b6ef0a9bbf7b581538bddcab.png)

Module 23

Partha Pratim Das

Objectives &amp; Outline

FD Theory

Armstrong's Axioms

Closure of FDs

Closure of Attributes

Decomposition using FDs

BCNF

3NF

Normalization

Module Summary

## BCNF (3): Lossless Join

- If we decompose a relation R into relations R 1 and R 2 :
- Decomposition is lossy if R 1 glyph[triangleright] glyph[triangleleft] R 2 ⊃ R
- Decomposition is lossless if R 1 glyph[triangleright] glyph[triangleleft] R 2 = R
- To check for lossless join decomposition using FD set, following must hold:
- Union of Attributes of R 1 and R 2 must be equal to attribute of R

R 1 ∪ R 2 = R

- Intersection of Attributes of R 1 and R 2 must not be NULL

glyph[negationslash]

R 1 ∩ R 2 = Φ

- Common attribute must be a key for at least one relation ( R 1 or R 2 )

R 1 ∩ R 2 → R 1 or R 1 ∩ R 2 → R 2

- Prove that BCNF ensures Lossless Join

Database Management Systems

Partha Pratim Das

23.17

![Image](Lecture 5.3_artifacts/image_000017_bbaa640f2b7c7b6f18cdf441c797dcf1ce99e755b6ef0a9bbf7b581538bddcab.png)

Module 23

Partha Pratim Das

Objectives &amp; Outline

FD Theory

Armstrong's Axioms

Closure of FDs

Closure of Attributes

Decomposition using FDs

BCNF

3NF

Normalization

Module Summary

## BCNF (4): Dependency Preservation

- Constraints, including FDs, are costly to check in practice unless they pertain to only one relation
- If it is sufficient to test only those dependencies on each individual relation of a decomposition in order to ensure that all functional dependencies hold, then that decomposition is dependency preserving .
- It is not always possible to achieve both BCNF and dependency preservation. Consider:
- R = CSZ , F = { CS → Z , Z → C }
- Key = CS
- CS → Z satisfies BCNF, but Z → C violates
- Decompose as: R 1 = ZC , R 2 = CSZ -( C -Z ) = SZ

glyph[negationslash]

- R 1 ∪ R 2 = CSZ = R , R 1 ∩ R 2 = Z = Φ, and R 1 ∩ R 2 = Z → ZC = R 1 . So it has lossless join
- However, we cannot check CS → Z without doing a join. Hence it is not dependency preserving
- We consider a weaker normal form, known as Third Normal Form (3NF)

Database Management Systems

Partha Pratim Das

![Image](Lecture 5.3_artifacts/image_000018_bbaa640f2b7c7b6f18cdf441c797dcf1ce99e755b6ef0a9bbf7b581538bddcab.png)

## Module 23

Partha Pratim Das

Objectives &amp; Outline

FD Theory

Armstrong's Axioms

Closure of FDs

Closure of Attributes

Decomposition using FDs

BCNF

3NF

Normalization

Module Summary

## 3NF: Third Normal Form

- A relation schema R is in third normal form (3NF) if for all:
- α → β ∈ F +
- at least one of the following holds:
- α → β is trivial (that is, β ⊆ α )
- α is a superkey for R
- Each attribute A in β -α is contained in a candidate key for R (Nore: Each attribute may be in a different candidate key)
- If a relation is in BCNF it is in 3NF (since in BCNF one of the first two conditions above must hold)
- Third condition is a minimal relaxation of BCNF to ensure dependency preservation (will see why later)

![Image](Lecture 5.3_artifacts/image_000019_bbaa640f2b7c7b6f18cdf441c797dcf1ce99e755b6ef0a9bbf7b581538bddcab.png)

## Module 23

Partha Pratim Das

Objectives &amp; Outline

FD Theory

Armstrong's Axioms

Closure of FDs

Closure of Attributes

Decomposition using FDs

BCNF

3NF

Normalization

Module Summary

## Goals of Normalization

- Let R be a relation scheme with a set F of functional dependencies
- Decide whether a relation scheme R is in 'good' form
- In the case that a relation scheme R is not in 'good' form, decompose it into a set of relation scheme { R 1 , R 2 , ..., R n } such that
- each relation scheme is in good form
- the decomposition is a lossless-join decomposition
- Preferably, the decomposition should be dependency preserving

![Image](Lecture 5.3_artifacts/image_000020_0d9dfbde1de846c018eea32fe6aba21e8a9c7f3c69ef770101468a6cfb66a6e5.png)

## Module 23

Partha Pratim Das

Objectives &amp; Outline

FD Theory

Armstrong's Axioms

Closure of FDs

Closure of Attributes

Decomposition using FDs

BCNF

3NF

Normalization

Module Summary

## Problems with Decomposition

There are three potential problems to consider:

- May be impossible to reconstruct the original relation! (Lossiness)
- Dependency checking may require joins
- Some queries become more expensive
- What is the building for an instructor?

Tradeoff: Must consider these issues vs. redundancy

![Image](Lecture 5.3_artifacts/image_000021_0d9dfbde1de846c018eea32fe6aba21e8a9c7f3c69ef770101468a6cfb66a6e5.png)

## Module 23

Partha Pratim Das

Objectives &amp; Outline

FD Theory

Armstrong's Axioms

Closure of FDs

Closure of Attributes

Decomposition using FDs

BCNF

3NF

Normalization

Module Summary

## How good is BCNF?

- There are database schemas in BCNF that do not seem to be sufficiently normalized
- Consider a relation

inst info (ID, child name, phone)

- where an instructor may have more than one phone and can have multiple children

inst info

| ID                      | child_name                  | phone                                               |
|-------------------------|-----------------------------|-----------------------------------------------------|
| 99999 99999 99999 99999 | David David William Willian | 512-555-1234 512-555-4321 512-555-1234 512-555-4321 |

![Image](Lecture 5.3_artifacts/image_000022_0d9dfbde1de846c018eea32fe6aba21e8a9c7f3c69ef770101468a6cfb66a6e5.png)

## Module 23

Partha Pratim Das

Objectives &amp; Outline

FD Theory

Armstrong's Axioms

Closure of FDs

Closure of Attributes

Decomposition using FDs

BCNF

3NF

Normalization

Module Summary

## How good is BCNF? (2)

- There are no non-trivial functional dependencies and therefore the relation is in BCNF
- Insertion anomalies - that is, if we add a phone 981-992-3443 to 99999, we need to add two tuples

(99999, David, 981-992-3443) (99999, William, 981-992-3443)

![Image](Lecture 5.3_artifacts/image_000023_0d9dfbde1de846c018eea32fe6aba21e8a9c7f3c69ef770101468a6cfb66a6e5.png)

## Module 23

Partha Pratim

Das

Objectives &amp;

Outline

FD Theory

Armstrong's Axioms

Closure of FDs

Closure of Attributes

Decomposition using FDs

BCNF

3NF

Normalization

Module Summary

## How good is BCNF? (3)

- Therefore, it is better to decompose inst info into:
- This suggests the need for higher normal forms, such as the Fourth Normal Form (4NF)

| inst child   | inst child   |
|--------------|--------------|
|              | child_name   |
| 99999        | David        |
| 99999        | William      |

| inst phone   | inst phone   |
|--------------|--------------|
| ID           | phone        |
| 99999        | 512-555-1234 |
| 99999        | 512-555-4321 |

![Image](Lecture 5.3_artifacts/image_000024_0d9dfbde1de846c018eea32fe6aba21e8a9c7f3c69ef770101468a6cfb66a6e5.png)

## Module 23

Partha Pratim Das

Objectives &amp; Outline

FD Theory

Armstrong's Axioms

Closure of FDs

Closure of Attributes

Decomposition using FDs

BCNF

3NF

Normalization

Module Summary

## Module Summary

- Introduced the theory of functional dependencies
- Discussed issues in 'good' design in the context of functional dependencies

Slides used in this presentation are borrowed from http://db-book.com/ with kind permission of the authors. Edited and new slides are marked with 'PPD'.
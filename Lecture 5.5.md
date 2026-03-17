![Image](Lecture 5.5_artifacts/image_000000_bbaa640f2b7c7b6f18cdf441c797dcf1ce99e755b6ef0a9bbf7b581538bddcab.png)

## Module 25

Partha Pratim Das

Objectives &amp; Outline

Lossless Join Decomposition Practice Problems

Dependency Preservation Practice Problems

Module Summary

## Database Management Systems

Module 25: Relational Database Design/5

## Partha Pratim Das

Department of Computer Science and Engineering Indian Institute of Technology, Kharagpur ppd@cse.iitkgp.ac.in

Partha Pratim Das

![Image](Lecture 5.5_artifacts/image_000001_0d2e8daa05c74407b310229f101057782122d2bf078613dc8c643ca2fdb280b5.png)

## Module 25

Partha Pratim Das

Objectives &amp; Outline

Lossless Join Decomposition Practice Problems

Dependency Preservation Practice Problems

Module Summary

## Module Recap

- Studied Algorithms for Properties of Functional Dependencies

![Image](Lecture 5.5_artifacts/image_000002_821f32da21a8bb9af0bddb9e2ff2419e915ba7e461f5dc4f05b60eaa6ed0b478.png)

## Module 25

Partha Pratim Das

Objectives &amp; Outline

Lossless Join Decomposition Practice Problems

Dependency Preservation Practice Problems

Module Summary

## Module Objectives

- To Understand the Characterizations for Lossless Join Decomposition
- To Understand the Characterizations for Dependency Preservation

![Image](Lecture 5.5_artifacts/image_000003_821f32da21a8bb9af0bddb9e2ff2419e915ba7e461f5dc4f05b60eaa6ed0b478.png)

## Module 25

Partha Pratim Das

## Objectives &amp; Outline

Lossless Join Decomposition Practice Problems

Dependency Preservation Practice Problems

Module Summary

## Module Outline

- Lossless Join Decomposition
- Dependency Preservation

![Image](Lecture 5.5_artifacts/image_000004_fde1132bf222cc20a3e76fd9bad23db921b22024804914407d2f2bc1b513e47e.png)

Module 25

Partha Pratim Das

Objectives &amp; Outline

Lossless Join Decomposition

Practice Problems

Dependency Preservation Practice Problems

Module Summary

## Lossless join Decomposition

## Lossless Join Decomposition

![Image](Lecture 5.5_artifacts/image_000005_bbaa640f2b7c7b6f18cdf441c797dcf1ce99e755b6ef0a9bbf7b581538bddcab.png)

Module 25

Partha Pratim Das

Objectives &amp; Outline

Lossless Join Decomposition

Practice Problems

Dependency Preservation Practice Problems

Module Summary

## Lossless Join Decomposition

- For the case of R = ( R 1 , R 2 ), we require that for all possible relations r on schema R

<!-- formula-not-decoded -->

- A decomposition of R into R 1 and R 2 is lossless join if at least one of the following dependencies is in F + :
- R 1 ∩ R 2 → R 1
- R 1 ∩ R 2 → R 2
- The above functional dependencies are a sufficient condition for lossless join decomposition; the dependencies are a necessary condition only if all constraints are functional dependencies

To Identify whether a decomposition is lossy or lossless, it must satisfy the following conditions:

- R 1 ∪ R 2 = R

glyph[negationslash]

- R 1 ∩ R 2 = φ and
- R 1 ∩ R 2 → R 1 or R 1 ∩ R 2 → R 2

![Image](Lecture 5.5_artifacts/image_000006_32155ccc63eaf8ac3b5d36be7560257f854d0b99536286a17a16546fbab339af.png)

Module 25

Partha Pratim Das

Objectives &amp; Outline

Lossless Join Decomposition

Practice Problems

Dependency Preservation Practice Problems

Module Summary

## Lossless Join Decomposition (2): Example

- Consider Supplier Parts schema: Supplier Parts(S#, Sname, City, P#, Qty)
- Having dependencies: S# → Sname, S# → City, (S#, P#) → Qty
- Decompose as: Supplier(S#, Sname, City, Qty): Parts(P#, Qty)
- Take Natural Join to reconstruct: Supplier glyph[triangleright] glyph[triangleleft] Parts
- We get extra tuples! Join is Lossy!
- Common attribute Qty is not a superkey in Supplier or in Parts
- Does not preserve (S#, P#) → Qty

| S#   | Sname   | City   | P#   | Qty   | S#   | Sname   | City   | Qty   | P#   | Qty   | S#   | Sname   | City   | P#   |   Qty |
|------|---------|--------|------|-------|------|---------|--------|-------|------|-------|------|---------|--------|------|-------|
|      | Smith   | London | 301  | 20    |      | Smith   | London | 20    | 301  | 20    |      | Smith   | London | 301  |    20 |
|      | Nick    | NY     |      | 50    |      | Nick    | NY     | 50    | 500  | 50    | 5    | Nick    | NY     |      |    50 |
|      | Steve   | Boston | 20   | 10    |      | Steve   | Boston | 10    | 20   | 10    |      | Nick    | NY     | 20   |    10 |
|      | Nick    | NY     | 400  | 40    |      | Nick    | NY     | 40    | 400  | 40    |      | Steve   | Boston | 20   |    10 |
|      | Nick    | NY     | 301  | 10    |      | Nick    | NY     | 10    | 301  | 10    |      | Nick    | NY     | 400  |    40 |
|      |         |        |      |       |      |         |        |       |      |       |      | Nick    | NY     | 301  |    10 |
|      |         |        |      |       |      |         |        |       |      |       |      | Steve   | Boston | 301  |    10 |

Database Management Systems

## Partha Pratim Das

![Image](Lecture 5.5_artifacts/image_000007_32155ccc63eaf8ac3b5d36be7560257f854d0b99536286a17a16546fbab339af.png)

Module 25

Partha Pratim Das

Objectives &amp; Outline

Lossless Join Decomposition

Practice Problems

Dependency Preservation Practice Problems

Module Summary

## Lossless Join Decomposition (3): Example

- Consider Supplier Parts schema: Supplier Parts(S#, Sname, City, P#, Qty)
- Having dependencies: S# → Sname, S# → City, (S#, P#) → Qty
- Decompose as: Supplier(S#, Sname, City): Parts(S#, P#, Qty)
- Take Natural Join to reconstruct: Supplier glyph[triangleright] glyph[triangleleft] Parts
- We get back the original relation. Join is Lossless .
- Common attribute S# is a superkey in Supplier
- Preserves all dependencies

| S#   | Sname   | City   |   P# |   Qty | S#   | Sname   | City   | S#   |   P# |   Qty | S#   | Sname   | City   |   P# |   Qty |
|------|---------|--------|------|-------|------|---------|--------|------|------|-------|------|---------|--------|------|-------|
|      | Smith   | London |  301 |    20 |      | Smith   | London |      |  301 |    20 | 3    | Smith   | London |  301 |    20 |
|      | Nick    | NY     |  500 |    50 |      | Nick    | NY     | 5    |  500 |    50 | 5    | Nick    | NY     |  500 |    50 |
| 2    | Steve   | Boston |   20 |    10 |      | Steve   | Boston | 2    |   20 |    10 | 2    | Steve   | Boston |   20 |    10 |
|      | Nick    | NY     |  400 |    40 |      | Nick    | NY     | 5    |  400 |    40 | 5    | Nick    | NY     |  400 |    40 |
|      | Nick    | NY     |  301 |    10 |      | Nick    | NY     | 5    |  301 |    10 |      | Nick    | NY     |  301 |    10 |

Database Management Systems

![Image](Lecture 5.5_artifacts/image_000008_bbaa640f2b7c7b6f18cdf441c797dcf1ce99e755b6ef0a9bbf7b581538bddcab.png)

## Module 25

Partha Pratim Das

Objectives &amp; Outline

Lossless Join Decomposition

Practice Problems

Dependency Preservation

Practice Problems

Module Summary

## Lossless Join Decomposition (4): Example

- R = ( A , B , C )
- F = { A → B , B → C }
- Can be decomposed in two different ways
- R 1 = ( A , B ) , R 2 = ( B , C )
- Lossless-join decomposition: R 1 ∩ R 2 = { B } and B → BC
- Dependency preserving
- R 1 = ( A , B ) , R 2 = ( A , C )
- Lossless-join decomposition: R 1 ∩ R 2 = { A } and A → AB
- Not dependency preserving
- (cannot check B → C without computing R 1 glyph[triangleright] glyph[triangleleft] R 2 )

![Image](Lecture 5.5_artifacts/image_000009_0d2e8daa05c74407b310229f101057782122d2bf078613dc8c643ca2fdb280b5.png)

## Module 25

Partha Pratim Das

Objectives &amp; Outline

Lossless Join Decomposition

Practice Problems

Dependency Preservation

Practice Problems

Module Summary

## Practice Problems on Lossless Join

- Check if the decomposition of R into D is lossless:
- a) R ( ABC ) : F = { A → B , A → C } . D = R 1 ( AB ) , R 2 ( BC )
- b) R ( ABCDEF ) : F = { A → B , B → C , C → D , E → F } .
- D = R 1 ( AB ) , R 2 ( BCD ) , R 3 ( DEF
- )
- c) R ( ABCDEF ) : F = { A → B , C → DE , AC → F } . D = R 1 ( BE ) , R 2 ( ACDEF )
- d) R ( ABCDEG ) : F = { AB → C , AC → B , AD → E , B → D , BC → A , E → G }
- i) D 1 = R 1 ( AB ) , R 2 ( BC ) , R 3 ( ABDE ) , R 4 ( EG )
- ii) D 2 = R 1 ( ABC ) , R 2 ( ACDE ) , R 3 ( ADG )
- e) R ( ABCDEFGHIJ ) : F = { AB → C , B → F , D → IJ , A → DE , F → GH }
- i) D 1 = R 1 ( ABC ) , R 2 ( ADE ) , R 3 ( BF ) , R 4 ( FGH ) , R 5 ( DIJ )
- ii) D 2 = R 1 ( ABCDE ) , R 2 ( BFGH ) , R 3 ( DIJ )
- iii) D 3 = R 1 ( ABCD ) , R 2 ( DE ) , R 3 ( BF ) , R 4 ( FGH ) , R 5 ( DIJ )

![Image](Lecture 5.5_artifacts/image_000010_821f32da21a8bb9af0bddb9e2ff2419e915ba7e461f5dc4f05b60eaa6ed0b478.png)

Module 25

Partha Pratim Das

Objectives &amp; Outline

Lossless Join Decomposition Practice Problems

Dependency Preservation

Practice Problems

Module Summary

## Dependency Preservation

## Dependency Preservation

![Image](Lecture 5.5_artifacts/image_000011_0d9dfbde1de846c018eea32fe6aba21e8a9c7f3c69ef770101468a6cfb66a6e5.png)

## Module 25

Partha Pratim Das

Objectives &amp; Outline

Lossless Join Decomposition Practice Problems

Dependency Preservation

Practice Problems

Module Summary

## Dependency Preservation

- Let F i be the set of dependencies F + that include only attributes in R i
- A decomposition is dependency preserving , if

<!-- formula-not-decoded -->

- If it is not, then checking updates for violation of functional dependencies may require computing joins, which is expensive

Let R be the original relational schema having FD set F. Let R 1 and R 2 having FD set F 1 and F 2 respectively, are the decomposed sub-relations of R. The decomposition of R is said to be preserving if

- F 1 ∪ F 2 ≡ F { Decomposition Preserving Dependency }
- If F 1 ∪ F 2 ⊂ F { Decomposition NOT Preserving Dependency } and
- F 1 ∪ F 2 ⊃ F { this is not possible }

![Image](Lecture 5.5_artifacts/image_000012_bbaa640f2b7c7b6f18cdf441c797dcf1ce99e755b6ef0a9bbf7b581538bddcab.png)

Module 25

Partha Pratim Das

Objectives &amp; Outline

Lossless Join Decomposition Practice Problems

Dependency Preservation

Practice Problems

Module Summary

## Dependency Preservation (2): Testing

- To check if a dependency α → β is preserved in a decomposition of R into D = { R 1 , R 2 , . . . , Rn } we apply the following test (with attribute closure done with respect to F )
- The restriction of F + to Ri is the set of all functional dependencies in F + that include only attributes of Ri .
- compute F + ;

for each schema

Ri in

D

do begin

Fi = the restriction of F + to Ri ;

end

F ′ = φ

for each restriction Fi do begin

F

′

= F ′ ∪ Fi end

compute F ′ + ;

if

(

F

′

+ =

F

+ )

then return (true) else return (false);

- The procedure for checking dependency preservation takes exponential time to compute F + and ( F 1 ∪ F 2 ∪ · · · ∪ Fn ) +

Database Management Systems

Partha Pratim Das

25.13

![Image](Lecture 5.5_artifacts/image_000013_bbaa640f2b7c7b6f18cdf441c797dcf1ce99e755b6ef0a9bbf7b581538bddcab.png)

## Module 25

Partha Pratim Das

Objectives &amp; Outline

Lossless Join Decomposition Practice Problems

Dependency Preservation

Practice Problems

Module Summary

## Dependency Preservation (3): Example

- R ( A, B, C, D, E, F )
- F = { A → BCD , A → EF , BC → AD , BC → E , BC → F , B → F , D → E }
- Decomposition:
- R1 (A, B, C, D) R2 (B, F) R3 (D, E)
- A → BCD , BC → AD are preserved on table R1
- D → E is preserved on table R3
- B → F is preserved on table R2
- We have to check whether the remaining FDs: A → E , A → F , BC → E , BC → F are preserved or not.

## R1

R2

R3

F 1= { A → ABCD , B → B , C → C , D → D , AB → ABCD , BC → ABCD , CD → CD , AD → ABCD ABC → ABCD , ABD → ABCD , ACD → ABCD BCD → ABCD }

- F ′ = F 1 ∪ F 2 ∪ F 3.
- Checking for: A → E , A → F in F ′ +

glyph[triangleright]

A

→

D

(from R1),

D

→

E

(from R3) :

A

glyph[triangleright]

→

B

(from R1),

B

→

F

(from R2) :

A

→

A

→

E

F

F 2= { B → BF , F → F }

F 3= { D → DE , E → E }

(By Transitivity)

(By Transitivity)

- Checking for: BC → E , BC → F in F ′ +
- BC → D (from R1), D → E (from R3) : BC → E (By Transitivity)

BC → F (By Augmentation)

- glyph[triangleright] glyph[triangleright] B → F (from R2) :

Database Management Systems

Partha Pratim Das

Hence all dependencies are preserved .

25.14

![Image](Lecture 5.5_artifacts/image_000014_0d9dfbde1de846c018eea32fe6aba21e8a9c7f3c69ef770101468a6cfb66a6e5.png)

## Module 25

Partha Pratim Das

Objectives &amp; Outline

Lossless Join Decomposition Practice Problems

## Dependency Preservation

Practice Problems

Module Summary

## Dependency Preservation (4): Example

- R ( A, B, C, D )
- F = { A → B , B → C , C → D , D → A
- }
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

![Image](Lecture 5.5_artifacts/image_000015_0d9dfbde1de846c018eea32fe6aba21e8a9c7f3c69ef770101468a6cfb66a6e5.png)

## Module 25

Partha Pratim Das

Objectives &amp; Outline

Lossless Join Decomposition Practice Problems

Dependency Preservation

Practice Problems

Module Summary

## Dependency Preservation (5): Testing

- To check if a dependency α → β is preserved in a decomposition of R into R 1 , R 2 , · · · , R n we apply the following test (with attribute closure done with respect to F )
- result = α

while (changes to result) do for each R i in the decomposition t = ( result ∩ R i ) + ∩ Ri result = result ∪ t

- If result contains all attributes in β , then the functional dependency α → β is preserved.
- We apply the test on all dependencies in F to check if a decomposition is dependency preserving
- This procedure takes polynomial time, instead of the exponential time required to compute F + and ( F 1 ∪ F 2 ∪ · · · ∪ F n ) +

![Image](Lecture 5.5_artifacts/image_000016_bbaa640f2b7c7b6f18cdf441c797dcf1ce99e755b6ef0a9bbf7b581538bddcab.png)

Module 25

Partha Pratim Das

Objectives &amp; Outline

Lossless Join Decomposition Practice Problems

## Dependency Preservation

Practice Problems

Module Summary

## Dependency Preservation (6): Example

- R ( ABCDEF ) :. F = { A → BCD , A → EF , BC → AD , BC → E , BC → F , B → F , D → E }
- Decomp = { ABCD , BF , DE }
- On projections:
- Need to check for: ✭✭✭✭ A → BCD , A → EF , ✭✭✭✭ BC → AD , BC → E , BC → F , ✘✘✘ B → F , ✘✘✘ D → E
- ( BC ) + / F 1 = ABCD . ( ABCD ) + / F 2 = ABCDF . ( ABCDF ) + / F 3 = ABCDEF . Preserves BC → E , BC → F
- BC → AD ( R 1), AD → E ( R 3) implies BC → E B → F ( R 2) implies BC → F
- ( A ) + / F 1 = ABCD . ( ABCD ) + / F 2 = ABCDF . ( ABCDF ) + / F 3 = ABCDEF . Preserves A → EF A → B ( R 1), B → F ( R 2) implies A → F A → D ( R 1), D → E ( R 3) implies A → E

| ABCD (RI)     | BF (R2)   | DE (R3)   |
|---------------|-----------|-----------|
| A = BCD BC AD | B = F     |           |

## Partha Pratim Das

![Image](Lecture 5.5_artifacts/image_000017_fde1132bf222cc20a3e76fd9bad23db921b22024804914407d2f2bc1b513e47e.png)

## Module 25

Partha Pratim Das

Objectives &amp; Outline

Lossless Join Decomposition Practice Problems

## Dependency Preservation

Practice Problems

Module Summary

## Dependency Preservation (7): Example

- R ( ABCDEF ) : F = { A → BCD , A → EF , BC → AD , BC → E , BC → F , B → F , D → E } . Decomp = { ABCD , BF , DE }
- On projections:
- Infer reverse FD's:
- B + / F = BF : B → A cannot be inferred
- C + / F = C : C → A cannot be inferred
- D + / F = DE : D → A and D → BC cannot be inferred
- A + / F = ABCDEF : A → BC can be inferred, but it is equal to A → B and A → C
- F + / F = F : F → B cannot be inferred
- E + / F = E : E → D cannot be inferred
- Need to check for: ✭✭✭✭ A → BCD , A → EF , ✭✭✭✭ BC → AD , BC → E , BC → F , ✘✘✘ B → F , ✘✘✘ D → E
- ( BC ) + / F = ABCDEF . Preserves BC → E , BC → F
- ( A ) + / F = ABCDEF . Preserves A → EF

| ABCD (RI)   | BF (R2)   | DE (R3)   |
|-------------|-----------|-----------|
| D _ E       |           |           |

![Image](Lecture 5.5_artifacts/image_000018_0d2e8daa05c74407b310229f101057782122d2bf078613dc8c643ca2fdb280b5.png)

## Module 25

Partha Pratim Das

Objectives &amp; Outline

Lossless Join Decomposition Practice Problems

Dependency Preservation

Practice Problems

Module Summary

## Practice Problems on Dependency Preservation

- Check whether the decomposition of R into D is preserving dependency:
- a) R ( ABCD ) : F = { A → B , B → C , C → D , D → A } . D = { AB , BC , CD }
- b) R ( ABCDEF ) : F = { AB → CD , C → D , D → E , E → F } . D = { AB , CDE , EF }
- c) R ( ABCDEG ) : F = { AB → C , AC → B , BC → A , AD → E , B → D , E → G } . D = { ABC , ACDE , ADG }
- d) R ( ABCD ) : F = { A → B , B → C , C → D , D → B } . D = { AB , BC , BD }
- e) R ( ABCDE ) : F = { A → BC , CD → E , B → D , E → A } . D = { ABCE , BD }

![Image](Lecture 5.5_artifacts/image_000019_0d9dfbde1de846c018eea32fe6aba21e8a9c7f3c69ef770101468a6cfb66a6e5.png)

## Module 25

Partha Pratim Das

Objectives &amp; Outline

Lossless Join Decomposition Practice Problems

Dependency Preservation Practice Problems

Module Summary

## Module Summary

- Understood the Characterization for and Determination of Lossless Join
- Understood the Characterization for and Determination of Dependency Preservation

Slides used in this presentation are borrowed from http://db-book.com/ with kind permission of the authors. Edited and new slides are marked with 'PPD'.
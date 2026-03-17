![Image](Lecture 5.4_artifacts/image_000000_bbaa640f2b7c7b6f18cdf441c797dcf1ce99e755b6ef0a9bbf7b581538bddcab.png)

## Module 24

Partha Pratim Das

Objectives &amp; Outline

Algorithms for FDs

Attribute Set Closure

Extraneous

Attributes

Equivalence of FD Sets

Canonical Cover of

FDs

Practice Problems

Module Summary

## Database Management Systems

Module 24: Relational Database Design/4

## Partha Pratim Das

Department of Computer Science and Engineering Indian Institute of Technology, Kharagpur ppd@cse.iitkgp.ac.in

Partha Pratim Das

![Image](Lecture 5.4_artifacts/image_000001_0d9dfbde1de846c018eea32fe6aba21e8a9c7f3c69ef770101468a6cfb66a6e5.png)

## Module 24

Partha Pratim Das

Objectives &amp; Outline

Algorithms for FDs

Attribute Set Closure

Extraneous Attributes

Equivalence of FD Sets

Canonical Cover of

FDs

Practice Problems

Module Summary

## Module Recap

- Introduced the theory of functional dependencies
- Discussed issues in 'good' design in the context of functional dependencies

![Image](Lecture 5.4_artifacts/image_000002_0d2e8daa05c74407b310229f101057782122d2bf078613dc8c643ca2fdb280b5.png)

Module 24

Partha Pratim Das

Objectives &amp; Outline

Algorithms for FDs

Attribute Set Closure

Extraneous

Attributes

Equivalence of FD Sets

Canonical Cover of

FDs

Practice Problems

Module Summary

## Module Objectives

- To Learn Algorithms for Properties of Functional Dependencies

![Image](Lecture 5.4_artifacts/image_000003_0d9dfbde1de846c018eea32fe6aba21e8a9c7f3c69ef770101468a6cfb66a6e5.png)

Module 24

Partha Pratim Das

Objectives &amp; Outline

Algorithms for FDs

Attribute Set Closure

Extraneous

Attributes

Equivalence of FD Sets

Canonical Cover of

FDs

Practice Problems

Module Summary

## Module Outline

- Algorithms for Functional Dependencies

![Image](Lecture 5.4_artifacts/image_000004_0d2e8daa05c74407b310229f101057782122d2bf078613dc8c643ca2fdb280b5.png)

## Module 24

Partha Pratim Das

Objectives &amp; Outline

Algorithms for FDs

Attribute Set Closure

Extraneous

Attributes

Equivalence of FD Sets

Canonical Cover of

FDs

Practice Problems

Module Summary

## Algorithms for Functional Dependencies

## Algorithms for Functional Dependencies

![Image](Lecture 5.4_artifacts/image_000005_bbaa640f2b7c7b6f18cdf441c797dcf1ce99e755b6ef0a9bbf7b581538bddcab.png)

## Module 24

Partha Pratim Das

Objectives &amp; Outline

Algorithms for FDs

Attribute Set Closure

Extraneous Attributes

Equivalence of FD Sets

Canonical Cover of FDs

Practice Problems

Module Summary

## Attribute Set Closure

- R = ( A , B , C , G , H , I )
- F = { A → B , A → C , CG → H , CG → I , B → H }
- ( AG ) +
- a) result = AG
- b) result = ABCG
- c) result = ABCGH
- d) result = ABCGHI
- Is AG a candidate key?
- a) Is AG a super key?
- i) Does AG → R ? == Is ( AG ) + ⊇ R
- b) Is any subset of AG a superkey?
- i) Does A → R ? == Is ( A ) + ⊇ R
- ii) Does G → R ? == Is ( G ) + ⊇ R

( A → C and A → B )

( CG → H and CG ⊆ AGBC )

( CG → I and CG ⊆ AGBCH )

## Partha Pratim Das

![Image](Lecture 5.4_artifacts/image_000006_bbaa640f2b7c7b6f18cdf441c797dcf1ce99e755b6ef0a9bbf7b581538bddcab.png)

## Module 24

Partha Pratim Das

Objectives &amp; Outline

Algorithms for FDs

Attribute Set Closure

Extraneous Attributes

Equivalence of FD Sets

Canonical Cover of FDs

Practice Problems

Module Summary

## Attribute Set Closure: Uses

There are several uses of the attribute closure algorithm:

- Testing for superkey:
- To test if α is a superkey, we compute α + , and check if α + contains all attributes of R .
- Testing functional dependencies
- To check if a functional dependency α → β holds (or, in other words, is in F + ), just check if β ⊆ α + .
- That is, we compute α + by using attribute closure, and then check if it contains β .
- Is a simple and cheap test, and very useful
- Computing closure of F
- For each γ ⊆ R , we find the closure γ + , and for each S ⊆ γ + , we output a functional dependency γ → S .

![Image](Lecture 5.4_artifacts/image_000007_bbaa640f2b7c7b6f18cdf441c797dcf1ce99e755b6ef0a9bbf7b581538bddcab.png)

Module 24

Partha Pratim Das

Objectives &amp; Outline

Algorithms for FDs

Attribute Set Closure

Extraneous Attributes

Equivalence of FD Sets

Canonical Cover of FDs

Practice Problems

Module Summary

## Extraneous Attributes

- Consider a set F of FDs and the FD α → β in F .
- Attribute A is extraneous in α if A ∈ α and F logically implies ( F -{ α → β } ) ∪ { ( α -A ) → β } .
- Attribute A is extraneous in β if A ∈ β and the set of FDs ( F -{ α → β } ) ∪ { α → ( β -A ) } logically implies F .
- Note: Implication in the opposite direction is trivial in each of the cases above, since a 'stronger' functional dependency always implies a weaker one
- Example: Given F = { A → C , AB → C }
- B is extraneous in AB → C because { A → C , AB → C } logically implies A → C (that is, the result of dropping B from AB → C ).
- A + = AC in { A → C , AB → C }
- Example: Given F = { A → C , AB → CD }
- C is extraneous in AB → CD since AB → C can be inferred even after deleting C ◦ AB + = ABCD in { A → C , AB → D }

![Image](Lecture 5.4_artifacts/image_000008_bbaa640f2b7c7b6f18cdf441c797dcf1ce99e755b6ef0a9bbf7b581538bddcab.png)

## Module 24

Partha Pratim Das

Objectives &amp; Outline

Algorithms for FDs

Attribute Set Closure

Extraneous Attributes

Equivalence of FD Sets

Canonical Cover of FDs

Practice Problems

Module Summary

## Extraneous Attributes (2): Tests

- Consider a set F of functional dependencies and the functional dependency α → β in F .
- To test if attribute A ∈ α is extraneous in α
- a) Compute ( { α } -A ) + using the dependencies in F
- b) Check that ( { α } -A ) + contains β ; if it does, A is extraneous in α
- To test if attribute A ∈ β is extraneous in β
- a) Compute α + using only the dependencies in F ′ = ( F -{ α → β } ) ∪ { α → ( β -A ) } ,
- b) Check that α + contains A ; if it does, A is extraneous in β

![Image](Lecture 5.4_artifacts/image_000009_821f32da21a8bb9af0bddb9e2ff2419e915ba7e461f5dc4f05b60eaa6ed0b478.png)

## Module 24

Partha Pratim Das

Objectives &amp; Outline

Algorithms for FDs

Attribute Set Closure

Extraneous Attributes

Equivalence of FD Sets

Canonical Cover of FDs

Practice Problems

Module Summary

## Equivalence of Sets of Functional Dependencies

- Let F &amp; G are two functional dependency sets.
- These two sets F &amp; G are equivalent if F + = G + . That is: ( F + = G + ) ⇔ ( F + ⇒ G and G + ⇒ F )
- Equivalence means that every functional dependency in F can be inferred from G , and every functional dependency in G an be inferred from F
- F and G are equal only if
- F covers G : Means that all functional dependency of G are logically members of functional dependency set F ⇒ F + ⊇ G .
- G covers F : Means that all functional dependency of F are logically members of functional dependency set G ⇒ G + ⊇ F .

| Condition   | CASES   | CASES   | CASES   | CASES         |
|-------------|---------|---------|---------|---------------|
| F Covers G  | True    | True    | False   | False         |
| Covers      | True    | False   | True    | False         |
| Result      | F=G     |         | G-F     | No Comparison |

Partha Pratim Das

![Image](Lecture 5.4_artifacts/image_000010_bbaa640f2b7c7b6f18cdf441c797dcf1ce99e755b6ef0a9bbf7b581538bddcab.png)

Module 24

Partha Pratim Das

Objectives &amp; Outline

Algorithms for FDs

Attribute Set Closure

Extraneous Attributes

Equivalence of FD Sets

Canonical Cover of FDs

Practice Problems

Module Summary

## Canonical Cover

- Sets of FDs may have redundant dependencies that can be inferred from the others
- Can we have some kind of 'optimal' or 'minimal' set of FDs wto work with?
- A Canonical Cover for F is a set of dependencies F c such that ALL the following properties are satisfied:
- F + = F + c . Or,
- glyph[triangleright] F logically implies all dependencies in F c
- glyph[triangleright] F c logically implies all dependencies in F
- No functional dependency in F c contains an extraneous attribute
- Each left side of functional dependency in F c is unique. That is, there are no two dependencies α 1 → β 1 and α 2 → β 2 in such that α 1 → α 2
- Intuitively, a Canonical cover of F is a minimal set of FDs
- Equivalent to F
- Having no redundant FDs
- No redundant parts of FDs
- Minimal / Irreducible Set of Functional Dependencies

Database Management Systems

Partha Pratim Das

![Image](Lecture 5.4_artifacts/image_000011_bbaa640f2b7c7b6f18cdf441c797dcf1ce99e755b6ef0a9bbf7b581538bddcab.png)

Module 24

Partha Pratim Das

Objectives &amp; Outline

Algorithms for FDs

Attribute Set Closure

Extraneous Attributes

Equivalence of FD Sets

Canonical Cover of FDs

Practice Problems

Module Summary

## Canonical Cover (2): Example

- For example: A → C is redundant in: { A → B , B → C , A → C }
- Parts of a functional dependency may be redundant
- For example: on RHS: { A → B , B → C , A → CD } can be simplified to { A → B , B → C , A → D }
- -In the forward: (1) A → CD ⇒ A → C and A → D (2) A → B , B → C ⇒ A → C
- -In the reverse: (1) A → B , B → C ⇒ A → C (2) A → C , A → D ⇒ A → CD
- For example: on LHS: { A → B , B → C , AC → D } can be simplified to { A → B , B → C , A → D }
- -In the forward: (1) A → B , B → C ⇒ A → C ⇒ A → AC (2) A → AC , AC → D ⇒ A → D
- -In the reverse: A → D ⇒ AC → D

![Image](Lecture 5.4_artifacts/image_000012_fde1132bf222cc20a3e76fd9bad23db921b22024804914407d2f2bc1b513e47e.png)

## Module 24

Partha Pratim Das

Objectives &amp; Outline

Algorithms for FDs

Attribute Set Closure

Extraneous Attributes

Equivalence of FD Sets

Canonical Cover of FDs

Practice Problems

Module Summary

## Canonical Cover (3): RHS

- { A → B , B → C , A → CD } ⇒ { A → B , B → C , A → D }
- (1) A → CD ⇒ A → C and A → D
- (2) A → B , B → C ⇒ A → C
- A + = ABCD
- { A → B , B → C , A → D } ⇒ { A → B , B → C , A → CD }
- A → B , B → C ⇒ A → C
- A → C , A → D ⇒ A → CD
- A + = ABCD

![Image](Lecture 5.4_artifacts/image_000013_fde1132bf222cc20a3e76fd9bad23db921b22024804914407d2f2bc1b513e47e.png)

## Module 24

Partha Pratim Das

Objectives &amp; Outline

Algorithms for FDs

Attribute Set Closure

Extraneous Attributes

Equivalence of FD Sets

Canonical Cover of FDs

Practice Problems

Module Summary

## Canonical Cover (4): LHS

- { A → B , B → C , AC → D } ⇒ { A → B , B → C , A → D }
- A → B , B → C ⇒ A → C ⇒ A → AC
- A → AC , AC → D ⇒ A → D
- A + = ABCD
- { A → B , B → C , A → D } ⇒ { A → B , B → C , AC → D }
- A → D ⇒ AC → D
- AC + = ABCD

![Image](Lecture 5.4_artifacts/image_000014_bbaa640f2b7c7b6f18cdf441c797dcf1ce99e755b6ef0a9bbf7b581538bddcab.png)

## Module 24

Partha Pratim Das

Objectives &amp; Outline

Algorithms for FDs

Attribute Set Closure

Extraneous Attributes

Equivalence of FD Sets

Canonical Cover of FDs

Practice Problems

Module Summary

## Canonical Cover (5)

- To compute a canonical cover for F :
- repeat

Use the union rule to replace any dependencies in F

α 1 → β 1 and α 1 → β 2 with α 1 → β 1 β 2 Find a functional dependency α → β with an extraneous attribute either in α or in β

- /* Note: test for extraneous attributes done using F c , not F */

If an extraneous attribute is found, delete it from α → β

- until F does not change
- Note: Union rule may become applicable after some extraneous attributes have been deleted, so it has to be re-applied

![Image](Lecture 5.4_artifacts/image_000015_bbaa640f2b7c7b6f18cdf441c797dcf1ce99e755b6ef0a9bbf7b581538bddcab.png)

Module 24

Partha Pratim Das

Objectives &amp; Outline

Algorithms for FDs

Attribute Set Closure

Extraneous Attributes

Equivalence of FD Sets

Canonical Cover of FDs

Practice Problems

Module Summary

## Canonical Cover (6): Example

- R = ( A , B , C )
- F = { A → BC , B → C , A → B , AB → C }
- Combine A → BC and A → B into A → BC
- Set is now { A → BC , B → C , AB → C }
- A is extraneous in AB → C
- Check if the result of deleting A from AB → C is implied by the other dependencies
- glyph[triangleright] Yes: in fact, B → C
- is already present!
- Set is now { A → BC , B → C }
- C is extraneous in A → BC
- Check if A → C is logically implied by A → B and the other dependencies
- glyph[triangleright] Yes: using transitivity on A → B and B → C .
- Can use attribute closure of A in more complex cases
- The canonical cover is: A → B , B → C

Database Management Systems

Partha Pratim Das

![Image](Lecture 5.4_artifacts/image_000016_0d2e8daa05c74407b310229f101057782122d2bf078613dc8c643ca2fdb280b5.png)

## Module 24

Partha Pratim Das

Objectives &amp; Outline

Algorithms for FDs

Attribute Set Closure

Extraneous Attributes

Equivalence of FD Sets

Canonical Cover of FDs

Practice Problems

Module Summary

## Practice Problems on Functional Dependencies

- Find if a given functional dependency is implied from a set of Functional Dependencies:
- a) For: A → BC , CD → E , E → C , D → AEH , ABH → BD , DH → BC
- i) Check: BCD → H
- ii) Check: AED → C
- b) For: AB → CD , AF → D , DE → F , C → G , F → E , G → A
- i) Check: CF → DF
- ii) Check: BG → E
- iii) Check: AF → G
- iv) Check: AB → EF
- c) For: A → BC , B → E , CD → EF
- i) Check: AD → F

![Image](Lecture 5.4_artifacts/image_000017_0d9dfbde1de846c018eea32fe6aba21e8a9c7f3c69ef770101468a6cfb66a6e5.png)

## Module 24

Partha Pratim Das

Objectives &amp; Outline

Algorithms for FDs

Attribute Set Closure

Extraneous Attributes

Equivalence of FD Sets

Canonical Cover of FDs

Practice Problems

Module Summary

## Practice Problems on Functional Dependencies (2)

- Find Super Key using Functional Dependencies:
- a) Relational Schema R ( ABCDE ). AB → C , DE → B , CD → E
- Functional dependencies:
- b) Relational Schema R ( ABCDE ). Functional dependencies: AB → C , C → D , B → EA

![Image](Lecture 5.4_artifacts/image_000018_0d9dfbde1de846c018eea32fe6aba21e8a9c7f3c69ef770101468a6cfb66a6e5.png)

## Module 24

Partha Pratim Das

Objectives &amp; Outline

Algorithms for FDs

Attribute Set Closure

Extraneous Attributes

Equivalence of FD Sets

Canonical Cover of FDs

Practice Problems

Module Summary

## Practice Problems on Functional Dependencies (3)

- Find Candidate Key using Functional Dependencies:
- a) Relational Schema R ( ABCDE ). AB → C , DE → B , CD → E
- Functional dependencies:
- b) Relational Schema R ( ABCDE ). Functional dependencies: AB → C , C → D , B → EA

![Image](Lecture 5.4_artifacts/image_000019_bbaa640f2b7c7b6f18cdf441c797dcf1ce99e755b6ef0a9bbf7b581538bddcab.png)

Module 24

Partha Pratim Das

Objectives &amp; Outline

Algorithms for FDs

Attribute Set Closure

Extraneous Attributes

Equivalence of FD Sets

Canonical Cover of FDs

Practice Problems

Module Summary

## Practice Problems on Functional Dependencies (4)

- Find Prime and Non Prime Attributes using Functional Dependencies:
- a) R ( ABCDEF ) having FDs { AB → C , C → D , D → E , F → B , E → F }
- b) R ( ABCDEF ) having FDs { AB → C , C → DE , E → F , C → B }
- c) R ( ABCDEFGHIJ ) having FDs { AB → C , A → DE , B → F , F → GH , D → IJ }
- d) R ( ABDLPT ) having FDs { B → PT , A → D , T → L }
- e) R ( ABCDEFGH ) having FDs
- { E → G , AB → C , AC → B , AD → E , B → D , BC → A }
- f) R ( ABCDE ) having FDs { A → BC , CD → E , B → D , E → A }
- g) R ( ABCDEH ) having FDs { A → B , BC → D , E → C , D → A }
- Prime Attributes : Attribute set that belongs to any candidate key are called Prime Attributes
- It is union of all the candidate key attribute: { CK 1 ∪ CK 2 ∪ CK 3 ∪ · · · }
- If Prime attribute determined by other attribute set, then more than one candidate key is possible.
- For example, If A is Candidate Key, and X → A , then, X is also Candidate Key.
- Non Prime Attribute : Attribute set does not belong to any candidate key are called Non Prime Attributes

![Image](Lecture 5.4_artifacts/image_000020_0d9dfbde1de846c018eea32fe6aba21e8a9c7f3c69ef770101468a6cfb66a6e5.png)

## Module 24

Partha Pratim Das

Objectives &amp; Outline

Algorithms for FDs

Attribute Set Closure

Extraneous Attributes

Equivalence of FD Sets

Canonical Cover of FDs

Practice Problems

Module Summary

## Practice Problems on Functional Dependencies (5)

- Check the Equivalence of a Pair of Sets of Functional Dependencies:
- a) Consider the two sets F and G with their FDs as below :
- i) F : A → C , AC → D , E → AD , E → H
- ii) G : A → CD , E → AH
- b) Consider the two sets P and Q with their FDs as below :
- i) P : A → B , AB → C , D → ACE
- ii) Q : A → BC , D → AE

![Image](Lecture 5.4_artifacts/image_000021_0d9dfbde1de846c018eea32fe6aba21e8a9c7f3c69ef770101468a6cfb66a6e5.png)

## Module 24

Partha Pratim Das

Objectives &amp; Outline

Algorithms for FDs

Attribute Set Closure

Extraneous Attributes

Equivalence of FD Sets

Canonical Cover of FDs

Practice Problems

Module Summary

## Practice Problems on Functional Dependencies (6)

- Find the Minimal Cover or Irreducible Sets or Canonical Cover of a Set of Functional Dependencies:
- a) AB → CD , BC → D
- b) ABCD → E , E → D , AC → D , A → B

![Image](Lecture 5.4_artifacts/image_000022_0d9dfbde1de846c018eea32fe6aba21e8a9c7f3c69ef770101468a6cfb66a6e5.png)

Module 24

Partha Pratim Das

Objectives &amp; Outline

Algorithms for FDs

Attribute Set Closure

Extraneous

Attributes

Equivalence of FD Sets

Canonical Cover of FDs

Practice Problems

Module Summary

## Module Summary

- Studied Algorithms for Properties of Functional Dependencies

Slides used in this presentation are borrowed from http://db-book.com/ with kind permission of the authors.

Edited and new slides are marked with 'PPD'.
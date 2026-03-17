![Image](Lecture 6.1_artifacts/image_000000_bbaa640f2b7c7b6f18cdf441c797dcf1ce99e755b6ef0a9bbf7b581538bddcab.png)

## Module 26

Partha Pratim Das

Week Recap

Objectives &amp;

Outline

Normal Forms

1NF

2NF

3NF

Module Summary

## Database Management Systems

Module 26: Relational Database Design/6: Normal Forms

## Partha Pratim Das

Department of Computer Science and Engineering Indian Institute of Technology, Kharagpur ppd@cse.iitkgp.ac.in

Partha Pratim Das

![Image](Lecture 6.1_artifacts/image_000001_bbaa640f2b7c7b6f18cdf441c797dcf1ce99e755b6ef0a9bbf7b581538bddcab.png)

## Module 26

Partha Pratim Das

Week Recap

Objectives &amp; Outline

Normal Forms

1NF

2NF

3NF

Module Summary

## Week Recap

- Identified the features of good relational design
- Familiarized with the First Normal Form
- Introduced the notion and the theory of functional dependencies
- Discussed issues in 'good' design in the context of functional dependencies
- Studied Algorithms for Properties of Functional Dependencies
- Understood the Characterization for and Determination of Lossless Join and Determination of Dependency Preservation

![Image](Lecture 6.1_artifacts/image_000002_0d2e8daa05c74407b310229f101057782122d2bf078613dc8c643ca2fdb280b5.png)

Module 26

Partha Pratim

Das

Week Recap

Objectives &amp; Outline

Normal Forms

1NF

2NF

3NF

Module Summary

## Module Objectives

- To Understand the Normal Forms and their Importance in Relational Design

![Image](Lecture 6.1_artifacts/image_000003_0d2e8daa05c74407b310229f101057782122d2bf078613dc8c643ca2fdb280b5.png)

Module 26

Partha Pratim

Das

Week Recap

Objectives &amp;

Outline

Normal Forms

1NF

2NF

3NF

Module Summary

## Module Outline

- Normal Forms

![Image](Lecture 6.1_artifacts/image_000004_0d9dfbde1de846c018eea32fe6aba21e8a9c7f3c69ef770101468a6cfb66a6e5.png)

## Module 26

Partha Pratim Das

Week Recap

Objectives &amp; Outline

Normal Forms

1NF

2NF

3NF

Module Summary

## Normal Forms

## Normal Forms

![Image](Lecture 6.1_artifacts/image_000005_0d9dfbde1de846c018eea32fe6aba21e8a9c7f3c69ef770101468a6cfb66a6e5.png)

## Module 26

Partha Pratim Das

Week Recap

Objectives &amp; Outline

Normal Forms

1NF

2NF

3NF

Module Summary

## Normalization or Schema Refinement

- Normalization or Schema Refinement is a technique of organizing the data in the database
- A systematic approach of decomposing tables to eliminate data redundancy and undesirable characteristics
- Insertion Anomaly
- Update Anomaly
- Deletion Anomaly
- Most common technique for the Schema Refinement is decomposition.
- Goal of Normalization: Eliminate Redundancy
- Redundancy refers to repetition of same data or duplicate copies of same data stored in different locations
- Normalization is used for mainly two purpose:
- Eliminating redundant (useless) data
- Ensuring data dependencies make sense, that is, data is logically stored

## Partha Pratim Das

![Image](Lecture 6.1_artifacts/image_000006_c66187055de285596be50032d73dadd82d2ef960cecf03026d68ecb78134d5c9.png)

![Image](Lecture 6.1_artifacts/image_000007_dbde90e0b0f8bc763541272f0cb0a05bffe9e5f119d42bd42219fccf8f28b8d9.png)

## Anomalies

- a) Update Anomaly: Employee 519 is shown as having different addresses on different records

## Employees' Skills

Resolution: Decompose the Schema

![Image](Lecture 6.1_artifacts/image_000008_c3d3be50ad3426670ca6b7258da7a6fdb312558af1a656fca56c14c27c0d23b8.png)

- a) Update : (ID, Address), (ID, Skill)
- b) Insert : (ID, Name, Hire Date), (ID, Code)
- c) Delete : (ID, Name, Hire Date), (ID, Code)

## Database Management Systems

- b) Insertion Anomaly : Until the new faculty member, Dr. Newsome, is assigned to teach at least one course, his details cannot be Faculty Their Courses and
- c) Deletion Anomaly : All information about Dr. Giddens is lost if he temporarily ceases to be assigned to any courses. Faculty and Their Courses

![Image](Lecture 6.1_artifacts/image_000009_2d1d689563e801ce8fb623dda12713416552133beffce29e8808ce6a31e375dd.png)

![Image](Lecture 6.1_artifacts/image_000010_9c1fd4735296e2a053eca11dc5e15b9a7deff3dc2640c9defcfc845623b0dd75.png)

## Partha Pratim Das

![Image](Lecture 6.1_artifacts/image_000011_bbaa640f2b7c7b6f18cdf441c797dcf1ce99e755b6ef0a9bbf7b581538bddcab.png)

## Module 26

Partha Pratim Das

Week Recap

Objectives &amp; Outline

Normal Forms

1NF

2NF

3NF

Module Summary

## Desirable Properties of Decomposition

- Lossless Join Decomposition Property
- It should be possible to reconstruct the original table
- Dependency Preserving Property
- No functional dependency (or other constraints should get violated)

![Image](Lecture 6.1_artifacts/image_000012_bad5517ee4fc9f601ff84dbb26135026a4d24fddefa8d2f414d99a6c8f460fb6.png)

## Database Management Systems

Partha Pratim Das

![Image](Lecture 6.1_artifacts/image_000013_0d9dfbde1de846c018eea32fe6aba21e8a9c7f3c69ef770101468a6cfb66a6e5.png)

## Module 26

Partha Pratim Das

Week Recap

Objectives &amp; Outline

Normal Forms

1NF

2NF

3NF

Module Summary

## Normalization and Normal Forms

- A normal form specifies a set of conditions that the relational schema must satisfy in terms of its constraints - they offer varied levels of guarantee for the design
- Normalization rules are divided into various normal forms. Most common normal forms are:
- First Normal Form (1NF)
- Second Normal Form (2NF)
- Third Normal Form (3NF)
- Informally, a relational database relation is often described as 'normalized' if it meets third normal form. Most 3NF relations are free of insertion, update, and deletion anomalies

![Image](Lecture 6.1_artifacts/image_000014_0d9dfbde1de846c018eea32fe6aba21e8a9c7f3c69ef770101468a6cfb66a6e5.png)

## Module 26

Partha Pratim Das

Week Recap

Objectives &amp; Outline

Normal Forms

1NF

2NF

3NF

Module Summary

## Normalization and Normal Forms

- Additional Normal Forms
- Elementary Key Normal Form (EKNF)
- Boyce-codd Normal Form (BCNF)
- Multivalued Dependencies And Fourth Normal Form (4NF)
- Essential Tuple Normal Form (ETNF)
- Join Dependencies and Fifth Normal Form (5NF)
- Sixth Normal Form (6NF)
- Domain/Key Normal Form (DKNF)

![Image](Lecture 6.1_artifacts/image_000015_bbaa640f2b7c7b6f18cdf441c797dcf1ce99e755b6ef0a9bbf7b581538bddcab.png)

## Module 26

Partha Pratim

Das

Week Recap

Objectives &amp;

Outline

Normal Forms

1NF

2NF

3NF

Module Summary

## 1NF: First Normal Form

- A relation is in First Normal Form if and only if all underlying domains contain atomic values only (doesn't have multivalued attributes (MVA))
- STUDENT(Sid, Sname, Cname)

![Image](Lecture 6.1_artifacts/image_000016_a98f2fd4340962b1991c7dbe4472d8dc6c8e0bb079bae80a9e239331f469af77.png)

| SID             | Sname           | Cname           |
|-----------------|-----------------|-----------------|
| S1              | A               | C,C++           |
| S2              | B               | C++, DB         |
| S3              | A               | DB              |
| SID Primary Key | SID Primary Key | SID Primary Key |

## Students

No MVA = In INF

| SID         | Sname       | Cname       |
|-------------|-------------|-------------|
| S1          | A           |             |
| S1          | A           | C++         |
| S2          | B           | C++         |
| S2          | B           | DB          |
| S3          | A           | DB          |
| Primary Kev | Primary Kev | Primary Kev |

Source:

http://www.edugrabs.com/normal-forms/#fnf

Partha Pratim Das

![Image](Lecture 6.1_artifacts/image_000017_bbaa640f2b7c7b6f18cdf441c797dcf1ce99e755b6ef0a9bbf7b581538bddcab.png)

Module 26

Partha Pratim

Das

Week Recap

Objectives &amp;

Outline

Normal Forms

1NF

2NF

3NF

Module Summary

## 1NF (2): Possible Redundancy

- Example: Supplier(SID, Status, City, PID, Qty)

![Image](Lecture 6.1_artifacts/image_000018_c13af947073a77b507facf234c584bb74883a82634311b13dc926ffc067e8346.png)

| Supplier:      | Supplier:      | Supplier:      | Supplier:   | Supplier:   |
|----------------|----------------|----------------|-------------|-------------|
| SID            | Status         | City           | PID         | Qty         |
| S1             | 30             | Delhi          | Pl          | 100         |
| S1             | 30             | Delhi          | P2          | 125         |
| SI             | 30             | Delhi          |             | 200         |
| SI             | 30             | Delhi          |             | 130         |
| S2             | 10             | Karnal         |             | 115         |
| S2             | 10             | Karnal         | P2          | 250         |
| S3             | 40             | Rohtak         | PI          | 245         |
| S4             | 30             | Delhi          | P4          | 300         |
|                | 30             | Delhi          | P5          | 315         |
| (SID, PID) Key | (SID, PID) Key | (SID, PID) Key |             |             |

![Image](Lecture 6.1_artifacts/image_000019_a34cbef2a8870833048422810bbb422cabd5a4096981d3d4f0d825955ae6e483.png)

## Drawbacks:

- Deletion Anomaly: If we delete &lt; S3,40,Rohtak,P1,245 &gt; , then we lose the information that S3 lives in Rohtak.
- Insertion Anomaly: We cannot insert a Supplier S5 located in Karnal, until S5 supplies at least one part.
- Update Anomaly: If Supplier S1 moves from Delhi to Kanpur, then it is difficult to update all the tuples having SID as S1 and City as Delhi.

Normalization is a method to reduce redundancy. However, sometimes 1NF increases redundancy.

## Partha Pratim Das

![Image](Lecture 6.1_artifacts/image_000020_bbaa640f2b7c7b6f18cdf441c797dcf1ce99e755b6ef0a9bbf7b581538bddcab.png)

## Module 26

Partha Pratim Das

Week Recap

Objectives &amp;

Outline

Normal Forms

1NF

2NF

3NF

Module Summary

## 1NF (3): Possible Redundancy

## · When LHS is not a Superkey :

- Let X → Y be a non trivial FD over R with X is not a superkey of R , then redundancy exist between X and Y attribute set.
- Hence in order to identify the redundancy, we need not to look at the actual data, it can be identified by given functional dependency.
- Example : X → Y and X is not a Candidate Key
- ⇒ X can duplicate
- ⇒ Corresponding Y value would duplicate also.

![Image](Lecture 6.1_artifacts/image_000021_5d4274147bc7cb71201719d4c8c4e883d851d334520dae664b4c1b37e82723a3.png)

## Database Management Systems

## · When LHS is a Superkey :

- If X → Y is a non trivial FD over R with X is a superkey of R , then redundancy does not exist between X and Y attribute set.
- Example : X → Y and X is a Candidate Key ⇒ X cannot duplicate
- ⇒ Corresponding Y value may or may not duplicate.

![Image](Lecture 6.1_artifacts/image_000022_f4d3bd16cc9e4730500a1ad25d875c21324b08af45eac4dfb43de6edd49ce5df.png)

## Partha Pratim Das

![Image](Lecture 6.1_artifacts/image_000023_bbaa640f2b7c7b6f18cdf441c797dcf1ce99e755b6ef0a9bbf7b581538bddcab.png)

## Module 26

Partha Pratim Das

Week Recap

Objectives &amp; Outline

Normal Forms

1NF

2NF

3NF

Module Summary

## 2NF: Second Normal Form

- Relation R is in Second Normal Form (2NF) only iff :
- R is in 1NF and
- R contains no Partial Dependency

## Partial Dependency:

Let R be a relational Schema and X , Y , A be the attribute sets over R where X : Any Candidate Key, Y : Proper Subset of Candidate Key, and A : Non Prime Attribute

If Y → A exists in R , then R is not in 2NF.

( Y → A ) is a Partial dependency only if

- Y : Proper subset of Candidate Key
- A : Non Prime Attribute
- A prime attribute of a relation is an attribute that is a part of a candidate key of the relation

Partha Pratim Das

![Image](Lecture 6.1_artifacts/image_000024_32155ccc63eaf8ac3b5d36be7560257f854d0b99536286a17a16546fbab339af.png)

## Module 26

Partha Pratim

Das

Week Recap

Objectives &amp;

Outline

Normal Forms

1NF

2NF

3NF

Module Summary

![Image](Lecture 6.1_artifacts/image_000025_3dbb0b964488a49815b60616d7d52593183d784a35babc639f144aaa0bad963f.png)

- STUDENT(Sid, Sname, Cname) (already in 1NF)
- Redundancy?
- Sname
- Anomaly?
- Yes

![Image](Lecture 6.1_artifacts/image_000026_15686bcee3dcb41924332e6318bcc7d9e4282909c7174a5d7951d1cc6685ccdf.png)

| Students:                 | Students:                 | Students:                 |
|---------------------------|---------------------------|---------------------------|
| SID                       | Sname                     | Cname                     |
| S1                        |                           |                           |
| S1                        |                           | C++                       |
| S2                        |                           | C++                       |
| S2                        |                           | DB                        |
| S3                        |                           | DB                        |
| (SID, Cname): Primary Key | (SID, Cname): Primary Key | (SID, Cname): Primary Key |

![Image](Lecture 6.1_artifacts/image_000027_33df540c999b12b0a612c0392b4c2198b864a5c5021aa9ba9b638ea91943fee9.png)

Functional Dependencies: { SID , Cname } → Sname SID → Sname

## Partial Dependencies:

SID → Sname (as SID is a Proper Subset of Candidate Key { SID , Cname } )

![Image](Lecture 6.1_artifacts/image_000028_75a3474bc70aeaea6d7eb68344125c50766d3fff5482920dce7ba13649ef354f.png)

Source: http://www.edugrabs.com/2nf-second-normal-form/

## Partha Pratim Das

![Image](Lecture 6.1_artifacts/image_000029_bbaa640f2b7c7b6f18cdf441c797dcf1ce99e755b6ef0a9bbf7b581538bddcab.png)

## Module 26

Partha Pratim

Das

Week Recap

Objectives &amp;

Outline

Normal Forms

1NF

2NF

3NF

Module Summary

## 2NF (3): Possible Redundancy

- Supplier(SID, Status, City, PID, Qty)

![Image](Lecture 6.1_artifacts/image_000030_f989ee9e1f26c41cf7782fae50888cb0bca0e79a1b20e9aea3a80423ba946ddb.png)

![Image](Lecture 6.1_artifacts/image_000031_1f7d2ef5ee4d04d49afce288d8de4d674796ee7ab8dc5c1d90ab77800ef462f5.png)

## Drawbacks:

- Deletion Anomaly : If we delete a tuple in Sup City , then we not only loose the information about a supplier, but also loose the status value of a particular city.
- Insertion Anomaly : We cannot insert a City and its status until a supplier supplies at least one part.

Partial Dependencies : SID → Status SID → City

![Image](Lecture 6.1_artifacts/image_000032_a392fec6bcd85a55d6a368bc93ed3527687ed9b74b46670fcbb08d1694f5b72a.png)

- Update Anomaly : If the status value for a city is changed, then we will face the problem of searching every tuple for that city.

| Supplier:      | Supplier:      | Supplier:      | Supplier:   | Supplier:   |
|----------------|----------------|----------------|-------------|-------------|
| SID            | Status         | City           | PID         | Qty         |
| SI             | 30             | Delhi          | Pl          | 100         |
|                | 30             | Delhi          | P2          | 125         |
|                | 30             | Delhi          | P3          | 200         |
|                | 30             | Delhi          | P4          | 130         |
| S2             | 10             | Karnal         | Pl          | 115         |
| S2             | 10             | Karnal         | P2          | 250         |
| S3             | 40             | Rohtak         | Pl          | 245         |
| S4             | 30             | Delhi          | P4          | 300         |
| S4             | 30             | Delhi          |             | 315         |
| Key (SID, PID) | Key (SID, PID) | Key (SID, PID) |             |             |

Source:

http://www.edugrabs.com/2nf-second-normal-form/

Partha Pratim Das

![Image](Lecture 6.1_artifacts/image_000033_bbaa640f2b7c7b6f18cdf441c797dcf1ce99e755b6ef0a9bbf7b581538bddcab.png)

## Module 26

Partha Pratim Das

Week Recap

Objectives &amp; Outline

Normal Forms

1NF

2NF

3NF

Module Summary

## 3NF: Third Normal Form

Let R be the relational schema.

- [E. F. Codd,1971] R is in 3NF only if:
- R should be in 2NF
- R should not contain transitive dependencies (OR, Every non-prime attribute of R is non-transitively dependent on every key of R )
- [Carlo Zaniolo, 1982] Alternately, R is in 3NF iff for each of its functional dependencies X → A , at least one of the following conditions holds:
- X contains A (that is, A is a subset of X , meaning X → A is trivial functional dependency), or
- X is a superkey, or
- Every element of A -X , the set difference between A and X , is a prime attribute (i.e., each attribute in A -X is contained in some candidate key)
- [Simple Statement] A relational schema R is in 3NF if for every FD X → A associated with R either
- A ⊆ X (that is, the FD is trivial) or
- X is a superkey of R or
- A is part of some candidate key (not just superkey!)
- A relation in 3NF is naturally in 2NF

![Image](Lecture 6.1_artifacts/image_000034_bbaa640f2b7c7b6f18cdf441c797dcf1ce99e755b6ef0a9bbf7b581538bddcab.png)

## Module 26

Partha Pratim Das

Week Recap

Objectives &amp; Outline

Normal Forms

1NF

2NF

3NF

Module Summary

## 3NF (2): Transitive Dependency

- A transitive dependency is a functional dependency which holds by virtue of transitivity. A transitive dependency can occur only in a relation that has three or more attributes.
- Let A , B , and C designate three distinct attributes (or distinct collections of attributes) in the relation. Suppose all three of the following conditions hold:
- A → B
- It is not the case that B → A
- B → C
- Then the functional dependency A → C (which follows from 1 and 3 by the axiom of transitivity) is a transitive dependency

![Image](Lecture 6.1_artifacts/image_000035_bbaa640f2b7c7b6f18cdf441c797dcf1ce99e755b6ef0a9bbf7b581538bddcab.png)

Module 26

Partha Pratim Das

Week Recap

Objectives &amp; Outline

Normal Forms

1NF

2NF

3NF

Module Summary

## 3NF (3): Transitive Dependency

- Example of transitive dependency
- The functional dependency { Book } → { Author Nationality } applies; that is, if we know the book, we know the author's nationality. Furthermore:
- { Book } → { Author }
- { Author } does not → { Book }
- { Author } → { Author Nationality }
- Therefore { Book } → { Author Nationality } is a transitive dependency.
- Transitive dependency occurred because a non-key attribute (Author) was determining another non-key attribute (Author Nationality).

![Image](Lecture 6.1_artifacts/image_000036_8ccb7125e32fd61a87ba08290fd35a2d6147594bcc5fa6959dc6c69758f62a2b.png)

| Book                                  | Genre                   | Author       | Author Nationality   |
|---------------------------------------|-------------------------|--------------|----------------------|
| Twenty Thousand Leagues Under the Sea | Sclence Fiction         | Jules Verne  | French               |
| Journey the Earth                     | Sclence Fiction         | Jules Verne  | French               |
| Leaves of Grass                       | Poetry                  | Walt Whitman | American             |
| Anna Karenina                         | Literary Fiction        | Leo Tolstoy  | Russian              |
| Confession                            | Religious Autobiography | Leo Tolstoy  | Russian              |

## Database Management Systems

Partha Pratim Das

![Image](Lecture 6.1_artifacts/image_000037_32155ccc63eaf8ac3b5d36be7560257f854d0b99536286a17a16546fbab339af.png)

## Module 26

Partha Pratim

Das

Week Recap

Objectives &amp;

Outline

Normal Forms

1NF

2NF

3NF

Module Summary

## 3NF (4): Example

- Example:

## Sup City(SID, Status, City) (already in 2NF)

![Image](Lecture 6.1_artifacts/image_000038_f40de5f0e3b8e56180ca7e5d8e6637e6525f9a9ba176bf29b7644a90e2f4bb5b.png)

![Image](Lecture 6.1_artifacts/image_000039_771f91032b2c808526ac3c81a6fa763cadcb369fb11cae03d31d044264b00fe9.png)

Database Management Systems

![Image](Lecture 6.1_artifacts/image_000040_2a1373eb95ef5c7f0777625de2e226e3b0e9d2e1a43e77ddefdb3dfa709db30d.png)

Functional Dependencies: SID → Status, SID → City, City → Status Transitive Dependency : SID → Status { As SID → City and City → Status }

## Partha Pratim Das

![Image](Lecture 6.1_artifacts/image_000041_2e87325d2258c46856c2a268fe03ef5b7de6d67db5b9da6ca37654375401bf88.png)

|                  |                  | CS:               | CS:               |
|------------------|------------------|-------------------|-------------------|
| SID              | City             | City              | Status            |
| S1               | Delhi            | Delhi             | 30                |
| S2               | Karnal           | Karnal            | 10                |
| S3               | Rohtak           | Rohtak            | 40                |
| S4               | Delhi            | City: Primary Key | City: Primary Key |
| SID: Primary Key | SID: Primary Key |                   |                   |

![Image](Lecture 6.1_artifacts/image_000042_8bb106b266d9eefe8d8e1fa30284628dc98561985d45715065bd9ac4f716ce4c.png)

![Image](Lecture 6.1_artifacts/image_000043_bbaa640f2b7c7b6f18cdf441c797dcf1ce99e755b6ef0a9bbf7b581538bddcab.png)

Module 26

Partha Pratim Das

Week Recap

Objectives &amp; Outline

Normal Forms

1NF

2NF

3NF

Module Summary

## 3NF (5): Example

- Relation dept advisor ( s ID , i ID , dept name )
- F = { s ID , dept name → i ID , i ID → dept name }
- Two candidate keys: s ID , dept name , and i ID , s ID
- R is in 3NF
- s ID , dept name → i ID
- glyph[triangleright] s ID , dept name is a superkey
- i ID → dept name
- glyph[triangleright] dept name is contained in a candidate key

A relational schema R is in 3NF if for every FD X → A associated with R either

- A ⊆ X (i.e., the FD is trivial) or
- X is a superkey of R or
- A is part of some key (not just superkey!)

![Image](Lecture 6.1_artifacts/image_000044_bbaa640f2b7c7b6f18cdf441c797dcf1ce99e755b6ef0a9bbf7b581538bddcab.png)

## Module 26

Partha Pratim Das

Week Recap

Objectives &amp; Outline

Normal Forms

1NF

2NF

3NF

Module Summary

## 3NF (6): Redundancy

- There is some redundancy in this schema
- Example of problems due to redundancy in 3NF ( J : s ID , L : i ID , K : dept name )
- R = ( J , L , K ). F = { JK → L , L → K }
- Repetition of information (for example, the relationship l 1 , k 1 )
- ( i ID , dept name )
- Need to use null values (for example, to represent the relationship l 2 , k 2 where there is no corresponding value for J ).
- ( i ID , dept name ) if there is no separate relation mapping instructors to

| J    | L   | K   |
|------|-----|-----|
|      |     | E   |
| null | 12  | kz  |

departments

Database Management Systems

Partha Pratim Das

![Image](Lecture 6.1_artifacts/image_000045_0d9dfbde1de846c018eea32fe6aba21e8a9c7f3c69ef770101468a6cfb66a6e5.png)

Module 26

Partha Pratim Das

Week Recap

Objectives &amp; Outline

Normal Forms

1NF

2NF

3NF

Module Summary

## Module Summary

- Studied the Normal Forms and their Importance in Relational Design - how progressive increase of constraints can minimize redundancy in a schema

Slides used in this presentation are borrowed from http://db-book.com/ with kind permission of the authors.

Edited and new slides are marked with 'PPD'.
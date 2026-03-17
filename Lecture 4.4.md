![Image](Lecture 4.4_artifacts/image_000000_bbaa640f2b7c7b6f18cdf441c797dcf1ce99e755b6ef0a9bbf7b581538bddcab.png)

## Module 19

Partha Pratim Das

Objectives &amp; Outline

ER Diagram

Entity Sets

Relationship Sets

Cardinality

Constraints

Participation

Bounds

ER Model to Relational Schema

Entity Sets

Relationship

Composite Attributes

Multivalued

Attributes

Redundancy

Module Summary

## Database Management Systems

Module 19: Entity-Relationship Model/2

## Partha Pratim Das

Department of Computer Science and Engineering Indian Institute of Technology, Kharagpur ppd@cse.iitkgp.ac.in

Partha Pratim Das

![Image](Lecture 4.4_artifacts/image_000001_0d9dfbde1de846c018eea32fe6aba21e8a9c7f3c69ef770101468a6cfb66a6e5.png)

## Module 19

Partha Pratim Das

Objectives &amp; Outline

ER Diagram

Entity Sets

Relationship Sets

Cardinality

Constraints

Participation

Bounds

ER Model to Relational Schema

Entity Sets

Relationship

Composite Attributes

Multivalued Attributes

Redundancy

Module Summary

## Module Recap

- Design Process for Database Systems
- ER Model for real world representation with entities, entity sets, attributes, and relationships

![Image](Lecture 4.4_artifacts/image_000002_0d9dfbde1de846c018eea32fe6aba21e8a9c7f3c69ef770101468a6cfb66a6e5.png)

## Module 19

Partha Pratim Das

Objectives &amp; Outline

ER Diagram

Entity Sets

Relationship Sets

Cardinality

Constraints

Participation

Bounds

ER Model to Relational Schema

Entity Sets

Relationship

Composite Attributes

Multivalued

Attributes

Redundancy

Module Summary

## Module Objectives

- To illustrate ER Diagram notation for ER Models
- To explore translation of ER Models to Relational Schemas

![Image](Lecture 4.4_artifacts/image_000003_0d9dfbde1de846c018eea32fe6aba21e8a9c7f3c69ef770101468a6cfb66a6e5.png)

## Module 19

Partha Pratim Das

Objectives &amp; Outline

ER Diagram

Entity Sets

Relationship Sets

Cardinality

Constraints

Participation

Bounds

ER Model to Relational Schema

Entity Sets

Relationship

Composite Attributes

Multivalued

Attributes

Redundancy

Module Summary

## Module Outline

- ER Diagram
- ER Model to Relational Schema

![Image](Lecture 4.4_artifacts/image_000004_bbaa640f2b7c7b6f18cdf441c797dcf1ce99e755b6ef0a9bbf7b581538bddcab.png)

## Module 19

Partha Pratim Das

Objectives &amp; Outline

ER Diagram

Entity Sets

Relationship Sets

Cardinality

Constraints

Participation

Bounds

ER Model to Relational Schema

Entity Sets

Relationship

Composite Attributes

Multivalued

Attributes

Redundancy

Module Summary

## ER Diagram

![Image](Lecture 4.4_artifacts/image_000005_bbaa640f2b7c7b6f18cdf441c797dcf1ce99e755b6ef0a9bbf7b581538bddcab.png)

## Module 19

Partha Pratim Das

Objectives &amp;

Outline

ER Diagram

Entity Sets

Relationship Sets

Cardinality

Constraints

Participation

Bounds

ER Model to

Relational

Schema

Entity Sets

Relationship

Composite Attributes

Multivalued

Attributes

Redundancy

Module Summary

## Entity Sets

- Entities can be represented graphically as follows:
- Rectangles represent entity sets.
- Attributes are listed inside entity rectangle.
- Underline indicates primary key attributes.

![Image](Lecture 4.4_artifacts/image_000006_bc16005a709ae01143e3342e1bc7e442c2d60be95344bd170457d511edd4a31a.png)

![Image](Lecture 4.4_artifacts/image_000007_443fae0583b8b7c9ed48456031cc0c4fb9e4aff544e4b91a9d80fc2bbf4176fd.png)

![Image](Lecture 4.4_artifacts/image_000008_0d9dfbde1de846c018eea32fe6aba21e8a9c7f3c69ef770101468a6cfb66a6e5.png)

## Module 19

Partha Pratim

Das

Objectives &amp;

Outline

ER Diagram

Entity Sets

Relationship Sets

Cardinality

Constraints

Participation

Bounds

ER Model to

Relational

Schema

Entity Sets

Relationship

Composite Attributes

Multivalued

Attributes

Redundancy

Module Summary

## Relationship Sets

- Diamonds represent relationship sets.

![Image](Lecture 4.4_artifacts/image_000009_83b3032fcbce071acbcb3e8b9f8c7579c8f444489fece4e132d300b5e82fd68e.png)

![Image](Lecture 4.4_artifacts/image_000010_bbaa640f2b7c7b6f18cdf441c797dcf1ce99e755b6ef0a9bbf7b581538bddcab.png)

Module 19

Partha Pratim

Das

Objectives &amp;

Outline

ER Diagram

Entity Sets

Relationship Sets

Cardinality

Constraints

Participation

Bounds

ER Model to

Relational

Schema

Entity Sets

Relationship

Composite Attributes

Multivalued

Attributes

Redundancy

Module Summary

## Relationship Sets with Attributes

![Image](Lecture 4.4_artifacts/image_000011_ea32834193cb9b67e0fc26932e9720843839d59ed3fa8901685f6af68d47a9c0.png)

![Image](Lecture 4.4_artifacts/image_000012_0d9dfbde1de846c018eea32fe6aba21e8a9c7f3c69ef770101468a6cfb66a6e5.png)

## Module 19

Partha Pratim Das

Objectives &amp; Outline

ER Diagram

Entity Sets

Relationship Sets

Cardinality

Constraints

Participation

Bounds

ER Model to

Relational

Schema

Entity Sets

Relationship

Composite Attributes

Multivalued

Attributes

Redundancy

Module Summary

## Roles

- Entity sets of a relationship need not be distinct Each occurrence of an entity set plays a 'role' in the relationship
- The labels 'course id' and 'prereq id' are called roles .

![Image](Lecture 4.4_artifacts/image_000013_7c58554f432ad0c938688ad17c19de467b3ea82a13b6d869b82adaddac21348b.png)

![Image](Lecture 4.4_artifacts/image_000014_bbaa640f2b7c7b6f18cdf441c797dcf1ce99e755b6ef0a9bbf7b581538bddcab.png)

## Module 19

Partha Pratim Das

Objectives &amp; Outline

ER Diagram

Entity Sets

Relationship Sets

Cardinality

Constraints

Participation

Bounds

ER Model to

Relational

Schema

Entity Sets

Relationship

Composite Attributes

Multivalued

Attributes

Redundancy

Module Summary

## Cardinality Constraints

- We express cardinality constraints by drawing either a directed line ( → ), signifying 'one,' or an undirected line (-), signifying 'many,' between the relationship set and the entity set.
- One-to-one relationship between an instructor and a student :
- A student is associated with at most one instructor via the relationship advisor
- An instructor is associated with at most one student via the relationship advisor

![Image](Lecture 4.4_artifacts/image_000015_507a1e843a4e0b42df9e8f6be35d49bacab575e5929b23dcc41fc9d311defde3.png)

![Image](Lecture 4.4_artifacts/image_000016_bbaa640f2b7c7b6f18cdf441c797dcf1ce99e755b6ef0a9bbf7b581538bddcab.png)

## Module 19

Partha Pratim Das

Objectives &amp; Outline

ER Diagram

Entity Sets

Relationship Sets

Cardinality

Constraints

Participation

Bounds

ER Model to

Relational

Schema

Entity Sets

Relationship

Composite Attributes

Multivalued

Attributes

Redundancy

Module Summary

## One-to-Many Relationship

- one-to-many relationship between an instructor and a student
- an instructor is associated with several (including 0) students via advisor ◦ a student is associated with at most one instructor via advisor

![Image](Lecture 4.4_artifacts/image_000017_b904c0e2f2b42b6e9cc2b754c50b8af4ffbe590b03d29ac4c3365b8915520ef4.png)

![Image](Lecture 4.4_artifacts/image_000018_bbaa640f2b7c7b6f18cdf441c797dcf1ce99e755b6ef0a9bbf7b581538bddcab.png)

## Module 19

Partha Pratim Das

Objectives &amp;

Outline

ER Diagram

Entity Sets

Relationship Sets

Cardinality

Constraints

Participation

Bounds

ER Model to

Relational

Schema

Entity Sets

Relationship

Composite Attributes

Multivalued

Attributes

Redundancy

Module Summary

## Many-to-One Relationships

- many-to-one relationship between a student and an instructor ,
- an instructor is associated with at most one student via advisor,
- and a student is associated with several (including 0) instructors via advisor

![Image](Lecture 4.4_artifacts/image_000019_e2af5a6e64b32c4f80032148b0b517faf1769596117ae7f38c8f96520f3f465d.png)

![Image](Lecture 4.4_artifacts/image_000020_0d9dfbde1de846c018eea32fe6aba21e8a9c7f3c69ef770101468a6cfb66a6e5.png)

Module 19

Partha Pratim

Das

Objectives &amp;

Outline

ER Diagram

Entity Sets

Relationship Sets

Cardinality

Constraints

Participation

Bounds

ER Model to

Relational

Schema

Entity Sets

Relationship

Composite Attributes

Multivalued

Attributes

Redundancy

Module Summary

## Many-to-Many Relationship

- An instructor is associated with several (possibly 0) students via advisor
- A student is associated with several (possibly 0) instructors via advisor

![Image](Lecture 4.4_artifacts/image_000021_d06af06551d3668aee87663f107e657c03d244e06f3aa5c7e6064030ff4859aa.png)

![Image](Lecture 4.4_artifacts/image_000022_bbaa640f2b7c7b6f18cdf441c797dcf1ce99e755b6ef0a9bbf7b581538bddcab.png)

## Module 19

Partha Pratim

Das

Objectives &amp;

Outline

ER Diagram

Entity Sets

Relationship Sets

Cardinality

Constraints

Participation

Bounds

ER Model to

Relational

Schema

Entity Sets

Relationship

Composite Attributes

Multivalued

Attributes

Redundancy

Module Summary

## Total and Partial Participation

- Total participation (indicated by double line): every entity in the entity set participates in at least one relationship in the relationship set
- participation of student in advisor relation is total
- glyph[triangleright] every student must have an associated instructor
- Partial participation: some entities may not participate in any relationship in the relationship set
- Example: participation of instructor in advisor is partial

![Image](Lecture 4.4_artifacts/image_000023_6009e53301b15d60aacba843ab946adc26c5014396250447df57a8f51985808c.png)

![Image](Lecture 4.4_artifacts/image_000024_0d9dfbde1de846c018eea32fe6aba21e8a9c7f3c69ef770101468a6cfb66a6e5.png)

## Module 19

Partha Pratim Das

Objectives &amp; Outline

ER Diagram

Entity Sets

Relationship Sets

Cardinality

Constraints

Participation

Bounds

ER Model to Relational Schema

Entity Sets

Relationship

Composite Attributes

Multivalued

Attributes

Redundancy

Module Summary

## Notation for Expressing More Complex Constraints

- A line may have an associated minimum and maximum cardinality, shown in the form l..h , where l is the minimum and h the maximum cardinality
- A minimum value of 1 indicates total participation.
- A maximum value of 1 indicates that the entity participates in at most one relationship
- A maximum value of * indicates no limit.

![Image](Lecture 4.4_artifacts/image_000025_aceea2eed108b6fe494f36e1658994d48f045f106d523670050ee9c423cf40be.png)

Instructor can advise 0 or more students.

A student must have 1 advisor; cannot have multiple advisors

![Image](Lecture 4.4_artifacts/image_000026_0d9dfbde1de846c018eea32fe6aba21e8a9c7f3c69ef770101468a6cfb66a6e5.png)

Module 19

Partha Pratim

Das

Objectives &amp;

Outline

ER Diagram

Entity Sets

Relationship Sets

Cardinality

Constraints

Participation

Bounds

ER Model to

Relational

Schema

Entity Sets

Relationship

Composite Attributes

Multivalued

Attributes

Redundancy

Module Summary

## Notation to Express Entity with Complex Attributes

![Image](Lecture 4.4_artifacts/image_000027_e23ba19043ee6124be4c714bbe8040edd4bbb5c1dc5896a1951fd5b1d9798e58.png)

Partha Pratim Das

![Image](Lecture 4.4_artifacts/image_000028_bbaa640f2b7c7b6f18cdf441c797dcf1ce99e755b6ef0a9bbf7b581538bddcab.png)

## Module 19

Partha Pratim Das

Objectives &amp; Outline

ER Diagram

Entity Sets

Relationship Sets

Cardinality

Constraints

Participation

Bounds

ER Model to

Relational

Schema

Entity Sets

Relationship

Composite Attributes

Multivalued

Attributes

Redundancy

Module Summary

## Expressing Weak Entity Sets

- In ER diagrams, a weak entity set is depicted via a double rectangle
- We underline the discriminator of a weak entity set with a dashed line
- The relationship set connecting the weak entity set to the identifying strong entity set is depicted by a double diamond
- Primary key for section - (course id, sec id, semester, year)

![Image](Lecture 4.4_artifacts/image_000029_bb757d7416f681cd8b8eaf8a65b4d026dd1ba70539c0b33a01dd8f8a9202eaa8.png)

![Image](Lecture 4.4_artifacts/image_000030_bbaa640f2b7c7b6f18cdf441c797dcf1ce99e755b6ef0a9bbf7b581538bddcab.png)

Module 19

Partha Pratim

Das

Objectives &amp;

Outline

ER Diagram

Entity Sets

Relationship Sets

Cardinality

Constraints

Participation

Bounds

ER Model to

Relational

Schema

Entity Sets

Relationship

Composite Attributes

Multivalued

Attributes

Redundancy

Module Summary

## ER Diagram for a University Enterprise

Database Management Systems

![Image](Lecture 4.4_artifacts/image_000031_546762c22da1d9377e1cb5cc2e393ae96fa8a0b9785846b1b88fae1b43506797.png)

![Image](Lecture 4.4_artifacts/image_000032_44b3949ffed21c5ac1d653f0732b20837d9420307dd478fe439496b389adbd32.png)

## Module 19

Partha Pratim Das

Objectives &amp; Outline

ER Diagram

Entity Sets

Relationship Sets

Cardinality

Constraints

Participation

Bounds

ER Model to Relational Schema

Entity Sets

Relationship

Composite Attributes

Multivalued

Attributes

Redundancy

Module Summary

## ER Model to Relational Schema

![Image](Lecture 4.4_artifacts/image_000033_6c84160e4155ee195cba5dbf6477f94d4dd6c1476bd300cc9b03b2e6d682c709.png)

![Image](Lecture 4.4_artifacts/image_000034_0d9dfbde1de846c018eea32fe6aba21e8a9c7f3c69ef770101468a6cfb66a6e5.png)

## Module 19

Partha Pratim Das

Objectives &amp; Outline

ER Diagram

Entity Sets

Relationship Sets

Cardinality

Constraints

Participation

Bounds

ER Model to Relational Schema

Entity Sets

Relationship

Composite Attributes

Multivalued Attributes

Redundancy

Module Summary

## Reduction to Relation Schema

- Entity sets and relationship sets can be expressed uniformly as relation schemas that represent the contents of the database
- A database which conforms to an ER diagram can be represented by a collection of schemas
- For each entity set and relationship set there is a unique schema that is assigned the name of the corresponding entity set or relationship set
- Each schema has a number of columns (generally corresponding to attributes), which have unique names

![Image](Lecture 4.4_artifacts/image_000035_1fee3e82d1b67a0ea80851dc77c4b6bcbc3ff998ca25ce1a6457e95ce5186f9e.png)

![Image](Lecture 4.4_artifacts/image_000036_0d9dfbde1de846c018eea32fe6aba21e8a9c7f3c69ef770101468a6cfb66a6e5.png)

## Module 19

Partha Pratim Das

Objectives &amp; Outline

ER Diagram

Entity Sets

Relationship Sets

Cardinality

Constraints

Participation

Bounds

ER Model to Relational Schema

## Entity Sets

Relationship

Composite Attributes

Multivalued

Attributes

Redundancy

Module Summary

## Representing Entity Sets

- A strong entity set reduces to a schema with the same attributes
- student(ID, name, tot cred)
- A weak entity set becomes a table that includes a column for the primary key of the identifying strong entity set

section (course id, sec id, sem, year )

![Image](Lecture 4.4_artifacts/image_000037_93c9c824b8dcfe9fad0a59ba6498bdf79cefbdac41a866fad785fcb47377530d.png)

![Image](Lecture 4.4_artifacts/image_000038_0d9dfbde1de846c018eea32fe6aba21e8a9c7f3c69ef770101468a6cfb66a6e5.png)

## Module 19

Partha Pratim Das

Objectives &amp; Outline

ER Diagram

Entity Sets

Relationship Sets

Cardinality

Constraints

Participation

Bounds

ER Model to

Relational

Schema

Entity Sets

Relationship

Composite Attributes

Multivalued

Attributes

Redundancy

Module Summary

## Representing Relationship Sets

- A many-to-many relationship set is represented as a schema with attributes for the primary keys of the two participating entity sets, and any descriptive attributes of the relationship set.
- Example: schema for relationship set advisor

advisor = ( s id, i id )

![Image](Lecture 4.4_artifacts/image_000039_6a66aae883380233f465ef450274060b650259effdee9b8d31ec1794deace3af.png)

![Image](Lecture 4.4_artifacts/image_000040_bbaa640f2b7c7b6f18cdf441c797dcf1ce99e755b6ef0a9bbf7b581538bddcab.png)

Module 19

Partha Pratim

Das

Objectives &amp;

Outline

ER Diagram

Entity Sets

Relationship Sets

Cardinality

Constraints

Participation

Bounds

ER Model to

Relational

Schema

Entity Sets

Relationship

Composite Attributes

Multivalued

Attributes

Redundancy

Module Summary

## Representation of Entity Sets with Composite Attributes

- Composite attributes are flattened out by creating a separate attribute for each component attribute
- Example: given entity set instructor with composite attribute name with component attributes first name and last name the schema corresponding to the entity set has two attributes name first name and name last name
- glyph[triangleright] Prefix omitted if there is no ambiguity ( name first name could be first name )
- Ignoring multivalued attributes, extended instructor schema is
- instructor(ID, first name, middle initial, last name, street number, street name, apt number, city, state, zip code, date of birth)

![Image](Lecture 4.4_artifacts/image_000041_1b0f12d36836debccd60e892dafb2b089ef648710adbaab7eba3499e6ed505c2.png)

![Image](Lecture 4.4_artifacts/image_000042_0d9dfbde1de846c018eea32fe6aba21e8a9c7f3c69ef770101468a6cfb66a6e5.png)

Module 19

Partha Pratim Das

Objectives &amp; Outline

ER Diagram

Entity Sets

Relationship Sets

Cardinality

Constraints

Participation

Bounds

ER Model to Relational Schema

Entity Sets

Relationship

Composite Attributes

Multivalued Attributes

Redundancy

Module Summary

## Representation of Entity Sets with Multivalued Attributes

- A multivalued attribute M of an entity E is represented by a separate schema EM
- Schema EM has attributes corresponding to the primary key of E and an attribute corresponding to multivalued attribute M
- Example: Multivalued attribute phone number of instructor is represented by a schema: inst phone = ( ID, phone number)
- Each value of the multivalued attribute maps to a separate tuple of the relation on schema EM
- For example, an instructor entity with primary key 22222 and phone numbers 456-7890 and 123-4567 maps to two tuples: (22222, 456-7890) and (22222, 123-4567)

![Image](Lecture 4.4_artifacts/image_000043_0d9dfbde1de846c018eea32fe6aba21e8a9c7f3c69ef770101468a6cfb66a6e5.png)

## Module 19

Partha Pratim Das

Objectives &amp; Outline

ER Diagram

Entity Sets

Relationship Sets

Cardinality

Constraints

Participation

Bounds

ER Model to Relational Schema

Entity Sets

Relationship

Composite Attributes

Multivalued

Attributes

Redundancy

Module Summary

## Redundancy of Schema

- Many-to-one and one-to-many relationship sets that are total on the many-side can be represented by adding an extra attribute to the 'many' side, containing the primary key of the 'one' side
- Example: Instead of creating a schema for relationship set inst dept , add an attribute dept name to the schema arising from entity set instructor

![Image](Lecture 4.4_artifacts/image_000044_4024897b11e94cfb0f653b3e23d3e87eebe2d0c5c14f9bd4cc4d9cedef4949d8.png)

Database Management Systems

Partha Pratim Das

![Image](Lecture 4.4_artifacts/image_000045_0d9dfbde1de846c018eea32fe6aba21e8a9c7f3c69ef770101468a6cfb66a6e5.png)

## Module 19

Partha Pratim Das

Objectives &amp; Outline

ER Diagram

Entity Sets

Relationship Sets

Cardinality

Constraints

Participation

Bounds

ER Model to Relational Schema

Entity Sets

Relationship

Composite Attributes

Multivalued

Attributes

Redundancy

Module Summary

## Redundancy of Schema (2)

![Image](Lecture 4.4_artifacts/image_000046_8f2b6d38d5ce951c730e2e778decb9a2ca18ddbffea3d793614368c63d7b614e.png)

- For one-to-one relationship sets, either side can be chosen to act as the 'many' side
- That is, an extra attribute can be added to either of the tables corresponding to the two entity sets
- If participation is partial on the 'many' side, replacing a schema by an extra attribute in the schema corresponding to the 'many' side could result in null values

![Image](Lecture 4.4_artifacts/image_000047_0d9dfbde1de846c018eea32fe6aba21e8a9c7f3c69ef770101468a6cfb66a6e5.png)

## Module 19

Partha Pratim Das

Objectives &amp; Outline

ER Diagram

Entity Sets

Relationship Sets

Cardinality

Constraints

Participation

Bounds

ER Model to Relational Schema

Entity Sets

Relationship

Composite Attributes

Multivalued

Attributes

Redundancy

Module Summary

## Redundancy of Schema (3)

- The schema corresponding to a relationship set linking a weak entity set to its identifying strong entity set is redundant.
- Example: The section schema already contains the attributes that would appear in the sec course schema

![Image](Lecture 4.4_artifacts/image_000048_b3bd085c01161ccfa937a5f3d7699c1c92943aeb0a346080fb2c961ede5df4f3.png)

![Image](Lecture 4.4_artifacts/image_000049_0d9dfbde1de846c018eea32fe6aba21e8a9c7f3c69ef770101468a6cfb66a6e5.png)

## Module 19

Partha Pratim Das

Objectives &amp; Outline

ER Diagram

Entity Sets

Relationship Sets

Cardinality Constraints

Participation

Bounds

ER Model to Relational Schema

Entity Sets

Relationship

Composite Attributes

Multivalued

Attributes

Redundancy

Module Summary

## Module Summary

- Illustrated ER Diagram notation for ER Models
- Discussed translation of ER Models to Relational Schema

Slides used in this presentation are borrowed from http://db-book.com/ with kind permission of the authors.

Edited and new slides are marked with 'PPD'.
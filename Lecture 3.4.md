![Image](Lecture 3.4_artifacts/image_000000_bbaa640f2b7c7b6f18cdf441c797dcf1ce99e755b6ef0a9bbf7b581538bddcab.png)

## Module 14

Partha Pratim Das

Objectives &amp; Outline

Transactions

Integrity Constraints

Referential Integrity

SQL Data Types and Schemas Built-in Types

Index

UDT

Domains

Large Object

Authorization

Privileges

Revocation

Roles

Module Summary

## Database Management Systems

Module 14: Intermediate SQL/3

## Partha Pratim Das

Department of Computer Science and Engineering Indian Institute of Technology, Kharagpur ppd@cse.iitkgp.ac.in

Partha Pratim Das

14.1

![Image](Lecture 3.4_artifacts/image_000001_821f32da21a8bb9af0bddb9e2ff2419e915ba7e461f5dc4f05b60eaa6ed0b478.png)

Module 14

Partha Pratim Das

Objectives &amp; Outline

Transactions

Integrity Constraints

Referential Integrity

SQL Data Types and Schemas

Built-in Types

Index

UDT

Domains

Large Object

Authorization

Privileges

Revocation

Roles

Module Summary

## Module Recap

- SQL expressions for Join and Views

![Image](Lecture 3.4_artifacts/image_000002_0d9dfbde1de846c018eea32fe6aba21e8a9c7f3c69ef770101468a6cfb66a6e5.png)

## Module 14

Partha Pratim Das

Objectives &amp; Outline

Transactions

Integrity Constraints

Referential Integrity

SQL Data Types and Schemas Built-in Types

Index

UDT

Domains

Large Object

Authorization

Privileges

Revocation

Roles

Module Summary

## Module Objectives

- To understand Transactions
- To learn SQL expressions for Integrity Constraints
- To understand more Data Types in SQL
- To understand Authorization in SQL

![Image](Lecture 3.4_artifacts/image_000003_0d9dfbde1de846c018eea32fe6aba21e8a9c7f3c69ef770101468a6cfb66a6e5.png)

## Module 14

Partha Pratim Das

Objectives &amp; Outline

Transactions

Integrity Constraints

Referential Integrity

SQL Data Types and Schemas Built-in Types

Index

UDT

Domains

Large Object

Authorization

Privileges

Revocation

Roles

Module Summary

## Module Outline

- Transactions
- Integrity Constraints
- SQL Data Types and Schemas
- Authorization

![Image](Lecture 3.4_artifacts/image_000004_bbaa640f2b7c7b6f18cdf441c797dcf1ce99e755b6ef0a9bbf7b581538bddcab.png)

## Module 14

Partha Pratim Das

Objectives &amp; Outline

Transactions

Integrity Constraints

Referential Integrity

SQL Data Types and Schemas

Built-in Types

Index

UDT

Domains

Large Object

Authorization

Privileges

Revocation

Roles

Module Summary

## Transactions

## Transactions

![Image](Lecture 3.4_artifacts/image_000005_bbaa640f2b7c7b6f18cdf441c797dcf1ce99e755b6ef0a9bbf7b581538bddcab.png)

## Module 14

Partha Pratim Das

Objectives &amp; Outline

Transactions

Integrity Constraints

Referential Integrity

SQL Data Types and Schemas

Built-in Types

Index

UDT

Domains

Large Object

Authorization

Privileges

Revocation

Roles

Module Summary

## Transactions

- Unit of work
- Atomic transaction
- either fully executed or rolled back as if it never occurred
- Isolation from concurrent transactions
- Transactions begin implicitly
- Ended by commit work or rollback work
- But default on most databases: each SQL statement commits automatically
- Can turn off auto commit for a session (for example, using API)
- In SQL:1999, can use: begin atomic ... end
- glyph[triangleright] Not supported on most databases

![Image](Lecture 3.4_artifacts/image_000006_bbaa640f2b7c7b6f18cdf441c797dcf1ce99e755b6ef0a9bbf7b581538bddcab.png)

Module 14

Partha Pratim Das

Objectives &amp; Outline

Transactions

Integrity Constraints

Referential Integrity

SQL Data Types and Schemas

Built-in Types

Index

UDT

Domains

Large Object

Authorization

Privileges

Revocation

Roles

Module Summary

## Integrity Constraints

## Integrity Constraints

![Image](Lecture 3.4_artifacts/image_000007_0d9dfbde1de846c018eea32fe6aba21e8a9c7f3c69ef770101468a6cfb66a6e5.png)

## Module 14

Partha Pratim Das

Objectives &amp; Outline

Transactions

Integrity Constraints

Referential Integrity

SQL Data Types and Schemas Built-in Types

Index

UDT

Domains

Large Object

Authorization

Privileges

Revocation

Roles

Module Summary

## Integrity Constraints

- Integrity constraints guard against accidental damage to the database, by ensuring that authorized changes to the database do not result in a loss of data consistency
- A checking account must have a balance greater than Rs. 10,000.00
- A salary of a bank employee must be at least Rs. 250.00 an hour
- A customer must have a (non-null) phone number

![Image](Lecture 3.4_artifacts/image_000008_0d9dfbde1de846c018eea32fe6aba21e8a9c7f3c69ef770101468a6cfb66a6e5.png)

## Module 14

Partha Pratim Das

Objectives &amp; Outline

Transactions

Integrity Constraints

Referential Integrity

SQL Data Types and Schemas Built-in Types

Index

UDT

Domains

Large Object

Authorization

Privileges

Revocation

Roles

Module Summary

## Integrity Constraints on a Single Relation

- not null
- primary key
- unique
- check (P), where P is a predicate

![Image](Lecture 3.4_artifacts/image_000009_0d9dfbde1de846c018eea32fe6aba21e8a9c7f3c69ef770101468a6cfb66a6e5.png)

## Module 14

Partha Pratim Das

Objectives &amp; Outline

Transactions

Integrity Constraints

Referential Integrity

SQL Data Types and Schemas Built-in Types

Index

UDT

Domains

Large Object

Authorization

Privileges

Revocation

Roles

Module Summary

## Not Null and Unique Constraints

## · not null

- Declare name and budget to be not null name varchar (20) not null budget numeric (12,2) not null
- unique ( A 1 , A 2 , . . . , A m )
- The unique specification states that the attributes A 1 , A 2 , . . . , A m form a candidate key
- Candidate keys are permitted to be null (in contrast to primary keys).

![Image](Lecture 3.4_artifacts/image_000010_bbaa640f2b7c7b6f18cdf441c797dcf1ce99e755b6ef0a9bbf7b581538bddcab.png)

## Module 14

Partha Pratim Das

Objectives &amp; Outline

Transactions

Integrity Constraints

Referential Integrity

SQL Data Types and Schemas

Built-in Types

Index

UDT

Domains

Large Object

Authorization

Privileges

Revocation

Roles

Module Summary

## The check clause

- check (P), where P is a predicate
- Ensure that semester is one of fall, winter, spring or summer:

create table section

( course id varchar (8), sec id varchar (8), semester varchar (6), year numeric (4,0), building varchar (15), room number varchar (7), time slot id varchar (4), primary key ( course id, sec id, semester, year ), check (semester in ('Fall', 'Winter', 'Spring', 'Summer'))

![Image](Lecture 3.4_artifacts/image_000011_9f85e738fbd012c44fb81223a5584a65fd8c16cedea0018f18896bf3121c82bb.png)

![Image](Lecture 3.4_artifacts/image_000012_0d9dfbde1de846c018eea32fe6aba21e8a9c7f3c69ef770101468a6cfb66a6e5.png)

## Module 14

Partha Pratim Das

Objectives &amp; Outline

Transactions

Integrity Constraints

Referential Integrity

SQL Data Types and Schemas Built-in Types

Index

UDT

Domains

Large Object

Authorization

Privileges

Revocation

Roles

Module Summary

## Referential Integrity

- Ensures that a value that appears in one relation for a given set of attributes also appears for a certain set of attributes in another relation
- Example: If 'Biology' is a department name appearing in one of the tuples in the instructor relation, then there exists a tuple in the department relation for 'Biology'
- Let A be a set of attributes. Let R and S be two relations that contain attributes A and where A is the primary key of S. A is said to be a foreign key of R if for any values of A appearing in R these values also appear in S

![Image](Lecture 3.4_artifacts/image_000013_32155ccc63eaf8ac3b5d36be7560257f854d0b99536286a17a16546fbab339af.png)

Module 14

Partha Pratim Das

Objectives &amp; Outline

Transactions

Integrity Constraints

Referential Integrity

SQL Data Types and Schemas Built-in Types

Index

UDT

Domains

Large Object

Authorization

Privileges

Revocation

Roles

Module Summary

## Cascading Actions in Referential Integrity

- With cascading, you can define the actions that the Database Engine takes when a user tries to delete or update a key to which existing foreign keys point
- create table course (

course id char (5) primary key , title varchar (20), dept name varchar (20) references department

)

- create table course (

. . .

dept name varchar (20), foreign key ( dept name ) references department on delete cascade on update cascade ,

. . .

)

- Alternative actions to cascade: no action, set null, set default Database Management Systems Partha Pratim Das

![Image](Lecture 3.4_artifacts/image_000014_0d9dfbde1de846c018eea32fe6aba21e8a9c7f3c69ef770101468a6cfb66a6e5.png)

## Module 14

Partha Pratim Das

Objectives &amp; Outline

Transactions

Integrity Constraints

Referential Integrity

SQL Data Types and Schemas

Built-in Types

Index

UDT

Domains

Large Object

Authorization

Privileges

Revocation

Roles

Module Summary

## Integrity Constraint Violation During Transactions

- create table person ( ID char (10), name char (40), mother char (10), father char (10), primary key ID , foreign key father references person , foreign key mother references person

)

- How to insert a tuple without causing constraint violation?
- Insert father and mother of a person before inserting person
- OR, Set father and mother to null initially, update after inserting all persons (not possible if father and mother attributes declared to be not null )
- OR Defer constraint checking (will discuss later)

![Image](Lecture 3.4_artifacts/image_000015_fde1132bf222cc20a3e76fd9bad23db921b22024804914407d2f2bc1b513e47e.png)

Module 14

Partha Pratim Das

Objectives &amp; Outline

Transactions

Integrity Constraints

Referential Integrity

SQL Data Types and Schemas

Built-in Types

Index

UDT

Domains

Large Object

Authorization

Privileges

Revocation

Roles

Module Summary

## SQL Data Types and Schemas

## SQL Data Types and Schemas

![Image](Lecture 3.4_artifacts/image_000016_bbaa640f2b7c7b6f18cdf441c797dcf1ce99e755b6ef0a9bbf7b581538bddcab.png)

## Module 14

Partha Pratim Das

Objectives &amp; Outline

Transactions

Integrity Constraints

Referential Integrity

SQL Data Types and Schemas

Built-in Types

Index

UDT

Domains

Large Object

Authorization

Privileges

Revocation

Roles

Module Summary

## Built-in Data Types in SQL

- date : Dates, containing a (4 digit) year, month and date
- Example: date '2005-7-27'
- time : Time of day, in hours, minutes and seconds.
- Example: time '09:00:30' time '09:00:30.75'
- timestamp : date plus time of day
- Example: timestamp '2005-7-27 09:00:30.75'
- interval : period of time
- Example: interval '1' day
- Subtracting a date/time/timestamp value from another gives an interval value
- Interval values can be added to date/time/timestamp values

![Image](Lecture 3.4_artifacts/image_000017_0d9dfbde1de846c018eea32fe6aba21e8a9c7f3c69ef770101468a6cfb66a6e5.png)

Module 14

Partha Pratim Das

Objectives &amp; Outline

Transactions

Integrity Constraints

Referential Integrity

SQL Data Types and Schemas Built-in Types

Index

UDT

Domains

Large Object

Authorization

Privileges

Revocation

Roles

Module Summary

## Index Creation

- create table student

( ID varchar (5), name varchar (20) not null , dept name varchar (20), tot cred numeric (3,0) default 0, primary key ( ID ))

- create index studentID index on student(ID)
- Indices are data structures used to speed up access to records with specified values for index attributes
- select *

from student where ID = '12345'

- Can be executed by using the index to find the required record, without looking at all records of student
- More on indices in Chapter 9

Partha Pratim Das

![Image](Lecture 3.4_artifacts/image_000018_bbaa640f2b7c7b6f18cdf441c797dcf1ce99e755b6ef0a9bbf7b581538bddcab.png)

## Module 14

Partha Pratim Das

Objectives &amp; Outline

Transactions

Integrity Constraints

Referential Integrity

SQL Data Types and Schemas

Built-in Types

Index

UDT

Domains

Large Object

Authorization

Privileges

Revocation

Roles

Module Summary

## User-Defined Types

- construct in SQL creates user-defined type (alias, like typedef in C)
- create type create type Dollars as numeric (12,2) final

◦ create table department (

dept name varchar (20), building varchar (15), budget Dollars );

![Image](Lecture 3.4_artifacts/image_000019_bbaa640f2b7c7b6f18cdf441c797dcf1ce99e755b6ef0a9bbf7b581538bddcab.png)

## Module 14

Partha Pratim Das

Objectives &amp; Outline

Transactions

Integrity Constraints

Referential Integrity

SQL Data Types and Schemas

Built-in Types

Index

UDT

Domains

Large Object

Authorization

Privileges

Revocation

Roles

Module Summary

## Domains

- create domain construct in SQL-92 creates user-defined domain types create domain person name char (20) not null
- Types and domains are similar
- Domains can have constraints, such as not null , specified on them create domain degree level varchar (10) constraint degree level test check ( value in ('Bachelors', 'Masters', 'Doctorate'));

![Image](Lecture 3.4_artifacts/image_000020_bbaa640f2b7c7b6f18cdf441c797dcf1ce99e755b6ef0a9bbf7b581538bddcab.png)

## Module 14

Partha Pratim Das

Objectives &amp; Outline

Transactions

Integrity Constraints

Referential Integrity

SQL Data Types and Schemas Built-in Types

Index

UDT

Domains

Large Object

Authorization

Privileges

Revocation

Roles

Module Summary

## Large-Object Types

- Large objects (photos, videos, CAD files, etc.) are stored as a large object :
- blob : binary large object - object is a large collection of uninterpreted binary data (whose interpretation is left to an application outside of the database system)
- clob : character large object - object is a large collection of character data
- When a query returns a large object, a pointer is returned rather than the large object itself

![Image](Lecture 3.4_artifacts/image_000021_fde1132bf222cc20a3e76fd9bad23db921b22024804914407d2f2bc1b513e47e.png)

## Module 14

Partha Pratim Das

Objectives &amp; Outline

Transactions

Integrity Constraints

Referential Integrity

SQL Data Types and Schemas

Built-in Types

Index

UDT

Domains

Large Object

Authorization

Privileges

Revocation

Roles

Module Summary

## Authorization

## Authorization

![Image](Lecture 3.4_artifacts/image_000022_0d9dfbde1de846c018eea32fe6aba21e8a9c7f3c69ef770101468a6cfb66a6e5.png)

## Module 14

Partha Pratim Das

Objectives &amp; Outline

Transactions

Integrity Constraints

Referential Integrity

SQL Data Types and Schemas

Built-in Types

Index

UDT

Domains

Large Object

Authorization

Privileges

Revocation

Roles

Module Summary

## Authorization

- Forms of authorization on parts of the database:
- Read - allows reading, but not modification of data
- Insert - allows insertion of new data, but not modification of existing data
- Update - allows modification, but not deletion of data
- Delete - allows deletion of data
- Forms of authorization to modify the database schema
- Index - allows creation and deletion of indices
- Resources - allows creation of new relations
- Alteration - allows addition or deletion of attributes in a relation
- Drop - allows deletion of relations

![Image](Lecture 3.4_artifacts/image_000023_0d9dfbde1de846c018eea32fe6aba21e8a9c7f3c69ef770101468a6cfb66a6e5.png)

## Module 14

Partha Pratim Das

Objectives &amp; Outline

Transactions

Integrity Constraints

Referential Integrity

SQL Data Types and Schemas

Built-in Types

Index

UDT

Domains

Large Object

Authorization

Privileges

Revocation

Roles

Module Summary

## Authorization Specification in SQL

- The grant statement is used to confer authorization

grant

&lt;

privilege list

&gt;

- on &lt; relation name or view name &gt; to &lt; user list &gt;
- &lt; user list &gt; is:
- a user-id
- public , which allows all valid users the privilege granted
- A role (more on this later)
- Granting a privilege on a view does not imply granting any privileges on the underlying relations
- The grantor of the privilege must already hold the privilege on the specified item (or be the database administrator)

![Image](Lecture 3.4_artifacts/image_000024_0d9dfbde1de846c018eea32fe6aba21e8a9c7f3c69ef770101468a6cfb66a6e5.png)

## Module 14

Partha Pratim Das

Objectives &amp; Outline

Transactions

Integrity Constraints

Referential Integrity

SQL Data Types and Schemas

Built-in Types

Index

UDT

Domains

Large Object

Authorization

Privileges

Revocation

Roles

Module Summary

## Privileges in SQL

- select : allows read access to relation, or the ability to query using the view
- Example: grant users U 1 , U 2 , and U 3 select authorization on the instructor relation: grant select on instructor to U 1 , U 2 , U 3
- insert : the ability to insert tuples
- update : the ability to update using the SQL update statement
- delete : the ability to delete tuples.
- all privileges : used as a short form for all the allowable privileges

![Image](Lecture 3.4_artifacts/image_000025_0d9dfbde1de846c018eea32fe6aba21e8a9c7f3c69ef770101468a6cfb66a6e5.png)

## Module 14

Partha Pratim Das

Objectives &amp; Outline

Transactions

Integrity Constraints

Referential Integrity

SQL Data Types and Schemas

Built-in Types

Index

UDT

Domains

Large Object

Authorization

Privileges

Revocation

Roles

Module Summary

## Revoking Authorization in SQL

- •
- The revoke statement is used to revoke authorization revoke &lt; privilege list &gt;
- on &lt; relation name or view name &gt; from &lt; user list &gt;
- Example:

## revoke select on branch from U 1 , U 2 , U 3

- &lt; privilege-list &gt; may be all to revoke all privileges the revokee may hold
- If &lt; revokee-list &gt; includes public , all users lose the privilege except those granted it explicitly
- If the same privilege was granted twice to the same user by different grantees, the user may retain the privilege after the revocation
- All privileges that depend on the privilege being revoked are also revoked

![Image](Lecture 3.4_artifacts/image_000026_0d9dfbde1de846c018eea32fe6aba21e8a9c7f3c69ef770101468a6cfb66a6e5.png)

## Module 14

Partha Pratim Das

Objectives &amp; Outline

Transactions

Integrity Constraints

Referential Integrity

SQL Data Types and Schemas

Built-in Types

Index

UDT

Domains

Large Object

Authorization

Privileges

Revocation

Roles

Module Summary

## Roles

- create role instructor

Amit;

- ; grant instructor to
- Privileges can be granted to roles: grant select on takes to instructor ;
- Roles can be granted to users, as well as to other roles create role teaching assistant grant teaching assistant to instructor ;
- Instructor inherits all privileges of teaching assistant
- Chain of roles
- create role dean;
- grant instructor to dean;
- grant dean to Satoshi;

![Image](Lecture 3.4_artifacts/image_000027_0d9dfbde1de846c018eea32fe6aba21e8a9c7f3c69ef770101468a6cfb66a6e5.png)

## Module 14

Partha Pratim Das

Objectives &amp; Outline

Transactions

Integrity Constraints

Referential Integrity

SQL Data Types and Schemas

Built-in Types

Index

UDT

Domains

Large Object

Authorization

Privileges

Revocation

Roles

Module Summary

## Authorization on Views

- create view geo instructor as
- ( select *

from instructor

- where dept name = 'Geology');
- grant select on geo instructor to geo staff
- Suppose that a geo staff member issues select * from geo instructor ;
- What if
- geo staff does not have permissions on instructor ?
- creator of view did not have some permissions on instructor ?

![Image](Lecture 3.4_artifacts/image_000028_bbaa640f2b7c7b6f18cdf441c797dcf1ce99e755b6ef0a9bbf7b581538bddcab.png)

## Module 14

Partha Pratim Das

Objectives &amp; Outline

Transactions

Integrity Constraints

Referential Integrity

SQL Data Types and Schemas Built-in Types

Index

UDT

Domains

Large Object

Authorization

Privileges

Revocation

Roles

Module Summary

## Other Authorization Features

- references privilege to create foreign key grant reference ( dept name ) on department to Mariano;
- why is this required?
- Transfer of privileges
- grant select on department to Amit with grant option ;
- revoke select on department from Amit, Satoshi cascade ;
- revoke select on department from Amit, Satoshi restrict ;

![Image](Lecture 3.4_artifacts/image_000029_0d9dfbde1de846c018eea32fe6aba21e8a9c7f3c69ef770101468a6cfb66a6e5.png)

## Module 14

Partha Pratim Das

Objectives &amp; Outline

Transactions

Integrity Constraints

Referential Integrity

SQL Data Types and Schemas Built-in Types

Index

UDT

Domains

Large Object

Authorization

Privileges

Revocation

Roles

Module Summary

## Module Summary

- Introduced transactions
- Learnt SQL expressions for integrity constraints
- Familiarized with more data types in SQL
- Discussed authorization in SQL

Slides used in this presentation are borrowed from http://db-book.com/ with kind permission of the authors. Edited and new slides are marked with 'PPD'.

Database Management Systems

Partha Pratim Das
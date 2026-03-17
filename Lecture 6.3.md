![Image](Lecture 6.3_artifacts/image_000000_bbaa640f2b7c7b6f18cdf441c797dcf1ce99e755b6ef0a9bbf7b581538bddcab.png)

## Module 28

Partha Pratim Das

Objectives &amp; Outline

Library

Information

System

Specification

Entity Sets

Relationships

Relational Schema

Schema Refinement

Final Schema

Module Summary

## Database Management Systems

Module 28: Relational Database Design/8: Case Study

## Partha Pratim Das

Department of Computer Science and Engineering Indian Institute of Technology, Kharagpur ppd@cse.iitkgp.ac.in

Partha Pratim Das

![Image](Lecture 6.3_artifacts/image_000001_b551d1d039a350a56349b412170007d20638ad0732feb40b06cdb100cf6ab680.png)

## Module 28

Partha Pratim Das

Objectives &amp; Outline

Library

Information

System

Specification

Entity Sets

Relationships

Relational Schema

Schema Refinement

Final Schema

Module Summary

## Module Recap

- Learnt how to decompose a schema into 3NF while preserving dependency and lossless join
- Learnt how to decompose a schema into BCNF with lossless join

![Image](Lecture 6.3_artifacts/image_000002_821f32da21a8bb9af0bddb9e2ff2419e915ba7e461f5dc4f05b60eaa6ed0b478.png)

## Module 28

Partha Pratim Das

Objectives &amp; Outline

Library

Information

System

Specification

Entity Sets

Relationships

Relational Schema

Schema Refinement

Final Schema

Module Summary

## Module Objectives

- To design the schema for a Library Information System

![Image](Lecture 6.3_artifacts/image_000003_0d2e8daa05c74407b310229f101057782122d2bf078613dc8c643ca2fdb280b5.png)

## Module 28

Partha Pratim Das

Objectives &amp; Outline

Library

Information

System

Specification

Entity Sets

Relationships

Relational Schema

Schema Refinement

Final Schema

Module Summary

## Module Outline

- Library Information System

![Image](Lecture 6.3_artifacts/image_000004_0d9dfbde1de846c018eea32fe6aba21e8a9c7f3c69ef770101468a6cfb66a6e5.png)

## Module 28

Partha Pratim Das

Objectives &amp; Outline

## Library Information System

Specification

Entity Sets

Relationships

Relational Schema

Schema Refinement

Final Schema

Module Summary

## Library Information System (LIS)

We are given to design a relational database schema for a Library Information System (LIS) of an Institute

- The specification document of the LIS has already been shared with you
- In this presentation, we include the key points from the Specs; but the actual document must be referred to
- We carry out the following tasks in the module:
- Identify the Entity Sets with attributes
- Identify the Relationships
- Build the initial set of relational schema
- Refine the set of schema with FDs that hold on them
- Finalize the design of the schema
- The coding of various queries in SQL, based on these schema are left as exercises

## Partha Pratim Das

![Image](Lecture 6.3_artifacts/image_000005_bbaa640f2b7c7b6f18cdf441c797dcf1ce99e755b6ef0a9bbf7b581538bddcab.png)

## Module 28

Partha Pratim Das

Objectives &amp; Outline

Library Information System

Specification

Entity Sets

Relationships

Relational Schema

Schema Refinement

Final Schema

Module Summary

## LIS Specs Excerpts

- An institute library has 200000+ books and 10000+ members
- Books are regularly issued by members on loan and returned after a period.
- The library needs an LIS to manage the books, the members and the issue-return process
- Every book has
- title
- author (in case of multiple authors, only the first author is maintained)
- publisher
- year of publication
- ISBN number (which is unique for the publication), and
- accession number (which is the unique number of the copy of the book in the library)
- There may be multiple copies of the same book in the library

![Image](Lecture 6.3_artifacts/image_000006_bbaa640f2b7c7b6f18cdf441c797dcf1ce99e755b6ef0a9bbf7b581538bddcab.png)

## Module 28

Partha Pratim Das

Objectives &amp; Outline

Library Information System

Specification

Entity Sets

Relationships

Relational Schema

Schema Refinement

Final Schema

Module Summary

## LIS Specs Excerpts (2)

- There are four categories of members of the library:
- undergraduate students
- post graduate students
- research scholars, and
- faculty members
- Every student has
- glyph[triangleright] name
- glyph[triangleright] roll number
- glyph[triangleright] department
- glyph[triangleright] gender
- glyph[triangleright] mobile number
- glyph[triangleright] date of birth, and
- glyph[triangleright] degree
- -undergrad
- -grad
- -doctoral

Database Management Systems

![Image](Lecture 6.3_artifacts/image_000007_0d9dfbde1de846c018eea32fe6aba21e8a9c7f3c69ef770101468a6cfb66a6e5.png)

## Module 28

Partha Pratim Das

Objectives &amp; Outline

Library Information System

Specification

Entity Sets

Relationships

Relational Schema

Schema Refinement

Final Schema

Module Summary

## LIS Specs Excerpts (3)

- Every faculty has
- name
- employee id
- department
- gender
- mobile number, and
- date of joining
- Library also issues a unique membership number to every member . Every member has a maximum quota for the number of books she / he can issue for the maximum duration allowed to her / him. Currently these are set as:
- Each undergraduate student can issue up to 2 books for 1 month duration
- Each postgraduate student can issue up to 4 books for 1 month duration
- Each research scholar can issue up to 6 books for 3 months duration
- Each faculty member can issue up to 10 books for six months duration

![Image](Lecture 6.3_artifacts/image_000008_bbaa640f2b7c7b6f18cdf441c797dcf1ce99e755b6ef0a9bbf7b581538bddcab.png)

## Module 28

Partha Pratim Das

Objectives &amp; Outline

Library Information System

Specification

Entity Sets

Relationships

Relational Schema

Schema Refinement

Final Schema

Module Summary

## LIS Specs Excerpts (4)

- The library has the following rules for issue:
- A book may be issued to a member if it is not already issued to someone else (trivial)
- A book may not be issued to a member if another copy of the same book is already issued to the same member
- No issue will be done to a member if at the time of issue one or more of the books issued by the member has already exceeded its duration of issue
- No issue will be allowed also if the quota is exceeded for the member
- It is assumed that the name of every author or member has two parts
- glyph[triangleright] first name
- glyph[triangleright] last name

![Image](Lecture 6.3_artifacts/image_000009_c66187055de285596be50032d73dadd82d2ef960cecf03026d68ecb78134d5c9.png)

## Module 28

Partha Pratim Das

Objectives &amp; Outline

Library

Information

System

Specification

Entity Sets

Relationships

Relational Schema

Schema Refinement

Final Schema

Module Summary

## LIS Specs Excerpts (5): Queries

LIS should support the following operations / query:

- Add / Remove members, categories of members, books.
- Add / Remove / Edit quota for a category of member, duration for a category of member.
- Check if the library has a book given its title (part of title should match). If yes: title, author, publisher, year and ISBN should be listed.
- Check if the library has a book given its author. If yes: title, author, publisher, year and ISBN should be listed.
- Check if a copy of a book (given its ISBN) is available with the library for issue. All accession numbers should be listed with issued or available information.
- Check the available (free) quota of a member.
- Issue a book to a member. This should check for the rules of the library.
- Return a book from a member.
- and so on

![Image](Lecture 6.3_artifacts/image_000010_821f32da21a8bb9af0bddb9e2ff2419e915ba7e461f5dc4f05b60eaa6ed0b478.png)

## Module 28

Partha Pratim Das

Objectives &amp; Outline

Library Information System Specification

Entity Sets

Relationships

Relational Schema

Schema Refinement

Final Schema

Module Summary

## LIS Entity Sets: books

- Every book has title, author (in case of multiple authors, only the first author is maintained), publisher, year of publication, ISBN number (which is unique for the publication), and accession number (which is the unique number of the copy of the book in the library). There may be multiple copies of the same book in the library
- Entity Set:
- books
- Attributes:
- title
- author name (composite)
- publisher
- year
- ISBN no
- accession no

![Image](Lecture 6.3_artifacts/image_000011_821f32da21a8bb9af0bddb9e2ff2419e915ba7e461f5dc4f05b60eaa6ed0b478.png)

## Module 28

Partha Pratim Das

Objectives &amp; Outline

Library

Information

System

Specification

Entity Sets

Relationships

Relational Schema

Schema Refinement

Final Schema

Module Summary

## LIS Entity Sets (2): students

- Every student has name, roll number, department, gender, mobile number, date of birth, and degree (undergrad, grad, doctoral)
- Entity Set:
- students
- Attributes:
- member no - is unique
- name (composite)
- ◦
- roll no - is unique
- department
- gender
- mobile no - may be null
- dob
- degree

![Image](Lecture 6.3_artifacts/image_000012_821f32da21a8bb9af0bddb9e2ff2419e915ba7e461f5dc4f05b60eaa6ed0b478.png)

## Module 28

Partha Pratim Das

Objectives &amp; Outline

Library

Information

System

Specification

Entity Sets

Relationships

Relational Schema

Schema Refinement

Final Schema

Module Summary

## LIS Entity Sets (3): faculty

- Every faculty has name, employee id, department, gender, mobile number, and date of joining
- Entity Set:
- faculty
- Attributes:
- member no - is unique
- name (composite)
- id - is unique
- department
- gender
- mobile no - may be null
- doj

![Image](Lecture 6.3_artifacts/image_000013_821f32da21a8bb9af0bddb9e2ff2419e915ba7e461f5dc4f05b60eaa6ed0b478.png)

## Module 28

Partha Pratim Das

Objectives &amp; Outline

Library Information System Specification

Entity Sets

Relationships

Relational Schema

Schema Refinement

Final Schema

Module Summary

## LIS Entity Sets (4): members

- Library also issues a unique membership number to every member. There are four categories of members of the library: undergraduate students, post graduate students, research scholars, and faculty members
- Entity Set:
- members
- Attributes:
- member no
- member type (takes a value in ug, pg, rs or fc)

![Image](Lecture 6.3_artifacts/image_000014_c66187055de285596be50032d73dadd82d2ef960cecf03026d68ecb78134d5c9.png)

## Module 28

Partha Pratim Das

Objectives &amp; Outline

Library Information System Specification

Entity Sets

Relationships

Relational Schema

Schema Refinement

Final Schema

Module Summary

## LIS Entity Sets (5): quota

- Every member has a maximum quota for the number of books she / he can issue for the maximum duration allowed to her / him. Currently these are set as:
- Each undergraduate student can issue up to 2 books for 1 month duration
- Each postgraduate student can issue up to 4 books for 1 month duration
- Each research scholar can issue up to 6 books for 3 months duration
- Each faculty member can issue up to 10 books for six months duration
- Entity Set:
- quota
- Attributes:
- member type
- max books
- max duration

![Image](Lecture 6.3_artifacts/image_000015_821f32da21a8bb9af0bddb9e2ff2419e915ba7e461f5dc4f05b60eaa6ed0b478.png)

## Module 28

Partha Pratim Das

Objectives &amp; Outline

Library

Information

System

Specification

Entity Sets

Relationships

Relational Schema

Schema Refinement

Final Schema

Module Summary

## LIS Entity Sets (6): staff

- Though not explicitly stated, library would have staffs to manage the LIS
- Entity Set:
- staff
- Attributes: (speculated - to ratify from customer)
- name (composite)
- id - is unique
- gender
- mobile no
- doj

![Image](Lecture 6.3_artifacts/image_000016_821f32da21a8bb9af0bddb9e2ff2419e915ba7e461f5dc4f05b60eaa6ed0b478.png)

## Module 28

Partha Pratim Das

Objectives &amp; Outline

Library

Information

System

Specification

Entity Sets

Relationships

Relational Schema

Schema Refinement

Final Schema

Module Summary

## LIS Relationships

- Books are regularly issued by members on loan and returned after a period. The library needs an LIS to manage the books, the members and the issue-return process
- Relationship
- book issue
- Involved Entity Sets
- students / faculty / members
- glyph[triangleright] member no
- books
- glyph[triangleright] accession no
- Relationship Attribute
- doi - date of issue
- Type of relationship
- Many-to-one from books

![Image](Lecture 6.3_artifacts/image_000017_b551d1d039a350a56349b412170007d20638ad0732feb40b06cdb100cf6ab680.png)

## Module 28

Partha Pratim Das

Objectives &amp; Outline

Library

Information

System

Specification

Entity Sets

Relationships

Relational Schema

Schema Refinement

Final Schema

Module Summary

## LIS Relational Schema

- books (title, author fname, author lname, publisher, year, ISBN no, accession no)
- book issue (members, accession no, doi)
- members (member no, member type)
- quota (member type, max books, max duration)
- students (member no, student fname, student lname, roll no, department, gender, mobile no, dob, degree)
- faculty (member no, faculty fname, faculty lname, id, department, gender, mobile no, doj)
- staff (staff fname, staff lname, id, gender, mobile no, doj)

![Image](Lecture 6.3_artifacts/image_000018_0d2e8daa05c74407b310229f101057782122d2bf078613dc8c643ca2fdb280b5.png)

## Module 28

Partha Pratim Das

Objectives &amp; Outline

Library

Information

System

Specification

Entity Sets

Relationships

Relational Schema

Schema Refinement

Final Schema

Module Summary

## LIS Schema Refinement: books

- books (title, author fname, author lname, publisher, year, ISBN no, accession no)
- ISBN no → title, author fname, author lname, publisher, year
- accession no → ISBN no
- Key: accession no
- Redundancy of book information across copies
- Good to normalize:
- book catalogue (title, author fname, author lname, publisher, year, ISBN no)
- glyph[triangleright] ISBN no → title, author fname, author lname, publisher, year glyph[triangleright] Key: ISBN no
- book copies (ISBN no, accession no)
- glyph[triangleright] accession no → ISBN no
- glyph[triangleright] Key: accession no
- Both in BCNF. Decomposition is lossless join and dependency preserving

## Partha Pratim Das

![Image](Lecture 6.3_artifacts/image_000019_821f32da21a8bb9af0bddb9e2ff2419e915ba7e461f5dc4f05b60eaa6ed0b478.png)

## Module 28

Partha Pratim Das

Objectives &amp; Outline

Library

Information

System

Specification

Entity Sets

Relationships

Relational Schema

Schema Refinement

Final Schema

Module Summary

## LIS Schema Refinement (2): book issue

- book issue (member no, accession no, doi)
- member no, accession no → doi
- Key: members, accession no
- In BCNF

![Image](Lecture 6.3_artifacts/image_000020_888591e5dd6dea054336d6d8e77787822b7eeba224e5492bf3f9820e7c8defbc.png)

![Image](Lecture 6.3_artifacts/image_000021_0d9dfbde1de846c018eea32fe6aba21e8a9c7f3c69ef770101468a6cfb66a6e5.png)

## Module 28

Partha Pratim Das

Objectives &amp; Outline

Library

Information

System

Specification

Entity Sets

Relationships

Relational Schema

Schema Refinement

Final Schema

Module Summary

## LIS Schema Refinement (3): quota

- quota (member type, max books, max duration)
- member type → max books, max duration
- Key: member type
- In BCNF

![Image](Lecture 6.3_artifacts/image_000022_0d9dfbde1de846c018eea32fe6aba21e8a9c7f3c69ef770101468a6cfb66a6e5.png)

## Module 28

Partha Pratim Das

Objectives &amp; Outline

Library

Information

System

Specification

Entity Sets

Relationships

Relational Schema

Schema Refinement

Final Schema

Module Summary

## LIS Schema Refinement (4): members

- members (member no, member type)
- member no → member type
- Key: member no
- Value constraint on member type
- glyph[triangleright] ug, pg, or rs: if the member is a student
- glyph[triangleright] fc: if the member is a faculty
- In BCNF
- How to determine the member type?

![Image](Lecture 6.3_artifacts/image_000023_0d9dfbde1de846c018eea32fe6aba21e8a9c7f3c69ef770101468a6cfb66a6e5.png)

## Module 28

Partha Pratim Das

Objectives &amp; Outline

Library

Information

System

Specification

Entity Sets

Relationships

Relational Schema

Schema Refinement

Final Schema

Module Summary

## LIS Schema Refinement (5): students

- students (member no, student fname, student lname, roll no, department, gender, mobile no, dob, degree)
- roll no → student fname, student lname, department, gender, mobile no, dob, degree
- member no → roll no
- roll no → member no
- 2 Keys: roll no | member no
- In BCNF
- Issues:
- member no is needed for issue / return queries. It is unnecessary to have student's details with that.
- member no may also come from faculty relation.
- member type is needed for issue / return queries. This is implicit in degree - not explicitly given.

![Image](Lecture 6.3_artifacts/image_000024_0d9dfbde1de846c018eea32fe6aba21e8a9c7f3c69ef770101468a6cfb66a6e5.png)

## Module 28

Partha Pratim Das

Objectives &amp; Outline

Library

Information

System

Specification

Entity Sets

Relationships

Relational Schema

Schema Refinement

Final Schema

Module Summary

## LIS Schema Refinement (6): faculty

- faculty (member no, faculty fname, faculty lname, id, department, gender, mobile no, doj)
- id → faculty fname, faculty lname, department, gender, mobile no, doj
- id → member no
- member no → id
- 2 Keys: id | member no
- In BCNF
- Issues:
- member no is needed for issue / return queries. It is unnecessary to have faculty details with that.
- member no may also come from students relation.
- member type is needed for issue / return queries. This is implicit by the fact that we are in faculty relation.

![Image](Lecture 6.3_artifacts/image_000025_bbaa640f2b7c7b6f18cdf441c797dcf1ce99e755b6ef0a9bbf7b581538bddcab.png)

## Module 28

Partha Pratim Das

Objectives &amp; Outline

Library

Information

System

Specification

Entity Sets

Relationships

Relational Schema

Schema Refinement

Final Schema

Module Summary

## LIS Schema Refinement (7): Query

- Consider a query:
- Get the name of the member who has issued the book having accession number = 162715
- glyph[triangleright] If the member is a student,
- SELECT student fname as First Name, student lname as Last Name
- FROM students , book issue
- WHERE accession no = 162715 AND book issue.member no = students.member no;
- glyph[triangleright] If the member is a faculty,
- SELECT faculty fname as First Name, faculty lname as Last Name
- FROM faculty , book issue
- WHERE accession no = 162715 AND book issue.member no = faculty.member no;
- Which query to fire!

![Image](Lecture 6.3_artifacts/image_000026_0d9dfbde1de846c018eea32fe6aba21e8a9c7f3c69ef770101468a6cfb66a6e5.png)

## Module 28

Partha Pratim Das

Objectives &amp; Outline

Library

Information

System

Specification

Entity Sets

Relationships

Relational Schema

Schema Refinement

Final Schema

Module Summary

## LIS Schema Refinement (8): members

There are 4 categories of members: ug students, grad students, research scholars, and faculty members. This leads to the following specialization relationships:

- Consider the entity set members of a library and refine:
- Attributes:
- glyph[triangleright] member no
- glyph[triangleright] member class - 'student' or 'faculty', used to choose table
- glyph[triangleright] member type - ug,pg, rs, fc, ...
- glyph[triangleright] roll no (if member class - 'student'. Else null)
- glyph[triangleright] id (if member class - 'faculty'. Else null)
- We can then exploit some hidden relationship:
- students IS A members
- faculty IS A members
- Type of relationship
- One-to-one

![Image](Lecture 6.3_artifacts/image_000027_bbaa640f2b7c7b6f18cdf441c797dcf1ce99e755b6ef0a9bbf7b581538bddcab.png)

## Module 28

Partha Pratim Das

Objectives &amp; Outline

Library

Information

System

Specification

Entity Sets

Relationships

Relational Schema

Schema Refinement

Final Schema

Module Summary

## LIS Schema Refinement (9): Query

- Consider the access query again:
- Get the name of the member who has issued the book having accession number = 162715

SELECT ((SELECT faculty fname as First Name, faculty lname as Last Name FROM faculty WHERE member class = 'faculty' AND members.id = faculty.id) UNION (SELECT student fname as First Name, student lname as Last Name FROM students WHERE member class = 'student' AND members.roll no = students.roll no)) FROM members , book issue

WHERE accession no = 162715 AND book issue.member no = members.member no;

![Image](Lecture 6.3_artifacts/image_000028_0d9dfbde1de846c018eea32fe6aba21e8a9c7f3c69ef770101468a6cfb66a6e5.png)

## Module 28

Partha Pratim Das

Objectives &amp; Outline

Library

Information

System

Specification

Entity Sets

Relationships

Relational Schema

Schema Refinement

Final Schema

Module Summary

## LIS Schema Refinement (10): members

- members (member no, member class, member type, roll no, id)
- member no → member type, member class, roll no, id
- member type → member class
- Key: member no

![Image](Lecture 6.3_artifacts/image_000029_0d9dfbde1de846c018eea32fe6aba21e8a9c7f3c69ef770101468a6cfb66a6e5.png)

## Module 28

Partha Pratim Das

Objectives &amp; Outline

Library

Information

System

Specification

Entity Sets

Relationships

Relational Schema

Schema Refinement

Final Schema

Module Summary

## LIS Schema Refinement (11): students

- students (student fname, student lname, roll no, department, gender, mobile no, dob, degree)
- roll no → student fname, student lname, department, gender, mobile no, dob, degree
- Keys: roll no
- Note:
- glyph[triangleright] member no is no longer used
- glyph[triangleright] member type and member class are set in members from degree at the time of creation of a new record.

![Image](Lecture 6.3_artifacts/image_000030_7ecea76d9f966d8e75ee26e313871ef559cac6cbff3465c37bb55be8fdff2482.png)

![Image](Lecture 6.3_artifacts/image_000031_0d9dfbde1de846c018eea32fe6aba21e8a9c7f3c69ef770101468a6cfb66a6e5.png)

## Module 28

Partha Pratim Das

Objectives &amp; Outline

Library

Information

System

Specification

Entity Sets

Relationships

Relational Schema

Schema Refinement

Final Schema

Module Summary

## LIS Schema Refinement (12): faculty

- faculty (faculty fname, faculty lname, id, department, gender, mobile no, doj)
- id → faculty fname, faculty lname, department, gender, mobile no, doj
- Keys: id
- Note:
- glyph[triangleright] member no is no longer used
- glyph[triangleright] member type and member class are set in members at the time of creation of a new record

![Image](Lecture 6.3_artifacts/image_000032_0d9dfbde1de846c018eea32fe6aba21e8a9c7f3c69ef770101468a6cfb66a6e5.png)

## Module 28

Partha Pratim Das

Objectives &amp; Outline

Library

Information

System

Specification

Entity Sets

Relationships

Relational Schema

Schema Refinement

Final Schema

Module Summary

## LIS Schema Refinement (13): Final

- book catalogue (title, author fname, author lname, publisher, year, ISBN no)
- book copies (ISBN no, accession no)
- book issue (member no, accession no, doi)
- quota (member type, max books, max duration)
- members (member no, member class, member type, roll no, id)
- students (student fname, student lname, roll no, department, gender, mobile no, dob, degree)
- faculty (faculty fname, faculty lname, id, department, gender, mobile no, doj)
- staff (staff fname, staff lname, id, gender, mobile no, doj)

![Image](Lecture 6.3_artifacts/image_000033_0d9dfbde1de846c018eea32fe6aba21e8a9c7f3c69ef770101468a6cfb66a6e5.png)

## Module 28

Partha Pratim Das

Objectives &amp; Outline

Library

Information

System

Specification

Entity Sets

Relationships

Relational Schema

Schema Refinement

Final Schema

Module Summary

## Module Summary

- Using the specification for a Library Information System, we have illustrated how a schema can be designed and then refined for finalization
- Coding of various queries based on these schema are left as exercises

Slides used in this presentation are borrowed from http://db-book.com/ with kind permission of the authors. Edited and new slides are marked with 'PPD'.
<!-- image -->

## Database Management Systems Professor Patha Pratim Das Department of Computer Science and Engineering Indian Institute of Technology, Kharagpur Course Overview

Welcome students to the IIT Madras online BSc program. I am very happy to meet you in this  program,  I  am  Professor  Partha  Pratim  Das,  I  teach  in  the  Computer  Science  and Engineering  Department  of  IIT  Kharagpur.  I  have  been  teaching  for  several  decades  now. And I am really happy to be part of this course, which is unique in India, the first time you are going to get an opportunity to get an online BSc degree from an IIT.

So,  let  us  get  started  with  the  course,  as  you  know  this  will  be  on  database  management systems. And in the, this is the first module in which I will take you through the overview of the course primarily.

<!-- image -->

So, this is the objective to understand the importance of database management systems today, I  am sure all of  you in some form of other are familiar with the need and use of database systems in today's life. But we will try to take a deeper look, go deeper and deeper as the course progresses. And also in this module we will give you the necessary information about the course.

## (Refer Slide Time: 1:58)

<!-- image -->

So, the outline would be why databases and the know your course prerequisites, outline and the course textbook. (Refer Slide Time: 2:07) 2

<!-- image -->

So, why databases? A database management system contains information about a particular enterprise when you use the term enterprise it could mean a small business, it could mean a big  business,  it  could  mean  a  nation,  it  could  mean  a  bank,  it  could  mean  a  global organization or even it could mean a small group or even individuals. So, any entity which has the requirement of collecting collection of interrelated data, set of programs to process that data. And it is an environment that is convenient and efficient to use will need a database system and that is what the database system will provide.

Now, if  we  just  quickly  tried  to  talk  of  what  different  kinds  of  applications  the  databases have, you will know that the most familiar possibly is banking applications. We are regularly doing various forms of net banking transactions now you have UPI, Paytm, BHIM, Google Pay, all of that are very large database applications at the back.

We have reservation applications, airlines, railways,  IRCTC, all of those, they are all very important  applications,  critical  applications.  Then  we  have  a  lot  of  academic  applications, universities will deal with reservations,  your admissions, examination, registration, grading all of that, we typically say it is an ERP system. And all IITs, NITs and several Institute's use those kinds of systems, very heavy database applications.

Any  different  kinds  of  sales,  like  the  whole  of  e-commerce  retailers,  Amazon,  e-bay, Snapdeal. All of those are very, very wide big database applications. Then even in other areas like  manufacturing,  in  human  resources,  in  travel,  everywhere  databases  are  kind  of applications on which we necessarily survive today.

And what might come as a little bit of surprise for you that several applications which you do not  really  associate  with  a  typical  database  application  like  net  banking  transaction, applications  like  your  email  system,  say  Gmail,  Google  Mail,  or  Yahoo  Mail,  or  your Hotmail, they are also database applications because they keep all the information about your mails and your contacts, your send-receive information and so on inside them.

Even the social media, the Facebook, the Instagram, the Twitter, the WhatsApp kind of chat applications, telegram all of these need databases. So, it is so pervading in our daily life, in our daily applications today that it is very difficult to isolate and talk about only one that or only a few which will be useful.

So, what you are going to learn here is going to be useful all across the board and therefore, the skills of database programming, skills of database design, skills of database administration  has  a  deep  requirement  in  the  industry  both  in  the  core  IT  infrastructure industry as well as IT applications industry in varied kinds of BPOs, and so on.

## (Refer Slide Time: 6:15)

<!-- image -->

So, databases, as I said, touches all aspects of our life. So, simple application and university database  application  so  you  can  add  new  students,  new  faculty,  courses,  instructors, timetable, classroom, you can register students for courses, generate rosters for classes, the timetable, assign grades on examination, compute the grade point average, all of these were actually are part of a university database application.

(Refer Slide Time: 6:48)

<!-- image -->

Naturally,  in  earlier  days,  these  database  application  were  built  directly  on  top  of  the  file system, you all know that by now that a computer system always has a file system, what if we are  working  on  Windows  what  you  get  to  see  through  Windows  Explorer  or  if  you  are working on  Linux what  you  get to see through the  you know hierarchy of directories is a view of the file system.

So,  you  can  keep  any  document  electronically  in  that  system,  you  can  bundle  them  into folders, and you can have variety of types of files. And you can have hierarchy of folders this is this in simple terms what a file system is all about. So, naturally data can also be kept in terms of  files,  which  we typically  say  is  a  flat  file.  So,  if  you  want  to  refer  to  the  nearest approximation of a flat file today, as we widely use is what is known as CSV, you must have seen this CSV in dot CSV it is called comma separated value.

So, where do you write various different values like this separating them by comma meaning that they are the values of various different fields. And it is a very common way that we, in a small scale share data in terms of file system today.

So, the question is, what are the problems of using file system simply to store data? In fact, historically, we will soon go through that in the next module. Historically, file systems have been used for databases for a long time. So, some of the key issues are data redundancy and inconsistency, we will see that when you keep them in terms of flat files, parts of the same data  needs  to  be  duplicated  and  kept  at  multiple  places  which  lead  to  duplication  of information that is bloating of data as well as it becomes difficult to keep them consistent, consistent in the sense that if you have the same data at two files or two places, then when you update one, it is quite possible that you will forget to update the other.

So, the other is difficulty in accessing the data. Like if you have data in CSV files, the only way you can access is open it either as a notepad and just like a text, keep on reading it. Or at best,  you  can  open  it  with  the  Excel  kind  of  spreadsheet  application  and  traverse  them  as table  but  you  cannot  do  anything  easily  in  an automated  fashion.  Data  isolation  is  another problem  where  if  there  are  multiple  files  and  formats,  it  is  very  difficult  to  keep  them integrated and consistent.

Integrity  is  a  big  question  because  in  several  places  we  need  to  have  integrity  to  be maintained. For example, if I am holding a savings account in a bank, then most banks will mandate  that  I  must  have  a  minimum  balance.  So,  I  cannot  make  a  transaction  to  debit enough amount, so, that my balance could go below that minimum balance, if it does, then the bank will not allow it, the minimum balance could be 0 or could be a positive number.

So, for any action that you do, you will have to remember what is this minimum balance and the fact that this integrity has to be maintained, which is very difficult if you use files where this condition that fact that account balance has to be more than 0 or more than a minimum amount will get buried somewhere deep down in the code. So, it is very difficult to make those kinds of things.

(Refer Slide Time: 11:09)

8

<!-- image -->

So, it becomes with all these it becomes quite problematic to use file system for managing data. Further there are more fine issues like atomicity is a big question, you are probably not so familiar with atomicity, unless you have studied about atomicity in terms of the operating system course. Atomicity talks about that when I do something to keep the consistency it is important that I do the entire task or I do not do it at all.

So, what am I talking about, let us say we are talking about a basic net banking transaction that I am paying my friend an amount of 100 rupees. So, this has two parts; one is 100 rupees will have to get debited from my account after the check that I have enough balance to pay 100  rupees  and  then  the  100  rupees  debited  has  to  be  has  to  get  credited  to  my  friends account.

Now, this whole thing if it is  done,  then  the  transaction  is  fine,  but  suppose  after  the  100 rupees have been debited from my account, suppose the system fails and rest of the program could not be executed. So, what will happen? My account has been debited by 100 rupees, but my friend's account has not been credited by 100 rupees. So, which means that in their entire banking system 100 rupees have simply got lost.

So, this is a very big consistency problem and that mandates that we must do such operations in an atomic fashion which means that they cannot be divided further that either the whole transaction debit and credit and logging whatever happens together or it does not happen at all.

Concurrency of access is of course, you understand because the same system is being used by several earlier it used to be tens of users and hundreds of users now, it is more than couple of millions of users who use the same system in a concurrent fashion from different parts of the organization, different parts of a nation or different parts of the world.

So, at any point of time, two people might want to actually reserve a berth on the train at the same time. Naturally if one berth is left, you cannot allow both of them to take that berth. So, you have to manage it in such a way that the system remains fair and also the berth can go and go only to one of them, but not to both. So, these are there are several such issues with concurrency.

Security of course, you know what is going on in the world, you know all the spyware and all those identity theft issues happening. So, with that security is a big big problem. So, these are we talked about few points in the earlier slide and these points of atomicity, concurrency, security,  these  are  finer  and  more  difficult  points  to  maintain  using  a  file  based  or  a  file system based data management application. So, you need a database and database can offer a solution to all those, all these issues as well as actually to lot more.

(Refer Slide Time: 14:25)

<!-- image -->

So, let me move on to give you a quick roundup of the course. So, so first what I talk about is what is the, what are the prerequisites that is to understand this course comfortably. You must know a couple of things.  I  am  sure  most  of  you  know  this,  but  still  I  made  a  moderately exhaustive list so that in case you do not, you can take your time in between and go and brush them up so that you do not have any difficulty in following the course.

So, the first is about set theory, I am sure all of you know what set is, the basic definition and different ways set can be like a set of people, a set of horses, a set of accounts or a set of prime numbers which is a subset of natural numbers where no other natural number other than itself can divide it. So, these kind of different forms of definition you must be aware of membership, subsets, superset, power set, universal set, all these concepts should be clear. Then the basic operations like union, intersection, complementation, set difference, Cartesian product, we will very randomly and widely use them De Morgan's law will use it very often. So, please get yourself familiarized with this. There could be several references from where you can study this, I have just mentioned some of the online courses like so, you could just go through  their  videos,  the  courses  may  not  be  running  or  you  may  not  have  time  to  attend them.

Like in MOOCs NPTEL you have a discrete mathematics course, which is very useful, you can look at those videos, if you are not sure of some of these prerequisite topics. Then I think for set theory, at least, you already have had a mathematics for data science 1 which should have covered these topics anyway. So, in that case, you would not need to study anything further.

Then you need to know about relations and functions, what makes a relation which builds up on the set what are binary relations, order pairs, different notions of domain, range, image, pre  image,  inverts,  the  properties  of  relations  and  what  is  a  function  and  what  are  the properties  of  functions  and  so  on.  Again,  the  discrete  mathematics  course  and  your  data science course, would be sufficient to give you the required knowledge in case you have got dusty.

<!-- image -->

We need some knowledge about propositional logic that is, basically in simple terms, it is little bit of a different representation of Boolean algebra. So, I am sure you would have done it at some point in your course, but still specifically we need the notion of truth values, truth tables,  operations  like  conjunction,  disjunction,  negation,  implication,  equivalence,  closure and a closure under operation and so on. In case you are not very familiar, then please refer to videos in the discrete mathematics course, you can obviously take up some books as well.

More importantly, we need familiarity with predicate logic as well, which is called the next order logic beyond the propositional logic, where we talk about quantifiers for all men, men are  mortal,  this  'for  all'  is  a  property  which  does  not  belong  to  a  specific  person,  but  it belongs to the entire collection of the set or we can say that for every child, there is a mother. So, there, it is not specific for any particular child, but you pick up any child, the child will have a mother.

So, these are different kinds of notions of quantification in terms of existential and universal quantification, you must be familiar with those. While I need them, use them, I would try to give a quick definition round up, but that may not be enough to use it in the context where we need it. So, better get prepared with these prerequisites, you can use this course or some other book as well.

<!-- image -->

It will be good to have a good knowledge of data structure, we you will use it get, after all database is data structure in a very very large sense, I will talk about what are the differences is to when we call it a data structure and when you call it a database system, but in terms of data  structure,  lot  of  the  notions  are  rampantly  used  in  database  course  the  arrays,  list, particularly search trees, binary search trees and other kinds of search trees, balanced trees, B tree, hashing and hash map those kinds of data structures.

Not very esoteric data structures like splays and all that we will need but these are the basic data  structures  notions  about  which  would  be  very,  very  critical.  You  could  refer  to  these MOOCs NPTEL videos or refer to a standard textbook in the algorithm or data structure.

(Refer Slide Time: 20:05)

<!-- image -->

The next is, this course need that you know about Python, programming in Python is going to be stapled food for this course as well. I think  you already have a course Programming in Python,  that  would  be  enough,  whatever  additional  may  be  required  in  terms  of  Python libraries  and  features,  like  DB  connectivity  of  Python  and  so  on,  will  be  covered  in  this course itself. But be very, very, try to be very, very proficient not only familiar, but proficient with Python, try to write and read as much of Python code as you can.

(Refer Slide Time: 20:49)

<!-- image -->

So, these were all the essential prerequisites of the course. Finally, before I end, this is the desirable, I should say the desirable prerequisites that it would not significantly harm if you do  not  know  them  or  do  not  know  them  well.  But  knowing  them  will  certainly  help  you understand  some  of  the  intricate  issues  of  databases  better,  particularly  I  will  talk  about algorithms and Programming in C, we do not we will not use C much in this course, but it comes handy in terms of understanding several algorithmic issues, particularly sorting and searching would be widely used. So, if you are not very familiar, in any case, this is going to be very, very useful to you in terms of whatever you desire to do. So, try to be familiar with them as well.

<!-- image -->

Last, but not the least, object oriented analysis and design or object oriented programming is a  concept where you try to look at data elements as kind of capsules, described by certain properties,  and  their  interrelationships,  which  come  in  in  some  way  very  handy  and  close with the database system concepts and also at the same time differ in certain significant ways.

So, if you are familiar with object oriented analysis and design, it will have a good overlap with the  database  system  design,  and  some  of  the  core  issues,  it  is  not  again,  an  essential prerequisite, but it is good to know. So, if you know say the related programming languages like Java or C++, that would also be of great help, but these are the desirable prerequisites.

(Refer Slide Time: 22:50)

<!-- image -->

3

In terms of the course outline, as you are aware, this is a 12 week course. So, naturally, we have in this 12 weeks, 5 modules per week, so, we will have a total of 60 modules out of these 12 weeks, the first 8 weeks would be primarily around application programming, which is  kind  of  I  should  say,  the  simpler  part  of  the  database  management  system  and  the  part which more people need to do in the industry.

So, kind of the if you just look at the number of jobs or the variety of jobs available with the database knowledge, this is primarily around the application programming, we will talk about what application programming is, but just know that application programmers need to know the content of week 1 to 8 very well and that gives you a good job opportunity.

For some of the advanced tasks and some of the more, little bit more difficult to get but more paying jobs are related to database administration and design. Those are the aspects that we discuss from week 9 to 12 and that is what will form the whole gamut of things that we need to do in this course. (Refer Slide Time: 24:14) 2

<!-- image -->

So, this is the textbook that will follow, Silberschatz, Korth and Sudarshan, there are multiple editions available. The content that you see here has been prepared based on the 6th edition, but  obviously  7th  edition  will also  do  it  has  some  more  stuff  which  you  will  have  to  skip anyway.

And of course of the 6th edition also we are not being able to cover everything. We have taken a few things selectively but it will be good to buy this book if you do not have already because this will need references to do with this book in every module almost at every minute and this is an excellent book to learn and practice database management system.

(Refer Slide Time: 24:59)

<!-- image -->

So, to summarize, we have talked about the importance of database management systems in modern  day  applications,  wide  range  of  applications.  And  I  have  introduced  to  you  the various basic aspects of the course, doing, giving you the KYC for this course, and from the next module onward, we will move on to talking about the actual content of the course. Have a nice day and let us meet in the next module.
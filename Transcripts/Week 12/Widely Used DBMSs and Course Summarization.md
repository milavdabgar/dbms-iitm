<!-- image -->

## Database Management Systems

## Professor Partha Pratim Das

## Department of Computer Science &amp; Engineering

Indian Institute of Technology Kharagpur

## Widely Used DBMSs and Course Summarization

Welcome to Module 60 of Database Management Systems course, in the IIT Madras, online BSc program.

<!-- image -->

In the last module we talked about big data, which is emerging very strongly these days. And we understood the approach of NOSQL, that is non-relational approach to database modeling, design and implementation. And saw the consequences of the CAP theorem, in contrast to the ACID properties, the BASE properties so to say. We also took a tour of common types of NOSQL databases and compared the relational and non-relational databases.

<!-- image -->

In this module, which is going to be the last module of the course, we would take a look into the  widely  use  RDBMS systems. So, you must understand that this is not for memorizing everything by heart, but to give you an idea of what are the commonly used systems and the probability that when you go to work, he will work with one of them is extremely high. And we  of  course,  recap  the  weeks  of  the  course  very  briefly,  just  to  be  able  to  summarize everything.

(Refer Slide Time: 01:48)

5

<!-- image -->

So, those are the two topics for this module.

2

<!-- image -->

So,  first  we  will  talk  about  the  widely  used  relational  database  management  systems.  The relational  data model  organizes  data  into  one  or  more  tables  or  relations  as  we  have  seen, which has rows and columns and unique key for each row. And since each row has a own unique key, the row of a table can be linked to rows of other tables using the unique key and we may have linking through the foreign key. We have learnt about SQL the language  for querying and maintaining database which is mostly used by all of these relational databases.

And one of the reasons for dominance of relational databases, we will see the extent of this dominance  soon  are  these  properties  like  simplicity,  robustness,  flexibility,  performance, scalability to a certain extent, to the extent of enterprise requirement, we have seen the issues of scalability as well. And compatibility in managing generic data and RDBMS are mostly using large enterprise scenarios.

(Refer Slide Time: 03:00)

<!-- image -->

So,  here,  I  present  some  very  specific  business  data  corresponding  to  the  widely  used RDBMSs they fall  into  broadly  two  categories  commercial  or  proprietary  where  you  will have to pay for using that database and the other is free or open source databases, which work under the GNU, General Public License and you may not need to pay primarily for using that database may have to pay for some maintenance.

Now,  in  this  what  is  the  way  this  is  ranked  is  these  are  the  top  five  relational  databases according to the market share data. This is not absolutely recent data, this is as of 10 years back, but that is what comprehensively available. You can see that the Oracle from Oracle is dominating the market with about 48.8 percent of the revenue share followed by not closely but the next second next is Db2 from IBM with about 20 percent, SQL Server of Microsoft is close by with 17 percent and then much lower on the rank is Sybase which is primarily SAP 4.7 percent and Teradata and there are several others, which are also quite widely used and popular.

In terms of the free space, PostgreSQL, MySQL and SQLite are the three major dominating relational databases and there are others like MariaDB, Hive, Hive is primarily used for data warehousing.  And  there  are  some  which  are  called  object  relational  databases,  which  are relational databases having certain object linking properties like Illustra and objective DB this of course, are get merged into the NOSQL databases very soon.

<!-- image -->

So, if you look into DB engines is a, is an organization which keeps on ranking the database servers  or  the  database  relational  databases,  all  databases  actually  on  a  regular  basis  on  a monthly basis. So, this is the latest ranking report where 147 database RDBMSs have been ranked as of August 2021. And these are this is kind of the rank score to understand the rank score you will have to study go to their site and study, the site link is given below and study that their actual approach of doing the analysis.

And  on  the  next  two  columns,  this  show  compared  to  the  previous  month,  what  is  the increase or decrease increase as shown in green and decrease in red. And compared to the one year back, what is their increase or decrease. So, what you can see is Oracle and MySQL,

Oracle from proprietary and MySQL from the kind of public space are kind of the leaders when they are very closed by in this.

Similarly, next year followed our Microsoft SQL Server and PostgreSQL, which are again proprietary  and  free,  they  are  in  the  next  two  slots  followed  by  IBM  Db,  SQLite,  your Microsoft  Access,  you  have  Teradata  here,  you  have  SAP  HANA,  SAP  adaptive  servers, these  are  actually  which  subsumes  the  Sybase  databases.  So,  this  is  kind  of  the  current ranking.  So  you  can  know  that  what  do  you  what  would  be  your  expectation  to  see  the different databases as you go for work.

(Refer Slide Time: 06:55)

<!-- image -->

Now, this is a kind of a trend curve over the last about a decade from 2013. And here, you can see that  how in terms of this is  a  y axis  is  a logarithmic  scale  to  keep things  because suddenly  things  are  exponentially  increasing,  because  the  data  is  exponentially  increasing. So, in the log scale, if something is flat, then it shows that that is the level of exponential increase and so on.

So,  you  can  see  that  on  the  top  are  a  couple  of  clattered  are  some  of  the  three  databases, RDBMSs which have kind of held on to the top position over a decade. So that is kind of the trend. Whilst, PostgreSQL has been increasing. So, it is getting more and more popular, you have then then you have a clutter of a number of different databases, which are kind of they started  at  different  levels  and  over  the  last  couple  of  years  have  kind  of  settled  down  at  a similar kind of growth happening across them, those will be all of these databases there.

And you can see some of the recent databases like  Snowflake, which started as a about  5 years back has had a very steep growth in terms of this. So, it is, I mean it is something to watch out for. So, this is kind of the trend overall.

(Refer Slide Time: 08:27)

<!-- image -->

Now, I will also present you a data on what is happening in the entire you know market space of databases in general not only the relational, relational as well as non-relational including the NOSQL databases. So, if you take a look into that. So, it is this is a data of 377 systems, we are just presenting the top 20 the site has entire list as of the current month, August 2021.

And you can see that the top quite a few Oracle, MySQL, SQL Server PostgreSQL, the top four  are  still  the  relational  databases.  So,  you  can  see  that  dominance  that  still  goes  on MongoDB  is  the,  Redis  these  are  the  top  non-relational  or  NOSQL  databases  which  are dominating in the popularity space. IBM Db is again, relational Elasticsearch is little bit of a different  it  is,  it  is  more  a  search  engine  than  a  typical  database,  but  it  has  all  the functionalities that the database needs, but the primary focus is on, on searching.

So that is also non-relational and has is a multi-modal database which has a lot of popularity. Again  followed  by  relational  databases  SQLite  Microsoft  Access,  followed  by  NOSQL Cassandra,  relational  MariaDB,  Splunk  search  engine,  relational  Hive,  relational  Azure NOSQL Dynamo, relational Teradata, NOSQL Neo4j and so on.

So, you can see that actually the scalability and functionality decides a lot of things, but the space is very uniformly it is not, it is clearly that to a certain extent the relational database systems do dominate the space, but non-relational are catching up, the NOSQL is catching up they have a, but typically what happens is for relational there are a large number of enterprise which use that because they need all those transactional online transaction processing OLTP services.

In terms of NOSQL, the each and every organization using it use for a very large data space very large user base like Facebook, like Amazon, like Google and so on. But, the number of such organizations number of such requirements are certainly less because there cannot be that huge organizations or applications in tens of thousands or hundreds of thousands. So, that is the kind of the differentiator.

(Refer Slide Time: 11:17)

<!-- image -->

And if you look at the trend data of all databases, again, you will observe interesting things like on the top, the clutter is with the relational databases followed by MongoDB here, this is the one and Redis somewhere below that here. So, this is again, again, the kind of view again, see the three groups that we are seeing in the relational in terms of the trend of changes, but you can see that more or less most of the players are kind of in a stable position, except for again, PostgreSQL we saw is growing so is MongoDB.

So, these are these are the growing trends, naturally, this one has a which is Microsoft Azure SQL  Database,  which  is  also  having  a  recent  growing  trend  and  so  on.  So,  just  keep  on tracking even know what is happening in this space and what would be the appropriate things to learn further.

<!-- image -->

Now in the next couple of slides, what are present and I am not going to discuss through them except for one or two. I present the basic information about these top proprietary as well as free  databases  say  for  Oracle,  it  is  a  database  which  kind  of  came  into  strong commercial existence in 1977. The latest version as of August 2021 is Oracle Database 19c, but different organizations would be using different versions.

And these are the application domains almost everything except for the non NOSQL kind of requirements.  But  even  then,  in  some  of  those  cases,  there  is  backbone  from  Oracle.  So primarily  online  transaction  processing,  data  warehousing,  and  mixed  applications  are  the primary.  And  Oracle  specifically  offers  different  services  based  on  the  Oracle  database, which  are  sector  specific.  So  for  example,  if  you  want  a  customer  management,  customer experience tracking kind of database to be built, you do not have to build it from scratch, Oracle customer experience gives you modules which can be directly customized for your requirement and used.

Languages all across the SQL are kind of, all across the relational databases are SQL or the procedural versions of that. There are further tools of many databases provide for facilitating development and  connectivity  as  you  have  learned  is  typically  I  have  tried  to  give  some, some specifics but it they are typically in terms of I should say four buckets one is ODBC in general, which most databases support, then for Java you have JDBC, for Microsoft specific stuff, you will have the Microsoft dot net ADB ODB dot net, ADO etc. for Microsoft specific stuff.

And Python often has third party libraries provided in Python for doing this we have taken a big look into all that. So, I will not go through the details of everyone, you can read them study them and make a feeling about how the competitions are going on. And what you can get from different databases.

(Refer Slide Time: 14:32)

<!-- image -->

## (Refer Slide Time: 14:48)

<!-- image -->

You have SQL Server from Microsoft, these are all competing as we have seen. (Refer Slide Time: 14:51)

5

<!-- image -->

You have Sybase which used to be quite a competitor of Oracle in the late 80s  and quite a much 90s, they eventually got acquired by SAP and they became the backbone of SAP. So, it mostly goes for SAP application transact SQL is a major component. So, they have specific SQL API's for use, which are built on ODBC.

## (Refer Slide Time: 15:19)

<!-- image -->

Teradata is also another which is, as you seen, quite popular.

(Refer Slide Time: 15:24)

5

<!-- image -->

Now coming to the free and open source ones, PostgreSQL, MySQL are some of the leaders. Now this is the latest version of PostgreSQL as of June 2021, that is two months back, but we are using this in the course but we are using an old stable version, the download link is here in case you have not already downloaded it yet. And it can be used for several of the OLTP data warehousing and other applications. And you have, we have already discussed quite a bit about this particular database system.

<!-- image -->

MySQL is another open database system, which was managed by the community but later, currently is owned by Oracle, but it is still open source and used, can be used freely.

(Refer Slide Time: 16:17)

<!-- image -->

SQLite is a community initiative led by a group of international independent developers and its latest version is of June 2021. This is going to be the database system that your application development course which goes hand in hand with this DBMS course will use, you have to check  the  version  from  the  instructor.  And  here  have  given  certain,  certain  indicative  big applications  which  are  based  on  SQLite  and  they  come  from  big  companies  like  Adobe, Bosch, Google, Airbus, McAfee and so on.

<!-- image -->

Now, there are object relational databases like Illustra and Object Db which have, can support many to many relationships accessed by the use of pointers. So, that gets rid of the excessive use of join, which is the most costly operation in a relational database. So, its advantages in that way, their penetration is still not very high, because strong object based databases have actually gone into the NOSQL space as we have already seen.

(Refer Slide Time: 17:34)

<!-- image -->

<!-- image -->

Now, in the in the next couple of slides, you will see the comparison of these databases based on  various  parameters,  how  do  they  compare  with  in  terms  of  operating  system  support fundamental features, limits, tables, views and so on. So again, I will not go through them in detail. For example, here we are showing the five, top five proprietary databases and the top three databases as to what and the operating system that they support.

So,  Linux,  Windows  Mac  kind  of  is  universal,  almost  everybody  supports  but  like  SQL server does not support you can understand the reason they do not. So, but there are several other operating systems where which has support variedly like PostgreSQL is supported on Android, MySQL is supported on Android. Sybase is supported on Android. So, these are useful for your mobile application development.

(Refer Slide Time: 18:34)

<!-- image -->

These are a list of basic features they support, most of the basic ones would be this would be supported by everyone the special things which will vary.

(Refer Slide Time: 18:43)

<!-- image -->

Tables and views type systems, they vary between type systems vary between being static, and being a combination of static and dynamic.

## (Refer Slide Time: 19:05)

<!-- image -->

So, you certainly the expectation is not that he will learn these tables by heart, but these are more like references to give you a feel of the variability you have and the commonality of these properties that you have already learned in the course.

(Refer Slide Time: 19:20)

<!-- image -->

So, you should be able to get into any of these databases and seamlessly start working. Of course, you will have to defer to the specific manual for all this information.

## (Refer Slide Time: 19:30)

| Oracle                                                                                                                                                | Sybase                                                                                                                                                | SQL Server                                                                                                                                              | DB2                                                                                                                                            | Teradata                                                                                                                                                 | PostgreSQL                                                              |                                                                                           |
|-------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------|-------------------------------------------------------------------------------------------|
| Supports Union Intersect Inner Joins Outer Joins Except Inner Selects Merger Joins Blobs and Clobs; Common Table Expressions Windowing Parallel Query | Supports Union Intersect Inner Joins; Outer Joins; Except Inner Selects, Merger Joins Blobs and Clobs Common Table Expressions Funcuons Paralel Query | Supports Union; Intersect Inner Joins Outer Joins Except Inner Selects Jcins Blobs and Clobs Common Table Expressions Windowing Functions Paralel Query | Supports Union Intersect Inner Joins , Outer Joins Except Inner Selects Joins Blobs and Clobs Common Table Expressions Funchons Parallel Query | Supports Intersect Inner Joins Outer Joins Except Inner Selects Merger Joins, Blobs and Clobs Common Table Expressions Wincowing Funcuons Parallel Query | Supports Union Intersect Inner Joins Outer Joins Except Blobs anc Clobs | Supports Union Outer Joins Except Inner Selects, Blobs anc Clobs Common Table Expressions |

| Oracle                                                                  | Sybase                                                                    | SQL Server                                                                | DB2                                                             | Teradata                                                      | PostgreSOL                                                                | MySQL                                                        |
|-------------------------------------------------------------------------|---------------------------------------------------------------------------|---------------------------------------------------------------------------|-----------------------------------------------------------------|---------------------------------------------------------------|---------------------------------------------------------------------------|--------------------------------------------------------------|
| Suppors Data Doman; Cursar; Tnigger Function; Proceaure Exernal Rouuine | Supports Data Domain Cursar; Trigger; Funcuon; Procedure External Routine | Supports Data Domain Cursar; Trigger, Function Procedure Extemnal Routine | Supports Data Domain; Cursor Trigger Procecure Erternal Routine | Supports Cursor; Trigger; Functon; Procecure External Routine | Supports Data Domain Cursar; Trigger Function; Procecure External Routine | Supports Cursor; Trigger; Funcuon Procedure External Routine |

<!-- image -->

(Refer Slide Time: 19:42)

<!-- image -->

The access  control  information,  the  authentication  facilities  available  in  different  database systems and so on. So, these are this is just to give you whole idea of the space which is complex, growing full of opportunity for you to jump in and make your lifelong career in this because databases are something that are not going to disappear from life.

<!-- image -->

Now, coming to the course recap, this is just a overall summary of what we did week wise and in each one of them, I have mentioned the key points from the modules, 5 modules that every  week  had.  So,  in  week  1,  we  had  a  course  overview  and  we  introduced  the  basic concept of the data DBMS why we need it as against the file system and what are the typical database design and engine considerations.

<!-- image -->

We followed it up by introducing the relational model and SQL. So, kind of relational model and  SQL  are  kind  of  synonymous.  So,  that  is  the  reason  you  can  you  can  see  that  nonrelational is being referred to as NOSQL, not no relational. So, we talked about the relational model the  basic  features  of  that  and  introduced  you  to  the  basic  formulation  of  relational query  which  starts  with  data  definition  and  manipulation  languages  and  has  additional features.

(Refer Slide Time: 21:20)

5

<!-- image -->

We  moved  on  to  delve  deeper  into  the  relational  at  intermediate  level  taking  examples, talking  about  nested  queries, joint expression  views,  transactions  in SQL  integrities, authorization in SQL and took up some advanced SQL features also I would not say that we have  comprehensively  covered  everything,  but  we  have  tried  to  be  solid  on  the  basic  and intermediate side and somewhat sketchy on the advanced side because you can always want to know the fundamentals you can always read up and move forward in SQL.

(Refer Slide Time: 21:54)

<!-- image -->

Being a database expert is necessarily whichever databases you work with at least expertise with SQL is required even for non NOSQL I have mentioned if you, if you recall that there are SQL (())(22:06) which are widely used in a good range of NOSQL databases. Then we moved on to relational query models and modeling of the real world in general.

So,  we  talked  about  relational  algebra,  calculi  with  certain  introduction  to  predicate  logic which  you  must  brush  up,  the  discrete  structures  you  must  brush  up,  talked  about  their equivalence and then moved on to modeling using the ER models, ER diagram conversion of ER models to relational schema, Entity Relationship features and so on.

And I mentioned that these are kind of restricted subset of a generalized modeling that you have today, which is called UML, Universal Modeling Language which we did not have time here to to study in depth because it talks about several other things, but if you are specializing from relational to NOSQL, I would strongly suggest that you also study UML in depth.

Because of the simple reason that ER models are very restrictive and more suitable for just relational modeling, the more of the connective modeling, more of the hierarchical modeling more of the inter connection, the sequence modeling, activity modeling you need which are very typical of more complex applications will be available in UML on top of what you have in the ER model.

<!-- image -->

Moving on, we dealt really deep into the relational database design which is a, which is a very formalized subject. And we looked at how the mathematically the real world constraints can  be  modeled,  what  is  atomic  domains  and  normal  forms  and  why  are  normal  forms important, starting from the first normal form going upwards and then how the constraints of the real world can be modeled in terms of dependencies.

And we looked at the functional dependency theory, the first level of dependency theory, the and  the  decomposition  using  the  functional  dependencies,  the  algorithms  for  that,  your lossless joint, dependency preservation, what are the properties you need.

(Refer Slide Time: 24:24)

<!-- image -->

And we carried on into the sixth week in terms of talking more about the normal forms going to the second normal form, decomposition into third normal form, decomposition into Boyce Code  normal  form.  Took  an  extensive  example  to  illustrate  the  basic  design  refinement process using these normal forms and functional dependency constraints. And remember that along with this module 28 you will also need a specification document of the LIS which will be shared separately.

And  moving  on  we  took  a  good  look  in  that  relational  database  design  in  terms  of multivalued  dependency  when  it  attributes  necessarily  have  multiple  values,  which  is  also very common, and how do you decompose into 4NF which is more powerful than the BCNF as well.

And  finally,  we  talked  about  the  database  design  process  and  touched  upon  the  issues  of handling modeling time in a database. This is, this again becomes a very, very big question in terms of NOSQL databases, but relational databases can also model temporal data to a good extent, time series data, spatial data all of these can be modeled in relational as well.

(Refer Slide Time: 25:43)

Week 7 is what we will, where we discuss that how to develop applications based on the databases that you have already created. So, or you are intending to create, so what does it take to develop an application, how to architect the application in terms of two tier, three tier or  n  tier,  what  is  typically  the  web  application  requirements,  the  mobile  application requirements and so on.

<!-- image -->

How you can use free databases like PostgreSQL, Python or frameworks like flask in terms of doing that, what is the role of rapid application development in this, how do you connect easily  from  a  language,  from  a  programming  language  to  a  database  system  to  write  the intermediate layer of the application and so on.

This is  something which you will find will have quite some overlap with your application development course, many of these ideas will be re-iterated, reinforced in your application development course and even I will emphasize that you really need to learn that course while along with the database, so that you can become a powerful software engineer in the database application space.

<!-- image -->

Next we took a having done the basic modeling and design, we took into the other aspects of database,  more  of  the  physical  and  temporal  aspects,  how  do  you  manage  storage,  initial modules on this talk in general about background of data structures, which are primarily in memory and then we moved on to talking about the different physical storage and physical organization of the file organization of the data, comprehensively trying to look at what are the options available to store your files, your data files, your index files and so on.

<!-- image -->

This naturally led to the design and considerations for indexing because indexing as we have learned  is  you  can  organize  the  data  in  only  one  way,  based  on  the  key  primary  key  or something, but if you have the requirement of searching and updating the data in multiple, through multiple different attributes,  then  you  need  to  have  easy  access  through  those  and that can be done in terms of creating indexes. We again went back to the in-memory data structures for that what is balanced binary, search trees quick review of that.

And went on to discussing the 2-3-4 tree which is a very unique tree, where the height always remains the same for all the leaf nodes and you have flexible nodes having multiple number of keys going in them. And then we could generalize it in terms of the B plus tree, which are widely used for not only for index files, but actually also for the data files and talked about the specialization of B trees.

We looked at the,  in  the  same  week  we  looked  at  the  other  option  for  indexing  which  is through hashing, which is kind of is a mathematical mapping from a, from an attribute value to a specific address location where the particular record can be found.

And we did, basics of static dynamic hashing compared the schemes and talked about bitmap indices  and  also  looked  at  actually  in  SQL  how  can  you  create  indexes  and  give  your instruction that this is where I need a bitmap index, this is what I need a composite index, how  do  I  do  a  composite  index  and  so  on.  So,  this  will  be  very  required  for  your  query formulation and optimization.

<!-- image -->

The core of the whole thing revolves around transaction the tasks that you want to do. So, we introduced the concept of transactions, states, concurrency of that and obviously the moment you make transactions concurrent, then the possibility of having incorrect result comes up. So, we talked about serializability, the conflict serializability we talked about the recoverability of transactions if you have to roll them back. If you have to, you have some failure  and  you  cannot  complete  a  transaction,  we  talked  about  the  view  serializability  in different ranges of that.

And  saw  that  well  with  all  these,  we  finally  end  up  may  end  up  with  a  very  few  serial serializable  schedules,  which  are  polynomial  time  decidable,  because  view  serializabilities and be complete.

So, we talk about the different mechanisms that are available to get the concurrency control on the fly, keeping the core idea of isolation in view that a particular data item can be read by two or more transactions at the same time, but can be written by only one transaction. And during that time, it has to be exclusive. So, we talked about log based protocols, two phase locking, time based protocol and consequences of that in terms of deadlock, live log and how to handle those.

<!-- image -->

Week 11 focus primarily on backup and recovery, which is very required for the persistency of the database. What are the backup strategies, the backup plan and what are the ways that you  can  recover  from  that  by  using  particularly  the  transaction  logging  the  log  based recovery, which is the key idea that we introduced here and revolved our strategies around that  and  we  ended  with  a  kind  of  a  stable  storage  description  of  redundant  array  of independent disks.

(Refer Slide Time: 31:31)

5

<!-- image -->

And  in  the  current  week,  we  started  with  query  processing  and  optimization  making evaluation plans, which are good in terms of estimated cost and how to use that effectively, we  talked  about.  Then  we  digressed  a  little  bit  in  the  last  two  modules  talking  about  the performance of RDBMS, how does the architecture affect that performance and how can you scale the, scale the infrastructure, scale the RDBMS along with the scaling of the application.

And we saw that horizontal scaling scale out is the primary way to go and in view of that, we took a look into what is emerging in terms of big data, why do we have not only SQL that is NOSQL  in  place,  and  what  are  the  compromise  that  you  do  in  terms  of  so  the  CAP requirements that is Consistency, Availability and Partitioning all of the three you cannot get together.

So, you have to decide which two primarily you want and there are different protocols like Gossip protocol and so on, which allow you to compromise in a restrictive or in a controlled way.  And  in  this  module,  as  it  is  you  have  seen  we  have  talked  about  the  widely  use RDBMSs. (Refer Slide Time: 32:51) 8

<!-- image -->

So, it is it is my pleasure that I could do work with you, work through this particular course, which is very close to my heart, which I think is a very effective technology to learn, to grow in the industry as a software developer, as a database engineer, as a data systems engineer and growing to the DBAs and data scientists and so on.

So,  to  prepare  well  for  this  course  read  the  textbook  very  thoroughly,  solve  the  exercise, practice query coding, this is very, very important as an engineering course. So, it is practice, practice, practice, practice design, practice specification, practice coding. And also remember that to have a good hold over the database, you must be strong in algorithm, data structure and discrete structures, at least the fundamentals of that.

And beyond that, if you need any help, we will be happy to help you, wish you all the best in this course, and in your future career. Thank you very much for being with me in this course. Have a good day and a good time ahead.

<!-- image -->
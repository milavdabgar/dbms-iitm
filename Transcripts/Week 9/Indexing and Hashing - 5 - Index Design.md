<!-- image -->

## Database Management Systems

## Professor Pratha Pratim Das

## Department of Computer Science &amp; Engineering

Indian Institute of Technology, Kharagpur

Indexing and Hashing/5: Index Design

Welcome to module 45 of Database Management Systems course in the IIT Madras online B.Sc. program.

(Refer Slide Time: 0:30)

<!-- image -->

We have been discussing about indexing and hashing to make the accesses faster. And in the last  week, we talked  extensively about hashing particularly the static and dynamic hashing schemes and we compared the ordered indexing with hashing and we also took a look at a nice  way of  representing  or  making  sure  that  you  have  fast  access  of  columns,  which  has limited number of distinct values using a reverse mapping called the bitmap index.

9

(Refer Slide Time: 1:05)

<!-- image -->

So, index definition and guidelines.

## (Refer Slide Time: 1:29)

2

5

<!-- image -->

<!-- image -->

<!-- image -->

## Index in SQL

- Create an index

create index &lt;index-name on &lt;relation-name

&lt;attribute:

For example: create index b-index on branch (branch\_name)

- Use create unique index to indirectly specify and enforce the conditi key is a candidate key
- Not really required if SQL unique integrity constraint is supporter
- To drop an index

index &lt;index-name drop

- Most database systems allow specification of type of index, and clusti
- You can also create an index for a cluster
- You can create a composite index on multiple columns up to a m; columns

## Index in SQL

- Create an index
- create index &lt;index-name on &lt;relation-name &lt;attribute: For example: create index b-index on branch (branch\_name)
- Use create unique index to indirectly specify and enforce the conditi key is a candidate key
- Not really required if SQL unique integrity constraint is supporter
- To an index index &lt;index-name drop drop
- Most database systems allow specification of type of index, and clusti
- You can also create an index for a cluster
- You can create a columns

So, we start with the index definition in SQL. So, to create an index in SQL, it is I mean SQL style you have understood by now. So, if you have to create anything you have create, then you say what you are creating that is index give a name to that index, and then you have to specify which on which file on which relation are you creating it. So, you give a name of that relation.

And finally, is specify the list of attributes which would be used in index creating this index, it could be one attribute or more than one attribute that is an index could be simple or it could be composite, and we will come to the different issues of that, but this is the basic structure. So, the example as a example says create index this b-index is a name and we are creating index on a relational file called branch and using branch name as a attribute to be used in the index.

<!-- image -->

8

<!-- image -->

## Index in SQL

- Create an index

create index &lt;index-name on &lt;relation-name &lt;attribute: For create index b-index on branch (branch\_name) example:

- Use create unique index to indirectly specify and enforce the conditi key is a candidate key
- Not really required if SQL unique integrity constraint is supporter
- To an index drop

index &lt;index-name drop

- Most database systems allow specification of type of index, and clusti
- You can also create an index for a cluster
- can create a composite index on multiple columns up to a m; columns You

<!-- image -->

## Index in SQL

- Create an index
- create index &lt;index-name on &lt;relation-name &lt;attribute: For example: create index b-index on branch ( branch\_name)
- Use create unique index to indirectly specify and enforce the conditi key is a candidate key
- Not really required if SQL unique integrity constraint is supporter

2

- To an index drop

index &lt;index-name drop

- Most database systems allow specification of type of index, and clusti
- You can also create an index for a cluster
- You can create a composite index on multiple columns up to a m; columns

You can also specify unique while writing the index to indirectly specify and enforce that the search key is  a  candidate  key  because  if  it  becomes  unique,  it  means  that  there  cannot  be duplicates of that value in the field. You it may not be required in SQL, if the unique integrity constraint is supported, if it is supported use that in your table design and do not have to use it in the index. But if it is not there, then you can also handle it for a specific index like this.

To delete an index or drop an index, it is called drop index like you have drop table and give the index name. So, this is a basic two commands to create and drop index. It also the index also optionally allow you to specify the type of index and the type of clustering you could create  an  index  for  a  cluster,  you  could  create  composite  index  on  multiple  columns, maximum limit supported in SQL is 32 columns.

8

Of course, you would never in real designs you will hardly require that. So, the Composite Index key since you can have multiple columns involved will become large. So, there is a restriction  that  it  cannot  exceed  roughly  one-half  of  a  data  block  of  course,  there  is  some more I mean, it has to be a little less than that, because some overhead data will also have to go  in  there,  because  otherwise,  if  it  is  more  than  half  then  you  cannot  keep  the  other information.

(Refer Slide Time: 4:21)

<!-- image -->

So, this is a basic way so to take more examples and showing you the options. So, you are creating an index, emp\_ename ON employee table using the ename attribute as your indexing field. So, this will just create the index with default options, but you can specify a number of options, some key ones I have mentioned here.

One  is  you  can  specify  the  TABLESPACE.  We  did  not  talk  about  TABLESPACE. TABLESPACE is basically when the database is organizing its physical space. It has it might partition that into certain TABLESPACEs. So, you can specify in which TABLESPACE you want that or otherwise, if you do not specify it will go to the default. So, this is a allocation of space in the database, which will contain the schema object, the index in this case.

Then you can specify the STORAGE options. So, this specifies how the database should store the option for example, how much should it allocate initially for this index schema object and how should that space grow and so, on. So, the options are that you can specify an INITIAL size that is called the first extent of the object for example, I have specifies 20 kilobytes and then  you  can  specify  the  NEXT  which  is  the  number  of  bytes  that  by  which  it  will  be extended  when  once  the  initial  extent  is  exhausted  and  you  need  to,  need  to  have  more storage. So, NEXT is used for the second extent.

And further on you do not specify the extent, but what you specify is a percentage by which every time it will increase over the last extent. So, here for example, we had 20k, then 20k So,  the  second  extent  was  100  percent  increase,  but  from  there  on  I  am  saying  that  the percentage increase will be 75. So, you have after these two you have 40k. So, 75 percent of that will be increased three-fourth of that which is so, it will become 30, increase would be 30k. So, it will become 70k. The fourth extent will do increase by 75 percent of 70k and so on.

So,  so,  you  can  see  that,  by  percentage,  the  advantage  you  get  is  naturally  as  the  index  is growing, you would like to allocate more and more space in the subsequent extents, because it has a tendency to grow. If you feel that no it is initially only there is a lot of things will be required, but if the growth will be very low, then you could put PCTINCREASE percentage increase as a smaller value like say 10 percent, 20 percent.

You can also specify how much what percentage of the data block in the tables data segment should be kept free for updates, I have said the no nothing needs to be kept free. So, this is so, what we saw here from this part is the storage specification, then the PCTFREE and finally, you say which is again optional is compute statistics. So, that will tell you, how your index is doing, what is getting indexed, how often and so on so forth.

## (Refer Slide Time: 8:03)

2

<!-- image -->

## HT Madras

<!-- image -->

5

IT Madras

<!-- image -->

## Index in SQL: Examples

- Create an index for a single column, to speed up queries that test that column:
- CREATE INDEX emp\_ename ON emp\_tab(ename);
- Specify several storage settings explicitly for the index:
- CREATE INDEX emp\_ename ON emp\_tab(ename)
- Create index on two columns, to up queries that test either the first col speed

TABLESPACE users Allocation of space in the Database to contain STORAGE INITIAL 2OK Specify the size of the 1st extent of the object NEXT 20K Specify in bytes the size of the 2nd extent to be al PCTINCREASE 75) Specify the percent by which later extent: PCTFREE 0 / / 0% of each data block in this table's data segmei COMPUTE STATISTICS;

- If a query is going to sort on the function UPPER(ENAME) , an index on the

## Index in SQL: Examples

- that test that column:
- Create an index for a single column, to speed up CREATE INDEX emp\_ename ON emp\_tab(ename); queries
- Specify several storage settings explicitly for the index:
- CREATE INDEX emp\_ename ON emp\_tab(ename)

TABLESPACE users Allocation of space in the Database to contain STORAGE // Specify how Database should store a database object INITIAL 2K Specify the size of the 1st extent of the object NEXT 20K Specify in bytes the size of the 2nd extent to be al PCTINCREASE 75) Specify the percent by which later extent: PCTFREE 0 / / 0% of each data block in this table's data segmei COMPUTE STATISTICS;

- Create index on two columns, to up queries that test either the first col speed
- CREATE INDEX emp\_ename ON emp\_tab(ename, empno) COMPUTE ST
- If a query is going to sort on the function UPPER(ENAME) , an index on the

## Index in SQL: Examples

- Create an index for a single column, to speed up queries that test that column:
- CREATE INDEX emp\_ename ON emp\_tab(ename);
- Specify several storage settings explicitly for the index:
- CREATE INDEX emp\_ename ON emp\_tab(ename) TABLESPACE users Allocation of space in the Database to contain STORAGE
- Create index on two columns, to up queries that test either the first coll speed

// Specify how Database should store a database object INITIAL 2OK Specify the size of the 1st extent of the object NEXT 20K Specify in bytes the size of the 2nd extent to be al PCTINCREASE 75) Specify the percent by which later extent: PCTFREE 0 / / 0% of each data block in this table's data segmei COMPUTE STATISTICS;

- CREATE INDEX emp\_ename ON emp\_tab(ename, empno) COMPUTE ST
- If a query is going to sort on the function UPPER(ENAME) , an index on the

Now, to create index on two columns, you use the same command, but write two columns one  after  the  other  in  the  as  their  indexing  attribute.  So,  there  are  I  mean  if  you  use  two columns  naturally  the  question  is  what  will  be  used  primarily  and  what  will  be  used secondarily, we will talk about all that.

Now, if suppose a query is going to sort on the function or on the name, so you say, upper name so the an index on the ename column itself would not speed up this operation, because it has to sort, because sorting is, is changing the order. And the moment you change the order naturally, the index goes bad, it needs to be re computed, actually, it might slow down the call to this function.

So, if you want to have this kind of sorting be applied along with the indexing, then instead of creating the odd it  on ename, you will have to create it with the function for each column value. So, that will speed up queries that use the function for searching or sorting, so you will have to keep this in mind.

So, these are the couple of basic things we have learned how to create an index, how to give very  key,  parameters  to  it  if  you  want  to  control  the  space  better,  how  to  create  index  on multiple  attributes  and  how  to  create  index  when  a  function  is  intended  to  be  used  on  the column on which you are indexing.

(Refer Slide Time: 9:46)

<!-- image -->

g

<!-- image -->

So, you can also create index using the bitmap we talked about bitmaps in hashing. So, here is an example. This standard student database ID, name, age, address, etc. And we know that these two are attributes which will have limited values, because there are 2 possible gender values and 4 possible semesters as we were looking at.

So, what we will do is for these two, we will use a bitmap index, which is as we said that it is a long bit array, as long as the number of records that exist in the table, and if a particular attribute is available in a record, then you put 1, otherwise you put 0. So, first record has, 101 has gender as M, so, it is 1 here and the rest are f so, you put 1 in those.

Similarly, you can, you do the same thing on semester because there are 4 semesters and you will have for the first and second you have semester 1, for the third, for the third record, you have  semester  2,  for  semester  3,  you  have  no  record  and  the  last  one.  So,  with  this  your several of your computation like you want to do select star from where gender f and semester gender is equal to F and semester is equal to 4.

So, what do you take you take the bit pattern of f, you take the bit pattern of semester 4, and all that you need to do is to do an ending. So, take these and take these do an ending so you will get 0001 which tells you that the fourth record, fourth record only satisfies this condition. So,  this  naturally,  this  kind  of  index  speeds  up  operations  when  you  have  this  kind  of  a property. So, all that you need to do is to say that specify the bitmap field on which bitmap keyword to create a bitmap index and rest of it is the same.

2

<!-- image -->

<!-- image -->

## Multiple-Key Access

- Use multiple indices for certain types of queries
- Example:
- select ID

from instructor where dept\_name "Finance' and salary 80000

- Possible strategies for processing query using indices on single attribu
- Use index on dept\_name to find instructors with department nami salary = 80000
- Use index on salary to find instructors with a salary of 80000; test "Finance"
- Use dept\_name index to find pointers to all records pertaining to Tsl^

Now, you can have multi key access that is what because there could be more than one key, more than  one  attributes  on  which  you  want  to  index  because  oftentimes,  maybe  you  use them in a combined manner like you are doing it here that select ID of the instructor where the department name is finance and salary is 80000. So, what could be the possible strategy?

One possible strategy is to use an index on the department name only, I mean just use the index  on  the  department  name.  So,  that  will  quickly  find  new  instructors  with  that  given department  name  finance,  and  then  you  do  a  normal  test  for  the  salary  because  you  have index on this.

select ID

from instructor

where dept\_name

"Finance" andsalary = 80000

2

<!-- image -->

select ID

from instructor

where dept\_name = "Finance" and salary = 80000

Alternately,  you  could  have  index  on  salary  to  find  the  instructors  with  salary  80,000  and then test for the department name or you can use department name to find, department name index to find pointers to all records pertaining to finance and similarly use index on salary. So, intersection of both sets are the set of pointers obtained. So, these are the different kinds of possibilities when you have multiple such.

2

<!-- image -->

IIT Madras

Module 45

## Multiple-Key Access (2); Indices

- Composite Search are search keys containing more than one For example; (dept\_name salary) Keys
- Lexicographic ordering: (a1.a2) &lt; (b1,b2) if either a1 &lt; b1, or 91 = b1 and a2 b2
- Hence; the order is important

## Multiple-Key Access (2); Indices

- Composite Search are search keys containing more than one Keys=
- Lexicographic ordering: (a1.a2) (b1.b2) if either
- a1 b1, or
- b2 and
- Hence; the order is important

Now, if you use this as a composite index a department name salary, then the question is in terms  of  indexing,  indexing  is  basically  creating  a  virtual  ordering;  indexing  gives  you  a virtual sorting on the data. So, what is that sorting rule? Sorting rule is there is this order is important from left to right and the in this order whichever comes first is given the preference in terms of the comparison.

So, if I order in this way, then the ordering is a1 a2 is less than considered to be less than b1 b2 this tuple because you have two values now, if either a1 is less than b1, so you do not look at the other one. So, you consider that to be the earlier record. Or if a1 is equal to b1 and a2 is less than b2. So, this is the way you know you arrange the dictionary. So exactly you use that and  therefore  the  order  is  important.  So,  the  index  order  that  will  be  created  by  an  index, which  is  department  name,  salary  is  different  from  what  will  be  created  if  it  is  salary, department name.

(Refer Slide Time: 14:54)

<!-- image -->

So, when you index with this kind of multiple attributes, let us say you have done an index on department name, salary and you are trying to do this though. So, this can be used to fetch only  records  that  satisfy  both  conditions.  Now,  if  you  use  separate  indices,  it  will  be  less efficient, because each one of them will bring more records than what will actually go in that final case.

Actually, this will also be efficient in terms of this query, the difference is salary is less, why it is so? Because in department and salary, the first preference is being given to department name. So, department name has the primary ordering, so, it will filter out lot more because it has an equality, department name is finance. So, it will be it is expectedly, much less number of  tuples  within  which  the  index,  second  part  of  the  index  on  salary  will  be  used  to  get records less than 80,000.

But,  if  my  query  was  different,  just  think  of  it  is  department  name  is  less  than  finance, whatever it means, I mean, it is not a semantically very meaningful, the meaningful query, but  this  is  equal  to  80,000,  then  this  will  bring  a  lot  more  number  of  records,  because primarily it is going to look at the department name. So, not the second condition.

So, while you form your index, you have to also keep an eye on what kind of queries you are going to primarily look for or what kind of for which kind of queries do you need to do a speed up, you are intending to do a speed up using the, using all your indexing mechanisms.

(Refer Slide Time: 16:50)

<!-- image -->

8

Now moving on, can anybody create an index? The answer is no, because creating an index has  a  lot  of  impact  in  terms  of  speeding  up  a  few  queries,  which  is  true,  but  it  may  also impact in terms of various performance degradation in updates, we will discuss, I mean, you can easily understand that because every update will have to update the index, you, it also has implications in terms of the space that you use in the database.

So,  there are certain rights  or privileges that you will need to have to be  able to  create  an index otherwise you will have to, I mean for that you will have to ask your DBA to grant the privileges or otherwise you will have to just work with the indexes that exists. So, you must have a INDEX object privilege. And if the schema contains the index must also have a quota for the TABLESPACE you can specify this much of TABLESPACE I need, then you will need to have that kind of a system privilege, unlimited TABLESPACE and so on.

If you want to create an index on a schema that is not owned by you, it is owned by someone else, then you must have CREATE ANY INDEX privilege. One is a create index privilege, one is create any by create index privilege, you can create index for schemas that you own. With create any index privilege, you can also create schema that index for schema that others own.

Similarly,  function-based  indexes,  which  we  saw  in  terms  of  upper  ename  required  the QUERY  REWRITE  privilege,  or  and  the  QUERY  REWRITE  ENABLED  initialization parameter has to be set to true for that, I am sure you will not retain so much of details from this  description.  All  that  you  need  to  remember  is  you  need  privileges  and  when  you  are actually  working  on  the  system,  you  can  look  up  the  system  manual  to  see  exactly  what privileges  you  need  and  ask  the  DBA  to  grant you  those  privileges.  DBA  means  database administrator; the ultimate authority.

<!-- image -->

<!-- image -->

So, this was how you create indexes in SQL. Now, the question is, what should you index and how much should you index? So, if we step back a little, you will see that there have been certain basic design objectives we started with. And initially it was totally at the design level  so  we  work  extensively  on  normalization  of  tables,  which  lead  to  reduction  of redundancy  naturally,  consequently  minimizes  the  possibilities  of  anomaly,  it  become,  it makes it easier to adhere to different constraints by various dependencies and efficiency of access and update is better in a normalized design.

So, this is what you do at a design time, but remember design is done once, once you have, I mean, you hardly ever change the design because if you change the design in a live database, then all your data will have to be migrated and all those issues will come.

(Refer Slide Time: 20:16)

<!-- image -->

<!-- image -->

So,  subsequent  your  design  what  do  you  have  to  keep  doing  to  have  a  good  database performance is to see how the data is physically organized and managed. So, that is the next thing  we  have  talked  about  extensively  that  is  about  indexing  and  hashing,  what  kind  of index, what kind of hashes all these will have to be all these mechanisms have been given so that you can based on what your database needs at the execution time at the runtime with the real data depending on the idiosyncrasies of the real data that will have to be designed.

So, naturally How do you know about how your data is doing and these are the two tools that you have,  one is  collect  statistics  as  we  say  compute  statistics.  So,  which  will  give  you  a variety  of  on  various  tables,  you  will  be  able  to  learn  the  patterns  which  query  is  moving faster,  which  query  is  more  frequent,  what  is  slowing  down  a  certain  query  processing  or update processing and so on. And based on that, you have to adjust the indexes on the tables to optimize the performance.

Now,  unfortunately,  unlike  the  normalization  theory,  there  is  no  sound  theory  that  can determine optimal performance, because it significantly depends on the profile of the data in the real world. Given the same basic normalize design from the constraints of the data, you could  have  variety  of  different  actual  profiles  of  the  data,  statistics  of  the  data  requiring varied different kinds of indexes depending on the data distribution.

So, since we do not have a theory, what I would just show to you is a set of you know kind of rules,  these  rules  are  not,  not  any  rules  like  programming  language  rules,  these  are  cast  in stone, these are kind of guidelines, which has evolved over a large period of experience that the community has gathered by working with databases. So, you should keep these rules in your mind and then apply them as appropriate in different contexts based on the statistics and adjust the indices, so that your database remains agile in its behavior all the time.

(Refer Slide Time: 22:48)

<!-- image -->

So, I summarize I start with the summary of 7 ground rules for indexing. Rule 0 indexes lead to access, update, trade-off the more index you have you have better access more index you have updates become slower, disk space becomes more. So, there is a trade-off you will have to do it is not that you can have a design by indexing everything, disastrous, but at the same time,  if  you  do  not  index  then  anything,  then  your  frequently  asked  queries  will  be unnecessarily slow.

The second you have to look at is, index the correct table not index everything, which table should  you index you have to answer that, do you index every table? Or there are certain properties that you could look for, in a table what are the correct columns to index? Would you index on every column every combination that is explosive? So, you have to decide on the correct.

What is a number of different indexes that you will have on each table? So, this very, these are more significantly common-sense rules, but very significant in terms of actual execution. You may have composite indexes and the order of the columns we have explained with this department name and salary example that how the order of the columns become important in terms of the composite indexes. Then you have to gather statistics to make index usage more accurate and finally, drop the indexes that are no longer required. So, these are the 7 ground rules.

<!-- image -->

Rule 0 indexes lead to access update, trade off, so you know that the query access results in a search so index will help. So, specific index on that field or the set of fields will help and but update any update insert, delete or even a values update result in the update of the index file also. So, we have, for that reason only, we have seen all this self-adjusting B+ tree structure to maintain the data.

So, but it has a overhead or penalty. So, update is the overhead or penalty you pay for quicker access.  So,  having  unnecessary  indexes  will  cause  significant  degradation  of  performance. The index files could also occupy a lot of space. So, you have to have informed judgment to index, this is the basic first rule.

(Refer Slide Time: 25:43)

<!-- image -->

Second says index the correct table. So, this is a thumb rule being given create an index if you freak, I am sorry, create an index if you frequently want to retrieve less than 15 percent of the rows in a large table. Why, why so? Now, this percentage is not sacrosanct, it will vary according to the relative speed of the table scan and how clustered the row data are, you can think of it in this way that if the data is more clustered, lot of values are together, then you will have the need to index only if you want to access a whole lot of data.

But  if  it  is  very  sparse  in  terms  of  clustered  lot  of  values  are  distinct,  then  even  for small segment, small part of the data, small part of the rules being accessed, an index will help. The core idea behind this is index is good on distinct values. So, you have to make an assessment of how much of distinctness you have in your table in terms of those values.

Index columns can also be used to improve performance on join of multiple tables. So, you will have to know what you want to join. And remember, while indexing a table, that primary and unique keys are automatically indexed by the database, you do not have to create indexes for that. But you might want to create an index on a foreign key, which can make your joins better.

Last but not the least, if a table is small, you do not need to require an index, because it might actually have to do much of overhead, that serial scan in a small table would be fine. But then over a period of time, when you see that your query is taking too long, you know that your table have grown to a from a small to large size where you will have to index it. So, it is a live scenario and you will have to keep managing that. (Refer Slide Time: 28:06) 3

<!-- image -->

<!-- image -->

8

2

Index the correct column. So, as I said that indexes work well when the values are relatively unique. And there is a wide range of values you may have use the regular index, you have a smaller range of values like gender, semester and so on seasons, use a bitmap index there is a kind of tape to handle columns containing many nulls, so, you will, if you want to deal with the non-null values, you will normally say that where column x is not null that is a direct semantic way of doing it.

So, instead of saying that, you could say something like this, if you understand, so, what this is saying is minus 9.99 times 10 to the power 125 which means that it is an extremely small negative value. So, we are saying column is greater than this. So, expectedly whatever value you have in that column, obviously, this is true for numerical numeric column not for others. For a numeric column, whatever value we have expectedly it will be larger than this except for those which are null, because those will never match in a comparison.

So, what you, why do you want to prefer this because if you use this, and you have an index on column x, then it will use that index but if you use this it cannot use the index because null cannot be indexed. So, there are, these are some of the tips there if there are, if there are many nulls in the column and you do not search on the non-null values, then you do not index long and long row columns cannot be indexed, of course, long row is kind of deprecated now, it is blog, a blob you have you have, I have talked about blob that is that the binary data. So, this is your rule number 2.

(Refer Slide Time: 30:34)

OF

8

2

<!-- image -->

Rule number 3 says that the limit the number of indexes for each table, because if you have more indexes, moreover, it is incurred. So, when a row is inserted or deleted, all indexes will have to be updated. So, you must check that you really need the indexes that you have. And if a table is primarily read only, you might use more index because, then that possibility of data changes are very few. But if the table is heavily updated, you must use fewer indices.

TECH

2

<!-- image -->

<!-- image -->

Choose the order of columns in the composite Index, we have already talked about this, here is an example that I would like to, like you to look at, say there is a vendor table given here and it has vendor parts table, it has 5 vendors, and each vendor has about 10,000 parts. So, so, in  a  query  like  this  one,  where  you  have  part  number  as  well  as  Vendor  ID,  there  is  a possibility of using a composite index.

So, whether the Composite Index should be part number vendor id or vendor id part number, it should be part number vendor id. Why? Because when part number has a large number of possible values about 1000 whereas vendor id has very few possible values. So, if you can come to the specific part number, then your reduction in the number of records that you will have to look for the vendor id 1012 will be a lot more compared to if you had done vendor id, part number where 1012 will have thousands of part numbers and you will have to look for 457 between them. So, this is, these are kind of the judgments which you will have to there is this is all based on the profile of your data and cannot be generalized as such.

(Refer Slide Time: 32:44)

<!-- image -->

So, you have to gather statistics to know about all this. So, you can I have shown how to use compute statistics. And you can also update the update and distribution of the value changes periodically by refreshing the statistics, you have to call these procedures if you are working in Oracle otherwise, you will have to see what the corresponding ones are.

<!-- image -->

And drop an index that is no longer required, it is quite obvious why you will have to drop that. And when you drop a table, then all indexes on that table are dropped. And if you do not want any index on a table, can drop all existing indexes by dropping, drop any index kind of thing. And you need the privilege for that.

(Refer Slide Time: 33:31)

<!-- image -->

So,  this  brings  us  to  the  end  of  this  module.  We  have  now  closed  on  our  study  on  the indexing. We have learned how to create indexes of various types in SQL and what are the ground rules the guidelines for indexing. Thank you very much for your attention and we will meet in the next module.
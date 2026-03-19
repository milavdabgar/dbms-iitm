<!-- image -->

## Database Management Systems Professor Partha Pratim Das Department of Computer Science and Engineering, Indian Institute of Technology, Kharagpur

Application Design and Development/3: SQL and Native Language

Welcome to Module 33 of Database Management Systems course in IIT Madras online B.Sc. program. We are discussing application design and development using databases in the back. We have discussed about the architecture. And since significant  majority of these applications are web-based, Internet-based, we have also discussed about web fundamentals, the basic structure of the web architecture, the scripting and all these in the last module.

<!-- image -->

8

(Refer Slide Time: 01:04)

<!-- image -->

Now, going forward, so if I just to give you a quick reminder of the three-tier architecture, there is  a  presentation  layer  which  is  interacting  with  the  user  it  is  on  the  browser.  So,  what  is  the requirement, development requirement there? You have to be able to write the, design the HTML the  elements  and  all  that  and  the  validations  or  auto  fill  and  so  on,  you  need  to  have  the JavaScript's  or  some  client-side  scripting  for  it.  So,  this  is  something  which  we  can  practice more in the application development course.

The second part is a middle tier which is an application or business logic layer where primarily you will have different kinds of logic in typical object-oriented design Java or C++ and you will have object models corresponding to the relational models and so how to do that you know from your programming, an object-oriented programming background, so that I assume that you will be able to do that.

To facilitate the creation of HTML pages from servicing the query we have servlets or serverside scripting JSP and so on, so which can help you actually more easily write the query response by filling up an HTML template with the query results. And we have taken a quick look at how to do that. This is not difficult. Though you have not done it, you can easily pick it up. So, that part the server-side scripting we can assume that you will be able to do.

What is left? And beyond that is the data access layer or data layer, where you have the database, the tables, the query the constraints, the data instances and you know SQL to be able to access or update those data. So, this is the whole paradigm. So, the only missing piece in this is the fact that  in  your  servlet  or  in  your  high-level  programming  in  the  application  layer  based  on  the response, based on the request that you have got, you will need to get the right result from the database.

Now, database understands SQL. So, one part would be that you will have to go to the database and present the SQL query. If you present the SQL query, the database will give you a response. That response what is the response is a relation, which means it is a table. So that table you will have to take and put into HTML. So, anything from the beginning of the frontend to the point where you have the servlets or the high-level programming language, knowing what data it needs to extract from the database, this part is known to you. Once the query goes to the database, you know how to answer it. And once the table comes back again you know how to do the HTML and set it back.

So, the missing part in the game, in the jigsaw is from the high level how do I make that SQL execute and get the result and how do I get that result back from the database into the high-level program.

(Refer Slide Time: 05:10)

IIT Madras

Module 33

Panha Pratin

Objectives &amp;

Outline

1

That is what is the, that is a core application development area from the database perspective and we  would  like  to  discuss  that  working  with  SQL,  sequel  and  native  languages,  high  level programming languages.

## Module Outline

- Accessing SQL From a Programming Language

## (Refer Slide Time: 05:19)

5

<!-- image -->

<!-- image -->

So, the basic idea is simple. Is, you will have to create some kind of a Application Programming Interface API, which it can interact  with the database server. Now, what are the things that it grossly needs to do? It needs to connect with the database server. Because please do not assume that  there  is  only  one  database  server  there  could  be  multiple.  So,  it  needs  to  connect  to  the database server. Even one database server will have multiple users with different rights and so on. So, you need to connect to the database server with the proper user credentials.

Once that is done, you need to send the SQL command in some way to the database server. Once you send that the database server knows how to process that SQL command to generate the data. It generates a table or you can say a sequence of tuples. And then you will have to fetch those tuples  one  by  one  because  there  is  a  sequence  that  stable  rows  different  into  your  high-level program so that you can proceed further. And after you are totally done, what you can put here is close  connection.  Once  you  are done,  you  can  settle close  the  connection  so  that  it  cannot  be used by mistake somewhere else.

Now,  for  this  there  are  two  kinds  of  dominant  framework  one  which  is  the  connectionist framework which creates, I mean, kind of creates a driver which connects between the native language and the database server. This is called ODBC Open Database Connectivity and it works with almost  all  major programming languages. There are other connectionist APIs also which include say OLEDB, Object Linking and Embedding.

This Microsoft brought it in very early days. And ADO NET .NET and so on. And the other which is very popular is JDBC which is Java specific, which is Java Database Connectivity. So, this is one approach connectionist. So, in connectionist approach your SQL program is kind of created,  executed  through  a  set  of  APIs  that  these  drivers  provide.  The  other  approach  is embedding. In embedding, you put SQL commands in some format inside your native language, inside  your  native  language  program.  This  again  works  with  a  large  number  of  programming languages. So, we will take a look at both of them one by one.

<!-- image -->

So, this is the overall architecture of the connectionist one. So, you have a high-level program and you have SQL query with tables and all that and you have this connection library, which could be ODBC, it be JDBC some set of APIs which allows you from the high-level language to submit the query, connect and submit the query and get the result. And then it is the inside the database process the typical SQL query processing using the database in schema this part is what we have already covered.

## (Refer Slide Time: 09:33)

<!-- image -->

So, given this, what is ODBC? It is a standard API for accessing database. So, the objective of ODBC is it is database system independent as well as it is operating system independent. That is, if  you  have  written  an  application  program  using  the  ODBC  APIs,  then  it  will  work  on,  on operating  system  and  it  will  work  for  all  database  systems,  which  is  very  much  required, otherwise migration would be a big problem. It can be ported to other  platforms, both on the client as well as servers side with only few changes that may be required.

Those are required, few changes are required at times because of the hardware differences and so on. So, this is thematically what you will do in a ODBC used application, open the connection, send query and updates, get back result. Historically, it was developed by Microsoft and Simba Technology. And later on SQL is in 90s SQL subsumed it and it is in the standard.

## (Refer Slide Time: 10:47)

<!-- image -->

IIT Madras

## Module 33

Das

JDBC

## ODBC (2); Python Example

- The   code uses data source named "SQLS" from the odbc ini file to connect and issue a query;
- Itcreates a tal ble,   inserts data literal   and   parameterized statements and fetches the data using

import pyodbc conn

pyodbc . connect ( 'DSN-SQLS;UID-tesi conn

execule create lable Co13 varchar(10) )

CUIJOI execule insert into "ABC| ")

select

brCak

valuc 20.0 ,

## ODBC (2); Python Example

- The   code uses data source named "SQLS" from the odbc ini file to connect and issue a query;
- It creates table;   inserts data literal   and   parameterized statements and fetches the data using

## import pyodbc

<!-- image -->

pyodbc , connect ( 'DSN=SQLS;UID=tesi cursorEconn col3 varchar(10) )

ingert into "ABC) ")

break print (row)

CUISOI ,execule insert 20.0,

<!-- image -->

ODBC

HT Madras

<!-- image -->

## Module JJ

Das

## ODBC (2); Python Example

- The   code uses data source named "SQLS" from the odbc ini file to connect and issue a query;
- It creates literal   and   parameterized statements and fetches the data using

import pyodbc conn pyodbc . connect ( ' DSN-SQLS;UID-tesi CUIJOI conn

create table co13 varchar(10) )

CUIJOI "ABC| ")

CUISOI .execuce

<!-- image -->

brCak print (row)

CUISOI execure insert into

20.0,

CUISOI

## ODBC (2); Python Example

- The   code uses data source named "SQLS" from the odbc ini file to connect and issue a query:
- It creates table;   inserts data literal   and   parameterized statements and fetches the data using

## import pyodbc

conn pyodbc , connect ( 'DSN-SQLS;UID-tesi conn

CUISOI Insert into print (row)

insert 20.0,

<!-- image -->

IIT Madras

## Module 33

Das

Ouilbe

HT Madras

<!-- image -->

Das

Bode

## ODBC (2); Python Example

- The   code uses data source named "SQLS" from the odbc ini file to connect and issue a query.
- It creates table,   inserts data literal   and   parameterized statements and fetches the data using

import pyodbc conn CUIJOI conn

execule ( (col

CUIJOI ,execule ingert into "ABC| ")

CUISOI execute

break print (row)

20.0, insert into

gelect

## ODBC (2); Python Example

- The   code uses data source named "SQLS" from the odbc ini file to connect and issue a query;
- It creates table,   inserts data literal   and   parameterized statements and fetches the data using

import pyodbc conn

pyodbc , connect ( 'DSN-SQLS;UID-tesi cursoreconn

Creale col3 varchar (10)

CUISOI

'ABC|

Iov: brCak print (row)

insert 20.0,

'select able [vtest

(col

<!-- image -->

So,  let  me  just  quickly  show  you  an  ODBC  example  with  Python.  So,  Python  has  a  ODBC library  called  pyodbc.  Python  has  several  ways  we  will  see.  So,  the  first  thing  you  do  is  this library.connect. So, this is an API. And you pass as parameter the different information that is required, which is the database ID, SQLS, the user ID and the password. You will require that. Once you have done that, then you have got a connection object.

On the connection object, you create a cursor. A cursor is nothing but it is like pointer, like if you have a table, say you have a table with several rows, a cursor is a pointer, which is somewhere in the table and then it moves to the next. If you say I am done with this row, it goes to the next. You are done with this row goes to the next. So, it is like a pointer or you can think of it in C++, Java style, you can think of it as an iterator. It basically is an iterator. So you create a cursor and then  on  that  cursor  you  execute.  So,  execute  is  basically  it  will  take  an  SQL  command  and execute.

So, you can see that we have given a command to create table simply as a text string. So, this is an SQL command, we just give it a text string. Then you have another SQL command. So, it creates a table, inserts the data and there is a third statement executed which is select. When you do that, it will get back a result. Select star, so it will get back all those which is currently only one row, because you have created and inserted only one, will get back that. So, where will you get it, you will get it in the fetchone method of the cursor. So, fetchone will get you one row at a time. So, it gets you take it in the row. If it is not a row, which means that if it is at the end, then you break, you are done. Otherwise, you print. Similarly, it shows few more deletions inside.

I  mean you can write any kind of SQL query in this manner. This is your connect part, this is your result part and this is your SQL query part. Very simple structure. You can write, these are variants of the particular pyodbc style. You can directly write everything in the string or you can write the query as a string and keep some parameters which you put later on. So, that is the basic ODBC structure.

<!-- image -->

Similarly, there is a API for Java called JDBC. And this was brought out much later after ODBC in 97 in the Java Development Kit 1.1 and since then it has been the part of the Java Standard Edition platform supported by Oracle, of course, and it specifically works with Java. And since Java  is  a  significantly  platform  independent  language  and  efficient  in  terms  of  writing application programs. So, JDBC has that a very good acceptance.

Again, the steps are like ODBC open the connection. This is which is specific to JDBC because JDBC is completely object based, because it is specifically for Java. ODBC cannot assume that because ODBC supports languages which do not have any object. So, here it creates a statement object  that  becomes  the  handle  through  which  you  do  everything  and  you  execute  the  query using this statement objects to send query, to fetch results, the statement is your handle to do things, and it also has exception mechanism to handle errors very efficient, very simple and nice to use.

(Refer Slide Time: 15:24)

<!-- image -->

<!-- image -->

Now, initially, here, you will see that certain imports are making which is JDBC related imports. The first thing is connection. So, I need to build the connection URL. What do I connect to. I need the server with the port, where it is, I need the database in that, name of the database, I need the  user,  I  need  the  password.  So,  I  put  all  of  this  into  a  string  and  then  I  through  my  driver manager, because I said JDBC is a driver, we say get connection passing this parameter. So, it gives me connection. And with that connection, I do a create statement.

The  first  thing  was  to  get  connected  and  then  have  a  statement  which  will  work  as  a  handle between Java and the database. There is a try to take care of if the connection could not be done, for example, the password is wrong or the database name does not exist and so on. If it is then you handle it here with the stacktrace you print. If it is correct, then I first step I do is with the statement I called create table. So, let us see what is create table. As the name suggests it will create a table. So, let us go to the next slide and see what is create table.

## (Refer Slide Time: 17:11)

5

<!-- image -->

<!-- image -->

So, here is create table, private static void create table which takes a statement. So, it has got the statement using which you will do the creation. So, statement has an execute which executes any SQL command. So, you have given a command, I mean, we want to create a table. So, the first thing I want to ensure that the table does not exist. So, I do a select, star in the sys subject, sys subject is what, sys object is a collection of the data dictionary, where all table names and all those are kept. So, if that selection returns anything, then the table exists. So, if it exists then we will drop the table. If it does not, then we will do nothing.

So, now I formed the query for creating the table. This is create table the name, the first attribute with  all  the,  this  is  just  pure  plain  and  simple,  pure  SQL  except  this  notation  for  the  name. Everything else is exactly the same. Maybe the way you write the types are little different, but it exactly corresponds to SQL. So, I create a table with two attributes one and two. And then the statement I execute. The table is created. And then I keep on making a statement take a string to insert  a  pair  of  values  as  a  product  one  execute,  so  first  insert  done,  second  insert  done,  third insert done. So, after I have executed this method, obviously, I will have three, the table having three products into it.

(Refer Slide Time: 19:17)

<!-- image -->

So, let me get back here. So, I have done create table. Table is ready. Now, I make the query string, select star from the table and I define a result set. I said, the result will be in terms of a table. So, that is called the result set. So, this is this actually is like a like a table which we will be able to iterate and print. And then I do statement.execute query. On the statement I execute the query like this. I could have done statement execute within that, any of that is possible. Then I do display row. So, I have got the result set, now I have to show that, display that, create the HTML and so on.

## (Refer Slide Time: 20:13)

<!-- image -->

So, let me again, go to the next slide. So, what I have displayRow which takes a title and result set. So, the title is the title of the table. So, I print that title, which is simple. Then what I am doing  is  on  the,  I  iterate  on  this  table  with  the,  for  the  product  ID  rs  dot  next,  so  this  is  the iterator. And at every iteration value, I get the string corresponding to product ID and the name. This is the two things I had done product ID and name. So, that is the two columns that have come. So, I take two of those values from the row print it, take the next two print it, take the next two print it and I am done. So, this is how very easily using JDBC a simple Java application with database can be created.

## (Refer Slide Time: 21:06)

<!-- image -->

## Connectionist Bridge Configurations

- bridge is a kind of driver that uses another driver-based technc special
- This driver translates source function-calls into target function-calls
- Programmers usually use such a bridge when database but have access to a target driver they
- Common bridges are:
- ODBC-to-JDBC (ODBC-JDBC) bridges: An ODBC-JDBC bridge consists ODBC-JDBC Bridge, SequcLink ODBC-JDBC Bridge
- OLE DB-to-ODBC bridges: An OLE DB-ODBC bridge consists of an OLE [ target database, This pr DB method calls into
- JDBC-to-ODBC (JDBC-ODBC) bridges: 4 JDBC-ODBC bridge consists of target datal Bridge, SequeLink JDBC-ODBC Bridge ibase,

Now, there are often questions that certain databases may support ODBC, but you may want to use Java JDBC with that or vice versa. So, there are certain bridge drivers which bridge between two of these drivers. So, ODBC to JDBC bridge, it consists of a ODBC driver, which uses a JDBC driver to connect to a database. So, that your application program is written in ODBC, but the database is actually supporting JDBC.

You can still using this bridge driver you can do that. You can do the reverse also. You can do it from  OLEDB  to  ODBC,  you  can  do  ADO  dot  NET  to  ODBC.  So,  basically  putting  all  this together, you have immense connectionist power to use any of these drivers from any languages and  connect  to  any  database  with  any  kind  of  support  in  terms  of  the  connectivity  to  the application program. So, that was the connectionist view.

(Refer Slide Time: 22:24)

K

<!-- image -->

Next what we see is the embedding view, which is where what you do you do a different thing. You put the SQL query as a part of your source language and let the whole thing handle, be handled in the query processing itself.

(Refer Slide Time: 22:40)

<!-- image -->

So, for that you need, again, what do you need, you need to say that you execute a statement. So, you have a host language say Python or Java or C++ and in that you want some unique way to say  that  this  part  is  SQL.  So,  you  use  a  tag  like  EXEC  SQL  or  some  systems  use  #sql  and anything which is SQL you put inside that. So, the general structure is like that, EXEC SQL then you have an SQL statement. That is one part.

(Refer Slide Time: 23:22)

5

<!-- image -->

So, what will you need to do along with this? You will need to connect the first step. So, this is straightforward.  This  is  straightforward.  EXEC  SQL  connect  to  server  name,  user,  user  name using password. This will give you the connection. For multiple SQL commands, you write a section and you write the commands, SQL commands within that.

Now, the key point is how do you get give input values to the SQL and how do you get the result back. So, what is the communication between the host language variable and the SQL statement? So, that is done in a very simple way. You define, you declare a variable in the host language say you  have  declared  a  variable  credit  amount,  you  declared  a  credit  amount  then  this  becomes colon credit amount becomes a variable in the SQL statement, as simple. If you put a value in credit amount in the high level, it will be available in the SQL as colon credit amount. So, now you know. Now, you can put the value, get the value and so on. Very simple designs is that.

<!-- image -->

Now, we have seen that in the connectionist we need a way to take the table out. So, what we did we  used  iterators.  So,  we  need  a  similar  thing  here.  So,  what  is  supported  for  embedding  is defining declaring cursor. So, you declare c as a cursor for an SQL query. So, this is declare c as a cursor for this query, which means the result of this query will be available in this cursor c and then you can iterate on that cursor to get the values out. You can see that in the query we have used a host language variable value by using a colon before it so that it becomes a part of the SQL. Structurally very simple.

(Refer Slide Time: 25:56)

(Refer Slide Time: 26:01)

<!-- image -->

Now, after a connection, you open a cursor, you have defined a cursor, you open a cursor. So, cursor needs to be open so that it is available for taking your data. And then you fetch c into, c is a cursor, into what are these, these are obviously host language variables. So, from the cursor, you take the values to the specific host language variables.

Keep on doing that, repeatedly keep on calling the fetch in the SQL and you will keep on getting the subsequent tuples. Your iteration happens. So, it is declaring a cursor, opening it, executing the query and then doing fetch on the cursor repeatedly and every time you get the entire tuple you need to have placeholders for host language variables, which will get those values.

<!-- image -->

So, some you can do this for update as well. You can give a, take a cursor for update and then update using that cursor. So, here you are declaring a cursor. This is your query. You get the list of  instructors.  The  cursor  is  for  update  you  have  set.  And  then  you  update  instructor.  This  is same as before. You say the where the current of c. So, instead of actually giving you a separate relation to update from, you are giving a temporary table which is this cursor as a result of this. So, these are the different variants that you get.

(Refer Slide Time: 28:14)

<!-- image -->

So, time for a full example. So, here there is a sailor table. This is a C example. So, this is a sailor table which from where you can give the ID and get the sailor's age. That is a very simple.

2

## (Refer Slide Time: 28:33)

<!-- image -->

<!-- image -->

So,  let  us  see  what  are  the  embedding  requirements.  So,  these  two  are  for,  are  headers  for embedding SQL. This includes the error reporting, it says that the error reporting can be done. This is declarations section where you are declaring host language variables to be used in SQL sage sid, sname. This is simple programming variables. Then you have a macro for printing a message  which  the  macro  prints  a  message  in  SQLCA  if  the  return  code  is  0  and  is  error handling. Let us look at the meet of the thing.

## (Refer Slide Time: 29:28)

<!-- image -->

Now, let me go to the main first. So, what do you have in the main, you take a main as argc greater than 1. So, it checks that whether it is got a command line input. If it is there, it will go, otherwise it will not work. If it is there, then that is the sailor ID for whom I want the sailor age. So, I connect. This is the database name hard coded here for that example, some database name. This is the check, the macro to check for error. If there is error, it will exit. Then I have EXEC SQL, the actual query. So, what is sid is colon sid. This is the this sid, host language variable, so that ID will convey there. This is a table and I have got sname, sage into colon sname colon sage, which are also host language variable.

Here,  I  am  not  getting  into  so  much  of  cursor  and  all  because  I  know  there  will  be  only  one variable. So, then you, once this is done, then you can report, because you have the sname, you have the sage. So, this goes here, this goes here. If there is error, you reset the connection. So, this is a sample scheme of actually doing this.

(Refer Slide Time: 31:09)

<!-- image -->

So, there is a, if this is just to tell you what the result should be, if this is the instance and if your input is assuming sage is application name is 44, that is sid 44 then you will get, should get this sid  request  is  44.  This  is  guppy.  So,  guppy's  age  is  31  executed  successfully.  So,  this  is  an example of how you can do it through embedding.

2

## (Refer Slide Time: 31:43)

<!-- image -->

I have also given an example in Java, which is little bit longish.

## (Refer Slide Time: 32:00)

<!-- image -->

But  this  is,  this  has  more  functionality  in  terms  of  actually  having  the  two  different  types  of cursors. And you can see that in this particular embedding framework, instead of EXEC SQL it is using #sql. In different places in this code, you will find that I have given markers, I mean, comment with number so that you can go to the next slide. So, one here is an application cursor.

(Refer Slide Time: 32:38)

<!-- image -->

g

So, if you go to the next slide, you will find what is the explanation of what that step, in terms of embedded SQL is doing. In this way, it goes on.

## (Refer Slide Time: 32:52)

<!-- image -->

<!-- image -->

## Embedded SQL: Java Example (4)

(1

- 2 Initialize the iterator . The iterator object cursorl is initialized using
- 3 Advance the iterator to the next row.  The cursorl.next () method
- Move the data   The named accessor method empno() returns the v value of the column named firstnme on the current row
- 5 SELECT data into a host variable   The SELECT statement passes Fows in the table into the host variable countl
- Close the iterators   The close( ) method releases any resources held You should explicitly close iterators to ensure that system resources timely fashion;
- Initialize the iterator . The iterator object cursor2 is initialized using query   The query stores the result in cursor2
- Retrieve the data   The FETCH statement returns the current value column declared in the ByPos cursor from the result table into the hc
- 8 Check the success 0f a FETCH.INTO statement . The endFetch( fetch &amp; row failed . The endFetch() method returns false if the last at FETCHINTO statement implicitly calls the next() method,
- Close the iterators .  The close() method releases any resources held You should explicitly close iterators to ensure that system resources 0 timely fashion

<!-- image -->

<!-- image -->

It is little long to discuss in the lecture, but I have included it so that you can conveniently read through the code and look at the comments and get a complete feel of an application. This is just for a variant I have used Java here. So, this is the hole and with the final notes.

## (Refer Slide Time: 33:12)

<!-- image -->
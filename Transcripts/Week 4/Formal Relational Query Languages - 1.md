<!-- image -->

## Database Management Systems Professor Partha Pratim Das Department of Computer Science and Engineering Indian Institute of Technology, Kharagpur Formal Relational Query Languages/1

Welcome to week 4, module 16 of Database Management Systems course in the  IIT  Madras online B.Sc program. (Refer Slide Time: 0:30) TECH OF

<!-- image -->

In the week last, we covered a lot of features of the SQL language starting from practice of the basic  query  structure  to  nested  queries  and  data  modification  and  joins,  views,  transactions integrity constraints, data types authorization and finally, also dealt with some advanced features of SQL which deal with the procedural interface of the procedural components in SQL functions and procedures and finally, discussed triggers in SQL.

So, with that, in week 3, we have kind of concluded the discussion on the SQL language for now, maybe some specific aspects will take up later on, but we will now slowly move on to going towards the modeling of the database and towards the design of the databases.

## (Refer Slide Time: 1:39)

<!-- image -->

So,  in  this  module,  we  talk  about  relational  algebra.  Overall  as  I  said  that  there  are  3  formal relational query language systems relational algebra, which is procedural algebra based and there are  2  calculi,  tuple  relational  calculus  and  domain  relational  calculus  both  of  which  are  nonprocedural and predicate calculus based.

(Refer Slide Time: 2:31)

<!-- image -->

Now, for relational algebra, we have relations and this was created by Edgar Codd in IBM in 1970 is a procedural language it has to write relational algebra expressions to mean which shows the operations to be done, not it is not declarative in that way, it does not describe the result, but it describes a processes or operations that you do with the relations with using the six operators listed here. And the operators are unary or binary and it will always result in a new relation.

(Refer Slide Time: 3:19)

<!-- image -->

So,  you  know  by  now,  the  semantic  meaning  of  these  operations,  the  select  operation,  the notation is as you can, as you have already seen, where p this condition is called the selection predicate  or  the  condition  on  which  the  selection  is  happening.  So,  if  I  write  in  set  theoretic notation, which is what we will need more as I go into the calculus.

Then we have the collection of tuples t such that t belongs to r, it is a part of the relation and it satisfies this predicate p(t), there could be different types of conjunction, disjunction, negation and those different components could be attributes or constants and comparison can be done in. So, this kind of example, you already know.

Here is another example showing you based on the data of A=B, A=B, this being these 3 and D&gt;5, D&gt;5, I think this example we had seen earlier also. So, that retains this one and this one. So, this is a select operation. Now, you have to start, you know understanding and practicing it from  an  algebraic  mindset  because  we  are  going  to  use  this  to  build  more  and  more  on  this algebra.

## (Refer Slide Time: 5:05)

6

<!-- image -->

Project operation which takes out a set of specified columns, it is very simple, but certainly when it takes out columns, it is possible that some tuples will become, will occur more than once they will  be  duplicates.  And  since  every  relation  is  a  set  now  not  a  multiset  like  SQL,  so  the duplicates will be removed in every relational algebra operation. So, this is a project operation.

(Refer Slide Time: 5:35)

<!-- image -->

Then we have union operation which is simple union of two sets, r union s is t belongs to r or t belongs to s and this is an inclusive or, which means that it can belong to both, but for the union to  be  defined  the  conditions  are,  that  both  of  them  must  have  the  same  arity  that  is  the  same number of columns or same number of attributes and columns must be compatible, which means that the corresponding column in r and s must be of the same type, one column is integer other column is varchar, I cannot take a union.

That  is  not  that  will  not  be  admissible.  So,  here  is  an  example,  which  you  have  seen  several times. So, finding out courses taught in Fall 2009 semester as well as Spring 2010 semester. So, you take out courses in Fall 2009, take out the course\_id from that courses in Spring 2010 take out the course\_id, do a union there is only one arity only one course\_id the same type to a union we will get that result, a simple operation.

(Refer Slide Time: 6:56)

<!-- image -->

8

Naturally,  the  other  overset  operations  which  you  have  already  seen  is  difference,  so  that  t belongs to r and t does not belong to s, the same compatibility is required without that we cannot work  in  this  case.  So,  example  is  to  find  all  courses  taught  in  Fall  2009  but  not  in  semester Spring 2010.

## (Refer Slide Time: 7:26)

<!-- image -->

Intersection operation is finding out those tuples which belong to both. So, again the conditions is, they must have the same arity, they must be compatible in terms of type and we may note that intersection is expressible in terms of difference. So, I have r, I have s, this is r, this is s. So, I can do r-s, r-s is this part then I do r minus this part.

So, from r I take out this part. So, from this entire of r I take out this part. So, what I am left with is  this  part,  which  is  r  intersection  s.  So,  basically  the  point  is  that  they  are  not  independent operations one can be expressed in terms of the other, but having both helps in terms of writing queries quickly.

2

## (Refer Slide Time: 8:30)

<!-- image -->

The  Cartesian  product  we  have  discussed  at  depth.  So,  we  assume  for  Cartesian  product  in relational algebra that the attributes are disjoint, that is the same attribute does not occur to both relation.  If  they  are  not  disjoint,  then  we will  use  renaming  to  make them  disjoint  in SQL  we made those implicit by as and so on. But in algebra we will simply assume that they are not having the same name if they are there are some attributes which have common name which are common between r and s will make them distinct.

(Refer Slide Time: 9:18)

5

<!-- image -->

So,  we  need  a  way  to  rename.  So,  if  we  have  renamed  is  the  row  operator,  if  we  have  a expression  relational  algebraic  expression  E,  so  it  is  a  relation.  So,  I  can  give  it  a  new  name which is x and these are the names of the attributes. Now, it is a selective choice, I can rename everything I can rename part of it, but obviously what needs to be maintained is if I am using n attributes here, then it means that what E produces is an unary result.

If I have, E has 5 attributes, and here I am giving 3 attributes or 6 attributes, that is not going to work. So that the returns the result of E under the name x with the attributes renamed to A1 to An. So, this renaming is kind of a completeness process for the relational algebra, so that I can in any situation, I should be able to compute the Cartesian product. Now, obviously, there could be other extensional operations also.

<!-- image -->

8

So, there is one operation, which we did not talk of, in terms of SQL. We talked of, for example, the other extensional operator we talked of was joint. So, we will talk about joint. But these are kind of derived operators, the operator that I am going to discuss now is known as the division operator.  So,  it  is  a  very  interesting  operator.  So,  let  me  first  take  a  couple  of  examples  on division and then come back to this result, this formulation.

(Refer Slide Time: 11:37)

<!-- image -->

So  what  I  am  trying  to  do  is  divide  one  relation  say,  the  relation  r  here  with  relation  s.  The meaning of that division is now naturally, the division is possible, if the attribute or attributes that you have in the s are also present in r. So you divide based on those attributes. So here that correspondence is between module and subject, assume that they are the same category.

Now what you do is, like, what does division do, say if I divide 15 by 3? I find out how many times 15 goes in 3. Say, so the result is 5, so it is a 3, 3, 3, 3, 3 5 times I do, I get 15, similar concept.  So,  this  dividing  relation  is  a  table.  I  want  to  find  the  existence  of  that  table  on  the corresponding  attribute.  So,  that  the  values  on  the  remaining  attributes,  the  values  on  the  r-s attributes are same. That is dividing.

So, here it is pathological, because it is only one entry is there. So, this table is prolog. So, I get a prolog here, I get a prolog here. Now, since there is only other attributes, this is R-S, is Lecturer, there is only one other attribute. So, obviously, it will be the same. So, my result is green, my quotient is green, and Lewis, green and Lewis. So let's, you know, add one more tuple here and see what happens.

(Refer Slide Time: 14:06)

K

<!-- image -->

6

So, now I have this is corresponding this is R-S. Now, we have a table, which is databases and prolog. Remember the condition I am dividing, so I need two things, one is on S attributes, I must get this instance. And on R-S attribute, I must have same value. So, I have two tuples here. So, what do I see them? I see them let's if we, if we numbered these tuples 2, 3, 4, 5, 6 where do we see them 2 and 3, 2 and 5, 2 and 3, 2 and 5, 4 and 3, 4 and 5.

These are the possible pairs, which are it could be considered the instances of S. Now, if you see 3 and 2 and 3, 2 and 3, I have this table, but these values are different, R-S values are not same brown and green. So, 2, 3 is not acceptable. If I take 2 and 5, I have database prolog. So I get a subset of, do not look at consecutivity because you know, ordering is immaterial.

So, I've to get a value databases here, I get a value prolog here, but this is brown, this is Lewis not same will not work. Let's say 4 and 3, 4 and 3. Database, prolog, green and green, great. So, this will work. Let's take 4 and 5 database, prolog, green and Lewis this will not work. So, what finally  survived  is  4  and  3,  4  and  3.  So,  green  is  the  result.  This  is  this  indeed  is  a  division operator. So, if you think carefully, what does the division tell me is green is associated with all instances in S, green is associated with all instances in S. So, it is basically a for all kind of sense that comes in here.

(Refer Slide Time: 17:17)

<!-- image -->

Let's take some more examples. I will go back to the formal definition. Do not worry. So, here is a table A. So, these are the Bs, this is A-Bs and there are the different instances of B. So, one is p1, p2. p2 is here, p2 is here, p2 is here, p2 is here, there is only one other attribute and here is only one as well. So, all these four are candidates, so they go in the output.

Now, consider p2, p4. So, you have p2 here, you have p4 here, p2 here, p2 here, p2 here, p4 here. We have to see which p2 p4 pair has the same value, this p2 p4 has s1. This p2, p4 does not work, this p2, p4 does not work, this p2 this p2, p4 works s4. So, we have s1 and s4 as I divide A by B2.

If we divide A by B3 p1, p2, p4, p1, p2, p4, p1, p2, p2, p2, p4. So, you can clearly see p1, p2, p4 all of them has s1. You take p1 with p4, anywhere else, you do not have the same value. So, p1 p2 p4 cannot have the same value. So, in this case the result is s1. So that is that is the kind of the semantics of division.

(Refer Slide Time: 19:28)

<!-- image -->

So, let us say we have this relation, A and B, and these are the values and say A is a customer name and B is a branch name. So, 1, 2, I have 1, 2 here where there is alpha and I have 1 and 2 here, where the value is beta all other 1, 2 pairs are different. So, if this is a customer name and if this is branch, branch name, this is a customer name and this is a branch name, then what does it mean?

That this  customer alpha has  an  account  in  every branch.  Similarly,  the  customer  beta  has  an account in every branch. So, if we asked to find customers who have an account in all branches of the bank, then I can simply take the branches table and divide the account holding table by that whatever is a quotient are those set of customers. That is the power of the division operator.

(Refer Slide Time: 20:50)

K

<!-- image -->

6

This example is similar just to show you multiple stuff, students who have taken both A and B courses  with  instructor  1,  find  students  who  have  taken  all  courses  given  by  instructor  1.  So, what we are doing with A and so, D E, these are the columns on which I am doing the division and looking for A1 B1. I have A1 here, A1 here, A1 here.

Now, what A1 B1 matches in the rest is this one. Similarly, here at this one, no A1 B1 matches with the others. So, this is the result of this division, which gives me the students who have taken all courses that are offered by instructor 1. So, this is the, I mean I particularly work through a number of examples here, because I feel division is a little bit more complex operation and it is very useful.

2

## (Refer Slide Time: 22:21)

<!-- image -->

## Division Operation

- The division operation is applied to two relations
- attributes of R that are not attributes of $
- The result of DIVISION is a relation T(Y) that includes a tuple t if tuples tR appe t, and with
- tR[X] = ts for tuple ts in $ every
- For a tuple t to appear in the result T of the DIVISION , the values in t must appe combination with every tuple in $
- Division is a derived operation and can be expressed in terms of other operations
- TR-s,s(r))

<!-- image -->

So, let me get back to the basic definition is if we have a set of attributes, Z and X and let Y be difference of Z-X. So, Y will be the attributes of the quotient, the result of the relation T that includes a tuple tR appear in R with tR[Y]=t and so, you have a tuple t, which is got Y attributes, got X attributes.

So, this part is called t[Y], where Y is the total minus X, Z-X and this is called t[X]. So, we are saying that we will take that tR[Y] where tR[X] is equal to ts for every tuple in S, the whole table.  This  part  of the whole table has to come that is a formal definition of this and you can check  out  for  a  tuple  to  appear  in  result  t  of  the  division  the  value  t  must  appear  in  R  in combination with every tuple in S.

So, now it will not be difficult to work out that division is not an independent operation, but you can actually get the division by using the other relational algebra operators that you have. So, you first compute this which is  R-S of r which means the result table, the possibilities of the result table and these are possibilities of the result table you cannot have a result which is outside of this, this part.

And you take a product with s. So, you are generating all possible combinations, not all of them are there. Then you take out R-S s of r. So, you take out which exists. So, then you project that on  the  R-S  remaining  and  subtract  from  the  origin  which  will  give  you  the.  So,  if  you  have difficulty  in  understanding  this  expression,  I  would  suggest  that  you  work  through  a  given example  step  by  step  and  you  will  be  able  to  understand.  If  after  that  you  will  still  do  not understand do let us know we will discuss, but this is division is a very very powerful operation to be done besides the four I mean six basic relational algebra operators and division.

(Refer Slide Time: 25:58)

5

<!-- image -->

(r *ß)

Obviously, we have the joint which you already know written in this form where you can, you actually do a cross product and then you evaluate a condition on the attributes which is called a theta predicate of the join. Now, this theta predicate could be equality of common attributes on two tables then it becomes a natural join.

So, there are varieties of joint which can be written in this form. It is really not theta, I am sorry. So, join theta r, s is basically you take the Cartesian product and you do the selection based on the theta condition. So, this is called theta join, if theta is equality, it is called equal join. If theta enforces the values on the identical columns between r and s to be equal it is called natural join and so on so forth.

So, all of them can actually be written in terms of the selection and cross product and therefore, we do not again say that joint is an is an independent operation, but it is more like a derived operation. So, we conclude here on this module, so, we have taken a little bit in depth look into the relational algebra with some examples. Thank you very much for your attention and see you in the next module.

<!-- image -->
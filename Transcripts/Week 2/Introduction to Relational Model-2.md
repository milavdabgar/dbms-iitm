<!-- image -->

## Database Management System Professor. Partha Pratim Das Department of Computer Science and Engineering Indian Institute of Technology, Kharagpur

## Introduction to Relational Model/2

Welcome  to  module  7  of  database  management  systems  course  in  IIT  Madras  BSc  online program. OF

<!-- image -->

(Refer Slide Time: 0:38)

In the last module we have got started to talk about specific details of relational model, in that we introduced the basic notions of attributes their types, relational schema and instance, and keys and their categorization, and we just get talked about a glimpse of the languages that relational algebra will relational system will have.

## (Refer Slide Time: 1:02)

<!-- image -->

So,  these  are  the  list  of  operators  that  we  will  specifically  discuss  one  by  one.  So,  let  us  get started.

<!-- image -->

So, we talk about relational operators. Now, before I start talking of the operators I would like to remind you of something that I have already mentioned earlier is that, remember always that a relation is a set, so the ordering of elements or the ordering of rows and tuples in a relation is inconsequential, I can order them in whatever way I want.

So, if you look at the relation on left having two attributes A, B and 4 different tuples a1 b1, a1 b2, a2 b1, a2 b2, on the right you have them ordered in a different way, but it is the same set, so they are same, these relations are same, they are these instances are equivalent these instances are identical.

Second, a set must always have its elements as unique, so all rows and tuples must be distinct. So,  on  left  I  have  a  relational  instance  where  a1  b1  is  duplicated,  so  is  a1  b2,  these  are  not allowed. So, only one of those will have to be there, so what we show on right a1 b1 and a1 b2 is the correct relation the left one is wrong relation it will never exist. So, keep these two in mind as we discussed operators these principles will regularly periodically come into effect.

(Refer Slide Time: 3:11)

5

TEC

<!-- image -->

<!-- image -->

So,  we  talk  on  different  operators,  first  is  called  the  select,  and  as  the  name  suggest,  select operation  is  to  select  a  subset  of  rows  from  a  relational  instance  which  satisfy  a  particular condition.  So,  if  you  look  at  the  select  is  written  in  terms  of  this  notation,  you  know  Greek symbol, and then it has as a subscript a Boolean condition, which is a condition that every tuple being  selected  from  the  original  relational  instance  must  satisfy  and  this  is  the  name  of  the relational instance. So, this is your select is.

So, what does it say? It says A = B, this is the original relation r, that is I will take only those tuples where A is equal to B, that the first part of the condition, and then say and D &gt; 5, so even within that I will take only those where D &gt; 5. So, let us see let us try A equal to B, so these two will have to be identical, so this who is a candidate, this is a candidate, this is a candidate, this is crossed out because alpha beta A is not equal to B.

So, out of these three that we have got from A equal to B, since I have a conjunction, since I have and I have to check if D &gt; 5, D is greater than 5, D is not greater than 5, cancel out, D &gt; 5. So, finally I am left with two tuples, this and this, which is my selection result. What would have happened if instead of this if I would have or, instead of this if I would have or, then if I have A = B or D &gt; 5, A equal to B will take this, take this, take this, D greater than 5 will take this, take this and take this, and it is or, any one of them condition to satisfy.

So, if I do a select of A equal to B or D greater than 5 of r, then I will get the whole r itself, that this possible, but here it is and, so I got a smaller relation, so that is a selection is a very very important, you can select one specific tuple out or you can take a set of tuples out. Let us, go to the next operation.

(Refer Slide Time: 6:21)

<!-- image -->

<!-- image -->

The next operation is called projection, that is, it selection was taking out few rows horizontally, projection will take out some columns and if you take out a column you take out the column as a whole. So, projection is written in terms of by pi, pi here and you would list the columns that you want to project out, that you want to keep, anything that you do not right here is taken out and then the original relational schema, so you have A, B, C and you are doing projection on A, C, so this B will be simply erased out.

If you erased out B then this is what you get, alpha 1, alpha 1, beta 1, beta 2. Now, remember that principle that every row in a relation has to be unique. So, I cannot have entries like this, so one of them will get deleted and what I get is this relation. What will happen if I do pi A, B r, say pi A, B of r, what do I get? This is gone, now I will get this and you can see that all of them incidentally are unique, so there will be no removal of row that we will happen, what will be pi A of r? Only alpha and beta, so it is A, so that is the basic principle of projection. So, we know horizontal cuts, we know vertical cuts. Let us, go to the next one.

<!-- image -->

This is more classical set theory operation that is union. So, if two relations have identical set of attributes, then you can take their relation, if they take their union, I mean obviously if this is AB attribute AB and that is attribute CD you cannot do any union, AB and AB. If you are a union what will happen?

Then all tuples, it is just that after this table you put the rest, and then uniquify unification is required, because here if you do union, you will find that this and this will come twice because we are putting them together. So, you will have to uniquify and have it only once, this is your union. Very simple. Next is difference.

(Refer Slide Time: 9:28)

<!-- image -->

There  is  a  difference  set,  I  have  a  set  r,  I  have  a  set  s,  so  this  is  my,  what  is  difference? Differences what are there, what is there in r but not in s. So, you take out those things in s which are already in r. So, this is their, this is their, so you have to take out this element, this row and you are left with, so it is basically you can say that if you have, if you take the intersection of r and s and remove that from r then you have r - s, simple. But this again is set theoretic, other than select and project that we have seen so far the other two union and set difference a simple set operations.

(Refer Slide Time: 10:44)

<!-- image -->

Now,  you  have  intersection  as  well  tuples  which  are  common  to  both,  now  intersection  and difference are not independent, because we know that one can be written in terms of the other. So,  if  we  have  difference,  even  without  the  intersection  operator  you  have  the  intersection because it is this, very easy to see, so it is r - s is this, this is r, this is s, may if you do r - (r - s) that is from r if you take this out, then what will be left is this part which is intersection, so that is simple set algebra. OF

(Refer Slide Time: 11:28)

<!-- image -->

When you have Cartesian product again a set operation that is you know take the columns of this take the columns of this make all possible combinations. So, you have 2 tuples here, you have 4 tuples here, so you have 2 cross 4 is 8 tuples you will get, 1, 2, 3, 4, 5, 6, 7, 8. So, if you really see that all possible pairing of the tuples in table one and table two are present in the result which is the Cartesian product of the two relations.

And it is easy to see that if you take a Cartesian product, then you can get back, how do you get back the relation original relation? So, I can say that r is equal to we take Cartesian product of r and s and or rather I will write it as capital R, to mean that is a relational schema of R. So, if I take the Cartesian product and again project it on AB, I will get back to relation R. Similarly, for s, s is my new I mean I am using capital here to mean that R basically is A, B, S basically is C, D,  E  those  are  the  schema,  because  what  we  have  in  r  and  s  lower  case  are  basically  the instances. So, this is the Cartesian product which was a set.

(Refer Slide Time: 13:16)

K

<!-- image -->

6

Now, you get into little nuances, because suppose between the two relations that you want to do Cartesian product with suppose there is a column one or more columns, which have the same name, now in the result relation you cannot have this because you cannot have two attributes by the same name, so what is done is very simple you just uniquify the name. How do you uniquify? You make this B as r dot B and make this B as s dot B.

So, when you see that between the two relations there is one or more attribute which have which are identical, then you just qualify the name of that attribute with the name of the relation, this r and s are different, so their names are different. So, r dot B and s dot B are different. And then you do the normal Cartesian product.

So, only thing is you can you will have a different set of names, you will still have 5 attributes, but you will have different names for them. So, this is kind of a little bit additional trick that you need for the relational algebra, which you do not need in the set theory, because in set theory you do not talk about unification of attribute names.

(Refer Slide Time: 14:42)

<!-- image -->

Now, as you do that, two things one is how do you change this name? Is one question, other is maybe you have done this r.B and s.B and you are not happy you want to call r.B as say p and s d.B as q, so how do you rename something? So, what you can say is you can and the renaming is also required because you may want to rename a relation because suppose you want to take you want to do a self-cross product r cross r.

Now, you see it bring a self-cross product you cannot use the earlier principle because A, B cross you have A, B, now by qualification r.A and r.A, r.B and r.B they do not uniquify, because both relations are same. So, you can change the name of the relation, call it s, then the unification has happened, and in this way you can easily go around using any names.

NI -

(Refer Slide Time: 15:59)

K

<!-- image -->

6

Now, naturally like the set theory, you can do you can compose any number of operations. For example, here what we are doing is we have relations r and s, we have done a this is a Cartesian product and then we have done a projection, I am sorry then we have done a selection A equal to s,  so  this  is  the  result  of  the  Cartesian  product  and  then  you  say  this,  this,  this,  will  survive because  in  those  A  is  equal  to  s,  everything  else  is  removed.  So,  you  can  do  any  number  of composition of operators. So, it is like just building up the algebra.

(Refer Slide Time: 16:49)

<!-- image -->

Now, we get a new operation which is more specific for relational algebra, let us say R and S are relations on schemas capital R and capital S. The natural join, mind this word, the natural join, Cartesian product in general will also called join, natural join of R  and  S is a relation on the schema R union S, that is you have the attributes of R and you have the attributes of S, so that you take every pair of tuple from instance R and every tuple for instance S and so that is a kind of a Cartesian product, so you are making combinations, but there is more to it.

If tr and ts have the same value on each attribute in R ∩ S, that is if there is one attribute which is common between R and S, then tuples which have identical value on that attribute will only be taken in the natural join, that is not true for Cartesian product, in Cartesian product to take all possible values. 0

<!-- image -->

And therefore, we if the for attributes that are in R ∪ S we are using the qualified them r.A, s.A, r.B, s.B, here no, if two attributes have identical name between R and S then you only keep those tuples which have identical value on those identical attributes, that is what it is saying, example. (Refer Slide Time: 18:54)

So, look at these carefully, this is r, this is s, so you know this is capital R and this is capital S, so R ∪ S is A, B, C, D, E; R ∩ S is B, D. So, I have two identical column names, B and B, D and D, so when I do the join, I have 5 records here, I have 5 records here, I should get 25 in the

Cartesian product, but here know no, when I pair with this tuple any tuple here I have to make sure that the B and D values are identical.

So, I will be able to pair this with this and with this, but not with this, that is the first record or first row on the left on R can be paired with the first row on S, because B have identical values D have identical values, it can be paired with the third because they have identical values, it can be not  be  paired  with  anyone  else.  So,  you  have  this  resulting  from  that  pairing,  the  next  one resulting from that pairing.

If  you follow this all through is what you get the natural join on this. So, what will happen in natural  join?  r.B  and  s.B  necessarily  similarly  r.B  and  s.D  these  two  will  necessarily  have identical  values  in  the  columns  because  that  is  how  you  are  choosing,  1  1  you  have  chosen, similarly  let  us  say  if  you  take  the  next  one,  2a  there  is  not  2a,  so  this  entire  thing  will  not produce anything, take the next one, you have 4b, there is no b here, entire thing will not have anything, then you have this which has 1a, so again you will have two of this, then you have delta which is 2b, so 2b will only have this, this right now.

Now, necessarily on both these r dot B and s dot B you will have identical values and on r.D and s.D will also have identical values, this is by the way of making the choice, so it is redundant to keep both, so you remove 1 from the table and once you remove you do not need to call it by a qualified name, so that is exactly what how you get this table, so, in this table you do not get 2B's or 2D's that are identical.

So, if you look at what you have done, you have done a cross product, then on identical column names r dot B and s dot B you have checked if the values are equal on B equal on D inclusive, they will have to be equal on both, you have selected only those tuples, so then you have got 7 columns of that you have taken the distinct 3 and of the duplicate ones you have taken just 1, removing the other two, you have 5. We will see that this is  a very, very powerful  operation which we will use rampantly, rampantly I reiterate across different query processing. So, you will have to practice and learn this really well.

(Refer Slide Time: 23:38)

<!-- image -->

So,  that  was  about  the  relational  operators,  now  other  than  that  there  are  some  aggregate operators. So, relational operators you will have to remember that the operators always take one or two relations, some operators are unary, like select, like project, so they take one relation and give  you  one  relation,  some  are  binary  like  union,  intersection,  difference,  Cartesian  product, natural join, they take two relations and give you one relation.

Remember that the input will always have to be relation the output will always be a relation. And it  is  possible that in some cases you might get an empty relation also, relation which does not have any tuple, so we will go back and say there is no answer. Now, there are these are the basic relational operators, then we have a set of what is called aggregate operators, the concept of the aggregate  operators  is  that  you  take  a  relation  again,  then  based  on  one  or  more  columns  or certain conditions, you do an aggregation, so kind of you have a table A, B, I say that I want to do an aggregation on column B, what is that aggregation? I want to make a sum.

Of  course,  the  type  of  that  column  has  to  be  such  that  the  agree,  that  particular  aggregate operation is possible. So, I can do a sum on this column to get 10, I can do a max on this column to get 5, like this, you can do a aggregation on a relationally operated file also, for example, I will say that well, I want to do is I want to aggregate values that are more than 2, so I will take this  r  and  then  do  B  greater  than  2r,  what  does  this  give  me?  This  gives  me  a  new  relation, relation which does not have this, and on this I do a sum on B to get 8.

So, two main differences between the relational operators and aggregation operators, relational operators are always dealing with certain structure tuples and so on and always will produce a relation, whereas aggregate operations will do an a typical aggregate operations a numerical as you can see all of these are numerical operators, they will necessarily take one or more columns, the tuples and do some aggregation arithmetic on those and they will produce a single value, they do not produce a table, settle, because the sum of your budget or your maximum salary of an employee or the average execution time of a query and so on these are the different aggregations that can happen, does not will not produce a multiple value.

So, in aggregation you input is a table and the output is a single value, so that is how these are distinguish,  aggregation  operators  are  not  fundamental  to  pure  relational  algebra,  because relational algebra only talks about relation, but these are as we will see, will come as additional operators  as  we  write  relational  algebra  in  the  form  of  SQL  kind  of  language  because  they become very handy and we will show you how to do those in time.

(Refer Slide Time: 28:40)

| Symbol (Name)       | Lxample of Use                                         |
|---------------------|--------------------------------------------------------|
| (Selection)         | salary                                                 |
| (Cartesian Product) | Ihe sme nanc                                           |
| (Union)             | Output the union of tupks trom the tuv input relations |

<!-- image -->

So, these are summary, this is just for your quick reference till you get totally comfortable with these operators which we will have to soon get comfortable with.

(Refer Slide Time: 29:25)

<!-- image -->
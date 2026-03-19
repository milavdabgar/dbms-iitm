<!-- image -->

## Database Management Systems Professor Partha Pratim Das Department of Computer Science and Engineering Indian Institute of Technology, Kharagpur Formal Relational Query Languages/2

(Refer Slide Time: 0:20)

<!-- image -->

Welcome  to  Module  17  of  Database  Management  Systems  course  in  IIT  Madras  online  BSc program. From the last module, we have started a little formal discussion about the foundational mathematics of relational database. We have discussed about relational algebra and its operation in some depth.

## (Refer Slide Time: 0:45)

6

<!-- image -->

We  will  continue  on  that  stream,  but  just  take  a  quick  look  into  the  calculus-based  query languages through the equivalence with relational algebra, we do not intend to really go deep on the  calculus  because  first  of  all  for  two  reasons  one  is  the  calculus  needs  more  in-depth foundation on the results of predicate calculus, because they are based on predicate calculus and the other is they are all equivalent to relational algebra. So, just following one model on which particularly SQL is based would be quite okay for our future discussions.

(Refer Slide Time: 1:35)

5

<!-- image -->

## Formal Relational Query Language

- Relational Algebra
- Procedural and Algebra based
- Tuple Relational Calculus
- Non-Procedural and Predicate Calculus based
- Domain Relational Calculus
- Non-Procedural and Predicate Calculus based

But  it  will  be  good  for  you  all  to  know  that  these  kind  of  models  exist  and  what  is  their interrelationships  with  between  themselves.  So,  the  first  one  in  the  formal  relational  query language we have already done the second is what you get second and you know, just glimpse of the third will take.

<!-- image -->

Now, before I get into tuple relational calculus, the first language or first model, let me just take a  quick  look  at  predicate  logic  because  I  am  not  sure  how  much  of  predicate  logic  you  are familiar with, but few basic definitions are required for the entire of this calculus.

(Refer Slide Time: 2:19)

<!-- image -->

So, predicate logic or predicate calculus, these are 2 names interchangeably used in some case places  is  called  logic  some  place  is  called  calculus,  is  an  extension  of  propositional  logic  or propositional  calculus  or  what  more  simply  is  called  Boolean  algebra.  So,  what  we  have  in Boolean algebra?

In  Boolean  algebra,  we  have  say  variables,  Boolean  variables  or  propositions,  which  can  be either  true  or  false  either  true  or  false.  And  we  have  a  few  operators,  three  operators;  say something like this and, or, not and we using them we can write any number of formula and once the truth value is assigned to these Boolean variables, we evaluate them to get a final truth result.

So,  that  is  the  basic  formulation  of  Boolean  algebra  or  propositional  logic.  So,  you  have propositions  or  variables  which  take  true  or  false  value  and  based  on  that  you  have  a  result.

When it comes to predicate calculus, you have, you add a concept you still have propositions, but you add the concept of predicate and quantifiers to better capture the meaning of the statements which cannot be captured adequately appropriately precisely in terms of the propositional logic.

So, that is the extension. So, that is these are the key things to know, predicate and quantify plus the  propositions  A,  B,  C,  D  all  variables  which  could  be  true  or  false.  Now,  tuple  relational calculus and the domain calculus are completely based on predicate calculus. They are basically certain forms of predicate calculus.

<!-- image -->

(Refer Slide Time: 5:13)

K

<!-- image -->

Let us take a quick look at what these predicates and quantifiers are, you may know but it is always good to discuss for completeness. So, suppose I make a statement that x is greater than 3. If you look into the statement, there are 2 things in this; one is the variable x, I do not know what it values what is the variable normal variable which can take some number 17, 23, 112 and so on.

And the second part is a property, second part is actually a property. So, it says that is greater than 3. So, I have a, I have a variable and I have a property. Now, this part the property is called the predicate. It refers to the property that the subject of the statement x can have, may have or may not have.

So, what I do is we denote this typically in this kind of a notation, where P is the predicate such that and x is the x is the subject of that predicate x is a variable. So, that this predicate once I put a value to x this predicate is evaluated and becomes a proposition. So, P(x) is a predicate but P(5) is a proposition which has a value true or false. P(2) is a proposition which has a value true or false.

Naturally  if  my  predicate  P(x)  is  x  greater  than  3  then  P(5)  the  proposition  P(5)  is  true  the proposition P(2) is false. Alternatively, you can think about a predicate as a function because it tells you the truth value of P(x) at the assumed value of x. So, you have predicates, you can again write  conjunction,  disjunction,  negation  with  these  predicates,  you  have  a  predicate  calculus expression.

Once you put values truth value,  once you  put  the  different  variable  values  x,  y,  z  whatever. They become propositions. So, it becomes now from a predicate calculus formula it becomes a propositional calculus formula, a Boolean expression which will evaluate by the rules of Boolean expression and you finally have a truth value, the difference being that now, you are associating properties  with  variables  which  are  not  necessarily  Boolean  which  are  not  necessarily  binary, which can come from any domain and can have any property and a combination of those keeps you to capture the truth.

So,  this  obviously  subsumes  the  entire  of  the  propositional  calculus  but  has  lot  more.  Now, suddenly it is not limited to one variable. So, I can have any number of n number of variables for a predicate and I can denote them and if a variable if a predicate does not have a variable, it is a proposition. (Refer Slide Time: 9:36) 2

<!-- image -->

The predicate logic also has alongside the predicates they have quantifiers. Quantifiers are used to talk about properties that hold over the entire domain of discourse in a certain way. Now, I said x is greater than 3. So, what is the domain of discourse for x, I can say it is a natural number. It is a natural number. If I said it is a natural number, then it is the whole of the natural numbers. Now, there are certain properties, which I want to know, whether it holds, how it holds over the entire domain of discourse.

## (Refer Slide Time: 10:31)

<!-- image -->

## Module 17

Objectives &amp;

Predicate Logic

<!-- image -->

Madras

## Module 17

Das

Predicate Logic

## Universal Quantifier

Universal Quantification: Mathematical statements sometimes assert true for all the values of a variable in a particular domain, called the don

- Such a statement is expressed using universal quantification.
- asserts that P(x) is true for all values of x in this domain
- The domain is very important here since it decides the possible value'
- Formally; The universal quantification of P(x) is the statement P(x) in the domain'
- The notation VP(x) denotes the universal quantification of P(x) . He universal quantifier . VP(x) is read as for all x P(x)"
- Example: Let P(x) be the statement "x + 2 &gt; x

## Universal Quantifier

Universal Quantification: Mathematical statements sometimes assert true for all the values of a variable in a particular domain; called the don

- Such a statement is expressed using universal quantification.
- The universal quantification of P(x) for a particular domain is the pr6 asserts that P(x) is true for all values of x in this domain
- The domain is very important here since it decides the possible value'
- Formally; The universal quantification of P(x) is the statement P(x) in the domain'
- The notation VP(x) denotes the universal quantification of P(x). He universal quantifier . VP(x) is read as for all x P(x)"
- Example: Let P(x) be the statement 'X+ 2&gt; X

<!-- image -->

So, the first quantifier is known as a universal quantifier where it has a property which has to hold over the, why is it universal, because it talks about a property that has to universally hold true over the whole universe, which means it must be true for all elements in the domain. Only then, that quantification is true. So, the way I say so, it is written in terms of this notation for all.

So, I said this is a quantified formula for all x P(x). Now, P(x) depending on the value of x P(x) may be true or may be false individually. So, what is for all x P(x), it means, if I take any value in the domain of discourse, I can specify that domain or it can be implicitly known if I specify any value  in  that  domain.  And  for  that,  if  P(x)  is  true,  then  this  entire  statement  is  true.  This becomes a new predicate.

So,  I  say  that,  well,  I  am  looking  at  a  statement  x+2&gt;x.  If  that  is  my  P(x)  does  this  hold? Obviously, no matter what you take, the value of x as any real number, natural number x+2 will be always greater than x. So, I say that for all x P(x), I say my predicate M(x) is x is mortal. Whether domain of discourse is a population of the world, human population of the world, what is  for  all  x  M(x),  it  is  true;  which  in  proverbial  terms  we  say  men  are  mortal,  means  human beings are mortal. So that is a universal quantifier. Let us say that we were saying that earlier we saw that P(x) is x&gt;3. Now, what is for all x P(x)?

Over the domain of discourse, natural numbers. This quantified formula is not true. Well, it is true for 4, true for 5, true for 1000. But is not true for 3, true for 2, true for 1 and so on.

So, for all x P(x), x&gt;3 is not true. But if I say my domain of discourse is all positive numbers having two or more digits, let us say my domain of discourse is all positive numbers having two or more digits then P(x), x&gt;3 for all x P(x) is true. So, you can see that the truth is always with respect to certain domains. And with respect to that, we are saying that if it holds universally, then it is universal true otherwise it is false.

(Refer Slide Time: 15:03)

TEC

8

<!-- image -->

So, let us move on, the other is existential quantifier which is on very similar lines where, where it says that does there exist at least one value in the domain of discourse where P(x) is true, it is written in this way exist there exist x P(x). So, if I if we go back to P(x) being x&gt;3, then for all x P(x)  assuming  the  domain  of  discourse  is  natural  numbers  for  all  x  P(x)  was  false,  but  there exists x P(x) is true because it is true for 4, true for 5 so at least one.

So, these are the two kinds of quantifications which we often need to model there are other kinds of  quantifications  also,  but  not  so  popular  or  rather  to  put  it  in  different  terms,  they  are expressible  in  terms  of  you  know  these  quantification  and  the  predicate.  So,  we  move  from propositional  calculus  to  defining  predicate  and  quantification  and  that  model  is  what  is  the model for it.

## (Refer Slide Time: 16:14)

<!-- image -->

Is  what  the  tuple  relational  calculus  is.  So,  in  tuple  relational  calculus  all  that  we  do  is  very simple we say that the formula or the relation is basically a set of t, tuples t where P(t) where P(t) holds  good,  where  this  predicate  holds  good  and  predicate  may  have  various  conditions combinations of and, or, not, it could have quantifiers and so on so forth.

## (Refer Slide Time: 16:53)

| Student   | Student   | Student   | Student   |
|-----------|-----------|-----------|-----------|
| Fname     | Lname     | Age       | Course    |
| David     | Sharma    | 27        | DBMS      |
| Aaron     | Lilly     | 17        | JAVA      |
| Sahil     | Khan      | 19        | Python    |
| Sachin    | Rao       | 20        | DBMS      |
| Varun     | George    | 23        | JAVA      |
| Simi      | Verma     | 22        | JAVA      |

<!-- image -->

Couple of quick  examples,  say  we are talking  about  obtain;  there  is  a  student's  database  here obtain the first name of the students whose age is greater than 21. So, what we are looking for is say if t is the relation then we are looking for the first name is t.Fname. What will have to happen what is the domain of discourse? The truth depends on that; the domain of discourse is a relation student;  student  t  student  t  is  a  predicate  such  that  if  t  is  a  tuple  of  the  student  relation  then student t is true otherwise it is false.

So, this will make sure that this is equivalent to saying in different terms as okay this is already written here let t is an element of truth you could be writing in this way and age is greater than So, t.age is greater than 21. So, that defines this answer to this query, you could write it as a set member, you could also write it like this that in a set of tuples t set of names t such that you are there exist a tuple s with age greater than 21 and t name equal to S name in student. There is different ways of writing the formula means practically the same thing.

(Refer Slide Time: 19:12)

<!-- image -->

8

So, everything that we want to query on can be in this way written in multiple predicate calculus formula. Find the names of all students who have taken the course name DBMS. So, what is that we want? That for every student there is a course taken by the student called DBMS. So, let us look at the second one say s.name for the names. Domain of discourse has to be a student.

Then we say that there exists a course c having the same Id as what the student has taken you know, the domain is getting refined, courses that the student has taken is a s.courseId. So, there exists  a  course  c  having  the  same  Id  and  that  course  has  the  name  DBMS.  And  when  you evaluate the c, you do it in course table.

You could look at it differently; s is a student c is a course. So, the courseId is same and the name is DBMS and the students name matches that is a result t. So, that is basically the way to express in terms of predicate calculus or in this case, the tuple relational calculus. There are other queries.

(Refer Slide Time: 21:07 )

5

<!-- image -->

Let us look at this one. So, there are flights, flight number, starting point, ending point, distance, departure time, arrival time, there is aircraft with ID, aircraft name, cruising range, how far it can go, the certified so there are employees which are certified on aircrafts and the employee details, these are the four tables.

So  the  queries  is  find  the  eids,  employee  ID  of  pilots,  certified  for  Boeing  aircraft,  find  the employee ID of pilot,  this  is  your  final  result,  certified  for  Boeing  aircraft.  So,  you  need  the employee  ID  certified.  So,  you  need  a  certified,  you  need  the  Boeing.  So,  all  these  will  be involved.

Now, the first thing you need is how do you say? How do you find what are the employee IDs that are available for the Boeing aircraft that are certified for the Boeing aircraft? Naturally, these two will have to come together. And what works for that, if you just think the relational algebra way, the natural join between aircraft and certified.

This  will  give  you  a  relationship  between  employee  ID  and  aircraft  name,  which  could  have Boeing.  So  now  you  filter  this  for  Boeing.  You  are  just  interested  in  the  Boeing  part  of  it, nothing  else.  No  other  aircrafts.  So,  filter,  select  on  Boeing.  So,  whatever  will  remain  is  the employee  ID  of  those  who  are  certified  to  fly  eid.  Here  you  have  been  asked  to  find  the employee ID.

If you are asked to find the name, then what you will have to do? You'll have to again, because the name is available in the employees, you'll get the names. So, that is if you look at it in a relational way. Let us look at it in the calculus. It is very simple. In calculus actually, it is easier because what you are looking for are the certified employee IDs, c.eid. c has to be certified, has to come from there.

A has to be an aircraft which has a name Boeing and the certification of the aircraft ID available in the aircraft table and the aircraft ID available in the certification table has to match. That gives you the entire query. So, this is how, I mean, you need to, you need to practice a lot to be able to write this.

(Refer Slide Time: 25:00)

IIT Madras

Module 17

Das

Ohjectives &amp;

Tuple Relational

Calculus

Denain

Ckulls

## of Expressions Safety

- It is possible to write tuple calculus expressions that generate infinite
- For example {t 7t € r} results in an infinite relation if the domain relation r is infinite
- To guard the problem , we restrict the set of allowable express expressions against
- An expression {t | P(t)} in the tuple relational calculus is safe if ever appears in one of the relations, tuples, or constants that appear in P. NOTE: this is more than just a syntax condition
- it defines an infinite set values that do not appear in any relation or tuples or constants in

5

<!-- image -->

There are couple of things examples given round here, we can take them up in tutorials also. Now, so that is tuple relational calculus, it is just logical thinking nothing other than that. One point I would like to mention is before I close is that the you have to make sure that expressions are safe.

What  does  it  mean,  expression  is  safe,  it  means  that  the  result  of  your  expression  cannot  be infinite, it has to be finite, but so, you would say how can that happen? How come I am working with finite sets? How can it suddenly become infinite? It can because for example, I say that this is my predicate, set of tuples t such that t does not belong to relation r.

Now,  that  anything  in  the  world  can  belong  to,  not  belong  to  relation  r.  So,  you  have  to  be careful about that at least, if you have any attribute in the relation which has an infinite domain, then  you  must  be  careful  to  avoid  that.  Normally,  it  will  not  happen  when  you  are  working within SQL kind of situation because it is well taken care of within the SQL itself.

<!-- image -->

The domain relational calculus, I will not go in in detail, as practically no difference between the tuple relational calculus and domain relational calculus except the notation. In the tuple relational calculus, you have variable for the entire tuple club together. In domain relational calculus, every attribute is a different variable. So, you have a Cartesian product of that, which is the, so if I have an  array  tuple,  then  in  domain  relational,  in,  in  tuple  relational  calculus,  I  call  it  t  in  domain relational calculus,  I  will  call  it  the  attributes  x1,  x2,  xn  and  so,  what  becomes  anywhere  you use?  So,  it  is  just  a  different  way  of,  you  know,  syntactically  writing  things,  which  makes  it different conceptually, there is absolutely no difference between the two of them.

<!-- image -->

Now, finally the question is, I mean, the three models are the same. Now, in some cases, we have worked out, you can there is a formal proof for everything what the way you go is, is basically for  every  relational  algebra  operator.  If  you  can  show,  how  do  you  write  the  tuple  calculus expression, then you will know that that is equivalent.

That is, it is similarly for every tuple calculus predicate that is conjunction, disjunction, negation quantification, if you can show what is equivalent in the relational algebra, then you will know that both of them are equivalent. So, just showing you an example here that this is a selection operator B=17 on (r).

So,  we  know  that  in  tuple  calculus,  it  can  be  written  like  this,  and  if  the  relation  has  two attributes in domain calculus, it can be written like this. Now, this is by example, you can try to prove it in general, I am not going into those because, we want to keep closer to practice. These are things that people have worked on and have proven long ago, and you can take that, take that fact.

<!-- image -->

So, all that I have done is for every operation, I have just given one example, to elucidate that, what is the kind of structure that it equivalently takes. So, this is a projection. So, when you take a projection, how you can write it in terms of tuple calculus and so on. But we would not go into the detail mathematical proof of this. The proof is given in the book if you want you can read it up.

## (Refer Slide Time: 29:09)

R=(A,B,€)

Relational Algebra;

TUs

Tuple Calculus:

{ttervtes}

Domain Calculus:

<!-- image -->

<!-- image -->

## Module 17

Partha Pratim Das

Ohjectives &amp;

Denain

Algebra Jnd Calculus

<!-- image -->

## Module 17

Partha Das Pralu

Predicate Logic

Donain

Equivalence of Algebra Jnd Calculus

## Equivalence of RA, TRC and DRC

## CartesianICross Product

R=(A,B)

Relational Algebra;

Tuple Calculus:

Domain Calculus:

## Equivalence of RA, TRC and DRC

## Set Difference

R=(A,B€)

S = (A, B,€)

Relational Algebra;

Tuple Calculus;

Domain Calculus:

<!-- image -->

Module 17

Partha Pratim Das

Ohjectives &amp;

Denain

Algebra Jnd Calculus

Natural Join

S= (BDE)

Relational Algebra;

Tuple Calculus:

<!-- image -->

But  just  go  with  the  fact  that  there  is  equivalence  for  each  and  every  operation  and  their combination between relational algebra and the predicates in the calculus. So, this is for union, set difference, you can even just see through that when you are reading through this slides, the Cartesian product everything natural join.

So, it looks a little cumbersome, when you write down natural join, but you know, you can you can  always  it  is  always  possible  to  write  down  a  natural  join  in  tuple  calculus,  because  it  is possible to write a Cartesian product and the rest of it is just selection under different conditions. Division  too,  though  division  is  not  a  fundamental  operator.  So,  this  is  not  necessary  for  the equivalence proof.

## Equivalence of RA, TRC and DRC

## (Refer Slide Time: 30:00)

K

<!-- image -->

6

So,  with  this,  we  have  discussed  the  tuple  relational  domain  relational  calculus,  the  basic framework of that I said that I will be at the overview level, when primarily we will continue to use the relational algebra and we just mentioned an outline of how you can probably go around looking  at  the  equivalence  of  them.  So,  we  will  close  the  module  here  now.  Thank  you  very much for your attention and see you in the next module.

<!-- image -->
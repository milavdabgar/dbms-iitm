<!-- image -->

## Database Management Systems Professor Partha Pratim Das Department of Computer Science and Engineering Indian Institute of Technology, Kharagpur Entity- Relationship Model-2

(Refer Slide Time: 0:30)

<!-- image -->

Welcome to Module 19 of Database Management Systems course in the IIT Madras online B.Sc program. We have been discussing the database design process and we have taken a look at the basic premise of the design. And decided that we are initially focusing on the conceptual design or the logical model of the requirements. And for doing this, we are learning a framework or for this  modeling  which  is  entity relationship  model  in  terms  of  entity sets attributes  and relationships.

## (Refer Slide Time: 1:00)

<!-- image -->

So, in the module in this current module we will learn the representation of these E-R models in terms of a diagram known as E-R diagram Entity Relationship diagram. And then we will see how this diagram can be translated into relational schemas or tables. So, these are the two main things to discuss in this.

(Refer Slide Time: 1:28)

<!-- image -->

So, ER diagram ER diagram is a diagrammatic way to represent all the information that we have talked about so far. Now, this is something which evolved at the very early stages of database design and the notations were somewhat different at that time and at the end we will we have listed  those  alternate  notations  which  you  might  find  in  several  places.  But  over  time  it  has evolved  and  with  the  introduction  of  a  very  powerful  modeling  framework  known  as  UML unified modeling language.

These have got standardized now kind of in a certain diagrammatic way. So, for through this we will see how to represent attributes, how to represent entity sets, how to represent relationships, how  to  represent  cardinality  and  so  on  so  forth  a  lot  of  things.  So,  entities  are  typically represented like this is a rectangle and which has the name of the entity set. And then you have the list of attributes one after the other.

And the key of the entities set or the attributes that formed the primary key of the entity set are underlined. So, you can see what is the instructor and student and so on. And if you look up in terms of UML you will see that these are notations which are typically embedded in the class diagram set of diagrams in UML. And with the added information that every attribute there will not only have the name but will also have the type specified they go another level further. But we are we will for now just keep to the E-R model part of it. So, this is how you represent entity sets.

<!-- image -->

8

Now, between two entity sets you can have a relationship which are shown as diamond and in the middle of the diamond you give the name of the relationship and you draw connect the entity sets through lines. And implicitly it means that advisor is a relationship between instructor and student and the relationships unless otherwise specified will mean the relationship between the key  of  the  entity  set  on  left  and  the  key  of  the  entity  set  on  right.  So,  advisor  will  have instructor.id and student.id this pair to work with.

(Refer Slide Time: 4:07)

K

<!-- image -->

6

It is possible that we talked about that it is possible that the relationship itself has an attribute. So, if  it  has  if  the  advisor relationship has a date say from where the advising process has started. Then that attribute is directly connected to the relationship through a dashed line. Dashed line means  that  this  is  not  a  relationship  line  and  because  if  you  there  is  this  is  a  diagrammatic language. So, the note the symbols and notations are very important.

For example, if you make this what happens if you make this solid line? If you make this a solid line then date will be that will mean that advisor has a relationship with the entity set date. Now, date will mean an entity set which has no attribute possible. I am saying there is entity set which has no attribute I have not yet decided on the attributes. But there is a relationship with date there is a concept called date through which it will have a relationship.

But that is not the case we use a dashed line the moment we use a dashed line it does not mean a relationship  with  an  entity  set  it  means  that  this  relationship  has  an  attribute.  So,  date  now  is interpreted as an attribute and it is an attribute of advisors. So, advisor will now become triplet instructor.id student.id date so remember.

(Refer Slide Time: 5:48)

7

<!-- image -->

6

Be careful about the notation then their roles entity sets in the relationship may not be distinct. A entity set may have a relationship with itself for example course id and prerequisite we have seen every  prerequisite  is  itself  a  course\_id.  So,  prerequisite  is  a  relationship  between  course  and course where naturally. How do you distinguish them? You need to, so on the other side on one side you call it a course id on the other side you are calling it a prerequisite id.

You are giving a new name because it had two instances of the same relation. So, by name it is the  same  course.course\_id,  course.course\_id.  So,  kind  of  here  you  make  use  of  the  renaming concept we had used. So, whatever is a prerequisite you call it a prerequisite\_id. So, you say that an entity here in the relationship prereq is between a course\_id which has a role of defining the course and a prereq\_id which is actually a course\_id, but has the role of specifying that what is the prerequisite. So, this is a typical kind of model. 0

## (Refer Slide Time: 7:08)

6

<!-- image -->

There  could  be  cardinality  constraints  as  we  have  seen.  So,  cardinality  constraints  are  shown simply as if it is how the arrow ends. If it ends like this it is many if it ends like this it is one. If there is a arrow at the end then it is one, if it does not have an arrow at the end then it is many that is the basic meaning of the cardinality. So, you can very easily understand that it is saying that advisor is a relationship between instructor and student and it is one to one. Which means every instructor has only one student and every student has only one instructor that is what is being said.

(Refer Slide Time: 7:50)

0

<!-- image -->

So,  if  I  do  which  is  which  is  more  typical  that  it  is  one  to  many  that  every  advisor  every instructor will have many students as advising. Whereas every student will have a unique so you have to see which side that arrow is. So, arrow is on the left side. So, instructor is one student will be many.

(Refer Slide Time: 8:17)

<!-- image -->

And obviously when I say one it is possible that it is not existence so it 0 is also it is 0 or 1 I should rather say this is  many to one.  Where this now says that a student may have multiple advisors but every advisor will advise only one student.

(Refer Slide Time: 8:39)

<!-- image -->

And you can have many to many where every advisor may have multiple students every student may have multiple advisors you can see that there is no arrow on either side. So, these are how the cardinalities are shown.

(Refer Slide Time: 8:49)

<!-- image -->

Then the question of total and partial participation we just talked about it in the last module. So, when you have a total participation of an entity set in a relationship you show that by a double line. So, the advisor line has a double line connection with the student. So, it means that every student must participate in the advisor relationship. In generalize what are you say that is it could be many to one means it could be 0 also.

But that is not possible in this case. Whereas or between the instructor and advisor there is only one single line which means that this participation is partial. So, an instructor may or may not feature in an advisor relationship. So, instructor may not have a student but a student must have a instructor. So, this whole idea is getting modelled through this representation of total and partial participation.  We  discussed  total  participation  in  context  of  weak  entity  set  but  it  is  a  general concept which can be which will be represented and used in multiple ways.

## (Refer Slide Time: 10:16)

K

<!-- image -->

6

Now, it is possible that instead of just doing one to many or many to one and things like that you could actually specify the cardinality of a relationship on both sides of entity set. For example, here on advisor it is showing 1..1. So, this is a minimum to maximum. So, 1..1 it says that it has to be minimum 1 and it has to be maximum 1 which says that it is uniquely 1 which says that it is total  that's  it.  Whereas  on  the  instructor  side  it  is  saying  it  is  0..*,  *  means  anything  it  is  a wildcard no limit.

So, it says 0..* which means that an instructor may not have a student may have 1 student may have 10 students may have 1000 students everything is possible. So, this is a pure modeling of the meaning and it is this is therefore the moment you include 0 it means that it is possible that the instructor does not feature in the advisors. So, the participation is partial.

(Refer Slide Time: 11:26)

K

<!-- image -->

This is the notation for representing complex attributes. So, you write the composite attribute and then  write  the  component  attributes  with  a  tab.  So,  name  this  reads  that  name  is  an  attribute which  comprise  of  first  name,  middle  name,  last  name.  Address  is  a  composite  attribute comprising of street, city, state, zip. State in turn is a composite attribute and so on. Then note another thing that in the phone number we have put the phone number within curly braces.

That means that, this is a multivalued attribute you remember single attribute composite attribute and single valued attribute multivalued attribute. So, here in this we are showing the notation for composite attribute as well as multivalued attribute. In the last if you see age you see a pair of parenthesis after it which is what which is a function notation what do we write like this function notation which means that this attribute has to be computed.

And we discussed that age is a derived attribute because it cannot be stored directly it will have to be computed from the date of birth. So, that information of derived attributes represented here. So, this is just one single slide which tells you what are the different ways information can be represented  in  the  E-R  diagram  for  attributes  simple  attributes,  key  composite  attribute, multivalued attribute, derived attribute, everything is shown through this representation. So, just try to remember these.

(Refer Slide Time: 13:27)

<!-- image -->

If  you  have  to  represent  a  weak  entity  set  naturally  what  are  the  conditions  you  need  a relationship between the strong entity set and weak entity set. So, first the representation of a weak entity set is done by using a rectangle for the entity set which has double line boundary. See  course  has  single  line  boundary,  section  has  double  line  boundary.  So,  that  double  line boundary says that a section is a weak entity set.

That immediately means that section must be associated with some strong entity set through a relationship. So, that relationship is sec\_course. So, this relationship is linking a weak entity set to  a  strong  entity  set.  So,  to  represent  that  the  diamond  of  this  particular  relationship  is  also drawn with double lines. You see this diagrammatic language every way of drawing will mean something or the other.

So,  we  know  that  section  is  a  weak  entity  set,  course  is  a  strong  entity  set,  sec\_course  is  a relationship from section to course to define the weak entity set properly. So, since and then you see that between sec\_course and section the line connecting is double line. What does it mean? That  this  has  a  total  participation.  So,  now  you  see  that  all  of  these  conditions  have  been satisfied. So, what is remaining for the weak entity set I need to know the discriminator.

So, the discriminator is shown in the section entity set representation by doing hashed dashed underline of the attributes. So, section id semester and year this triplet is a discriminator. And this  is  underlined  with  dashed  saying  that  this  is  a  discriminator  not  a  primary  key.  So,  the section  course  will  associate  sec\_course  will  associate  this  with  the  strong  entity  set  course whose primary key course id along with this discriminator that is course\_id, section\_id, semester and year, this four together will be the primary key of the weak entity set section.

(Refer Slide Time: 15:58)

<!-- image -->

So, this is a more detailed diagram of the university representation that you had seen. So, earlier it was just showing well this is there that is there this kind of now it formally shows in terms of a ER model, you have to understand it very thoroughly and study it, get satisfied that all conditions that are being shown by the E-R model actually. What does it mean in the real world whether what whether it is kind of how meaningful it is and whether it is capturing the real world in the proper way or not.

## (Refer Slide Time: 16:47)

6

<!-- image -->

So, we will move to the E-R model to relational schema that now we have the E-R model. So, we had a concept from that concept we form the attributes entity sets and relationships. Then we have represented  that  without  ambiguity  in  terms  of  the  E-R  diagram.  Now,  we  have  to  start creating the relational schema.

(Refer Slide Time: 17:15)

<!-- image -->

## Reduction to Relation Schema

- Entity sets relationship sets can be expressed uniformly as relatio represent the contents of the database and
- A database which conforms to an ER diagram can be represented by schemas
- For each entity set and relationship set there is a unique schema that name of the corresponding entity set or relationship set
- Each schema has a number of columns (generally corresponding to al have unique names

This reduction this is called reduction to relational schema. So, all that we need to do is primarily we need to know two things one is how to show the relational schema for entity set how to show the relational schema for a relationship.

(Refer Slide Time: 17:33)

6

<!-- image -->

So, it  is  very  simple  for  a relational  schema  for  an  entity  set  is  you  just  take the name  of  the entity set as the name of the relation. And the list of the attributes as you have as a attributes. If it is a weak entity set then you have to do this process of going through the identifying relationship of  the  weak  entity  set  the  discriminator  the  primary  key  of  the  strong  entity  set.  And  get  the primary key of the weak entity set put that there is list using the name of the weak entity set as the relationship. So, it is very obvious how these relationships are now coming out.

(Refer Slide Time: 18:14)

5

<!-- image -->

And  you  will  see  that  things  just  go  in  a  very  smooth  way.  Then  is  a  relationship  in  the relationship as I said by default the relationship between the primary keys of the relations that it is connecting it is associating. So, here in advisor you have the instructor id and the student id so you say it is s\_id and i\_id as names given you can you can write it as instructor\_id, student\_id also.

But the idea is you take the primary keys of two sides and put them as attributes. So, here you can see that basically it is a very simple thing you need to have what is a relation, a relationship is  a  name  and a set of attributes and the information of the primary key. This is the fun three fundamental information for a relation the schema. So, the name is coming from the name of the entity set or the name of the relation and in terms of the attributes we are just figuring out how to get those attributes.

In  case  of  strong  entity  set  is  just  a  list  of  attributes  in  case  of  weak  entity  sets  is  a  list  of attributes of the weak entity sets plus the primary key of the strong entity set through identifying relation.  And  in  case  of  relationship,  it  is  a  set  of  primary  keys  put  together  of  the  two relationships that it is two entity sets that it is associating.

(Refer Slide Time: 19:43)

## Representation of Entity Sets with Composite Attribu

<!-- image -->

- Composite attributes are flattened out by creating a for each component attribute
- name with   component   attributes   first\_name the schema corresponding to the entity set h; name\_first\_name and name\_last\_name
- Prefix omitted if there is no ambiguity (name. be first\_name)
- Ignoring multivalued attributes; extended instructor instructor (ID , first\_name, middle\_initia street\_number , street\_name, apt\_number
- zip\_code, date\_of\_birth)

Now, how do you handle composite attributes? There could be two ways to handle that one is and that is what in most cases be done is called flattening. That you instead of getting into the

Module 19

composite hierarchy as you have on left. So, instead of having name as an attribute will have first name, middle name, last name as three different attributes.

So, that could be the unifying schema the other approach could be that which in some cases will be used is in case of a composite attribute you will actually not represent the attribute here rather you will represent that attribute as a separate entity. You will say make an entity set for address then it becomes or say an entity set of name then it becomes simple attributes if you say name is an entity set then these are simple attributes.

And then you define  a  relationship  between  these  two.  So,  it  could  be  something  of  that  but typically what we will do is flattening. So, if I have done that in the in the instructor design just ignoring  the  multivalued  facet  of  the  of  the  phone  number  you  will  see  that  we  have  the relational schema designed here.

(Refer Slide Time: 21:18)

<!-- image -->

Now, how to handle multivalued now if you have to handle multiple values naturally you cannot put it right there. So, what you will have to do is you will have to create a separate entity set and have a kind of relationship with the original entity set. So, that we can say that in the multivalued phone number what do we know it is between the phone number and the instructor. What is the type of relationship it is one to many.

That is one instructor can have multiple phone numbers but one phone number cannot belong to multiple  people.  So,  if  I  take  the  phone  number  phone  number  by  itself  is  a  key.  So,  I  can represent it in a table in a relationship I am sorry in an entity set with the id of the person who holds that phone number that becomes a relationship of using number which number am I using.

So, that could be a way to so that is why you see that inst\_phone is a doublet of id and phone number by which we can now have multiple phone numbers associated with this. But obviously this means that they will I mean while we want to extract phone number, they will have to be some additional logic in the processing. Because it is no more just a flat attribute but it is coming through a relationship in the process.

<!-- image -->

Now, many to  one  and  one  to  many  relationship  sets  that  are  total  on  the  many  side  can  be represented by adding an additional attribute. For example, what we are saying say we have here let us understand this diagram again. Three entity sets instructor, department, and student. Three entity sets instructor, department, student. And three relationships one is advisor which is many to one from student to instructor.

The other is the student department that is which department does a student belong to this is also many to one. But with the specificity that  on the student side this is total which  means that I cannot have a student who does not have a department is a total part. So, every student must be there  in  the  stud\_dept  relationship  which  means  that  no  student  can  be  there  without  a department.

Then  inst\_dept is a similar relationship but between the instructor and the department. Again, this is also a total thing. So, if every instructor is so what is say what is the stud\_dept relationship this relationship is if I when I put it into the relational schema it becomes department name and S\_ID where both of them together is a key that is this relationship. And this one is department name and I\_ID both of them are key.

Now, the point is since from the many side this is total which means that for every I\_ID there is an entry in this and it is many to one. So, that entry is unique. Two things one is every I\_ID will be there in this and it will be there only once. Because it is many to one it can have only one department if that be the case then the question is do we need this relationship or simply I can take the department name and put it as an attribute here.

Similar argument will say do we do I need this or I can take it and put it just like here. So, I can just  extend  the  instructor  and  student  entity  sets  or  relationships  by  an  additional  attribute department name and get rid of these two relationships. Which will be two different tables like this  altogether  reduces  my  overhead  of  doing  traversal  join  of  relationships  in  answering  the query.

(Refer Slide Time: 27:08)

<!-- image -->

## Redundancy of Schema (2)

- For one-to-one relationship sets, either side can be chosen to act as t That is, an extra attribute can be added to either of the tables co two entity sets
- If participation is partial on the "many" side, replacing a schema by in the schema corresponding to the "many" side could result in null

So, that is a some of the considerations to scrutinize after a basic design has been made.

## (Refer Slide Time: 27:19)

6

<!-- image -->

So, this is also something that you can look at you can take this also is from many to one. This is on the section side this is total. So, section will be there in sec\_course only once it will be unique and every section will be there. So, we can include course\_id in the section that is in terms of modeling the weak entity set. Now, we are saying that weak entity sets discriminator then the identifying relation then the key primary key of the strong entity set. After all these I can just take the key of the strong entity set and put it in the weak entity set to make it a strong one and get rid of the identifying relationship.

(Refer Slide Time: 28:16)

<!-- image -->

elidae

So, if you now go back and see the schema that exist in that we had been using you will see that because that was a relational schema. So, now we are slowly evolving and trying to come to that schema. So, you will see that this kind of considerations have gone in terms of first designing it, refining it and then removing the redundancy in a full-blown form. So, this brings us to the end of discussions in this module. We have discussed the basic E-R diagram and translation of E-R models to relational schema and we will continue in the next module. Thank you very much for your attention and see you in the next module.

<!-- image -->
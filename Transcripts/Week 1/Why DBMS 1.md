<!-- image -->

## Database Management Systems

## Professor. Partha Pratim Das

## Department of Computer Science and Engineering Indian Institute of Technology, Kharagpur Why DBMS? /1

Welcome back to Module 2 of database management systems course in the IIT Madras online BSc program. In Module 1, we have taken a very basic look at how databases have pervaded all aspects of our life, touch any part, touch any application or even when you are not aware, I mean just to tell you the extreme in a way, even for people who just use a basic cell phone to make calls,  you  are  using  an  extensively  large  database  application  which  not  only  keeps track of the numbers, the location tracks, the connection track and so on of the caller and the callee and the overall infrastructure of towers and base stations and all of that.

(Refer Slide Time: 1:35)

<!-- image -->

<!-- image -->

So, we cannot live without databases today. In the current module, we again in the current module and the next, which we have titled as part 1 and 2 of why DBMS, we take a little deeper look in two perspectives. In this module, what we want to do is to understand the need for  a  database  management  system  for  somewhat  of  a  historical  perspective.  Asking ourselves fundamentally what is that database management systems are needed for?

What did we do say 300 years back 400 years back, what did we do 100 years back, what did we  do  30  years  back,  what  did  we  do  10  years  back  and  why  and  how  the  database management  systems  are  evolving,  keeping  two  sides  in  balance,  one  is,  one  side  is  the availability  of  technology,  we  are  talking  about  a  time  where  technology  is  the  key  thing which keeps on moving makes more things available, and hand in hand with that on the other side are the way the society is transforming.

We have been part of a big pandemic. And you know, we all know in one of the ways or in some of the ways as a nation we have tried to respond to it was to use say an application called Aarogya Setu. Aarogya Setu is an application to find out about your health condition related to Coronavirus and the health conditions of people potentially near to you.

So, you can think of that these are people who do not even know. But it is possible to track and  correlate  this  information.  So,  what  kind  of  huge  database  go  behind  that,  which  is keeping track of the conditions of several people who use the Aarogya Setu App, and their locations and their movements and all.

The other that all of  you are aware of in this context is  the COWIN App which has been tracking  the  entire  nation's  vaccination  program.  It  is  tracking  who  is  getting  vaccinated, where is she or he getting vaccinated? What vaccine has been administered, what is the first dose or the second dose, a date when is the next vaccine to be given the other card or passport of that person and finally the certification. Another huge life changing database application.

Now, even if you look back 10 years ago, this were not possible. We did not have Aadhaar cards  we  did  not  have  this  kind  of  network.  We  did  not  have  this  kind  of  scalability  of database systems. So, in this module, we try to take a little historical look on how have we evolved as a civilisation. In terms of data, and records management, and in the next we will talk about specifically about why you need separate kind of systems for solving data related problems, why does not simple computer programs can solve this problem. So, we will talk about evolution of data management practices and a little bit of history of the DBMS.

(Refer Slide Time: 5:28)

<!-- image -->

So, first of all the evolution of data management. So, if we ask in principle, then what does the management of data or which earlier was used to be called management of records? What all are needed in the human society? What is the basic need? The first of course is storage, you need to remember things, how much money I have, how many inventory I control, how much of how many people an organization employs, and so on. So, storage is important.

Along with the storage comes retrieval, that I should not be whatever data is stored, I should be able to get it back. So, storage and retrieval are the key requirements of data and records management. I am not specifically talking about database systems, as you know today, but I am saying the need of management of data and management of records of different things.

Then you have transactions, transactions is where something is being exchanged, something is being done on that data, either certain part moving from one place to the other or one, so called account to another like I go to a showroom and buy a two wheeler. So, a transaction has happened, a two-wheeler whose ownership was with the dealer, or was with the company through the dealer is now transferred to my name. So, this is a transaction. And accordingly corresponding  to  that  there  are  financial  transactions,  the  money  that  I  had  to  pay  to  the company through the dealer. So, transactions are a very important part.

The fourth is audit, you always need to know what happened, did things happen properly? Was there any mistake? Are all the rules and regulations of that particular segment properly followed? Was tax paid? On the sale of the two-wheeler? Was, why are all these financial scams  we  are  looking  at?  Because  it  is  possible  to  dig  out  from  the  stored  data  with  the appropriate retrieval and audit to see what who did certain things may not be right. You have archival purposes, that you need to just keep that data for maybe some possible future use. There could be more, but I just talked about some of the salient requirements.

So, we will have to the reason I am putting I know you, all of you know this, all of you know this I am not saying anything new. But I just want to highlight these points because you have to always keep these in perspective, when you learn this course. This is your, these are your challenge points. You are trying to make a system, you are trying to improve a system you are trying to make changes to a system keeping these kinds of requirements in mind.

And obviously, related question is whom do you do it for? You could do it for an individual, for me for you, for your friend for your parents, or it could be for a small enterprise, small organization or for a big enterprise like Google, like Reliance Industries, like Tata Motors, so on. Or it could be for a global organization, it could be for United Nations, it could be for any other country's government or in more global organizations like Apple.

So,  what  do  you  have  to  do?  What  we  need  and  for  whom  we  need  are  very  clear.  The question is what should be the approach, and if you look at the human history, there has been primarily two major approaches in this practice, which are very natural. One is physical. So, the world started physical. So, from the day people started realizing the need for maintaining records to satisfy storage, retrieval, transaction, audit, archival these kinds of requirements. People started maintaining records, physically. And then came the electronic era.

<!-- image -->

So, most of the time, the human civilization has been around, we have seen physical forms of data  and  records  management,  which  is  in  certain  parlance,  very  formally  known  as bookkeeping. If we if any of you have familiarity with accounting courses and so on, you will know that there are courses like accountancy and bookkeeping, which basically talks about how you keep the physical Ledger's, how are you… I mean what in what style you put the data in it, what style you write journals, that is notes and so on.

Now, if you go back couple of centuries, you will find that well, this practice is coming from time immemorial. The practice of having ledgers and journals, but things started streamlining somewhat towards the end of nineteenth century when an American inventor by the name of Henry Brown, first invented something which is called respectable… receptacle for storing and preserving papers, which in today's time, we know as file cabinet, how to organize and have had a severe evolution based on that.

There is a significant correspondence between this physical organization of the data to the electronic  mimicry  of  that  in  terms  of  the  database  system.  So,  that  transfer  knowledge  is very important to realize, even in terms of memory, instant terms of, writing down everything is laborious as well as error prone. So, Hollerith, Herman Hollerith, who kind of started using adapting punch cards that were used in the Jacquard loom for weaving as memory so that you could do very simple mechanical computation based on these ledgers based on this ledger data, that also happened somewhere around towards the end of nineteenth century.

(Refer Slide Time: 12:26)

OF

2

7

<!-- image -->

And then,  so  on.  I  mean  before  that,  several  centuries,  people  followed  the  same  practice following the  getting  into  the  twentieth  century  also  the  same  practices  continued,  till  you came  to  almost  the  middle  of  the  twentieth  century  when  computer  programming  started, computer started happening, programming started and in 60s mostly, you started seeing the database  management  system  or  electronic  management  of  data,  where  you  need  storage, retrieval, transaction, audit, archival this kind of.

So, for storage, which is the primary thing because you have to keep the records where punch cards were used long punch tapes, I do not know if any one of you have seen, or were used then it evolved to magnetic tapes and so on, went on for about 10-15 years till in 70s certain significant  improvements  and  development  happens  in  terms  of  COBOL  language  being introduced, it is still used, 50 years on it is still used.

CODASYL approach that is one approach of doing data management came in, Apple first introduced  VisiCalc,  VisiCalc  is  kind  of  the  forefather  or  great  grand  forefather  of  our spreadsheets today, Excel or Google Sheet as easy, magnetic disks became prevalent and so on.  Then  in  80s,  we  had  relational  database  systems  which  changed  the  face  of  data management  in  90s.  Internet  came  in  so  that  started  making  the  whole  data  and  records management global.

In  2000s, ecommerce really started booming, all those most of the significant e commerce activities you see today, they started around 2000s and this some died, some flourished. And as that kept on happening, there was more and more need and more and more requirement to manage unstructured data, data which is not just textual data, which is just not numbers, data about images, the Facebook profile photos, data about videos, data about audio tracks and so on so forth. Data about just freely written natural language, text and so on. And no SQL was born.

In the last decade data science started riding high, and today you are there you will write the next  future  of  data  management  using  electronic  systems.  So,  let  us  this  is  a  very  broad evolution if you if you look at it.

<!-- image -->

Now,  in  this  whole  process,  there  are  several  parameters  on  which  this  data  and  records management system particularly in the electronic form has to take care, things like durability and  store  a  data  it  must  be  available  for  ages  together  that  was  a  basic,  drawback  of  the physical system, papers were out the termite will eat it up, or even the basic acid in the paper will cause the decay of the paper on which you kept the records but electronic records must be more durable. Are they? Is a big question.

And that will have to be ensure, how do you ensure that they remain durable as well. It must be  scalable;  it  should  work  for  say  10-20-100  people  as  well  as  10,000;  100,000  millions billions  of  people  or  transactions  and  so  on.  It  has  to  be  absolutely  secured.  Of  course, depending on the application, all of these will have a certain operating range, the security of say the different information systems that are associated with a difference.

And the security of a digital library are not equivalent. A digital library needs some security so that copyright is stuff and not stolen. But that security will be far less compared  to the security of where the ward management is done. So, though but those are those are aspects these aspects we will have to always keep in mind keep questioning about them, what is the retrieval? How quickly you need to retrieve, is it okay to get your data within a day within a couple of seconds under millisecond, under nanosecond and so on so forth.

It should be easy to use of course, otherwise, it has not served the basic purpose consistency, we talked a little bit about consistency in the last class that always if I do something on that database, if I do some transaction, then before the transaction and after the transaction, the database must be in a consistent state it should not be that of, a transaction has been done to make a payment of 100 rupees to my friend and in that process 100 rupees get disappears from the system. That is not certainly acceptable.

Efficiency  has  to  be  high  that  efficiency  as  a  whole  not  only  of  the  is  not  only  the  time efficiency,  it  must  be  that  is  what  the  speed  of  retrieval  is,  but  efficiency  in  terms  of  you know, amount of storage requirement maintenance requirement, efficiency and productivity of the staff those are involved, the programmers those are involved because all of these lead to the cost considerations. So, these are some of the not this is not a complete list the some of the key parameters on which data and record management's need to be looked at.

<!-- image -->

So, if we just you know, more a fun discussion, if we just look back into bookkeeping, you know, physical records management, widely used everywhere till today, you go to a grocery shop, many a grocery shop have a small PC, some have migrated, and they are more savvy, they are migrated to doing business on mobile phone, but there are several who will just write it down.

This is you go to particularly you go to a medicines shop, they give you the medicine and then they see that this particular they are low on that stock, they will take out a ledger right down on the journal that this medicine codopyrine is not there in stock and so on. So, if we recall  on  that,  then  we  will  know  we  have  seen  that.  What  are  the  problems?  There  are several problems one durability is a problem physical damage. I mean it can very easily get damaged can get as we say with rodent, termite, humidity, wear and tear, fire there are a lot of ways physical records might get destroyed. Scalability is very difficult to maintain.

You can manage a medicine store for maybe 100 customers, 200 customers on ledger you cannot maintain a medicine store of a million customers on paper. It is not possible. Security. Always because you always have to have trusted people you need physical lock and key and so on so forth, you know, big saves, and all that for maintaining the physical records.

Retrieval is obviously time consuming; you will have to look up, take out that big stuff from the file cabinet look up and so on. Consistency is certainly you can, it is quite possible that you have made a payment that has been received but has not been entered on your part of the ledger. So, there are several problems of this physical bookkeeping systems.

<!-- image -->

Somewhat of a better solution, which many of us is widely used, and kind of it came in about 40  years  back.  I  just  mentioned  VisiCalc.  So,  that  was  about  40  years  back.  So,  it  is  a spreadsheet  software  which  allow  you  to  keep  records  in  simple  terms,  you  have  paid applications  like  Excel or  you  can  use  Google  Sheet  which  is  free.  And  it  these  also  have different issues, these are, but these are less prone to durability issues of damage, because you can keep a Google Sheet in a Google Cloud which has a lot of backend infrastructure to make sure that it does not get lost.

Then there is scalability is easier to search, you can password protected is not a very good protection, there are several, you know systems available by which it can be broken, but well, some sort of  protection  can  be  there,  it  is  easy  to  use,  consistency  of  course,  is  not  much guaranteed in spreadsheets, you will have to either write lots of formula or kind of make sure that you are using it in the right way.

But  it  is  better  than  a  physical  ledger  and  journal-based  system,  which  according  to  these criteria, can access it based on more criteria, you can do it  yourself. So, this is still used, I mean this is widely used not still this is widely used for particularly single users or for small enterprise applications. A good example of how a moderate range data management solution can provide.

<!-- image -->

But certainly, these are all spreadsheets or CVS file CSV files and so on are all, basically file system  based,  we  say  these  are  flat  file  systems,  flat  file  solutions.  So,  they  have  lot  of limitations as well. If you they are scalability is limited, like spreadsheets have a maximum limit on the number of rows. Consistency management, we said is relatively a big challenge.

If we have certain constraints on the data, it is not easy I mean you can you can try in Excel then you will see that Excel does allow you to put some constraints, but they are just data entry  constraints  that  is,  you  cannot  enter  a  negative  value  in  this  cell.  But  if  you  have constraints resulting from transactions.

It  is  very  difficult  to  manage  that  in  a  file-based  system  because  you  will  have  to  write separate  code  for  doing  each  one  of  that,  it  permission  levels  are  limited,  you  can  give  a password  but  you  cannot  have  multiple  people  use  the  same  file  in  multiple  levels  of authority. So, these are some of the typical limitations in the evolution which finally makes sure  that  the  only  solution  is  a  database  management  system  which  we  are  going  to  study here.

<!-- image -->

Talking a little about the history I will be very brief here because it is a long and deep history. As I said it started between 1950s and 60s, tapes and punch cards, then in late 1960s and 70s hard  disks  magnetic  disks  came  in  and  these  are  some  of  the  people  whose  work  you  are going to read about like Ted Codd, who define the relational data model we will learn about Boyce Codd normal form and so on.

<!-- image -->

And slowly the, evolution towards more and more sophisticated data management systems started happening. 80's really saw a boom, through which SQL which we will learn about start learning about very soon in the coming modules became an industry standard. And it is also  saw  up  parallelisation  and  distribution  of  database  systems  that,  before  that  database systems were centralized.

That you have one machine, one server or one PC on which you are using it, but in the 80 slowly across enterprise you started using it, you need to use it across the enterprise, you need to use it across a local area network and so on. And in the 90s, as Internet came in this use, or this distribution certainly went all across the web.

In early 2000s, and so on the need for unstructured data management came into being so we had XML and XQuery standards coming in, will talk a little bit about XML and those kinds of  stuff  slowly  and  from  later  2000s  really  giant  data  storage  systems,  Google  Bigtable, Yahoo PNuts, Amazon these kinds of things have started coming.

Converging into the data science possibilities on the, the foundation of data science is not database,  it  is  the  foundational  part  in  this  is  database  system,  which  gives  you  data warehousing, data mining, all of that, and on top of that you have data science, of which you are trying to  gain an expertise. So, think  about  being a data scientist, among many things, what you will have to be really good at is database management systems.

## (Refer Slide Time: 26:46)

<!-- image -->

So, there are different evolution models that I have shown here, this is not this is more for, giving  a  picture  about  how  things  have  moved  from  60's  to  the  2010.  This,  you  know, horizontal axis show you what has primarily been happening during those decades.

(Refer Slide Time: 27:06)

<!-- image -->

Then  how  the  technology  has  moved  from  based  on  the  evolution  of  the  computer technology.

## (Refer Slide Time: 27:16)

<!-- image -->

And I will talk about this third part more subsequently, is how the database architecture as move in.  And  if  you  if  you  look  at  that  way,  then  basically,  this  is  primarily  the  area  of architecture  on  which  we  will  be  focusing,  talking  about  Oracle  system,  SQL  servers, MySQL, Postgre SQL, which is not named here, Sybase, and so on.

And these are what you all see around, this is your past. And this is kind of what has been happening, beyond that I am sorry. Let me choose this. So, this is what we primarily intend to do. This is the past stuff. And this is all different types of what you see here are all different types of systems that are taking things forward, particularly dealing with the big data and so on.

<!-- image -->

So, that is about the basic overview of how databases been playing a big role in our life, the evolution of the data and records management and the history of the DBMS. Thank you very much for your attention and see you in the next module.

<!-- image -->
<!-- image -->

## IIT Madras ONLINE DEGREE

## Database Management System Professor Partha Pratim Das Department of Computer Science and Engineering Indian Institute of Technology, Kharagpur

## Lecture 05

Application Design and Development/5: Application Development and Mobile

Welcome  to  Module  35  of  Database  Management  Systems  course  in  the  IIT  Madras online B. Sc. program. OF

(Refer Slide Time: 00:28)

<!-- image -->

We have been discussing about application design and development using the database and the three tiers architecture. We have talked about the architecture, a little bit of web, how to access databases from different programming languages, and specifically we have focused  on  Python  as  a  middle  tier  language,  because  it  is  getting  very  popular  and accessing some database, we have talked about PostgreSQL. We have also talked about frameworks like Flask which makes it easier to develop code.

(Refer Slide Time: 01:10)

<!-- image -->

And  certain  very  critical  factors  about  the  application  that  you  develop,  which  is performance and security.

2

<!-- image -->

First, Rapid Application Development. Actually, if you have studied software engineering  at  some  stage  then  you  will  be,  you  will  be  familiar  with  the  concept  of RAD, which says  that,  which  is  kind  of  an  agile  software  development  model,  where unlike the waterfall, you do the specification, I mean, requirement, capture, specification analysis,  then  deeper  system  analysis,  then  design,  then  implementation,  then  testing, then delivery, one after the other, you do not do that, rather you do very small things at every stage and do quick turnaround iterations.

So, you start with a few set of important features, try to do the design for that, do the analysis,  do  the  design,  implement  something  sketchy  and  go  back  to  the  customer  to show okay, this is I have done. So, the customer says, okay, this is what I wanted this is what I do not want. It becomes much easier, so it is often called the customer-in-the-loop kind of development. So, this is becoming more and more popular because it is shown to be, it has been shown to be more productive, better, it gives better quality and so on.

Now,  still  a  lot  of  efforts  are  needed  in  the  whole  thing  so  there  have  been  several approaches  to  speed  up  application.  One  is,  function  library  to  generate  user  interface elements. So, flask kind of system is somewhat towards that. Even there are lot of IDEs, Integrated Development Environments, which allow drag and drop feature to create user interface elements like in visual studio.

You can automatically generate code for user interfaces from a declarative specification. User interface code is, is basically procedural. You are saying this, this, this, but can you just specify that I want this and, much in the SQL. as you said this is a SQL style, this is what I need and how to do it, the system automatically generates.

So,  these  are  some  of  the  efforts  that  have  gone,  and  RAD  has  been  around  for  quite some time, so it is, as I said, is a agile model. Typically, an application development has four phases. One is, business modeling. You need to know what is the requirement, what is the business, what is that you want to satisfy.

Second is a data modeling. What are the data entities, how they will have to be modeled, how you will have different attributes, constraints, all of that. Then you have a process modeling. Process modeling is more like workflow modeling.

We talked about say, while discussing about variety of applications and so on, we talked about  a  basic  fact  that  if  you  are  buying  something  on  an  e-commerce  site,  there  is  a workflow. There is a workflow to buy. There is a workflow to check order. There is a workflow to cancel an order, and so on.

So, you first check the item, then check the details, then you put it to cart, you check out the cart, you validate for the payment, your payment is done, order is finalized, you track the order. So, this is a workflow. So, that is a process modeling.

So, the business model here will have the different kinds of items that you want to deal with, what is that you want to do, that you want to sell, you give, you want to give offers, you want to club different items together as a recommended bundle and so on so forth. So, there is a whole lot of business issues.

Then there is specific data modeling which says you model every item that you sell on the on the portal. You model books, specific books, you model different appliances, you model  apparels,  you  model  clothes  and  so  on  so  forth.  And  then  you  model  all  the different processes the workflows that can be done. So, that is the very important factor.

And then finally you have testing and turnover. Then you test and check and if things are happening okay, and so on. So, that involves defining the requirements, prototyping, you can make a small web, I mean, system which is supposed to be a very simplified form of your original system, then take feedback from the customer, as a customer-in-the-loop, and finalize the software.

So,  this  is  your  RAD  approach,  Rapid  Application  Development  approach.  So,  with RAD, the time between prototype and iteration has got very short, and integration occurs from  the  beginning  itself,  the  integration  of  different  business  models,  data  models, processes, and your customer engagement are all happening together. So, that is the, that is the agile model. If you want to learn more about it you have to go to a good Software Engineering course.

2

(Refer Slide Time: 07:21)

<!-- image -->

Now, for supporting RAD, there are various frameworks which has been developed, and if you want to, when you actually go to the industry and start working for your company you will have to possibly learn one or more of these.

For example, one framework which is very strong is called Java Server Faces. We talked about Java Server Pages. These are Java Server Faces. Java Server Page tries to model your data and your logic. Java Server Faces tries to model the user interface components.

What  are  their  states,  like  the  boxes,  the  buttons,  the  choices,  the  fonts,  what  are  the events on which they happen, how do you validate input, how do you define navigation between pages, do you support internalization, I am sorry, internationalization, internationalization means that you support any kind of language that some people may want to use, do you support accessibility, is it friendly to the people who have disabilities, say  some  people  may  have  disability  of  blindness,  low  vision,  or  some  may  have disability of hearing impairment and so on, is the site accessible for them as well.

So, all of these have been modeled through Java Server Faces, which, for which the JSP has a custom tag library. With that it can interface with the JSP, and this is a very, very strong,  I  mean,  getting  out  to  be  a  very,  very  strong  mechanism  for  doing  rapid development, rapid quality development of web applications.

The other is, you must have heard this name, I believe, is Ruby on Rails, which allow easy creation of CRUD, which is Create, Read, Update and Delete. So, interfaces by code generation from database schema or object model, you just take there and from that you generate this almost by automated means. Ruby on Rails are also getting very popular. Actually, these are links to the corresponding information pages in case you want to go deeper into any of these.

Besides that, there are several platforms and tools that you can use for Rapid Application Development, and that it may go beyond your web application. G Suite from Google, you must  have  heard  of,  it  is  very  popular.  Google  App  Engine  is  very,  very  powerful. Microsoft Azure has been around for quite some time. The Elastic suites from Amazon or AWS is particularly friendly, and there are several others.

So, I would suggest that while you prepare through this course and, there is a course on application development also which you will be doing after this, or you are doing at the same time, do look at, at least one of these RAD platforms and one of the frameworks and try it out so that when you go to the industry, you will know what these frameworks and tools do and that would be a big, big advantage in your interview as well as in your actual work life.

(Refer Slide Time: 11:02)

<!-- image -->

Okay,  going,  okay,  there  are  others  also.  I  have  put  it  separately  because  this  is proprietary,  and  I  do  not  like  proprietary  things  so  much.  So,  this  ASP.NET  from Microsoft which comes with a lot of RAD features in the Visual Studio.

(Refer Slide Time: 11:23)

<!-- image -->

Now, let me talk about few other aspects of the applications that you are developing. So, far, we have only been concerned with the architecture, how to, functionality. Now with that, please remember, two things are, many things are important, but two things are very, very important. One is performance, and the other is security.

A web page is expected,  many  web  pages  are  expected  to  be  accessed  by  millions  of users every day. So, how do you, I mean, that puts a lot of pressure on the, on the web servers, database servers and so on, because there, you, for everything you will have to do all those steps, send the request, connect, cursor, all that.

So, what can be done observing that while there are several requests, millions of requests come, there is also a lot of repetition of the request. When Neeraj Chopra won gold medal in Javelin for India in Tokyo 2020 Olympics, certainly millions of people have searched for Neeraj Chopra, for Javelin as a sport, for Tokyo Olympics, and so on.

So,  the  question  is,  can  we,  can  we  kind  of  use  a  mechanism  of  caching?  What  is caching? Caching is basically keeping a copy of a solution which you have already done so that in future if a similar, if the same question is asked you do not have to solve it again and you can just pass it on, the result.

So, you can do a lot of different caching, on the server side, you can cache the JDBC connection  between  the,  between  servlet  requests.  The  servlets  are  making  different JDBC connection requests so you can cache them. It is called connection pooling, so that every time, because the same servlet will keep on making the connection request several times in a short span of time.

So, instead of doing that connection every time just pull that in a data structure and keep reusing it. So, that is caching for connection pooling. You can cache results of database queries, as I was saying. Neeraj Chopra, so many people will look for. So, you can, once you have that query, you can cache the result, and keep on reusing it, giving it again and again, whenever the same query comes.

Of course, it will get dirty as the database changes, so the query result on Neeraj Chopra before, the day before he won the gold and the day after he won the gold would be very, very different. So, you have to be, while you cache you will also have to have strategies so that you do not keep dirty results, old results with respect to the database.

Finally, you can cache a whole lot of generated HTML. So, it is not the result, you can cache  the  entire  HTML  and  keep  it.  So,  all  that  you  need  to  do  is,  this  is  the  same question, this has been asked a million times already, just take the HTML and give it.

So these are different kinds of caching which can happen on the server side, at the client side also we can cache pages by what is called web proxy, that your web server tracks that well. The same request is being sent from multiple clients within that network.

So, it sends that and when the response come, it keeps a copy, so that whenever the next person  sends  it,  it  does  not  forward  the  request  to  the  web  server,  it  just  gives  a  last answer. Again, you will have to be careful about returning dirty pages, dirty links, and you  know  making  sure  that  you  do  not  cache  for  a  large  amount  of  time  so  that  the database changes are not reflected in the result.

But these are certain ways,  there are several others to improve  the  application performance besides what you can do as a developer in terms of coding and architecting the application.

(Refer Slide Time: 15:56)

<!-- image -->

Now, coming to security, security is a is a big, big concern because you are getting  a response and that response might do something we say, we already talked about that it tries  to  make  it  secure  so  that  all  the  client-side  scripts  are  not  allowed  to  use  the resources of the client machine without except the browser's own program space but, and, but there are several things that can go wrong.

There is a concept of SQL injection which actually use a pre-prepared SQL statement and push in the parameters. Now, when you do that there is a possibility that some malicious request can push in parameters values which can cause other defects. So, you have to be careful with those kind of.

(Refer Slide Time: 16:55)

<!-- image -->

A biggest, or one of the biggest issues is password leakage. So, never store passwords, such as, particularly the database password in clear text script, which can be accessible to others. You should always encrypt it very well.

For example, files in a directory  which is accessible to the web server.  Normally, you would, the web server would provide source of script file such as file.jsp, file.php, but source editor will backup like this.

Now, you have to be careful that well,  often  these  backup  files  stay  on  and  they  may cause other security breaches. Restrict that access to the database server from the IP of machines running application servers. Most database allow restriction of access by source IP address.

These  are  just,  as  we  put  doors  and  windows  to  secure  our  home  and  then  we  put  a boundary wall to secure our home, then we have a gated community to secure it further, similarly, similar kind of security protections will have to be looked at.

(Refer Slide Time: 18:20)

<!-- image -->

The other aspect is authentication. We are authenticating the right user for an application. Now  the  question  is,  is  any  kind  of  authentication  good.  Initially  it  used  to  be  only password, but it has now been established that password is really very, very weak. So, because users use the same password across sites, spyware can capture the password and so on.

So, at least it has to be a two factor authentication. Password with SMS, or password with a one-time password device. There are several devices which randomly generate numbers which remain valid for a few minutes, displayed to the user and the system gets to know that number through an encrypted channel and you can use that as a.

Other authentications that are more and more coming up, like you have authentication by the biometric fingerprint, face recognition, iris and so on but whatever approach you take, make sure at least two factor authentication is a part of your application development.

<!-- image -->

Now, one lacunae that we have is, at the application the authorization actually is at a total application  level.  So,  SQL  does  not  allow  fine  grained  authorization.  Like we say  that students can see their own grades but not the grades of others. How do you implement this?

SQL does not give you a solution to this. The problem is the database has no idea who the,  (applic)  who  are  the  application  users,  and  SQL,  authorization  is  in  the  level  of tables, columns of tables but not in terms of rows of table. When you are talking about a student can see his or her own grade you are talking about a row of a table.

Now, naturally you have to give the table level  and column level authorization to that person so that he or she can see his or her respective result, but that needed row level authorization which does not exist.

So, you need to kind of take care of it is in a roundabout way, you have to take the user ID,  in  some  way  and  in  the  query  or  in  the  application  program,  you  have  to  do  this validation, which is not very robust but it is a pain point, application level authorization is a pain point that remains.

<!-- image -->

And, but currently it is, have to be done totally in the application layer and therefore you have to be, as an application developer you have to be very, very careful to make sure that  you  have  done  the  proper  application,  for  proper  authentication,  authorization  on that.

Several alternates for fine grained low level authorization, row level, that is, authorization on  rows,  have  been  proposed  but  currently  not  implemented.  Oracle  Virtual  Private Database  allows  predicates  to  be  added  transparently  to  SQL  queries  to  enforce  fine grained authorization but these are not widely available, not standardized, you will not get them on the open source systems as yet.

So,  be  very  careful  and  make  sure  that  your  application  does  proper  authorization  for users  when you have restriction that a user can only see  a part of the information that your application is dealing with.

<!-- image -->

It is also important to keep audit trails. If lets something goes wrong how do you know what  has  gone  wrong?  So,  after  the  fact,  information  is  important  to  detect  security breaches  so  that  it  does  not  happen  again.  Repair  the  damages  that  have  already happened.

So,  keeping  the  audit  trail,  that  is,  keeping  on  writing  this  has  happened,  this  has happened, this, this person has done this, this person has done this regularly is a basic requirement,  which  is  needed  at  a  database  level  so  database  can  have  the  transaction audit trail, but it is also required at the application level because if a breach happens, and many a times a breach will happen at the application level, and you will need this audit trail to be able to investigate later on what went wrong.

In some cases, it may have caused a big losses, and it goes into criminal proceedings and all that, so police investigators need that. In other cases, you need to be able to look at the audit trail to be able to know what is the lacunae in your application.

See,  it  is  not  easy  to  check  for  breaches  in  an  application  because  you  are  an  expert application  developer,  you  are  not  an  expert  in  breaching  security.  So,  oftentimes  you would not be able to visualize the way people are trying to breach it. So, it is important that you keep the trail so that in case something happens you can go back and try to fix it.

## (Refer Slide Time: 23:59)

<!-- image -->

So, those are some general comments about application development. I would wrap up with a quick view at the Mobile Applications. Now mobiles, as you know are the most widely used and any type of application software designed to run on a mobile device, such as smartphone or tablet, computer is becoming very popular.

Now, while the architecture-wise everything is similar, but there are major differences in terms  of  resources,  like  form  factors  which  is  height  is  to  width,  is  very  different  for mobiles, is  much smaller. And at the same time, you have a, in a large  range of  form factors, I mean, you cannot, you cannot just enumerate and design for every form factor though that is the, that is the part which influences your display and navigation. You have limited memory, you have limited computing power, you have limited physical power, you have limited connection bandwidth, so all these are the shortcomings.

At the same time application development gets challenging because mobiles do provide you some additional features that you can make use in, that people have made use in lot of applications, like it has availability of sensors like accelerometer, by which, I mean, you are traveling and your phone tells you at what speed are you traveling.

You have a, you have a way to know the gravitational change, by which, if you rotate your  mobile,  your  display  rotates.  How  does  it  happen?  Because  your  gravitational direction  has  changed.  You  have  gesture-based  navigation.  You  can  just  swipe  on  this touch screen and do this or, just look at the touch screen and do something, and so there are, so it is a very similar development but with a very different ball game.

(Refer Slide Time: 26:03)

<!-- image -->

And that is why if you, even if you are a able web application developer you still need to learn about Mobile App Development separately. Now one aspect of mobile in the web application is, you can view your website on the mobile as a mobile website, which is similar to any other website, consists of browser-based HTML, can display any text, and so on.

But it has to be designed for a handheld device, it has to be designed for a touch screen interface because typically your mobile device will not have a mouse, it will have a touch screen. It could be, click-to-call kind of inputs may also be available. So, even if you are designing a website which is for the mobile device, you have to check out on the factors that you have to take care of.

And if you are doing a, doing a mobile app, then the actual application is downloaded and installed on your device. It is on your device, is running on your device, and you know how to download it for iOS app store and for Android Google Play Store.

Now, this app in turn will pull content and data from the internet, much like the way the website does. So, here, I mean, here the main drive is, I mean at your end, and it is not just a distributed set of code over your browser, your middle tier, at the server end or the back-end alone which gives you the functionality.

But your functionality is significantly encoded as a part of the app, but your, much of your  business  logic  could  be  a  part  of  the  app,  but  it  pulls  the  data  from  the  internet service, download the content as it is, as it can be accessed so that you can also work with it without any internet connection. If you have used maps they will always tell you that you are frequent in this area why do you not download the maps so that you do not need a internet connection to check the map.

(Refer Slide Time: 28:21)

<!-- image -->

So, it is again three tier. I have shown these tiers here, presentation, same as presentation business and data. But in data you often will  have a split. There may be a small local database,  cached  or  not  cached,  which  gives  you  very  quick  turnaround  and  gives,  or, very often used stuff would be there but which has to be small.

And  then  there  is  remote  data  which  is  expensive  to  access  because  you  have  to  go through the mobile network, and but you can have really bulk of that. So, you can see this user interface presentation layer, Application Façade, it is being called. So, this is your presentation. This is your business, which is Application Facade having workflow. You already know the components and the entities, and finally the data access layer.

So, it is a similar architecture but done in a very different component-wise way, and the idea is to do small things at a time because you have very little connection bandwidth for that,  and  of  course  it  needs,  it  is,  they  are  not  portable,  it  needs  customization  across platforms, separate app need to be written for Android and for iOS.

(Refer Slide Time: 29:40)

<!-- image -->

Typically, iOS use Objective-C as a language, where Android use Java or C or C++, so it is platform specific. It is heavily dependent on the operating system. So, while, I mean, there are web apps also which run completely inside the web browser like it does, and it may be powered by some platforms we have already talked of. Ruby on Rails is quite popular here even JavaScript.

And there are hybrid of these two also. Some part is native app, and some part is web app. These options are also there, like some parts you do there and at, at a certain point it brings  up  the  browser,  and  it  tries  to  do  some  part  through  the  browser.  So,  all  these different kind of options exist in your application course. I am sure you will have more insight into this.

(Refer Slide Time: 30:39)

<!-- image -->

So, these are some of the top-level design issues for the mobile app, determine the device, note the resources, very important, consider the bandwidth very carefully, decide on the architectural layers, I have just given an outline, and then select the technology, define UI, select navigation, maintain flow, and so on.

(Refer Slide Time: 31:04)

<!-- image -->

Okay, so that was a kind of a quick run around the application design and development based on databases for the web as well as for the mobile. So, that is what we invested in this week. So, this will give you some idea on whatever we are doing in the databases, how that is going to be really presented to the user and going to bring benefits to them.

The application development course will build up lot more on this and teach you on that side while we will digress now again back into the inside of the database making sure that we are making the right database with the right kind of performance and transactional efficiency and so on. Thank you very much for your attention. See you again in the next module, next week.
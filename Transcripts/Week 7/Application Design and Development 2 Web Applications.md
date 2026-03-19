<!-- image -->

## Database Management Systems Professor Partha Pratim Das Department of Computer Science &amp; Engineering, Indian Institute of Technology Kharagpur Application Design and Development/2: Web Applications

Welcome to Module 32 of Database Management Systems course in the IIT Madras online B.Sc. program. OF

<!-- image -->

<!-- image -->

In the last module we have started discussing about how to develop applications using databases at the backend. We had a glimpse of a collection of application programs. We understood that in spite  of  the  variety  there  is  a  strong  commonality  which  we  call  the  architecture  of  these applications, which is typically three-tier presentation, business logic and data access layer. We saw  the  classification  and  evolution  of  architectures  and  taken  a  glimpse  at  few  sample applications which you are to study and understand in more detail yourself. So, this is what we are going to do.

(Refer Slide Time: 01:11)

2

<!-- image -->

I will start with, though it is not really a part of this course, but since I am not sure how much, how many of you are familiar, so I will start with some fundamental definitions of the World Wide Web, www, so web fundamentals.

(Refer Slide Time: 01:30)

8

<!-- image -->

So, it is a distributed information system, which is based on hypertext, which means that most documents are  hypertext  document.  And  they  are  formatted  using  HTML  which  is  Hypertext Markup Language, which is a W3C standard. So, that contains texts along with specification of the  font  and  other  formatting.  And  it  has,  why  is  it  hypertext,  because  it  has  links  to  other documents, which is associated, it can be associated with certain regions of the text is a click this URL. It can contain forms to collect data from the user. So, this is, this basically is our basic document definition.

## (Refer Slide Time: 02:20)

<!-- image -->

IIT Madras

## Module 32

Das

5

## Uniform Resources Locators

- On the Web, functionality of pointers is provided by Uniform Resource
- URL example: http:/ /www.acm . orglsi gmod
- The first part indicates how the document is to be accessed (prot
- indicates that the document is to be accessed using th Transfer Protocol. "http"
- The second part gives the unique name of a machine on the Inter
- The rest of the URL identifies the document within the machine
- The local identification can be:
- The name of a file on the machine: A file at path
- C: /WINDOWS /media/Alarmo1 wav of local machine can be acces

## Uniform Resources Locators

- On the Web, functionality of pointers is provided by Uniform Resource
- URL example: http: //www . acm org/sigmod
- The first part indicates how the document is to be accessed (prot
- indicates that the document is to be accessed th Transfer Protocol. 'http"
- The second part gives the unique name of a machine on the Inter
- The rest of the URL identifies the document within the machine
- The local identification can be:
- The path name of a file on the machine: A file at
- wav

<!-- image -->

## Module J2

WW

2

<!-- image -->

IIT Madras

## Module 32

## Uniform Resources Locators

- On the Web; functionality of pointers is provided by Uniform Resource

URL example (ttp Y/www.acm . org/ sigmod

- The first part indicates how the document is to be accessed (prot
- "http" indicates that the document is to be accessed th Transfer Protocol. using
- The second part gives the unique name of a machine on the Inter
- The rest of the URL identifies the document within the machine
- The local identification can be:
- The path name of a file on the machine: A file at

<!-- image -->

## Uniform Resources Locators

- On the Web, functionality of pointers is provided by Uniform Resource
- URL example: http:/ /www.acn igmod org/sil
- The first part indicates how the document is to be accessed (prot
- indicates that the document is to be accessed th Transfer Protocol. 'http"
- The second part gives the unique name of a machine on the Inter
- The rest of the URL identifies the document within the machine
- The local identification can be:
- The path name of a file on the machine: A file at C: /WINDOWS /media/Alarmo1 . wav of local machine can be acces
- wav
- file:/ /localhost /c: /WINDOWS /media/Alarmo1 wav

<!-- image -->

Now, for identity, we have a what is called a uniform resource locator. That is, since documents are  distributed  worldwide,  I  need  to  have  a  mechanism  to  identify  it  locate  it.  So,  we  have  a URL. And if you look at this URL, there is a initial part which is http standing for hypertext transfer protocol, which says in what mechanism I should interact with that document. And we will talk a little bit more about that later.

Second part locates the unique name of the machine in the Internet in this entire world which is supposed to have that document and whatever you have after that could be very, very long is the actual  location  of  the  document  within  that  machine.  So,  one  is  how  you  interact  with  the document, where do you find the document, which machine and then the rest is the location in the machine. So, it could be also a document in your machine or in some other machine. So, for example, if I want to access this document, a local machine, then I will use a starting which is file colon, different from http colon. This tells us go and look in the Internet, world wide web. This tells us look in the local machine. And then it gives the path.

So, since this pertains to local machine, so I do not need to say that how to identify the machine. I can just directly go to the path of the document. Of course, there is an alternate way. The local machine can be called a local host, which could be, which could again have an IP address, which is  locating  the  machine  and  then  you  have  the  path  to  the  actual  document  in  that  machine. Besides  the  protocol,  the  machine,  you  could  also  actually  send  a  query  to  that.  Instead  of looking for a document you can send a query. So, you can send parameters with this request and that is, here, what we are saying is you do search with parameter q is equal to silberschatz. So, you can give multiple parameters. So, that is the basic purpose of the URL.

(Refer Slide Time: 05:15)

<!-- image -->

And  typically  you  will  hear  that  there  are  three  terms  that  go  around.  Of  course,  URL  is something which you are most familiar with, which is this whole thing of this. This is called URN that is the name of the document. This is the, I am sorry, this is URI, the identifier, the actual  what  name  the  document  is  stored  with.  This  is,  these  are  called  the  URN,  Uniform Resource Name. So, URN is more like a person's name and URL is more like person's address where you can find that person. So, we will typically use the term URL and at times when we want to generalize we will say URI, but mostly URL.

(Refer Slide Time: 06:18)

<!-- image -->

HTML  we  have  talked  off.  HTTP  is  a  protocol  which  is  used  for  communicating  with  the machine which has or which knows where your document can be found. HTML, as we said, will select from a set of options, pop-up menus, radio, etc., will enter values and you can fill up the input as you always do.

(Refer Slide Time: 06:49)

<!-- image -->

This is an HTML sample just for your understanding. So, HTML is these are known as tags. So, you have a corner bracket and you write some, these are predefined. I mean, in certain way you can define them, but take this as predefined. Every tag has a meaning. So, it is a parenthesized expression, which starts from a tag HTML and ends with the same tag and the end is marked by having a forward slash before the tag name.

So, I have the whole HTML page. And in this I have a body which gives me the body of the page. In the body I have a table and the tag actually is table and the tag qualifier is border which says that the table must come with a border. This is the end of table. And then we have tags for table entries. So, tr is table row. This table row ends. So, we are talking about this, first row th says it is a table header. So, you can see that it is, it comes as a different font. It comes in bold and little bigger.

So, th ID \th tells you that ID is a header. This is the next header. This is the next header. So, you can see there are three headers. There is the first row. This is the second row which says table data td, the next one, 00128, then Zhang, then comp sci the three. So, everything is in terms of parenthesis  and  this  entire  thing  forms  another  row  and  the  sequence  of  rows  any  number  of them will be the entire table as you can see.

So, after that you have form action. So, you have another HTML element called form which is to enter data. Now, we say with the form we say the qualifier is action for which we have given a name person query. How do we know this action? So, we will call it person query. Method is get which says that when the HTML is completed, submitted, then what should we do you should get that data. That is what I intend to do.

Now, this on this form, here if you look at, then I have written search for which is a normal text comes as search for and then here I have a drop down which has multiple options. One option is student, one option is instructor. So, it  is saying option begin option end, option begin option end. So, as I click on here at this point, this will drop down and whatever I have selected, it gets becomes the option that have taken.

Then I have a break, because I want to go to the next line. Then I was plain text name, which I say is followed by a box, edit box, input type is text, size is 20, its internal name is name. So, I will identify whatever you enter. I will identify it as name. And then I have input type is submit, the value is submit that it will, you will submit this to get value is submit. So, this button shows as a submit. So, if you just correspond you will be able to, and after you have done this for a couple of HTML pages and corresponding displays, you will learn this pretty easily. It is not that you regularly need to write in raw HTML, but it helps to be able to read it quickly.

(Refer Slide Time: 11:23)

8

<!-- image -->

Now, HTTP protocol is connectionless. What is connectionless? Connectionless is say you have, when you call someone on a phone, then it is  connection oriented,  because you  dial,  you  get connected  as  long  as  you  want  to  talk,  and  then  you  disconnect.  So,  you  are  thoroughly connected. But when you send a WhatsApp message, it is connectionless, because you send a message,  the  person  will  see  it  at  some  point  of  time  and  the  person  will  respond.  You  will receive that message and you will see at some point of time. It is not necessary that both of you have to be present at the same time and remain connected all through for this communication to go on. So, that is connectionless.

So, HTTP is connectionless. You send a request, you get a response from the servers. You send another request, you get a response. Now, this is fine as long as you are just requesting for static pages like in Google. You put a search query, you sent, it gives you a response. You read that, go to the links and so on. But suppose when you are in net banking, you have logged in, send the request, you have got the login, now when you send the next request that show me the account details,  the  server  has  to  know  that  it  is  the  same  you  who  were  authenticated  earlier,  who  is asking for that report, otherwise it cannot be given.

Which means that  every  time  this  kind  of  an  authentication  information  has  to  go  with  your request for information from the server. This becomes a huge load on the server. Also becomes a pretty much of a security risk, because your sending your authentication information every time. So, if somebody can, somebody, everybody will get a lot more of opportunity to break it. So, we use something here as what is called a cookie. Cookie is a small unit of information.

So, when you do the authentication, send the request you are authenticated, the response comes back saying that you are authenticated and it says it starts a session has started. That is  for  a certain period of time as you keep on doing the interaction the server is going to remember that it is you. How will the server do that? It will send you a piece of information called a cookie.

(Refer Slide Time: 14:21)

2

5

<!-- image -->

The small text contains identifying information in encrypted form. Now, every time the time you make the next request, this cookie goes back with that request and server as it has issued the cookie remembers that it has issued the cookie. So, when it gets the request along with a cookie, it  checks  whether  that  that  is  a  valid  cookie  which  is  live  scale.  If  it  then  it  continues  the operation. But if it does not find a cookie here, then it sends for fresh authentication. So that is the  basic  mechanism.  And  for  the  time  for  which  this  liveliness  of  the,  I  should  say,  virtual connection, this is not direct connection, but a virtual connection remains is called a session.

So,  while  working  on  different  net  banking  or  booking  sites  and  so  on,  you  must  have  come across that you have 10 seconds left, you have two minutes left, and then you have suddenly told your connection will get timeout. That is the concept of the timeout. Now, the question is, why does not the server remember the cookie forever? That is for several reasons. One is in that way, it does not, if you forget to explicitly log out and cancel the cookie, it will never get lost. It will remain to be in the server and server will create a lot of this chunk.

But a more important concern is it may be possible that you are not using the application for a long time means that you may not have access to that application. Somebody else may have got an access to the application. So, to protect you, it chooses a timeout option that after this much time from the last request if no other request has happened, then it is timed out. The cookie is considered dirty and thrown away. So, that is the concept of a session.

(Refer Slide Time: 16:32)

5

<!-- image -->

Now, web browser, all of you know. The web browser is the application program through which HTML is rendered. The rendering is a process by which the text is made into the graphics. And there is  certain  types  of  styling  and  non-text  element  can  be  shown  like  images,  videos,  even sound. So, there is a rendering machine which does that. I will not take more time to go into the browsers. As of last year, it is estimated that about nearly 5 billion people used a browser, most used is Google Chrome with 64%, followed by Apple's Safari at 19%.

(Refer Slide Time: 17:17)

<!-- image -->

Web server on the other side is a is basic service provider, which gets a HTTP request, forms a response to that for some by through some mechanism, makes it into an HTML and sends you back. So, it could be a web service, could be simply another program which does this or it could be a big web server and as you as you learn more you will see that. But the basic purpose of the web server is to get an HTTP request and give out the result HTML.

(Refer Slide Time: 17:57)

5

<!-- image -->

Now, other than HTTP also, there are other kinds of services particularly used for transferring larger volumes of data or maybe some unstructured data they are known as REST, JSON and so on. So, when you learn about web services in depth, you will learn about them. I just wanted to mention so that you know where these terms exists.

(Refer Slide Time: 18:20)

<!-- image -->

So, this is, in short, this is what, where we are. So, this is in your web architecture, this is your frontend,  this  is  your  web  server,  which  will  actually  go  to  the  database  or  the  file  system.  It could get the document directly from the file system, it could run a query from the database, get it  here, make it into HTML. So, you send a request here, which goes in HTTP, the web server does  this  backend  job  and  sends  back  a  response  which  is  HTML.  So,  this  is  a  basic  web architecture and you can see that the application architecture is basically trying to follow that.

2

## (Refer Slide Time: 18:56)

<!-- image -->

Scripting, scripts are nothing but programming languages, but the difference being that they are typically  text,  they  are  small,  and  they  are  usually  interpreted  within  another  program.  So, typically, when we write a C++ program, we need to first write the program, compile it, and on compilation correct, we execute. So, if we make a change in the source program, my executable does not change, but the script is not like that. Script is a text, piece of text, which is a program, some instructions, and every time you want to run it, you need to interpret that is you compile and run at the same time. These are typically small and done for dynamic systems. So, there are several scripting languages. Some of them I have mentioned here.

(Refer Slide Time: 19:51)

<!-- image -->

<!-- image -->

Now, here, there are a lot of tasks for which we need scripting in the in case of web application. Many of those scripts run in the browser and they are called client-side script. For example, I put a date and it needs to be validated to be corrected. You could have done it through going to the server also. You could take the date, go to the server, server or application layer checks, whether it  is  a  valid  date  comes  back and tells you. That would mean a lot more of Internet time, that would mean lot of delay.

Whereas to check for a valid date is a simple logic. So, you can implement it in terms of a script, which can run within the browser. This is an interesting concept that you are running a program not  directly  on  the  machine,  but  you  are  running  it  through  a  simulation  and  that  is  in  the browser. So, it is something like you have a similar situation for a JVM or PVM for Java and Python, but this is a very typical client-side scripting that you can do within the browser itself.

The other option is you will have several such requirements of processing, validation, extraction in the server-end. So, those are also often done in terms of scripting language. Those are called clients,  server-side  scripting.  So,  you  have  scripting,  but  these  two  are  different.  At  the server side, you could be doing connecting to a database, you could be extracting data and so on, so forth. Now, the question is, why do you use it as a script, because many times every individual task is a small one. And it is after having done the task you need to create the HTML.

So, this process of creating the HTML or the tags and so on, so that you can display it nicely, is far  more  difficult  to  do  in  a  normal  programming  language  than  in  a  script  which  you  can visualize as if you have an HTML page with certain information missing, the script can come and set those information so that your page is ready. Now, since this is in the server, this has lot more power. This can have a lot more computing. So, typically, it does not, unlike the client side, it  does  not  run  within  another  application,  you  may  have  a  separate  engine  which  runs  your script, which is called the scripting engine.

So, a modified view turns out to be that you have client-side scripts which validates. And when it is validated, then the request can come, it is taken up by the preprocessor, chooses the right script in the scripting engine, which does the scripting, does the computation, gets the data, generates the result as a translated HTML, locates that page template, gets the final HTML, returns it back here to the client. So, scripting at both these two ends basically are technological mechanisms to make the whole system far more efficient and easy to use and easy to change.

(Refer Slide Time: 23:21)

<!-- image -->

So, there are several ways to do client-side scripting. Many browsers execute them in the safe mode at the client side, which means that your security is not compromised. There are several naturally JavaScript you must have heard of. This is something you need a flash, plug-in to be set to see different media files. This is to see your SVG kind of dynamic graphics files, applets and so on. It could be variety of different these kinds of client side scripting options exist.

## (Refer Slide Time: 24:04)

6

<!-- image -->

Now, security is certainly a concern for the client-side scripting, because what if some malicious script has come to your machine, and through the browser, it spoils your machine. So, for that, there is very limited options are given to the scripting language at the client side. For example, typically,  the  scripts  are  not  allowed  to  write  anything  on  your  disk,  because  then  they  could write  a  virus.  It  will  not  allow  any  Java  applet  code  or  equivalent  scripting  language  will  not allow anything to be executed outside of the browser. So, that security is kind of built in.

(Refer Slide Time: 24:45)

2

<!-- image -->

The most common is JavaScript which follows a document object model. I will not get into the details of that. You study when you do the web services in general.

(Refer Slide Time: 24:58)

<!-- image -->

But this is just to give you an example. For example, here, you say that the script is JavaScript and you are doing a validation function. What it is saying that you have taken a credit amount, credits amount by getting the element by ID. So, credits was a HTML element, some value has been entered and you take that. And what you are checking? You checking is NAN, NAN is not a number. The credit has to be a number. So, if it is not a number, it fails. This becomes true that is it is not a number.

Is credit less than equal to 0 or if credit greater than equal to 16. If that happens, then you throw an alert. So, what you get to see that you enter 5, it works okay. You enter -3 or you enter PPD or you  enter  17,  you  will  get  an  alert,  saying  that  the  credit  must  be  and  this  whole  thing  is happening without an HTTP request being sent to the sender all in the JavaScript. So, that is the basic mechanism of JavaScript.

(Refer Slide Time: 26:13)

<!-- image -->

Similarly,  you  have  server-side  scripts,  as  I  said,  which  are,  which  take  a  request,  do  the scripting,  processing  and  prepares  your  final  HTML  for  return.  The  most  commonly  used  are these  days  are  JSP,  PHP  once  ASP  used  to  be  also  very  popular  earlier.  But  some  generalpurpose languages like Python can also be used for this purpose because they are also scripting languages.

(Refer Slide Time: 26:46)

5

<!-- image -->

g

And as a part of the  scripting,  as  I  said,  that  instead  of  just  running  the  script  within  another program, it makes it into a small program by itself. So, these are called servlets. Why servlets?

They are servers, because they are providing a service based on the input. And they are like book to booklet, is a small book similarly server to servlet is a small service, just one small service, and you can have many of them.

So, that it becomes a lot more manageable. You do not, because at a time at any request, you do not have too many things to do. Every request is a small thing and you would have possibly a separate servlet. They run on thread, because same instances of the, I mean, multiple instances of the same servlet could run at the same time, because different users have requested for the same service. So, servlet is a very strong concept in the on the server side.

(Refer Slide Time: 27:54)

<!-- image -->

8

So,  these  are  some  typical  examples  which  is  running  the  servlet  and,  in  the  format,  actually filling in the HTML. So, this is a header line, this is a body part we had shown and what does it get in the body you can.

## (Refer Slide Time: 28:19)

6

<!-- image -->

This is where it is building the body. It goes to the database to get the data. The HTMLs for the table and this is for the header part we had seen and this is where one by one for each as many results have come for each it is creating a row and putting in, very simple. I mean, the HTML example you saw that is getting automatically generated based on the result that we have got from the database. How we got it from the database is something we will discuss, but this is how a servlet typically would work.

(Refer Slide Time: 28:58)

2

<!-- image -->

So, naturally, servlets have sessions. We have talked about. So, you can see that for a request if the  get  session  tells  you  that  the  session  is  live  then  you  continue,  otherwise  you  redirect  to authenticate and create, start a new session after authentication and keep that as a new cookie.

(Refer Slide Time: 29:23)

<!-- image -->

This is servlets are supported on multiple web servers like Apache Tomcat is one of the most widely used then IBM, WebSphere, there are several of them. J2EE has options for that. (Refer Slide Time: 29:38)

5

<!-- image -->

The other one, which is very popular that is java server page, which is kind of the same concept, the only difference being that there you are using it like a programming language and generating the HTML. Here you have the HTML in the format and you are just putting the, so you have written as if an HTML and then you have certain parts which are missing, which is like what you will  put  in  this,  hello,  the  name  part  we  will  get  as  a  parameter  and  put  that  so  that  part  is missing. So, it is compiled into java plus servlet and then you run it. The advantage is it is much easier to write an HTML embedding in this way, instead of writing it by text output as we are seeing here earlier.

<!-- image -->

(Refer Slide Time: 30:36)

<!-- image -->

And  JSP  is  actually  getting  preferred  a  lot  over  the  competitive  ones  like  ASP.  ASP  is proprietary for Microsoft and uses proprietary VB, JSP is platform independent, portable easily. Against pure servlets, as I said, it is much easier to write the HTML format of JSP than having to write them by cout statements or print line statements and so on. And certainly, do not confuse between JSP Java Server Page and JavaScript. JavaScript is client side, runs in the browser. JSP server side, runs in the server, and obviously it is much better than static HTML which cannot have a dynamic information.

(Refer Slide Time: 31:24)

<!-- image -->

So, we have got introduced to some basic notions of the web fundamentals and the technology for applications about including scripting and servlets. This brings us to the end of the module. See  you  again  in  the  next  module.  Thank  you  for  your  attention.  We  will  continue  our discussions on the application development.

<!-- image -->
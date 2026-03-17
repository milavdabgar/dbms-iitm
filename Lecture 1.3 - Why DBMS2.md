![Image](Lecture 1.3 - Why DBMS2_artifacts/image_000000_bbaa640f2b7c7b6f18cdf441c797dcf1ce99e755b6ef0a9bbf7b581538bddcab.png)

## Module 03

Partha Pratim Das

Objectives &amp; Outline

File Systems vs Databases Python viz-a-viz SQL Parameterized Comparison

Module Summary

## Database Management Systems Module 03: Why DBMS?/2

## Partha Pratim Das

Department of Computer Science and Engineering Indian Institute of Technology, Kharagpur ppd@cse.iitkgp.ac.in

Partha Pratim Das

![Image](Lecture 1.3 - Why DBMS2_artifacts/image_000001_0d9dfbde1de846c018eea32fe6aba21e8a9c7f3c69ef770101468a6cfb66a6e5.png)

## Module 03

Partha Pratim Das

## Objectives &amp; Outline

File Systems vs Databases

Python viz-a-viz SQL

Parameterized

Comparison

Module Summary

## Module Recap

- Evolution of Data and Records Management
- History of DBMS

![Image](Lecture 1.3 - Why DBMS2_artifacts/image_000002_0d2e8daa05c74407b310229f101057782122d2bf078613dc8c643ca2fdb280b5.png)

Module 03

Partha Pratim Das

Objectives &amp; Outline

File Systems vs

Databases

Python viz-a-viz SQL

Parameterized

Comparison

Module Summary

## Module Objectives

- Comparison of File based data management and DBMS

![Image](Lecture 1.3 - Why DBMS2_artifacts/image_000003_0d2e8daa05c74407b310229f101057782122d2bf078613dc8c643ca2fdb280b5.png)

## Module 03

Partha Pratim Das

## Objectives &amp; Outline

File Systems vs Databases

Python viz-a-viz SQL Parameterized Comparison

Module Summary

## Module Outline

- File handling by Python viz-a-viz DBMS - Bank Transaction example
- Parameterized Comparison

![Image](Lecture 1.3 - Why DBMS2_artifacts/image_000004_44b3949ffed21c5ac1d653f0732b20837d9420307dd478fe439496b389adbd32.png)

## Module 03

Partha Pratim Das

Objectives &amp; Outline

File Systems vs Databases

Python viz-a-viz SQL Parameterized Comparison

Module Summary

## Case Study of Bank Transaction

![Image](Lecture 1.3 - Why DBMS2_artifacts/image_000005_0d9dfbde1de846c018eea32fe6aba21e8a9c7f3c69ef770101468a6cfb66a6e5.png)

## Module 03

Partha Pratim Das

Objectives &amp; Outline

File Systems vs Databases

Python viz-a-viz SQL Parameterized Comparison

Module Summary

## Case study: A bank transaction

## Banking Transaction System

Consider a simple banking system where a person can open a new account, transfer fund to an existing account and check the history of all her transactions till date.

The application performs the following checks:

- If the account balance is not enough, it will not allow the fund transfer
- If the account numbers are not correct, it will flash a message and terminate the transaction.
- If a transaction is successful, it prints a confirmation message.

![Image](Lecture 1.3 - Why DBMS2_artifacts/image_000006_bbaa640f2b7c7b6f18cdf441c797dcf1ce99e755b6ef0a9bbf7b581538bddcab.png)

## Module 03

Partha Pratim Das

Objectives &amp; Outline

## File Systems vs Databases

Python viz-a-viz SQL Parameterized Comparison

Module Summary

## Case study: A bank transaction (2)

We will use this banking transaction system to compare various features of a file-based (spreadsheet/.csv files) implementation viz-a-viz a DBMS-based implementation

- Account details are stored in
- Accounts.csv for file-based implementation
- Accounts table for DBMS implementation
- The transaction details are stored in
- Ledger.csv file for file-based implementation
- Ledger table for DBMS implementation

In the following slides we discuss a fund transfer transaction.

Source :

https: // github. com/ bhaskariitm/ transition-from-files-to-db/ tree/ main

## Partha Pratim Das

![Image](Lecture 1.3 - Why DBMS2_artifacts/image_000007_bbaa640f2b7c7b6f18cdf441c797dcf1ce99e755b6ef0a9bbf7b581538bddcab.png)

## Module 03

Partha Pratim Das

Objectives &amp; Outline

File Systems vs Databases

Python viz-a-viz SQL Parameterized Comparison

Module Summary

## Python viz-a-viz SQL

![Image](Lecture 1.3 - Why DBMS2_artifacts/image_000008_bbaa640f2b7c7b6f18cdf441c797dcf1ce99e755b6ef0a9bbf7b581538bddcab.png)

## Module 03

Partha Pratim Das

Objectives &amp; Outline

File Systems vs Databases

Python viz-a-viz SQL Parameterized Comparison

Module Summary

## Bank Transaction: Python viz-a-viz SQL

## Python

def begin\_Transaction(creditAcc, debitAcc, amount):

temp = [] success = 0

- # Open file handles to retrieve and store transaction data
- f\_obj\_Account1 = open('Accounts.csv', 'r')

f\_reader1 =

csv.DictReader(f\_obj\_Account1)

- f\_obj\_Account2 = open('Accounts.csv', 'r')
- f\_reader2 =

csv.DictReader(f\_obj\_Account2)

- f\_obj\_Ledger = open('Ledger.csv', 'a+')
- f\_writer =

csv.DictWriter(f\_obj\_Ledger, fieldnames=col\_name\_Ledger)

Database Management Systems

SQL

// Handled implicitly by the DBMS

![Image](Lecture 1.3 - Why DBMS2_artifacts/image_000009_bbaa640f2b7c7b6f18cdf441c797dcf1ce99e755b6ef0a9bbf7b581538bddcab.png)

## Module 03

Partha Pratim Das

Objectives &amp; Outline

File Systems vs

Databases

Python viz-a-viz SQL

Parameterized

Comparison

Module Summary

## Bank Transaction: Python viz-a-viz SQL (2)

## Python

try:

for sRec in f\_reader1: #CONDITION CHECK FOR ENOUGH BALANCE if sRec["AcctNo"] == debitAcc and int(sRec["Balance"]) &gt; int(amt):

...

## SQL

do $$ begin amt = 5000; sendVal = '1800090'; recVal = '1800100'; select balance from accounts into sbalance where account\_no = sendVal; if sbalance &lt; amt then ... $$

![Image](Lecture 1.3 - Why DBMS2_artifacts/image_000010_bbaa640f2b7c7b6f18cdf441c797dcf1ce99e755b6ef0a9bbf7b581538bddcab.png)

## Module 03

Partha Pratim Das

Objectives &amp; Outline

File Systems vs

Databases

Python viz-a-viz SQL

Parameterized

Comparison

Module Summary

## Bank Transaction: Python viz-a-viz SQL (3)

## Python

## try:

for

sRec

in

f\_reader1:

#CONDITION

CHECK

FOR

ENOUGH

BALANCE

if

sRec["AcctNo"]

==

debitAcc

and

int(sRec["Balance"])

&gt;

int(amt):

for rRec in f\_reader2:

if

rRec["AcctNo"]

== creditAcc:

sRec["Balance"]

=

#DEBIT

str(int(sRec["Balance"])-int(amt))

temp.append(sRec)

...

## SQL

do $$ begin amt = 5000; sendVal = '1800090'; recVal = '1800100'; select balance from accounts into sbalance where account\_no = sendVal; if sbalance &lt; amt then raise notice "Insufficient balance"; else update accounts set balance = balance - amt where account\_no = sendVal; ... $$

![Image](Lecture 1.3 - Why DBMS2_artifacts/image_000011_bbaa640f2b7c7b6f18cdf441c797dcf1ce99e755b6ef0a9bbf7b581538bddcab.png)

## Module 03

Partha Pratim Das

Objectives &amp; Outline

File Systems vs

Databases

Python viz-a-viz SQL

Parameterized

Comparison

Module Summary

## Bank Transaction: Python viz-a-viz SQL (4)

## Python

## try:

for

sRec

in

f\_reader1:

#CONDITION

CHECK

FOR

ENOUGH

BALANCE

if

sRec["AcctNo"]

==

debitAcc

and

int(sRec["Balance"])

&gt;

int(amt):

for rRec in f\_reader2:

if

rRec["AcctNo"]

==

creditAcc:

sRec["Balance"]

=

#DEBIT

str(int(sRec["Balance"])

-

int(amt))

temp.append(sRec)

#

Critical

point

f\_writer.writerow({

"Acct1":sRec["AcctNo"],

"Acct2":rRec["AcctNo"],

"Amount":amt,

"D/C":"D"})

rRec["Balance"]

=

#CREDIT

str(int(rRec["Balance"])

+

int(amt))

temp.append(rRec)

...

Database Management Systems

Partha Pratim Das

## SQL

do $$ begin amt = 5000; sendVal = '1800090'; recVal = '1800100'; select balance from accounts into sbalance where account\_no = sendVal; if sbalance &lt; amt then raise notice "Insufficient balance"; else update accounts set balance = balance - amt where account\_no = sendVal; insert into ledger(sendAc, recAc, amnt, ttype) values(sendVal, recVal, amt, 'D'); update accounts set balance = balance + amt where account\_no = recVal; ... 03.12

![Image](Lecture 1.3 - Why DBMS2_artifacts/image_000012_bbaa640f2b7c7b6f18cdf441c797dcf1ce99e755b6ef0a9bbf7b581538bddcab.png)

## Module 03

Partha Pratim

Das

Objectives &amp;

Outline

File Systems vs

Databases

Python viz-a-viz SQL

Parameterized

Comparison

Module Summary

## Bank Transaction: Python viz-a-viz SQL (5)

## Python

| try: for sRec in f_reader1: #CONDITION CHECK FOR ENOUGH BALANCE if sRec["AcctNo"] == debitAcc and int(sRec["Balance"]) > int(amt): for rRec in f_reader2: if rRec["AcctNo"] == creditAcc: sRec["Balance"] = #DEBIT str(int(sRec["Balance"]) - int(amt)) temp.append(sRec) # Critical point f_writer.writerow({"Acct1":sRec["AcctNo"], "Acct2":rRec["AcctNo"], "Amount":amt, "D/C":"D"}) rRec["Balance"] = #CREDIT str(int(rRec["Balance"]) + int(amt)) temp.append(rRec) f_writer.writerow({"Acct1":rRec["AcctNo"], "Acct2":sRec["AcctNo"], "Amount":amt,"D/C": "C"}) success = success + 1 break f_obj_Account1.seek(0) next(f_obj_Account1) for record in f_reader1: if record["AcctNo"] != temp[0]["AcctNo"] and record["AcctNo"] != temp[1]["AcctNo"]:   |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| except: print("Wrong input entered !!!") Database Management Systems                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |

## SQL

do $$ begin amt = 5000; sendVal = '1800090'; recVal = '1800100'; select balance from accounts into sbalance where account\_no = sendVal; if sbalance &lt; amt then raise notice "Insufficient balance"; else update accounts set balance = balance - amt where account\_no = sendVal; insert into ledger(sendAc, recAc, amnt, ttype) values(sendVal, recVal, amt, 'D'); update accounts set balance = balance + amt where account\_no = recVal; insert into ledger(sendAc, recAc, amnt, ttype) values(recVal, sendVal, amt, 'C'); commit; raise notice "Successful"; end if; end; $$

Partha Pratim Das

03.13

![Image](Lecture 1.3 - Why DBMS2_artifacts/image_000013_bbaa640f2b7c7b6f18cdf441c797dcf1ce99e755b6ef0a9bbf7b581538bddcab.png)

## Module 03

Partha Pratim

Das

Objectives &amp; Outline

File Systems vs

Databases

Python viz-a-viz SQL

Parameterized

Comparison

Module Summary

## Bank Transaction: Python viz-a-viz SQL (6)

## Python

#Writing back to the file f\_obj\_Account1.close()

f\_obj\_Account2.close()

f\_obj\_Ledger.close()

if success == 1:

f\_obj\_Account = open('Accounts.csv', 'w+', f\_writer = csv.DictWriter(f\_obj\_Account,

fieldnames=col\_name\_Account)

f\_writer.writeheader()

for data in temp:

f\_writer.writerow(data)

f\_obj\_Account.close()

print("Transaction is successful

!!")

else:

print('Transaction failed : Confirm Account details')

SQL

// Handled implicitly by the DBMS

newline='')

![Image](Lecture 1.3 - Why DBMS2_artifacts/image_000014_0d2e8daa05c74407b310229f101057782122d2bf078613dc8c643ca2fdb280b5.png)

Module 03

Partha Pratim

Das

Objectives &amp;

Outline

File Systems vs

Databases

Python viz-a-viz SQL

Parameterized

Comparison

Module Summary

## Comparison

| Parameter                                          | File Handling via Python                                                                                    | DBMS                                                                                                                   |
|----------------------------------------------------|-------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------|
| Scalability with re- spect to amount of data       | Very difficult to handle insert, update and querying of records                                             | In-built features to provide high scalability for a large number of records                                            |
| Scalability with re- spect to changes in structure | Extremely difficult to change the structure of records as in the case of adding or removing attributes      | Adding or removing attributes can be done seamlessly using simple SQL queries                                          |
| Time of execution                                  | In seconds                                                                                                  | In milliseconds                                                                                                        |
| Persistence                                        | Data processed using temporary data struc- tures have to be manually updated to the file                    | Data persistence is ensured via automatic, sys- tem induced mechanisms                                                 |
| Robustness                                         | Ensuring robustness of data has to be done manually                                                         | Backup, recovery and restore need minimum manual intervention                                                          |
| Security                                           | Difficult to implement in Python (Security at OS level)                                                     | User-specific access at database level                                                                                 |
| Programmer's productivity                          | Most file access operations involve extensive coding to ensure persistence, robustness and security of data | Standard and simple built-in queries reduce the effort involved in coding thereby increasing a programmer's throughput |
| Arithmetic opera- tions                            | Easy to do arithmetic computations                                                                          | Limited set of arithmetic operations are avail- able                                                                   |
| Costs                                              | Low costs for hardware, software and human resources                                                        | High costs for hardware, software and human resources                                                                  |

## Partha Pratim Das

![Image](Lecture 1.3 - Why DBMS2_artifacts/image_000015_bbaa640f2b7c7b6f18cdf441c797dcf1ce99e755b6ef0a9bbf7b581538bddcab.png)

## Module 03

Partha Pratim Das

Objectives &amp; Outline

File Systems vs Databases

Python viz-a-viz SQL

Parameterized Comparison

Module Summary

## Parameterized Comparison

![Image](Lecture 1.3 - Why DBMS2_artifacts/image_000016_32155ccc63eaf8ac3b5d36be7560257f854d0b99536286a17a16546fbab339af.png)

## Module 03

Partha Pratim Das

Objectives &amp; Outline

File Systems vs Databases

Python viz-a-viz SQL

Parameterized Comparison

Module Summary

## Scalability

## File handling via Python

- Number of records: As the # of records increases, the efficiency of flat files reduces:
- the time spent in searching for the right records
- the limitations of the OS in handling huge files
- Structural Change: To add an attribute, initializing the new attribute of each record with a default value has to be done by program. It is very difficult to detect and maintain relationships between entities if and when an attribute has to be removed.

## DBMS

- Number of records: Databases are built to efficiently scale up when the # of records increase drastically.
- In-built mechanisms, like indexing, for quick access of right data.
- Structural Change: During adding an attribute, a default value can be defined that holds for all existing records - the new attribute gets initialized with the default value. During deletion, constraints are used either not to allow the removal or ensure its safe removal

## Partha Pratim Das

![Image](Lecture 1.3 - Why DBMS2_artifacts/image_000017_bbaa640f2b7c7b6f18cdf441c797dcf1ce99e755b6ef0a9bbf7b581538bddcab.png)

## Module 03

Partha Pratim Das

Objectives &amp; Outline

File Systems vs Databases

Python viz-a-viz SQL

Parameterized Comparison

Module Summary

## Time and Efficiency

## File handling via Python

- The effort needed to implement a file handler is quite less in Python
- In order to process a 1GB file, a program in Python would typically take few seconds.

## DBMS

- The effort to install and configure a DB in a DB server is expensive &amp; time consuming
- In order to process a 1GB file, an SQL query would typically take few milliseconds.
- If the number of records is very small, the overhead in installing and configuring a database will be much more than the time advantage obtained from executing the queries.
- However, if the number of records is really large, then the time required in the initialization process of a database will be negligible as compared to the time saved in using SQL queries.

![Image](Lecture 1.3 - Why DBMS2_artifacts/image_000018_ed2b8c74ea63f4b2fac6f8382d928b2ae49209ec0cb7c41d1b8af9b37363394d.png)

![Image](Lecture 1.3 - Why DBMS2_artifacts/image_000019_32155ccc63eaf8ac3b5d36be7560257f854d0b99536286a17a16546fbab339af.png)

## Module 03

Partha Pratim Das

Objectives &amp; Outline

File Systems vs Databases

Python viz-a-viz SQL

Parameterized Comparison

Module Summary

## Persistence, Robustness, Security

## File handling via Python

- Persistence : Data processed using in-memory data structures stay in the memory during processing. After updates, these are manually updated to the file on disk
- Robustness : Ensuring consistency, reliability and sanity is manual via multiple checks. On a system crash, a transaction may cause inconsistency or loss of data.
- Security : Extremely difficult to implement granular security in file systems. Authentication is at the OS level.

## Database Management Systems

## DBMS

- Persistence : Data persistence is ensured via automatic, system mechanisms. The programmer does not have to worry about the data getting lost due to manual errors
- Robustness : Backup, recovery &amp; restore need minimum manual intervention. The backup and recovery plan can be devised for automatic recovery on a crash
- Security : DBMS provides user-specific access at the database level with restriction for to view only access

## Partha Pratim Das

![Image](Lecture 1.3 - Why DBMS2_artifacts/image_000020_0d9dfbde1de846c018eea32fe6aba21e8a9c7f3c69ef770101468a6cfb66a6e5.png)

Module 03

Partha Pratim Das

Objectives &amp; Outline

File Systems vs Databases

Python viz-a-viz SQL

Parameterized Comparison

Module Summary

## Programmer's Productivity

## File handling via Python

- Building the file handler : Since the constraints within and across entities have to be enforced manually, the effort involved in building a file handling application is huge
- Maintenance : To maintain the consistency of data, one must regularly check for sanity of data and the relationships between entities during inserts, updates and deletes
- Handling huge data : As the data grows beyond the capacity of the file handler, more efforts are needed

## DBMS

- Configuring the database : The installation and configuration of a database is specialized job of a DBA. A programmer, on the other hand, is saved the trouble
- Maintenance : DBMS has in-built mechanisms to ensure consistency and sanity of data being inserted, updated or deleted. The programmer does not need to do such checks
- Handling huge data : DBMS can handle even terabytes of data - Programmer does not have to worry

![Image](Lecture 1.3 - Why DBMS2_artifacts/image_000021_b551d1d039a350a56349b412170007d20638ad0732feb40b06cdb100cf6ab680.png)

## Module 03

Partha Pratim Das

Objectives &amp; Outline

File Systems vs Databases

Python viz-a-viz SQL

Parameterized Comparison

Module Summary

## Arithmetic Operations

## File handling via Python

- Extensive support for arithmetic and logical operations : Extensive arithmetic and logical operations can be performed on data using Python. These include complex numerical calculations and recursive computations.

## DBMS

- Limited support for arithmetic and logical operations : SQL provides limited arithmetic and logical operations. Any other complex computation has to be done outside the SQL.

![Image](Lecture 1.3 - Why DBMS2_artifacts/image_000022_0d9dfbde1de846c018eea32fe6aba21e8a9c7f3c69ef770101468a6cfb66a6e5.png)

## Module 03

Partha Pratim Das

Objectives &amp; Outline

File Systems vs Databases

Python viz-a-viz SQL

Parameterized Comparison

Module Summary

## Costs and Complexity

## File handling via Python

- File systems are cheaper to install and use. No specialized hardware, software or personnel are required to maintain filesystems.

## DBMS

- Large databases are served by dedicated database servers need large storage and processing power
- DBMSs are expensive software that have to be installed and regularly updated
- Databases are inherently complex and need specialized people to work on it like DBA
- The above factors lead to huge costs in implementing and maintaining database management systems

![Image](Lecture 1.3 - Why DBMS2_artifacts/image_000023_9e7e029dd28dcedaef4e37629afea5601c75c461d53164ccfca4a1acbfb17fd4.png)

![Image](Lecture 1.3 - Why DBMS2_artifacts/image_000024_0d9dfbde1de846c018eea32fe6aba21e8a9c7f3c69ef770101468a6cfb66a6e5.png)

Module 03

Partha Pratim Das

Objectives &amp; Outline

File Systems vs Databases

Python viz-a-viz SQL

Parameterized

Comparison

Module Summary

## Module Summary

- Elucidated the difference between File handling by Python viz-a-viz DBMS through an Bank Transaction example
- Parameterized Comparison

Slides used in this presentation are borrowed from http://db-book.com/ with kind permission of the authors.

Edited and new slides are marked with 'PPD'.

Database Management Systems

Partha Pratim Das

03.23
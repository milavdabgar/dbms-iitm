<!-- image -->

## Database Management System Professor. Partha Pratim Das Department of Computer Science and Engineering Indian Institute of Technology, Kharagpur Lecture No. 01 Backup &amp; Recovery/1: Backup/1

Welcome to module 51, Week 11 of Database Management Systems course in the IIT, Madras online B.Sc. program. (Refer Slide Time: 0:30) 2

8

2

<!-- image -->

2

In  the  last  week  we  have  talked  extensively  about  transactions,  that  is  how  to  perform  tasks, various  types  of  tasks  in  the  databases,  and  what  are  the  desired  properties  of  atomicity, consistency, isolation and durability that we need to ensure in a transaction to keep the database consistent and everything going perfect.

When transactions  get  concurrent,  which  they  frequently  do,  we  get  into  serializability  issues because instructions from two or more transactions are getting mixed up in the execution order, and we need to ensure correctness in spite of that and there are different serializability concepts, conflict  serializability  we  have  shown  can  be  ensured  by  acyclic  precedence  graph  which  is computable in polynomial time.

Whereas a weaker form of serializability, which gives us more range of serial schedules, needs a NP complete algorithm, or rather, rather it has NP completeness. So it cannot, is not likely to have a polynomial time algorithm. So we use certain adhoc schemes and with proper planning we can recover a database to a consistent state from an inconsistent events in case of failures. We have looked at cascaded, as well as cascadeless rollback for such kind of failures in transactions.

Finally,  we  have  looked  at  a  locking  mechanism  to  ensure  that  instead  of  pre-deciding  on serializable  schedules,  it  is  possible  to  have  schedules,  concurrent  schedules  with  better throughput be generated if by maintaining certain minimum criterion for isolation. And we have seen  that  deadlock  happens  to  be  a  big  disadvantage  in  that  whole  process.  So,  we  have explained how to detect, prevent, and recover from deadlock including time based protocols that avoid deadlocks.

(Refer Slide Time: 3:02)

<!-- image -->

So, with that with that background ready with us we will now move into discussing other very important factors in terms of database management. These are about backup and recovery. So, we start discussing in this module about the need for backup and recovery, and some of the basic strategies for backup.

## (Refer Slide Time: 3:20)

<!-- image -->

<!-- image -->

Now why do we need backup? Certainly, we all know the importance of backup. It's not, it will not have to be a database for which we have to specifically look for backup, we all backup our files, our file systems and if we fail to do that then we lose them. So, backup for a, of a database is  similarly,  like  as  we  do  is  a  representative  copy  of  the  data  containing  all  the  necessary contents of the database like, data tables, control files so that unexpected database failure, which are  due  to  factors  that  are  beyond  our  control  can  still  be  handled  by  recovering  from  those backups.

There are primarily two kinds of backup that we deal with. One is a physical backup where you just copy everything physically, like data control files, log files, archives and so on. Other is a logical  backup,  that  instead  of  physically  copying  everything  you  can  extract  the logical  data, may be some kind of an export consisting of tables and procedures and views and so on and back them up. So both strategies, depending on the context, can be used.

Now, given that we are doing a backup, certainly a, the recovery process will also have to be decided. So, what is a recovery? Recovery is the process of restoring the database to its latest known  consistent  state  after  a  system  failure  occurs  at  some  random  point  of  time.  And  a database log, we will talk about this in lot more detail, a database log records all transactions in a sequence. As transactions are done, they are logged, kind of written down. So, recovery using logs is quite popular in databases and we will try to, we will take look into those.

## (Refer Slide Time: 5:24)

<!-- image -->

So this is, what are the types, why backup is necessary? So what are the different situations for which you will do backup. So, depending on your requirement in future the nature of the backup could also be different. We just explained that the need for backup for disaster recovery, which is quite obvious. But there may be needs in according to the basic business process changes. Client want to modify the existing application to serve the business needs that have evolved at a later point of time.

So, the developers might need to restore a previous version of the database before these changes, in order to address such requirements or keep consistency or make sure that you can guarantee that  your  changes  have  not  regressed  in  terms  of  what  you  used  to  do  correctly  and  so  on. Auditing becomes another important factor.

You have seen that several financial misappropriation, fraud is going around all across the world and  so  from  audited  perspective  you  need  to  have  a  look  at  the  data,  and  the  database organization in the past so that if your organization is involved in a lawsuit you may want to have a look at the earlier snapshot of the database. This needs backups to be there.

And certainly, the downtime, without a backup the downtime of a, of a database system would be much higher. And downtime is certainly not at all good for a business. So you will want to minimize that downtime.

<!-- image -->

8

<!-- image -->

So  when  I  do,  we  do  backup,  let  us  see  what  are  the  types  of  data  that  we  would  backup. Certainly,  we  will  backup  the  business  data.  The  business  data  is  what  primarily  we  have designed for, the information of clients, employees, contractors, inventories, sales information, course details, etcetera, etcetera, all the rules and all that. That is the business data. That is, that is the basic model that you have created through all these design and so on.

The  second  is,  you  will  also  need  to  backup  the  system  data.  The  specific  environment,  the configuration,  the  systems  catalog  that  you  had  for  the  database,  the  log  files,  software dependency, different disk images and so on. So, this is a second category of data.

And  the  third  category  of  data  are  typically  called  the  media  data.  The  photographs,  videos, sound,  graphics,  all  that  we  have  talked  about  as  kind  of  blob  data,  that  have  gone  into  the database.  You  had  photographs  of  employees,  you  had  video  recordings  of  important  board meetings, and so on so forth, they will also have to be backed up, and typically this media files are much larger in size compared to the typical database files which are mostly textual.

## (Refer Slide Time: 8:40)

<!-- image -->

IIT Madras

Module 51

Parha Pratin

Backup

Strategies

<!-- image -->

## Backup Strategies

## Backup Strategies

## Types of Backup Strategies: Full Backup

- Full Backup\_backs\_up\_everything :  This is a complete copy; which stc Ful restore all components of the database system as it was at the time
- A full backup must be done at least once before any of the other typ
- The frequency of a full backup depends on the type of application. F backup is done on a daily basis for applications in which one or more isJare true:
- Either 24/7 availability is not a requirement, or system availabilit) consequence of backups.
- A complete backup takes a minimum amount of media, ie. the b too large.

<!-- image -->

Now, let us look at what could be the strategy to backup. So, the question certainly is, how much do  we  backup,  how  often  do  we  backup,  what  do  we  backup?  So,  all  these  questions  are answered in terms of forming a consistent backup strategy for the organization.

So,  the  first  and  most  important  kind  of  backup  is  called  a  Full  Backup,  which  as  the  name suggest backs up everything. It is a complete copy, It is a complete replica of what you have in the  database.  Tables,  procedures,  functions,  system  views,  everything.  So  a  Full  Backup  can completely restore all (complete) all components of the database system as it was at that time the crash happened.

So, what is very important, that when you are going to do something major in your database, or when you are going to do any other kind of backup, take any other kind of backup, before that at least once you must have a full backup. And then you can have anything else. Now naturally the question is, how often would you take full backup? That depends on the type of application. A full  backup  may  be  done  on  a  daily  basis,  where  you  have  a,  I  mean  you  do  not  have  a requirement of a 24/7 availability.

See if your system, say, your net banking system, which is 24/7 available. If you are, if users are currently using and changing the table every second, every millisecond, certainly you will not be able to do a full backup easily. Because the system availability is going to be restricted when you do this backup. So, this is one consideration.

Other is, naturally how much media do you need. If you do daily, backup on a daily basis and your backup requirement say, is 2 terabyte, then you can think of that in a year over 365, 366 days how much big media that you will need. Also, you may want to do the backup on a daily basis because you may not have easily available system administrators who can easily restore the system from a not so full backup also.

So, you just want to make sure that full backup is available. So, these are some of the reasons for which you do a full backup. Certainly, the advantage is obvious that it, it is a consolidated read from a single backup.

(Refer Slide Time: 11:29)

2

<!-- image -->

Generally it will not depend on anything else. So, there is two consecutive full backups do not have a dependency between them, and effectively the loss of single days backup does not affect the ability to recover other backups. Easy to set up, configure, maintain, but certainly, it takes a large amount of time, takes a large amount of results in a long down time for the, for the system for the backup process, and needs a huge amount of media. So, we will always not be able to do a full backup.

(Refer Slide Time: 12:10)

K

<!-- image -->

So incidentally, just to, just to give you an idea, I use a laptop which has a one terabyte hard disk, and I have about 500, about 600 gigabytes of data in that. My, different personal and work data. So, every week I do a backup. Now when I do a backup, it takes about 3 to 4 hours, when I cannot  work,  when  I  have  to  make  sure  that  the  power  does  not  go  off  so  that  the  backup  is inconsistent, closed at the middle.

So, what I started using is certain software which compute what has changed from the backup I did last week, and backs up only that part. It just looks at the time stamp of the files. I have to make  sure  that  my  system  has  a  correct  timestamp  always.  So,  anything  that  has  a  change timestamp, which is more than the timestamp in the last backup on my external hard disk is what is backed up. So, that is the basic idea of doing an incremental backup. It backs up only those files and item that has changed since the last backup.

So, when I started doing this, the, the backup requirement fell from 500 600  GB to down to 5, 6 GB. I mean, not even 1 percent, and the time came down to about from 3 to 4 hours, it came down to about 10 to 15 minutes. So, in a typical, maybe 2 TB database also, it may have changed only 5 percent during the day. It, all changes will not happen at the same time.

So,  an  incremental  backup  for  the  changed  data  only  takes  a  much  less  time.  So  what  most organizations would tend to do is do a full backup once a week and do incremental backup rest of the day. So, what it means, if you see here, say, on Friday suppose, they do a full backup, then on Saturday they do an incremental backup, that is, as much as changed from the Friday's full backup.

Sunday they do another incremental backup, which is as much as changed from the Saturday's incremental backup. Monday, they do incremental over Sunday, Tuesday, they do incremental over Monday, and so on. It goes on till Thursday. And again on the next Friday they do a full backup. So, this ensures that most of the time you need a minimum backup window, and, which you can place at a non-peak time and keep the best possible throughput from your system.

(Refer Slide Time: 15:00)

8

2

<!-- image -->

So, this is a basic idea of the incremental backup. The advantages are obvious. You need less storage,  you  need  less  downtime,  and  it  provides  a  considerable  cost  reduction  over  the  full backup. Naturally, there are flip slide.  The  flip  side is it  requires more effort  and time during recovery.  Because  now,  with  a  full  backup,  one  backup  will  give  the  entire,  I  mean,  if  I  had made, every week made a whole copy of my hard disk, then I can, when I need, I can just copy it back. In one go it will be done.

But if I have done increment and only, then every incremental change will have to be brought on with the full backup to start with. So it cannot be done without a full backup, and all incremental backups  that  have  happened  from  that  full  backup.  So  if  the  system,  say,  unfortunately  goes down  on  Monday,  I  have  to  take  the  full  back  of  Friday,  restore,  then  the  incremental  on Saturday, then the incremental on Sunday, and then I will be able to come to the Monday.

So, if any of these intermediate incremental backups are lost, then I cannot restore the system. So, these are, these are some of the disadvantages.

(Refer Slide Time: 16:18)

<!-- image -->

So we can, you can see that full backup has a very, I mean it is, it is, it is very, dealing the whole system  together  has  a  very  low  granularity.  Whereas,  incremental  backup  has  a  lot  more granularity. It is being done in small units every day. So, it has a trade-off between the two. So, differential backup is a strategy that does a medium range granularity.

So,  what  you  do  is,  differential  backup  backs  up  all  the  changes  that  occurred  with  the  most recent full backup, irrespective of what other incremental backups that you have taken. You take the last full backup and with respect to that you are doing the differential. So, you can say that doing on a daily basis, incremental is a form of differential.

But it is, differential only has a time window which is more than the incremental backup and less than the full  backup.  So,  it  is  somewhere  in  between.  So,  it,  again,  does  not  have  to  back  up everything but can still run the backup much faster than the full backup, and can facilitate the restore, recovery process.

## (Refer Slide Time: 17:36)

| Frday   | Saturday    | Sunday   | Monday                    | Iuesday      | Wednesday   |
|---------|-------------|----------|---------------------------|--------------|-------------|
| Full    | Incremental |          | Incremental | Incremental | Dilferential | Incremental |

<!-- image -->

| Frday   | Saturday    | Sunday      | Monday      | Iuesday      | Wednesday   |
|---------|-------------|-------------|-------------|--------------|-------------|
| Full    | Incremental | Incremental | Incremental | Dilferential | Incremental |

<!-- image -->

So, this could be another, a possible scheme. Again, modifying that you again do full backup on Friday,  do  incremental  on  Saturday,  Sunday,  Monday.  But  on  Thursday,  you  do  not  do incremental, you do differential. So, what you are doing? This is, this is where you have done full, and then, on, you have just incremental on Saturday. So, it is over the full. You have done incremental on Sunday, it is over the Saturday, incremental on Monday, over the Sunday. On Tuesday, you do a differential.

So, what you do, in Tuesday you do not do incremental with respect to Monday. Rather, you do an incremental, differential with respect to Friday. So, which means, and then again when you do the next incremental you do not go back to the last full backup, but rather you go back to the last differential backup. So, when you are doing it on Wednesday ,you are not going back to the full backup,  rather  you  are  doing  it  with  respect  to  the  differential  backup.  Then  you  go  on  the incremental backup.

So,  you  have  to  choose  your  resolution.  Full  backup,  less  granularity,  all  the  advantages, disadvantages,  incremental  backup,  maximum  granularity,  advantages,  disadvantages,  and differential backup stands in between to give you a nice trade-off between the two extremes. So, recovery on any given day only needs the data from the full backup and the most recent, recent differential backup and the remaining incremental backup.

So, if you have to restore something on this day, say, Thursday you need the full backup, the differential  backup,  and  just  this  incremental  backup.  Whereas,  if  you  did  not  have  the differential,  you  would  have  required,  1,  2,  3,  4,  5,  incremental  backups.  So,  that  is  the  basic trade-off. And you choose these time windows based on what your business requirements are.

(Refer Slide Time: 19:44)

<!-- image -->

So, advantages of differential backup is the recoveries are required fewer backup sets. So, it is faster, takes less time, gives better recovery option, when the full backup particularly is run less frequently. For example, you might, then with differential, you might run full backup not on a weekly basis but on a monthly basis.

But certainly, it has disadvantages. Although the number of backup sets required for recovery is less, but in differential backup also the amount of storage media required may exceed the storage media for incremental backup because it is a backup over a, after a longer period. It is true that incrementally in between the changes have been recorded. So, you have the recovery options but you are doing it after 3, 4 days so you have a bigger difference, and, so it could even reach the size of a full backup at times. In some systems it does.

(Refer Slide Time: 20:57)

<!-- image -->

So, this is just an illustration of what you back up on according to this strategy. So, here you are backing up everything, the full backup. After that B, C, D, these three files have changed. So, when you do that incremental, you just backup B, C, D. After that backup, F, file F has changed. So when you do differential, you are doing with respect to the full. So, you do B, C, D as well as the F.

After that D and E has changed, so you do incremental over D, E because you are doing it with respect to this last differential backup. Then only G has changed, but since you are going to do a full backup, you do a backup of everything, not only just G, or no not only does D, E, G. You do the full backup.

So, this is the basic strategy, and you have to find out your time resolution, your cyclicity, what kind of cycles you want, but this is just conceptualized over a span of 5 days. This is how your backups could be strategized.

## (Refer Slide Time: 22:19)

| Sunday   | Monday   | Tuesday ,   | Wednesday   | Thursday   |        | Saturday   |
|----------|----------|-------------|-------------|------------|--------|------------|
| (Full    |          | VIncr       |             |            | 6Incr  |            |
|          |          |             |             |            | Ilncr  |            |
|          |          |             |             | I9/Incr    | 2OIncr |            |
|          |          |             |             | 26Incr     |        |            |
|          | JOIncr   |             |             |            |        |            |

<!-- image -->

| Sunday   | Monday   | Iuesday   | Wednesday   | Thursday   |       | Saturday   |
|----------|----------|-----------|-------------|------------|-------|------------|
|          |          | Incr      |             |            | 6Incr |            |
|          |          |           |             | 2Incr      |       |            |

<!-- image -->

So  as  a,  as  a  case  study,  we  can  just  look  at  a  very  typical  monthly  backup  schedule.  For example,  let  us  look  at  a  monthly  schedule  like  this.  So,  just  without,  without  making  things complicated, I have just assumed that the month starts on a Sunday. And Sundays, expecting that the business will be less or the business is closed, more time can be given to backup. So, heavier backups are on Sunday.

So, what you do on the first of the month, on the Sunday, and if you are choosing Sunday to be preferential, then it may be some date other than the first of the month, also. It may be a Sunday. You  do  a  full  backup.  And  then  you  keep  on  doing  incremental  till  Saturday.  On  the  next Sunday,  that  is,  the  first  Sunday  after  the  full  backup,  you  do  a  differential.  And  again  do incremental till Saturday.

Again  do  differential,  incremental  till  Saturday,  again  differential,  incremental  till  Saturday, again differential. It goes on till you end the month, when you again come and do a full backup. So with this, if  you,  if  with  this,  this  kind  of  a  pattern  being  followed,  what  is  the  maximum number of, maximum number of backups that you will need to restore for, is certainly one full backup, which you took on the first Sunday of the month. Then one differential backup that you took on the last Sunday of the week in which you are trying to recover, trying to restore.

And then you can have at most 6 incremental backups because there are 7 days. So, at most 6 you will require to do, restore the whole system. If you had done full backups on the first Sunday of the month, and incremental for the rest you would have required 31 backup sets to be used.

So, there are, there are issues with that. One is there are every incremental backup to be restored has a separate process, separate cost and so on. And further so many files will have to be perfect, so many backup files, again, have to be perfect so that you can actually do the restore. Here, you are left with various different options.

<!-- image -->

## (Refer Slide Time: 25:28)

<!-- image -->

## Hot Backup

- Till now we have learnt about backup strategies which can not with a running application happe
- In systems where high availability is a requirement Hot backup is prt possible
- Hot backup refers to keeping a database up and running while the b performed concurrently
- Such a system usually has a module or plug-in that allows the dat backed up while staying available to end users
- Databases which stores transactions of asset management compal high frequency companies etc. try to implement Hot back are highly dynamic and the operations run 24x7 trading

But  what  is  important  is  hot  backup,  is  what  if  your  system  goes  down  when  you  are,  it  is actually in operation. Which is, which is quite possible. So, when that happens naturally your database will become inconsistent, and that is the recoverability, or the, that is the cascadeless, or cascaded recovery we were talking of. We were then talking primarily in terms of transactions having to roll back because of some reason.

But if it is to do that for certain reasons which is beyond your control, then you will be in deep difficulty  because  data  might  get  lost.  So,  database  which  stores  transactions  like  asset management companies, hedge funds, stock market transactions need to have hot backups as this data are very dynamic and operations run on 24/7. So, even real time systems will need that.

2

## (Refer Slide Time: 26:41)

<!-- image -->

So, hot backups are mechanisms by which the database always remains available to the end user, and the point of time recovery, point in time recovery is easier in this system, and certainly it is most efficient when you deal with dynamic and modularized data.

Disadvantages,  of  course  are  there.  It  is  may  not  be  feasible  when  the  data  set  is  huge  or monolithic.  That  is  the  reason  you  have  to  make  the  database  very  typically  modular.  Fault tolerance is less. That is, if something fails then detecting that on the fly can be difficult. So, any error could terminate your whole backup process. Maintenance and setup cost is large and so on.

(Refer Slide Time: 27:36)

<!-- image -->

## Transactional Logging as Hot Backup

- In database systems, hot backup is mainly used for Transactic regular
- Cold backup strategies like Differential,  Incremental are preferred The reason is evident from the disadvantages of Hot backup:
- Transactional Logging is used in circumstances where a possibly inc is taken, but another file generated and backed up (after the databas backed up) can be used to restore consistency: fully
- The information regarding data backup versions while recovery at a be inferred from the Transactional backup set. Log
- Thus they play a vital role in database recovery

So  typically,  the  hot  backup  use  the  concept  of  transaction  logs,  transaction  log  backup. Transaction  logging  is  a  mechanism,  and  that  is  what  we  are  going  to  discuss  in  the  coming modules,  is  a  mechanism  by  which  while  you  do  the  transactions  you  are  doing  read-write, commit, abort and all that, you keep a copy of what you have done, you keep a ledger in terms of what you have done.

So,  the  transaction  log  usually  is  much  lighter  compared  to  the  actual  database.  And  you  can have points where the transaction log is consistent with the database completely, and therefore you do not need the previous log anymore. So, how you use this transaction log in hot backup, and what is transaction logging is going to be the next thing that we are going to discuss while we talk about the recovery in transactions. (Refer Slide Time: 28:37) Module Summary 8

<!-- image -->

So, this brings us to the end of this module. Thank you for your attention, and we will continue in the next module.
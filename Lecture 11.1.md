![Image](Lecture 11.1_artifacts/image_000000_bbaa640f2b7c7b6f18cdf441c797dcf1ce99e755b6ef0a9bbf7b581538bddcab.png)

## Module 51

Partha Pratim Das

Week Recap

Objectives &amp; Outline

What is Backup and Recovery?

Why Backup?

Backup Data: Types

Backup Strategies Full Backup

Incremental Backup

Differential Backup

Example

Case: Monthly Schedule

Hot Backup Transactional Logging

Module Summary

## Database Management Systems

Module 51: Backup &amp; Recovery/1: Backup/1

## Partha Pratim Das

Department of Computer Science and Engineering Indian Institute of Technology, Kharagpur ppd@cse.iitkgp.ac.in

Partha Pratim Das

![Image](Lecture 11.1_artifacts/image_000001_bbaa640f2b7c7b6f18cdf441c797dcf1ce99e755b6ef0a9bbf7b581538bddcab.png)

## Module 51

Partha Pratim Das

Week Recap

Objectives &amp; Outline

What is Backup and Recovery?

Why Backup?

Backup Data: Types

Backup Strategies Full Backup

Incremental Backup

Differential Backup

Example

Case: Monthly Schedule

Hot Backup Transactional Logging

Module Summary

## Week Recap

- Concurrent transactions, serializability issues, and ACID properties are discussed
- Learnt the forms of serializability - conflict and view
- Conflict serializability can be ensured by acyclic precedence graph
- View Serializability is a weaker serializability system providing better concurrency. However, testing for view serializability is NP complete
- With proper planning, a database can be recovered back to a consistent state from inconsistent state in the face of system failures. Such a recovery is done via cascaded or cascadeless rollback
- Understood the locking mechanism and protocols
- Realized that deadlock is a peril of locking and needs to be handled through rollback
- Explained how to detect, prevent and recover from deadlock
- Introduced a time-based protocol that avoids deadlocks

## Partha Pratim Das

![Image](Lecture 11.1_artifacts/image_000002_b551d1d039a350a56349b412170007d20638ad0732feb40b06cdb100cf6ab680.png)

## Module 51

Partha Pratim Das

Week Recap

Objectives &amp; Outline

What is Backup and Recovery?

Why Backup?

Backup Data: Types

Backup Strategies Full Backup

Incremental Backup

Differential Backup

Example

Case: Monthly Schedule

Hot Backup Transactional Logging

Module Summary

## Module Objectives

- To understand need for having backup
- To learn about different strategies of backup and their suitability

![Image](Lecture 11.1_artifacts/image_000003_0d9dfbde1de846c018eea32fe6aba21e8a9c7f3c69ef770101468a6cfb66a6e5.png)

## Module 51

Partha Pratim Das

Week Recap

Objectives &amp; Outline

What is Backup and Recovery?

Why Backup?

Backup Data: Types

Backup Strategies Full Backup

Incremental Backup

Differential Backup

Example

Case: Monthly Schedule

Hot Backup Transactional Logging

Module Summary

## Module Outline

- Need for backup and recovery
- Different strategies of backup with examples

## References :

- Enterprise Systems Backup and Recovery: A Corporate Insurance Policy by Preston De Guise (Accessed 21-Aug-2021)
- Data Backup Recovery: The Essential Guide for Businesses (Accessed 19-Aug-2021)

![Image](Lecture 11.1_artifacts/image_000004_bbaa640f2b7c7b6f18cdf441c797dcf1ce99e755b6ef0a9bbf7b581538bddcab.png)

## Module 51

Partha Pratim Das

Week Recap

Objectives &amp; Outline

What is Backup and Recovery?

Why Backup?

Backup Data: Types

Backup Strategies Full Backup

Incremental Backup

Differential Backup

Example

Case: Monthly Schedule

Hot Backup Transactional Logging

Module Summary

## What is Backup and Recovery?

## What is Backup and Recovery?

![Image](Lecture 11.1_artifacts/image_000005_bbaa640f2b7c7b6f18cdf441c797dcf1ce99e755b6ef0a9bbf7b581538bddcab.png)

Module 51

Partha Pratim Das

Week Recap

Objectives &amp; Outline

What is Backup and Recovery?

Why Backup?

Backup Data: Types

Backup Strategies Full Backup

Incremental Backup

Differential Backup

Example

Case: Monthly Schedule

Hot Backup Transactional Logging

Module Summary

## What is Backup and Recovery?

- A Backup of a database is a representative copy of data containing all necessary contents of a database such as data files and control files
- Unexpected database failures, especially those due to factors beyond our control, are unavoidable. Hence, it is important to keep a backup of the entire database
- There are two major types of backup:
- ▷ Physical Backup : A copy of physical database files such as data, control files, log files, and archived redo logs.
- ▷ Logical Backup : A copy of logical data that is extracted from a database consisting of tables, procedures, views, functions, etc.
- Recovery is the process of restoring the database to its latest known consistent state after a system failure occurs.
- A Database Log records all transactions in a sequence. Recovery using logs is quite popular in databases
- A typical log file contains information about transactions to execute, transaction states, and modified values

## Partha Pratim Das

![Image](Lecture 11.1_artifacts/image_000006_bbaa640f2b7c7b6f18cdf441c797dcf1ce99e755b6ef0a9bbf7b581538bddcab.png)

## Module 51

Partha Pratim Das

Week Recap

Objectives &amp; Outline

What is Backup and Recovery?

Why Backup?

Backup Data: Types

Backup Strategies Full Backup

Incremental Backup

Differential Backup

Example

Case: Monthly Schedule

Hot Backup Transactional Logging

Module Summary

## Why Backup?

## Why Backup?

![Image](Lecture 11.1_artifacts/image_000007_bbaa640f2b7c7b6f18cdf441c797dcf1ce99e755b6ef0a9bbf7b581538bddcab.png)

Module 51

Partha Pratim Das

Week Recap

Objectives &amp; Outline

What is Backup and Recovery?

Why Backup?

Backup Data: Types

Backup Strategies Full Backup

Incremental Backup

Differential Backup

Example

Case: Monthly Schedule

Hot Backup

Transactional Logging

Module Summary

## Why is backup necessary?

## · Disaster Recovery

- Data loss can occur due to various reasons like hardware failures, malware attacks, environmental &amp; physical factors or a simple human error

## · Client Side Changes

- Clients may want to modify the existing application to serve their business's dynamic needs
- Developers might need to restore a previous version of the database in order to such address such requirements

## · Auditing

- From an auditing perspective, you need to know what your data or schema looked like at some point in the past
- For instance, if your organization happens to get involved in a lawsuit, it may want to have a look at an earlier snapshot of the database.

## · Downtime

- Without backup, system failures lead to data loss, which in turn results in application downtime
- This leads to bad business reputation Database Management Systems

Partha Pratim Das

![Image](Lecture 11.1_artifacts/image_000008_bbaa640f2b7c7b6f18cdf441c797dcf1ce99e755b6ef0a9bbf7b581538bddcab.png)

## Module 51

Partha Pratim Das

Week Recap

Objectives &amp; Outline

What is Backup and Recovery?

Why Backup?

Backup Data: Types

Backup Strategies Full Backup

Incremental Backup

Differential Backup

Example

Case: Monthly Schedule

Hot Backup Transactional Logging

Module Summary

## Backup Data: Types

## Backup Data: Types

![Image](Lecture 11.1_artifacts/image_000009_b551d1d039a350a56349b412170007d20638ad0732feb40b06cdb100cf6ab680.png)

## Module 51

Partha Pratim Das

Week Recap

Objectives &amp; Outline

What is Backup and Recovery?

Why Backup?

Backup Data: Types

Backup Strategies Full Backup

Incremental Backup

Differential Backup

Example

Case: Monthly Schedule

Hot Backup Transactional Logging

Module Summary

## Types of Backup Data

- Business Data includes personal information of clients, employees, contractors etc. along with details about places, things, events and rules related to the business.
- System Data includes specific environment/configuration of the system used for specialised development purposes, log files, software dependency data, disk images.
- Media files like photographs, videos, sounds, graphics etc. need backing up. Media files are typically much larger in size.

![Image](Lecture 11.1_artifacts/image_000010_bbaa640f2b7c7b6f18cdf441c797dcf1ce99e755b6ef0a9bbf7b581538bddcab.png)

## Module 51

Partha Pratim Das

Week Recap

Objectives &amp; Outline

What is Backup and Recovery?

Why Backup?

Backup Data: Types

Backup Strategies

Full Backup

Incremental Backup

Differential Backup

Example

Case: Monthly Schedule

Hot Backup Transactional Logging

Module Summary

## Backup Strategies

## Backup Strategies

![Image](Lecture 11.1_artifacts/image_000011_c66187055de285596be50032d73dadd82d2ef960cecf03026d68ecb78134d5c9.png)

Module 51

Partha Pratim Das

Week Recap

Objectives &amp; Outline

What is Backup and Recovery?

Why Backup?

Backup Data: Types

Backup Strategies

Full Backup

Incremental Backup

Differential Backup

Example

Case: Monthly Schedule

Hot Backup

Transactional Logging

Module Summary

## Types of Backup Strategies: Full Backup

- Full Backup backs up everything. This is a complete copy, which stores all the objects of the database: tables, procedures, functions, views, indexes etc. Full backup can restore all components of the database system as it was at the time of crash.
- A full backup must be done at least once before any of the other type of backup
- The frequency of a full backup depends on the type of application. For instance, a full backup is done on a daily basis for applications in which one or more of the following is/are true:
- Either 24/7 availability is not a requirement, or system availability is not affected as a consequence of backups.
- A complete backup takes a minimum amount of media, i.e. the backup data is not too large.
- Backup/system administrators may not be available on a daily basis, and therefore a primary goal is to reduce to a bare minimum the amount of media required to complete a restore.

Partha Pratim Das

![Image](Lecture 11.1_artifacts/image_000012_0d9dfbde1de846c018eea32fe6aba21e8a9c7f3c69ef770101468a6cfb66a6e5.png)

## Module 51

Partha Pratim Das

Week Recap

Objectives &amp; Outline

What is Backup and Recovery?

Why Backup?

Backup Data: Types

Backup Strategies

Full Backup

Incremental Backup

Differential Backup

Example

Case: Monthly Schedule

Hot Backup

Transactional Logging

Module Summary

## Types of Backup Strategies: Full Backup (2)

## · Full Backup: Advantages

- Recovery from a full backup involves a consolidated read from a single backup
- Generally, there will not be any dependency between two consecutive backups.
- Effectively, the loss of a single day's backup does not affect the ability to recover other backups
- It is relatively easy to setup, configure and maintain

## · Full Backup: Disadvantages

- The backup takes largest amount of time among all types of backups
- This results in longest system downtime during the backup process
- It uses largest amount of storage media per backup

![Image](Lecture 11.1_artifacts/image_000013_c66187055de285596be50032d73dadd82d2ef960cecf03026d68ecb78134d5c9.png)

Module 51

Partha Pratim Das

Week Recap

Objectives &amp; Outline

What is Backup and Recovery?

Why Backup?

Backup Data: Types

Backup Strategies Full Backup

Incremental Backup

Differential Backup

Example

Case: Monthly Schedule

Hot Backup Transactional Logging

Module Summary

## Types of Backup Strategies: Incremental Backup

- Incremental backup targets only those files or items that have changed since the last backup. This often results in smaller backups and needs shorter duration to complete the backup process.
- For instance, a 2 TB database may only have a 5% change during the day. With incremental database backups, the amount backed up is typically only a little more than the actual amount of changed data in the database.
- For most organizations, a full backup is done once a week, and incremental backups are done for the rest of the time. This might mean a backup schedule as shown below
- This ensures a minimum backup window during peak activity times, with a longer backup window during non-peak activity times.

| Friday   | Saturday    | Sunday      | Monday      | Tuesday     | Wednesday   | Thursday    |
|----------|-------------|-------------|-------------|-------------|-------------|-------------|
| Full     | Incremental | Incremental | Incremental | Incremental | Incremental | Incremental |

Partha Pratim Das

![Image](Lecture 11.1_artifacts/image_000014_32155ccc63eaf8ac3b5d36be7560257f854d0b99536286a17a16546fbab339af.png)

## Module 51

Partha Pratim Das

Week Recap

Objectives &amp; Outline

What is Backup and Recovery?

Why Backup?

Backup Data: Types

Backup Strategies Full Backup

Incremental Backup

Differential Backup

Example

Case: Monthly Schedule

Hot Backup

Transactional Logging

Module Summary

## Types of Backup Strategies: Incremental Backup (2)

## · Incremental Backup: Advantages

- Less storage is used per backup
- The downtime due to backup is minimized
- It provides considerable cost reductions over full backups

## · Incremental Backup: Disadvantages

- It requires more effort and time during recovery
- A complete system recovery needs a full backup to start with
- It cannot be done without the full backups and all incremental backups in between
- If any of the intermediate incremental backups are lost, then the recovery cannot be 100%

![Image](Lecture 11.1_artifacts/image_000015_b551d1d039a350a56349b412170007d20638ad0732feb40b06cdb100cf6ab680.png)

## Module 51

Partha Pratim Das

Week Recap

Objectives &amp; Outline

What is Backup and Recovery?

Why Backup?

Backup Data: Types

Backup Strategies Full Backup

Incremental Backup

Differential Backup

Example

Case: Monthly Schedule

Hot Backup

Transactional Logging

Module Summary

## Types of Backup Strategies: Differential Backup

- Differential backup backs up all the changes that have occurred since the most recent full backup regardless of what backups have occurred in between
- This 'rolls up' multiple changes into a single backup job which sets the basis for the next incremental backup
- As a differential backup does not back up everything, this backup process usually runs quicker than a full backup
- The longer the age of a differential backup, the larger the size of its backup window

![Image](Lecture 11.1_artifacts/image_000016_0d9dfbde1de846c018eea32fe6aba21e8a9c7f3c69ef770101468a6cfb66a6e5.png)

## Module 51

Partha Pratim Das

Week Recap

Objectives &amp; Outline

What is Backup and Recovery?

Why Backup?

Backup Data: Types

Backup Strategies Full Backup

Incremental Backup

Differential Backup

Example

Case: Monthly Schedule

Hot Backup Transactional Logging

Module Summary

## Types of Backup Strategies: Differential Backup (2)

- To evaluate how differential backups might work within an environment, consider the sample backup schedule shown in the figure below.
- a) The incremental backup on Saturday backs up all files that have changed since the full backup on Friday. Likewise all changes since Saturday and Sunday is backed up on Sunday and Monday's incremental backup respectively.
- b) On Tuesday, a differential backup is performed. This backs up all files that have changed since the full backup on Friday. A recovery on Wednesday should only require data from the full and differential backups, skipping the Saturday/Sunday/Monday incremental backups .

| Friday   | Saturday    | Sunday      | Monday      | Iuesday      | Wednesday   | Thursday    |
|----------|-------------|-------------|-------------|--------------|-------------|-------------|
| Full     | Incremental | Incremental | Incremental | Differential | Incremental | Incremental |

Recovery on any given day only needs the data from the full backup and the most recent differential backup

![Image](Lecture 11.1_artifacts/image_000017_ff6f3703d346fe4a5df7b640fe9f7f247e4075285466f136a32bce48b77dca26.png)

Database Management Systems

Partha Pratim Das

![Image](Lecture 11.1_artifacts/image_000018_0d9dfbde1de846c018eea32fe6aba21e8a9c7f3c69ef770101468a6cfb66a6e5.png)

## Module 51

Partha Pratim Das

Week Recap

Objectives &amp; Outline

What is Backup and Recovery?

Why Backup?

Backup Data: Types

Backup Strategies Full Backup

Incremental Backup

Differential Backup

Example

Case: Monthly Schedule

Hot Backup

Transactional Logging

Module Summary

## Types of Backup strategies: Differential Backup (3)

## · Differential Backup: Advantages

- Recoveries require fewer backup sets.
- Provide better recovery options when full backups are run rarely (for example, only monthly)

## · Differential Backup: Disadvantages

- Although the number of backup sets required for recovery is less but in differential backups the amount of storage media required may exceed the storage media required for incremental backups
- If done after quite a long time, differential backups can even reach the size of a full backup

![Image](Lecture 11.1_artifacts/image_000019_c66187055de285596be50032d73dadd82d2ef960cecf03026d68ecb78134d5c9.png)

## Module 51

Partha Pratim Das

Week Recap

Objectives &amp; Outline

What is Backup and Recovery?

Why Backup?

Backup Data: Types

Backup Strategies Full Backup

Incremental Backup

Differential Backup

Example

Case: Monthly Schedule

Hot Backup Transactional Logging

Module Summary

## Types of Backup Strategies: Illustrative Example

- The figure below depicts which of the updated files of the database will be backed up in each respective type of backup throughout a span of 5 days as indicated.

![Image](Lecture 11.1_artifacts/image_000020_e2ce00ff0e8df3afb9414df9489eca19ddcaf5741aeb90b41031534773bbf8bf.png)

Full

![Image](Lecture 11.1_artifacts/image_000021_7c3e29dc1ad015759d2f9ebc2b8866818610cd4e545ed9699fa9990f14be1d0b.png)

![Image](Lecture 11.1_artifacts/image_000022_9d2cc055f1871b04dbc6ea6249bfd3e3a6575c39f4092b6468fb540bba5e031e.png)

![Image](Lecture 11.1_artifacts/image_000023_41f9927e66ec437972b95cc333bdc0604c043cee2f0256001d2bdd27e01e1bf5.png)

![Image](Lecture 11.1_artifacts/image_000024_b4d0d044b4af192c78ce58add3cefb2e61612fba5d6d6aa722f7cad897ea8b48.png)

Incremental

Figure: Backup Types Differential

Incremental

Full

![Image](Lecture 11.1_artifacts/image_000025_ba4d8b908cd3f082a71b5fe342568f07e5b1e16e4fbe43c9e97a4de180bde5e2.png)

![Image](Lecture 11.1_artifacts/image_000026_7a35701447a912d783824f7a1b25d3429c7a470e77390919e16aed449aed7b03.png)

![Image](Lecture 11.1_artifacts/image_000027_f9482143fb1651b7b5b252d29a63effc59d7fd3959944772745e3b6c98b3b21d.png)

![Image](Lecture 11.1_artifacts/image_000028_32155ccc63eaf8ac3b5d36be7560257f854d0b99536286a17a16546fbab339af.png)

## Module 51

Partha Pratim Das

Week Recap

Objectives &amp; Outline

What is Backup and Recovery?

Why Backup?

Backup Data: Types

Backup

Strategies

Full Backup

Incremental Backup

Differential Backup

Example

Case: Monthly Schedule

Hot Backup Transactional Logging

Module Summary

## Case: Monthly Schedule

## Case: Monthly Schedule

![Image](Lecture 11.1_artifacts/image_000029_32155ccc63eaf8ac3b5d36be7560257f854d0b99536286a17a16546fbab339af.png)

## Module 51

Partha Pratim Das

Week Recap

Objectives &amp; Outline

What is Backup and Recovery?

Why Backup?

Backup Data: Types

Backup Strategies Full Backup

Incremental Backup

Differential Backup

Example

Case: Monthly Schedule

Hot Backup Transactional Logging

Module Summary

## Case: Monthly Data Backup Schedule

## Consider the following backup schedule for a month:

- Inference
- Here full backups are performed once per month, but with differentials being performed weekly, the maximum number of backups required for a complete system recovery at any point will be one full backup, one differential backup, and six incremental backups
- A full system recovery will never need more than the full backup from the start of the month, the differential backup at the start of the relevant week, and the incremental backups performed during the week
- If a policy were used whereby full backups were done on the first of the month, and incrementals for the rest of the month , a complete system recovery on last day of month will need as many as 31 backup sets
- Thus differential backups can improve efficiency of recovery when planned properly

| Sunday   | Monday   | Tuesday   | Wednesday   | Thursday   | Friday   | Saturday   |
|----------|----------|-----------|-------------|------------|----------|------------|
|          | 2Incr    | 3/Incr    |             |            | 6 Incr   |            |
| 8Diff    |          | OIncr     |             | 2Incr      |          |            |
| 15/Diff  | 16 /Incr | I7Incr    |             | I9/Incr    | 20/Incr  | 21/lncr    |
| 22/Diff  | 23/Incr  |           | 25/Incr     | 26Incr     | 27Incr   | 28/Incr    |
| 29/Diff  |          | 31lncr    |             |            |          |            |

Database Management Systems

Partha Pratim Das

![Image](Lecture 11.1_artifacts/image_000030_0d9dfbde1de846c018eea32fe6aba21e8a9c7f3c69ef770101468a6cfb66a6e5.png)

## Module 51

Partha Pratim Das

Week Recap

Objectives &amp; Outline

What is Backup and Recovery?

Why Backup?

Backup Data: Types

Backup Strategies Full Backup

Incremental Backup

Differential Backup

Example

Case: Monthly Schedule

Hot Backup

Transactional Logging

Module Summary

## Hot Backup

## Hot Backup

![Image](Lecture 11.1_artifacts/image_000031_0d9dfbde1de846c018eea32fe6aba21e8a9c7f3c69ef770101468a6cfb66a6e5.png)

Module 51

Partha Pratim Das

Week Recap

Objectives &amp; Outline

What is Backup and Recovery?

Why Backup?

Backup Data: Types

Backup Strategies Full Backup

Incremental Backup

Differential Backup

Example

Case: Monthly Schedule

Hot Backup

Transactional Logging

Module Summary

## Hot Backup

- Till now we have learnt about backup strategies which can not happen simultaneously with a running application
- In systems where high availability is a requirement Hot backup is preferable wherever possible
- Hot backup refers to keeping a database up and running while the backup is performed concurrently
- Such a system usually has a module or plug-in that allows the database to be backed up while staying available to end users
- Databases which stores transactions of asset management companies, hedge funds, high frequency trading companies etc. try to implement Hot backups as these data are highly dynamic and the operations run 24x7
- Real time systems like sensor and actuator data in embedded devices, satellite transmissions etc. also use Hot backup

![Image](Lecture 11.1_artifacts/image_000032_0d9dfbde1de846c018eea32fe6aba21e8a9c7f3c69ef770101468a6cfb66a6e5.png)

## Module 51

Partha Pratim Das

Week Recap

Objectives &amp; Outline

What is Backup and Recovery?

Why Backup?

Backup Data: Types

Backup Strategies Full Backup

Incremental Backup

Differential Backup

Example

Case: Monthly Schedule

Hot Backup

Transactional Logging

Module Summary

## Hot Backup (2)

## · Hot Backup: Advantages

- The database is always available to the end user.
- Point-in-time recovery is easier to achieve in Hot backup systems.
- Most efficient while dealing with dynamic and modularized data.

## · Hot Backup: Disadvantages

- May not be feasible when the data set is huge and monolithic.
- Fault tolerance is less. Occurrence of any error on the fly can terminate the whole backup process.
- Maintenance and setup cost is high.

![Image](Lecture 11.1_artifacts/image_000033_bbaa640f2b7c7b6f18cdf441c797dcf1ce99e755b6ef0a9bbf7b581538bddcab.png)

## Module 51

Partha Pratim Das

Week Recap

Objectives &amp; Outline

What is Backup and Recovery?

Why Backup?

Backup Data: Types

Backup Strategies Full Backup

Incremental Backup

Differential Backup

Example

Case: Monthly Schedule

Hot Backup

Transactional Logging

Module Summary

## Transactional Logging as Hot Backup

- In regular database systems, hot backup is mainly used for Transaction Log Backup.
- Cold backup strategies like Differential, Incremental are preferred for Data backup. The reason is evident from the disadvantages of Hot backup.
- Transactional Logging is used in circumstances where a possibly inconsistent backup is taken, but another file generated and backed up (after the database file has been fully backed up) can be used to restore consistency.
- The information regarding data backup versions while recovery at a given point can be inferred from the Transactional Log backup set.
- Thus they play a vital role in database recovery.

![Image](Lecture 11.1_artifacts/image_000034_0d9dfbde1de846c018eea32fe6aba21e8a9c7f3c69ef770101468a6cfb66a6e5.png)

## Module 51

Partha Pratim Das

Week Recap

Objectives &amp; Outline

What is Backup and Recovery?

Why Backup?

Backup Data: Types

Backup Strategies Full Backup

Incremental Backup

Differential Backup

Example

Case: Monthly Schedule

Hot Backup Transactional Logging

Module Summary

## Module Summary

- Learnt why having backup is essential
- Analysed different backup strategies and respective schedules
- Learnt how Hot backup of transaction log helps in recovering consistent database

Slides used in this presentation are borrowed from http://db-book.com/ with kind permission of the authors.

Edited and new slides are marked with 'PPD'.

Database Management Systems

Partha Pratim Das
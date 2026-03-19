<!-- image -->

## Database Management Systems Professor Partha Pratim Das Department of Computer Science and Engineering Indian Institute of Technology, Kharagpur Backup &amp; Recovery 5: Backup 2 RAID

Welcome to module 55 of Database Management Systems course, in the IIT Madras online BSc program.

<!-- image -->

2

<!-- image -->

In our last module of this week, on backup and recovery, we will talk about RAID Redundant Array of Independent Disks, which I am sure all of you have heard the name of and might wonder, what kind of benefits it can bring us.

<!-- image -->

So, RAID is Redundant Array of Independent Disks; when it was introduced, it was called a redundant array of inexpensive disks over time,  it is not always inexpensive. So, both the terms  Redundant  Array  of  Independent  Disks  or  redundant  array  of  inexpensive  disks  are used alternately, but more often, we will just call it RAID.

(Refer Slide Time: 1:43)

5

<!-- image -->

So, why do we need such a disk organization? Our basic motto or motivation for RAID is to manage a large number of disks while providing a view of a single disk. So, actually, there is a large number of disks, but when you look from the point of view of the CPU or the system writing to that disk, you view it as if it is a single disk.

<!-- image -->

So,  these  multiple  disks  in  parallel  provides  high  capacity  that  is,  you  can  since  there  are multiple  of  them,  you  can  have  high  volume  of  data  stored  there,  it  provides  high  speed through different possible parallel architecture that is adopted in different levels of rate.

Importantly,  it  provides  high  reliability  by  storing  data  redundancy,  please  do  not  get confused, we have since the beginning talked about the fact that redundancy is bad that was redundancy which was logical, that was redundancy in terms of your entities and attributes. But here we are talking about redundancy in the sense of having multiple copies of the same data. So that when one disk fails, if it does, then the data can be recovered from the other discs which are still working fine. (Refer Slide Time: 3:23) RAID: Redundant 2

<!-- image -->

So, obviously you should note at this point that the chance that some disk out of n disks will fail is much higher than the chance of a single specific disk fail, but the RAID helps in the way that if that specific disk which has a lesser probability of failure, if it at all fails, you lose everything. Here by providing parallel array, you are naturally having the condition that some disk might fail, but you will still be able to recover.

So, just back of the envelope kind of computation, if we have a system has 100 disks each with MTTF Minimum Time To Failure being 100,000 hours approximately 11 years then the system will have 1 by 100 of that as an MTTF given that at least one disk fail in the whole system that is about 41 days. So that is not very, very high. So, but the techniques for using redundancy to avoid data loss is critical with a large number of disks which are required also for a scalability that is high capacity and high speed. I already discussed the meaning of I in that acronym of RAID.

<!-- image -->

<!-- image -->

Now, there are three major techniques, primary techniques which are independently or in a mixed  form  used  to  achieve  different  types  of  RAID  levels.  The  first  is  called  mirroring, mirroring as the name suggests, also it is at times called shadowing  it is basically keeping duplicate copies.

So, you store extra information that can be used to rebuild the information that is lost in a disk failure. So, that your mean time to data loss and mean which depends on the mean time to  failure  can  be  less,  but  your  mean  time  to  repair  would  be  very,  very  fast.  So,  what mirroring does in principle is something very simple, you duplicate every  disk and when I mean say duplicate, it is not necessarily that it will have to be two copies, it could be more than that also.

And then the logical disk consists of two physical disks, that is a minimum of mirroring you have two disks copying the same data. So, when you carry out a write, it has to be done on both  disks  and  read  can  take  place  from  either  disk.  So,  read  immediately  becomes  much faster. Now, if one of the disks in the pair fail, data is still available in the other, so the data loss will occur only if a disk fails and if mirror disk also fails before the system is repaired.

So, the probability of that happening is very, very small. So, except for dependent failures, such as you have catastrophic failure like fire, building collapse or electrical power surge or things like that. So, the first technique we will use is mirroring.

<!-- image -->

Second is called striping. So, as we have stripes on the shirts, it is like that. So, what you do is  instead  of  keeping the entire data unit in one disk, you split and spread it over multiple disks, and you can do that at bit level, byte level or block level. In bit level, what you do you split the bits of each byte across multiple disks. So, assuming that you have an array of eight disks, you write bit i of each byte to disk i, it is all distributed.

So,  on  a  failure,  only  one  bit  can  be  affected,  but  not  everything.  Now,  the  flip  sides  the access can read data eight times at the rate of the single disk, because you are reading from eight  disks  together  in  parallel.  So,  that  access  would  be  would  be  fast,  but  the  seek  and access time would be worse than a single disk, because you will have to do the seek on all eight disks together through the controller. So, bit level striping has been an idea has been used, but not used strongly anymore. SV

<!-- image -->

You can do the same thing at byte level, divide the file into bytes each and say suppose you have four disks, then you write the first byte on the first drive, second byte and the second drive, third byte on the third drive, fourth byte on the fourth drive and fifth byte you again write on the first byte.

So, you can easily have an expression which says which drive it goes to. So again, you do things in parallel, but you are doing it at byte level, so you have a better trade off in terms of the volume of data that you can read in parallel. This is used but again, it is slowly getting limited.

(Refer Slide Time: 8:48)

<!-- image -->

What is more common is doing a block level striping with n disks, you write block i to the disk i mod n plus 1 I mean, a so if you have the block 0 goes to disk 1; block 1 goes to disk 2 and so on. So, the request for different blocks, block is the basic unit in terms of which we request we have already talked about that several times. So, request for different blocks can actually run in parallel, if the blocks reside on different disks.

Of course, some blocks after n it will fall back to the first disk, so some blocks will be on the same disk. So, a request for long sequence of blocks can utilize disks in parallel. So, striping is  a  way  to  like  mirroring  is  a  way  to  increase  redundancy  and  therefore  reliability  of  the other system, striping is a way to increase the parallelism at different possible granularity.

(Refer Slide Time: 9:58)

2

<!-- image -->

The third that we use is again for correctness, you use a parity, you know about order even parity. So, you take say a unit of data say one byte, you add up the bits and as you add up the bits, you put an extra bit suppose you have 0, you have 0 1 1 1 0 1 1 1, so you have six bits, so, you add a parity bit which is 1. So, which says that, this will always become odd parity, that is the number of 1s in the entire presentation eight bits and one parity bit would always be odd.

So, in contrast, if you had this then he will add a 0 parity bit to keep it odd parity Similarly, you can do a even parity also. So, naturally the consequences is one bit flips, suppose, this becomes 0 1 0 1 0 1 1 1 1 then this data becomes even parity. So, you can immediately know that an error has occurred. So, that is what is called error detection.

So, that is what normally would be available, but, a since, since these are this is known as to which disk is failed, because that you get to know independently, since you know that this disk has failed. So, you would know that from the parity information, it is not only that you will know that detect that one bit error has happened, but you can also correct for that error. To recover the data in the damage disk you XOR the bits of other disks including the parity bit discs.

So, that is wow so you can have parity of with bit interleaving or what is more common these days, you can have it at the block interleaving. So, parity is another way, which is you know a lot more I should say a lot more compact and less expensive in terms of storage compared to mirroring which is a smarter way to actually find out if there is some error that has happened and to correct for that error.

<!-- image -->

8

So, these are the three basic techniques that you have. And given that combination of these techniques  give  you  different  types  of  RAIDs  called  RAID  level.  So,  these  are  different architecture  that  you  that  you  use.  So,  which  employ  techniques  of  striping  mirroring  or parity to create reliable scalable storage using general purpose hard disk drive.

The basic advantage of RAID is it does not need a very high-quality special disk with high reliability, though that also exists but those are lot more expensive. So, there are a number of RAID  levels  RAID  0,  which  is  striping  RAID  1  which  is  mirroring,  RAID  5  which  is distributed parity, we will talk a little bit about that. And you can also mix multiple RAID levels through a nesting called hybrid RAID.  So, it can have striping of mirrors or mirroring of  stripes  and  so  on.  These  are  standardized  through  certain  standard  organization  into  a DDF.

Now, the important thing to note is do not think that this is a hierarchy of levels that is  1 is better than 0, 2 is better than 1 or something like that, it is just a way to identify there is no metric of performance or reliability that is associated with them. Now naturally, while these RAID will  provide  you  a  good  protection  against  for  recovery  against  different  hardware defects, defective sectors, read errors and so on.

But they will not give you protection against various other common forms of data loss like catastrophic error,  which  is  fire,  water,  soft  errors,  such  as  application  programming  error, software malfunction, malware infection and so on so forth. So, the thought that you must cast in your mind very strongly is RIAD is only a building block to prevent larger data loss but and provide recovery for that but it is not a replacement for a backup plan. It has to come along with the backup plan that is already required. (Refer Slide Time: 15:00) 2

<!-- image -->

So,  let  us  quickly  take  a  look  at  the  RAID  levels;  RAID  0  is  data  striping,  there  is  no redundant information. So, you are striping the data, you write A1 here, A2 in the other disk, there are two discs as you can see 0 and 1. A3, so odd ones are written here, even ones are written here.

So, it has a naturally independent disk, So the space utilization is 100 percent, whatever disk you have, you are being able to use anything, you are not keeping any redundant information. So, it has a best right performance because you can at least write two disks in parallel. And certainly it is the least costly, but the reliability is of course poor, because neither you are using parity nor you are using any kind of mirroring. So that is RAID 0.

(Refer Slide Time: 15:53)

<!-- image -->

We will see in what context which kind of RAID level will be used. RAID 1 talks about mirroring, so it is the most expensive solution. And it is one of the most expensive solution, I should say. And it has excellent fault tolerance. So, what you do is you simply replicate the disk. So, you can see that you have again two disks, you are not striping the entire data you have on disk 0 you also have it on disk 1.

So, two copies exist on different disks, you can distribute the reads between two disks and allow parallel reads wherever possible, and it does not stripe the data on different discs. So, the transfer rate for a single request is comparable to the transfer rate of a… of this disk array is comparable to that of a single disk, but the space utilization as you can see is 50 percent because you are needing, keeping 100 percent copy, so you need double the space.

<!-- image -->

The RAID 2 use parity. So, it uses parity for correction. So, RAID 2 we will stripe that unit with the striping unit is single bit and it uses hamming code, I do not know if you are familiar with hamming code; hamming code is you add, if you have a 4 bit data, you add some more bits to it in a unique way. So, that the entire code if it has a flip in one bit, you not only that you can detect that which you could do in a normal parity also, simple parity also, but you will  you  are  you  can  also  figure  out  what  is  the  particular  bit  position,  but  that  flip  has occurred.

So, it is single error correcting double error detecting code. So, what it means is it depends on how many bits you will need for this parity depends on the how many bits you are trying to code. So, if you have a 4 bit data, you need three additional bits to be added. So, here the illustration is with the 4 bit data. So, these are striped A1 A2 A3 A4, so, four bits are striped and four and then you have three parity bits, Ap1 Ap2 Ap3, these are the hamming bits which you spread.

So, you have seven disks which, over which the striping is happening right. So, if you have a disk array with D data discs, then the smallest unit of transfer for a read is a set of D blocks, because you can do that in parallel. And for writing obviously, you have to modify D + C blocks where C is the number of check disks, these are the check disks as I said. So, those additional like here the example is shown in terms of four bits of data and three bits of check. There is a I mean if you understand hamming code, you will see that there is a very structured formula to decide how many hamming bits you will require.

<!-- image -->

In RAID 3 level what you do you do a mix of byte striping with parity. So, you use a single parity disk. So, you have you are doing a byte striping, not a bit striping. So, you are writing A1 A2 A3 like this, and then you have a parity disk. In the parity disk, for example, here you are writing the parity of A1 A2 A3. Next you are writing the parity of A4 A5 A6 like that. So, you  will  write  byte  level  striping  with  dedicated  parity.  Naturally  RAID  3  cannot  service multiple  requests  simultaneously  because  any  single  block  of  data  is  spread  across  all members of the set. So, it does not have a very good parallel bandwidth.

(Refer Slide Time: 19:58)

6

RAID 4 use a striping, but at a block level. So, it does block striping plus it does parity. So, what it is saying again you have a parity disk, but now you are spreading blocks A1 A2 A3;

<!-- image -->

B1 B2 B3 are blocks and these are their respective parities which are kept in the parity check disk, you can obviously at the time of recovery, corrupted or lost data can be extracted by XOR mechanism, if you do not understand the XOR mechanism, you will have to read about the parity mechanism little bit in detail.

So, this facilitates that you can recover from at most one disk failure. So, at a time if one disk fail, then you will be able to, using the parity will be able to restore that data, but if more than one fails, then you will not be able to do that. So, naturally write performance is low because you need to write to, write all parity data to a single disk. So, that becomes a bottleneck, this becomes a bottleneck because wherever you are writing this disk 0, disk 1 or disk 2, you will have to write the parity on disk 3. So that becomes a bottleneck in terms of writing.

(Refer Slide Time: 21:14)

<!-- image -->

8

RAID 5 distributes the parity; it is trying to improve on RAID by distributing the parity. So, what it is doing, it is writing the blocks as well as the parity of some other, some block which is in a different disk here. So, there are four blocks, there are different blocks shown here. So, the parity of D is written here, parity of C is written here, parity of B is written here, parity of A is written here.

So, when you are reading, you will be able to, you are reading the parity from a different disk, but that is not a centralized single discs. So, read requests will have much higher level of parallelism, since the data is distributed all over the  disks read requests involve all disks whereas,  the  system  with  a  dedicated  check  disk,  the  check  disk  never  participant  in  the reads. So, it allows recovery of only one disk failure like level 4. So, in terms of failure, it is not got anything special.

<!-- image -->

In RAID 6, which extends RAID level 5, you do another parity block. So, it is a two-parity mechanism,  it  uses  another  type  of  code  called,  these  are  called  syndrome  codes,  Reed Solomon code, which has two parities P and Q, and you write them into different disks. So, for  example,  for  D,  the  syndrome  Dp  is  written  in  one  disk,  syndrome  Dq  is  written  in another disk.

And you will see that all these are distributed like for As syndrome, Ap is written here, Aq is written here. So, write performance is still poorer, because the increased complexity of parity calculation, because you will have to compute both P and both, P and Q both. It uses as I said Reed Solomon code, I will not try to explain that, but if you know. Therefore, it can handle a failure during recovery of a failed disk, this is because of this double syndrome, the extended dual  parity,  it  can  actually  handle  up  to  a  second  disk  failure.  So,  that  is  that  is  a  big advantage of RAID level 6.

<!-- image -->

Now, what you can do is you can also mix these, you can nest them that is have one level like kind of stack the whole organization, one level you do according to certain RAID level and then those RAID levels you connect through a different RAID level. So, for example, say if you have if you say RAID 50, actually 5 0 is not 50, it is 5 0 is 5 and 0. So, what it does it has a lower layer, which is RAID 0, that is it will stripe and it has a upper layer, which is RAID 5 which  is  distributed  parity,  in  that  way  you  can  improve  the  performance  of  certain combinations.

(Refer Slide Time: 24:33)

6

<!-- image -->

So, here is what I will just show you two examples of hybrid. So, you have RAID 01 so here is RAID 0, here is RAID 0, here is RAID 0. So, what is RAID 0? RAID 0 is pure striping, but then you are doing a mirror of this stripe discs by RAID 1. So, you are trying to get benefit of both, of course, you have less utilization of space, RAID 0 otherwise was optimal in terms of utilization of space, but now you have 100 percent redundancy on that, but you improve in terms of the reliability of the data.

(Refer Slide Time: 25:21)

<!-- image -->

In contrast, if you have RAID 10, then first at a lower level, you have RAID 1 which is RAID 1? RAID 1 is mirroring. So, first you mirror, these are mirrors and then the mirroring is on striped data. So, A1 is here, A2 is here, A3 is here, A4 is here. So, it has, it provides a better throughput  and  latency  than  all  other  RAID  levels  except  RAID  0.  So  that  is  one  of  the popular levels. So, there are there are several other, there are 50, there is 100 several others depending on what all you need.

<!-- image -->

So, the question comes as to since we have so many RAID levels, so what RAID level should we be using? So, some of the characteristics like RAID level 0 is not fault tolerant. So, if you need fault tolerance, you will not use it. So, you can see one criteria being used is whether it is fast one is whether it is fault tolerant, one is whether it is cheap, so RAID 0 falls on here, which is fast and cheap, but not fault tolerant. RAID 5 is fault tolerant and cheap, but not fast. RAID 10 is fast and fault tolerant, but not cheap, like that.

(Refer Slide Time: 26:39)

<!-- image -->

So,  different  such  choices  can  be  made  depending  on  what  you  need,  depending  on  the monetary cost, the performance, higher performance, performance during failure, performance during rebuilds. So, there are three performances we are talking of, one is during normal  operations,  which  is  obviously  most  critical,  but  what  is  the  performance  during failure what is the performance when you are rebuilding the disks after failure.

So, read the RAID 0 is used only when the data safety is not that important. 2 and 4 normally are not used because they are subsumed in 3 and 5, they are simpler cases in 3 and 5. 3 also is not used because bit striping forces a lot of single block reads. RAID 6 is used rarely, since level 1 and 5 offer adequate safety for most applications. So, there are the choices are, but both of these obviously, commercially we will not get all kinds of read levels available today.

(Refer Slide Time: 27:45)

0

So, for example, RAID 1, level 1 is, has a much better write performance and level 5; level 1 has higher storage cost than level 5. So, these are the different tradeoffs, I will show you a

<!-- image -->

summarized table  talking  about all  that.  So,  there  it  can  compare  the  RAID  levels  in  two ways. One is the current table which I would say more theoretical.

So,  here  the  basic  seven  RAID  levels  are  being  compared,  what  is  that  and  what  is  the minimum number of disks, what is the space efficiency in terms of if you are using n disks, how  much  of  the  disk  you  can  use  for  example,  RAID  0  you  can  see  it  is  certainly  100 percent because you are not copying anything, RAID 1 is 1 by n because you are making n copies of the data and so on so forth, these are a little more difficult to analyze.

And you can see what is the fault tolerance naturally in RAID 0, it is none no fault tolerance, here it is n minus 1 because you have n copies whereas in most others it is two, one and in RAID it is 2 and so on. So, given that, and that is good for study understanding, but what we will be more interested to look at is what are the practical comparisons. (Refer Slide Time: 29:02) IT Madras Comparison of RAID: Practical 8

<!-- image -->

<!-- image -->

So,  you  can  now  see  that  I  am  not  talking  about  all  RAID  levels,  because  they  are  not popular, they are not manufactured also, I mean most of the like 2 3 4 these kind of RAID level discs are rarely manufactured these days. So, what is important is if you can see, we have  already  talked  about  the  fault  tolerance,  the  performance  and  so  on  and  capacity utilization.

So, based on that, what you should focus on is looking at this last row, where we are talking about  what  kind  of  application  will  use  this  RAID  0,  what  is  the  characteristics  no  fault tolerance,  read  performance  is  high,  write  performance  is  high,  capacity  utilization  is  100 percent. So, your high-end workstations, data loggers, real time rendering, but very transitory data. You are not so concerned about the persistence but your performance is has to be the highest, you will use RAID 0.

<!-- image -->

You will use RAID 1, where you have a single drive failure protection, you have medium performance, 50 percent utilization for operating systems transaction databases, where you need a balance between safety and fault tolerance and performance. And you do not expect the I mean data size to grow really that large. 4As

Whereas, when it comes to say data warehousing web servers or archiving servers, you need a  very  high  capacity  utilization  that  is  very,  very  important  because  you  I  mean,  they  are very,  very  large.  So,  you  cannot  keep  on  spending  money  on  having  extra  storage,  single drive failure is fine, low performance you can even live with because warehousing is mostly an offline or semi offline application.

<!-- image -->

When it comes to data archives, backup to disk, high availability solutions, large capacity requirements, you will probably go for RAID 6, it gives you the big advantage of having 2 drive failure protection. One of the most common for fast databases, file servers, application servers that we are studying about is RAID 10, which has up to 1 disk failure in the sub array has a high read performance, which is what you need a medium write performance and you have to live with a capacity utilization which is 50 percent. So, keeping this in mind, you can decide on what kind of range you want.

<!-- image -->

And finally, before we close please keep these points in mind that RAID does not equate to 100 percent uptime, no system can guarantee you that and RAID does not replace backup, it does not protect data, protect against data corruption, human error or security issues for these two must, must you should have a robust backup plan and RAID also does not necessarily allow dynamically increasing the size of the array.

It is not easy to just you know plug in some more disks and increase your error you have to rebuild the RAID. So, it takes time. And it is also not the best option for virtualization or high availability failover which are provided by other solutions like system by SAN or NAS and stuff like that. (Refer Slide Time: 32:26) 3

<!-- image -->

So,  with  that,  we  come  to  the  end  of  this  module,  we  have  taken  a  look  at  the  high performance, high reliability, high capacity, disk arrays built out of ordinary disks red, which will  be  very  useful  in  terms  of  our  overall  backup  and  recovery  scheme  and  for  our  total database  hardware  design.  Thank  you  very  much  for  your  attention.  See  you  in  the  next module.

<!-- image -->
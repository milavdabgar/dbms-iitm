<!-- image -->

## Database Management Systems

## Professor Partha Pratim Das

## Department of Computer Science and Engineering

Indian Institute of Technology, Kharagpur

Storage and File Structure/I: Physical Storage

Welcome to Module 39 of Database Management Systems course in IIT Madras online BSc program.

(Refer Slide Time: 00:25)

<!-- image -->

We have in  the  last  three  modules  discussed  about  various  algorithms  and  data  structures linear as well as nonlinear for management of data primarily in-memory. Now, what we are going to get into is the management of storage, which is directly required for our database system, and the primary factor in this is along with the in-memory data structure because you need them to be able to do the operations while you are updating a database or during a query and so, on along with that, what you significantly need is a large volume of persistent data storage, which does not go away if your program has finished or not. And you also you need archivals that data becomes larger and larger and you need to keep it for the future archive. So, we are going to start discussing about all those.

(Refer Slide Time: 01:25)

<!-- image -->

So, what they give here is a glimpse of the physical, different forms of physical storage media that are there. Some we will discuss in little bit depth like magnetic disk, and some we will just hear because I want you to know the entire gamut of things and also in the future in the next couple of years what do you expect to be coming on our way.

(Refer Slide Time: 01:50)

<!-- image -->

<!-- image -->

So, physical storage media, what are the primary factors that we have to consider? Obviously, speed is the first factor, how quickly it can be accessed because database is large. If we take more time, the whole operation will become slow. Naturally the second is, cost per unit of data per byte of data or per megabyte of data or per gigabyte of data, that cost has to be as low as possible, because we are going to have very, very large data storage.

Then we are looking for persistency, so the reliability is very important. The power can fail, the system might crash, there can be physical failure in the storage device, will the data be protected against all these. So, for this whole discussion, that there are two parts that we will have to look at. One is the volatile storage, which is typically the computing memory, what we were saying as in-memory and non-volatile storage, which will stay. (Refer Slide Time: 03:03) 3

<!-- image -->

So, talking about the volatile storage, you have the cache as a fastest memory on your system. Besides your registers, besides your CPU registers, which are really few. So, it is a very, very fast and most costly form of storage, so you can have only a small amount of it maybe that could be hierarchy also.

Then you have the main memory, which is also volatile. It has fast access, but not as fast as a cache. Typically, tens to hundreds of nanoseconds, and usually, but it is usually too small or make it  too  expensive  to  store  the  entire  database  in  the  memory,  so  it  has  to  manage  by taking  only  a  part  of  the  database  do  the  manipulation  and  then  again  put  it  back  to  the persistent data, and volatility is the main factor.

(Refer Slide Time: 03:59)

2

<!-- image -->

Now, you have something intermediate coming up these days have come up these days which are flash memories. So, flash memories are those where, which are like the main memory, but they survive on power failure. Typically, the data can be written at a location only once, but it can be erased and written to again. It is a little different kind of technologies. It is not that you can read write, read write, read write, you cannot do that. You can write it once, and then you can do an operation called erase, and that need, that cannot be done at an isolated location that has to be done for the entire bank of memory.

And you can then  again write to  it, but also  you  cannot  do  this  in  finite  number  of  times possibly a flash memory will survive 10,000 erase cycles or maybe a million erase cycles, but not  indefinite.  But  this  is  a  good  alternate  in  many  places  as  an  extensional  larger  main memory, because that is one which survives the power failure. It is, so it is in performance it is like the main memory, in cost it is not that high, but in terms of persistency, it has some persistency against power failure.

(Refer Slide Time: 05:19)

<!-- image -->

Now,  what  is  the  mainstay  for  storage  of  persistent  data  is  magnetic  disks.  These  are basically, I mean, we will get to the details, but it is their collection of I am sorry. They are a collection of spinning disks where read/write is done magnetically and the magnetic memory remembers that. It is used for long term storage and but it cannot be directly operated on. The only thing you can do is go and write there and read back, access, that is it. Much slower than main memory, so you have to bring that data from the disk to the main memory and then operate on it, put it back.

The big advantage of magnetic disk is direct access, which means, in a very large database in a magnetic disk, you can go to any part of the data and you can read that. You do not have to, there is no seriality, serialization in that, so you do not have to go to pass through the earlier data like, so direct access is similar in concept to arrays, which we say is a random access, it is not as fine grained as random access that you can randomly go to a byte, but you can go to different  sectors,  pages  and  so  on,  but  you  can  directly  go  there  without  going  through anything else, which is in contrast to what you do in a linked list kind of structure, which we will call it sequential access, where unless you read the previous data items, you cannot read the later on.

So, this is, this property makes it persistence and this property makes it really attractive, as a store for the main store for the databases. Capacities could be larger, it runs typically 16 to 32 terabyte and every two to three years capacities typically double. It survives power failure, system crash, but if the disk itself fails then it will destroy the data, but that is very, very rare, we will talk about that. (Refer Slide Time: 07:25) &lt;

<!-- image -->

There are certain forms of optical storage, but most of them as you have been using the CD ROMs, the DVDs, the Blue-ray and so on are  primarily  write-only  device. You just  write once and read many times, so they are good for archival system, but not as a live database storage system.

<!-- image -->

Then you have tape storage. Tapes are, again, they are non-volatile, they are as I mean, you have seen the audio tapes. I hope you have, because they are rarely seen these days. So, these are  basically  long  tapes  where  you  keep  on  writing  the  data.  The  disadvantage,  main disadvantage of tape, as to why you cannot use it on a live database system is the fact that it has sequential access like it is a tape.

So, if you have written the data in the 100th position, you will have to skip the first 99 data items to read the 100th. If it is at 1 millionth position you will have to skip 1 million minus one number of data items. So, that makes it much slower because you do not have a direct access, but on the other side it has the advantage of having much larger capacity, it has much lower cost per unit compared to the disks, and there are jukeboxes of tape available which are of hundreds of terabytes or even multiples of petabytes. So, for again, archival storage tape often is a very, very good idea.

(Refer Slide Time: 09:05)

<!-- image -->

So, if I look into the whole gamut that we have just quickly run through, we just go through this on the top excluding the registers which are for computing. On the top we have cash, the fastest main memory followed by flash, magnetic disk, optical disk, if it is there as a, and the magnetic tapes.

We call this as primary memory, which means they are very fast, volatile, small, expensive, you can see those two these two, but is very needed for your regular computation. This is called  secondary  because  this  is  where  you  keep  your  live  database  data,  which  is intermediately expensive can be very, can be quite large and much less expensive than the cache or main memory.

And then you have this tertiary storage, which are for offline storage, as I say for archival purposes, which are optical disks and magnetic tapes and so on. So, primarily, we are going to focus on this part and this past, primarily on this because that is what gives us the main stay for management of storage and performance of a database.

(Refer Slide Time: 10:16)

<!-- image -->

<!-- image -->

So, onto magnetic disks. We are going to please study this part very, very carefully study the book  very  well  on  this,  because  this  is  going  to  be  used  in  a  whole  spectrum  of  physical design aspects. So, this is a basic physical architecture of a typical magnetic disk, you can see there are disks. If you have been fortunate to see some earlier long playing records or things like that, those are like this. They are both sided, this is the, these are the read write heads. So, the heads as you can see are a pair because they if I have the discs like this, the head goes in like this, so there is one on the top, which is and one on the so both surfaces can be read at the same time when it is at the same position.

Now, so you have a number of discs on the spindle, which keeps on rotating at a very high speed,  so  that  you  can  do  so  many,  so  many  arms  assembly  of  read  writes  can  work  in parallel. Now, since this is, this whole thing is rotating in together, when you position these disk heads, you position them at the same point. It is not that this will be more inside and this will be less inside, they are coupled, they go together.

So, what happens is, when at any position point they are as if virtually, if you think of they are looking at a virtual cylinder, where you have circles in every disk two sides of every disk, and if you connect them, virtually, you see is a cylinder. So, you can think of that as one unit given one position of the head, if we change the position, you have a different cylinder. So, that is the basic stuff. Let us get into some more details.

## (Refer Slide Time: 12:22)

<!-- image -->

## Magnetic Disk (2); Mechanism

- Read-write head
- Positioned very close to the platter surface
- Reads or writes ma gnetically encoded information
- Surface of platter divided into circular tracks
- Over 5OK-1OOK tracks per platter on typical hard disks
- Each track is divided into sectors
- A sector is the smallest unit of data read or written
- Sectors
- Sector size typically 512 bytes
- To read  write sector
- disk arm position head on right track swings
- platter spins: Read Write as sector passes under head
- Head-disk assemblies
- multiple disk platters on single (1 to 5 usually) spindle
- one head per platter, mounted on common arm.
- Cylinder consists of ith track of all the platters

<!-- image -->

<!-- image -->

2

<!-- image -->

So,  what  you  have  in  in  a  disk  is,  if  you  if  you  look  at  the  surface  of  one  disk,  you  have tracks, these are called tracks. You use the word track very much in context of music players and  all  that,  but  tracks  actually  came  from  that,  that  you  have  concentric  circles,  which basically can keep data. And as you can see that the outer tracks are naturally longer than the inner tracks, that is the basic geometry.

Now, given this track, you from the center, you think of radial lines. So, what will happen? Every track will get segmented and those segments are called. So, you have tracks and those segments are called sectors. So, you can have multiple sectors in a track. Now, naturally as you do this, the inner track has a shorter length, outer track has a longer length. So, what will happen is, number of sectors per track will differ.

So, what you do is, keep every sector size fixed, make it 512 bytes, let us say. Just for the sake of it there could be different, but sectors per track will vary maybe it is 500 to 1,000 in a inner track, whereas, it could be 2,000 to 1,000 to 2,000 for a outer track because the track is longer. So, those are those are your tracks.

So, A is a track B is a geometrical sector, the which is shown in blue, C is a track sector as we are showing in orange and D is what we say is a cluster or block. A cluster or block is basically a  set  of  consecutive  sectors  on  the  same  track,  which  you  typically  use  together, write together, read together and so on. And this is one of these disks, that is how it goes back and you can read them.

So, this physical organization just is very important, and you should try to have this in your mind. I mean, not need to look up this diagram you should be able to close your eyes and see this diagram because this is very, very required in terms of doing the analysis. So, the read write head positioning, you have understood, these are the tracks and per platter there may be 50,000  to  100,000  tracks  like  this,  as  you  go  radially.  Tracks  into  sectors  you  read  write finally, every sector that is a unit. So, your disk head swings into that position. And once it get  the  position  the  sector  is  below  it,  it  can  be  read  or  written.  And  cylinders,  we  have explained  what  the  cylinders  are  those  are  virtual  disks  that  are  getting  formed  by  one position of the arm assembly.

(Refer Slide Time: 15:32)

6

<!-- image -->

<!-- image -->

So, given this is the basic structure of a disk. What you typically have in the system is a disk controller.  A  disk  controller  is  what  controls  this  disk,  it  gets  commands  for  reading  or writing  sectors,  it  initiates  the  movement  of  the  arm  to  the  right  track,  then  it  checks  the rotation, so that you get to the right sector.

So, movement in rotation to get to the right sector and then you are able to read. And what it does, it  to  make sure that  there are not errors you normally  read write with a checksum. I mean, there is a mathematical, some mathematical formula used, so that from the entire data you compute a small number, so that if anything in the data changes and you compute it again this checksum will be different.

You could use MD5 hash or something of that sort. So, it ensures that success, I mean, every writing  is  successful,  because  first  it  writes  and  then  it  reads  back,  and  it  also  writes  the checksum, so in future when it is read, if after reading it computes the checksum and sees that the stored checksum is different, it knows that something has happened wrong, the sector has gone bad.

It  might map, remap bad sectors because if some sectors go bad it will try to map them to others  and  so  on.  Other  details  I  will  not  go  into  so  much  often.  You  will  have  a  disk subsystem so that every disk may have its own controller for most of it for the spindles and all  that  and  disk  controller  will  operate  at  a  higher  level  that  way  it  becomes,  that  way  it becomes much faster to have a disk assembly and then you have a system bus which is a very, very high-speed network connecting all these disks.

Naturally  to  be  able  to  put  any  disk  into  the  system  you  need  a  certain  disk  interface standards,  so  there  are  several  standards  that  you  have  heard  of.  Getting  into  the  disk interface standards is not something that we have time for, but just know that there is things like ATA SATA, SCSI and so on. And depending on how you connect them, you these days you have either SAN or NAS storage area networks or network attached storage.

(Refer Slide Time: 18:02)

8

<!-- image -->

<!-- image -->

2

<!-- image -->

So, this is the overall structure of a magnetic disk or the disk system that we typically have for database. Another question is, what are the, I mean, what are the metrics for performance? Obviously, the first metric is access time, the time to read or write a data, which is the time from the request, the issue of the request to the start of the data transfer. Why start of the data transfer? Because the remaining time does not depend on the disk, it depends on the channel you have between the disk and the actual main memory, which is a system bus and other systems.

Now, this access time is again divided into two parts. One is a seek time, because just recall there is a set of disk head and the disk is rotating. So, first it has to align for the track. So, first it has to align for the track, it has to decide in which track it is there, so it has to seek for the track.

Once it has got the track then on rotation it has to get to the write sector, the tracks are this way, sectors or this way. So, seek time is to find the track, rotational latency is to within a track get to that particular sector. So, typically, the average seek time happens to be half of the  worst  case  seek  time  and  it  is  4  to  11  milliseconds  on  typical  disks  and  the  rotation latency  is  also  of  the  same  order  assuming  that  what  RPM  rotations  per  minute  you  are spinning the disk.

So, this is a primary effect then is that net throughput metric the data transfer rate. Having given all that, if I have a chunk of data to transfer, then what is the rate at which I can transfer the data, so that will be typically 25, to 100 megabytes per second maximum rate. Naturally, lower tracks have less data, so there the overhead of seek time and rotational latency is more than the outer tracks.

So, inner tracks will have less transfer rate than the outer tracks, and multiple disks may share a  controller  I  showed  you the  disk system  configuration.  So, the  rate  is also dependent on how what strategy the controller is taking and how it manages it. The third and so, we talked about raw axis  time,  the  transfer  rate  and  then  the  reliability  question  is  known  as  MTTF Mean Time To Failure. That is, from one failure to the next how much time would elapse So, how often will this disk system fail or in other words, what is the average time for which it can run without failure continuously?

So, typically for disks today it is 3 to 5 years. And the probability of new disks are failing is very, very low, which is kind of it is expressed in terms of an almost million of hours. So, if we say that an MTTF of a new disk is 1, 2, 3, 1.2 million, 1 to 2, 1.2 million hours, then it means that the 1000, relatively new disks on the average will fail one of those. If I have 1000, relatively new disks, and one of those will fail every 1,200 hours. So, naturally it is needless to mention that MTTF will decrease as the disk ages. So, these are the three metrics to keep in mind, we might have to do some computations with them as well.

<!-- image -->

Now, the next important component is in the tertiary sector, which you have magnetic tapes, as I said, they are linear they are tapes. And therefore, they can hold large volume of data, provide high transfer rates, but nothing compared to what the disks can, but they are cheap compared  to  the  desk,  so  you  can  keep  really  large  amount  of  them.  There  are  different formats available that you may have heard of digital audio tape, which are also used for audio recording. And then you have higher and higher formats, which can have higher and higher orders of data storage.

The  sequentiality  is  predominant,  and  therefore,  your  access  is  slow,  but  it  is  good  as  a tertiary storage. And some of the recent disks are getting into couple of multiple of petabytes

I  mean  tape  storage  are  getting  into  couple  of  petabytes  as  well.  So,  as  a  tertiary  for  a permanency of storage of historical data, magnetic tapes are really good.

(Refer Slide Time: 23:17)

<!-- image -->

<!-- image -->

So, that was the core of what your database physical storage talk about. I will quickly take you through some of the other, I mean, available options because not always you are making an enterprise solution. So, if you are making a kind of a limited solution or if you can really make arrangements now a good option that has come up, which is more I should say it is technologically  not  very  different,  but  it  is  significantly  different  business  wise  because  it gives you a lot of options.

This is different forms of cloud storage. I mean, I am sure all of you are now familiar with it, we just uploading and spreadsheet and the Google Drive and saying, everybody can use it and Google gives that free up to a certain point. So that is a cloud storage. So, cloud storage is getting very, very popular in terms of the physical storage. And often times up to a certain extent,  you  have  complimentary  services.  So,  if  you  are  making  a  personal  database application  or  small  enterprise  database  application  then  you  may  be  able  to  even  manage without paying and have your databases there.

Obviously, they will never be as efficient as having your data onsite, but for that, there are other options as well. For example, you could also run your entire data application on that same  cloud,  so  that  it  is  remotely,  but  the  main  point  is,  it  will  collect,  manage,  secure analyze data as massive scale  for  you.  So,  some of  the options  that  you  have is  obviously Google Drive, Amazon drive, OneDrive, Evernote, Dropbox and so on, they give you varied options of cloud storage, which is really useful.

<!-- image -->

| IT Madras       | Cloud Storage vs .  Traditional Storage                                                                                                                                                             | Cloud Storage vs .  Traditional Storage                                                                                           |
|-----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------|
| Parameters      | Cloud Storage                                                                                                                                                                                       | Traditional Storage                                                                                                               |
| Cost            | Cloud storage per  GB than external drives . using                                                                                                                                                  | The hardware and infrastructure costs Jre high and on more space and upgrading only adds extra costs adding                       |
| Reliability     | Cloud storage is highly reliable as it takes less time to get under function- ing                                                                                                                   | Traditiona] storage requires high initial effort and is less reliable;                                                            |
| File Sharing    | Cloud storage supports file sharing dynamically as it can be shared where with network access any-                                                                                                  | Traditional storage requires physical drives to share data and network is to be established between both                          |
| Accessibility   | Cloud storage gives you access to vour files from anywhere                                                                                                                                          | Restricted to local access                                                                                                        |
| Backup Recovery | safe from on site disaster. case Of hard drive failure or other hardware ma alfunction, you can cess your files on the cloud, which' backup solution for your local storage on physical drives Very | Data that is stored Iocally is much more susceptible to unexpected events and lo- cal storage and local backups easily lost could |
|                 |                                                                                                                                                                                                     | Parth , Ptatun                                                                                                                    |

So, here is just a, point wise comparison, cloud storage is usually less expensive. Though it might  look  like  that  you  are  having  to  pay  every  month,  but  if  you  look  at  the  upfront investment you need to do for a traditional storage and the overhead of maintenance and stuff and all that cloud storage often is cost effective. It is reliable, because there is a lot of highend disk technologies like RAID, and all those are used to make sure that it does not fail. File sharing is good accessibility is from anywhere, so that gives you a lot of better functionality automatically to your, database application. And backup recovery is completely handled by the cloud storage provider and it is safe from a site disaster. So, lot of advantages. So more and more, I am sure the database applications are migrating towards cloud and that is a way to go.

2

## (Refer Slide Time: 26:13)

<!-- image -->

<!-- image -->

## Optical Disks

- Compact disk-read only memory (CD-ROM)
- Removable disks, 640 MB per disk
- Higher latency (3000 RPM) and lower data-transfer rates (3-6 MB /s) compared to magnetic disks
- Seek time about 100 msec (optical read head is heavier and slower)
- Digital Video Disk (DVD)
- DVD-5 holds 4.7 GB and DVD-9 holds 8.5 GB
- DVD: 27 GB (54 GB for double sided disk) Blu-ray
- DVD-10 and DVD-18 are double sided formats with capacities of 9.4 GB and 17 GB
- Slow seek time; for same reasons as CD-ROM
- Record once versions (CD-R and DVD-R) are popular
- data can only be written once, and cannot be erased.
- Multi-write versions (CD-RW, DVD-RW, DVD+RW and DVD-RAM) also available
- high capacity and lifetime; used for archival storage long

## Flash Drives

- Flash drives are often referred to as pen drives, thumb drives, or jump drives . have completely replaced 'drives for portable storage .  Considering how large and inexpensive they have become; they have nearly replaced CDs and DVDs for data storage purposes . They floppy
- USB flash drives are removable and rewritable storage devices that, as the name suggests, require a USB for connection and utilizes non-volatile flash memory technology port
- The storage space in USB flash drives is quite large with sizes ranging from 128MB to 2TB.
- The USB standard a flash drive is built around 'determine the number of about its potential performance , including maximum transfer rate. things

5

1

There are  several  other  storages like  optical disk  we  talked  about,  which  are  primarily  for tertiary or for other applications. There are flash drives, which are we all are often using. So, they are good in terms  of the fact that they are electronic, permanent storage.  There is no moving part, there is no magnetism, it is just that electronically stored. They are not volatile, they can remember what you write, so those are advantages in small scale application.

(Refer Slide Time: 26:50)

| Card Type   |   Year Debut | Capacity     | File System   | Supported Devices                       |
|-------------|--------------|--------------|---------------|-----------------------------------------|
| SD          |         1996 | 128MB to 2GB | FATI6         |                                         |
| SDHC        |         2006 | 4GB to 32GB  | FAT32         | All host devices that support SDHC SDXC |
| SDXC        |         2009 | 646B to 2TB  | exFAT         |                                         |

<!-- image -->

8

Others, which you are very familiar with, I am sure you are regularly pushing in and out to your mobile phone or SD cards, which are called Secure Digital cards, which are also, storage of  certain  small  size,  but  they  are  getting  popular  in  terms  of  consideration  for  a  database design application, because you could have a database, small database application running on your handheld device where your secondary storage is primarily the SD cards, that is very, very possible.

<!-- image -->

They are typically on different flash storage technologies. I will not go into those, those are deeper in in electronics, but these are some of the features that you have and there are NOR flash technology and NAND flash technology of which NAND is more popular. I should say is more reliable and so on and it has a lot of advantages, but it is a flash, so it you can it is conceptually write-only so you can write then erase and then write it again, but it does go bad after. So, you see that your pendrive is not working after getting old for a year or two, that is basically often the reason is you have run out of your erase cycles.

(Refer Slide Time: 28:13)

<!-- image -->

<!-- image -->

There is a in this class, there exists solid state drives, which are basically flash-based memory not the disk one. It is little it is a little bigger than the usual flash memory we use. But the advantage is  it  is  very,  very  fast.  It  is  very,  very  fast  and  it  is  much  larger  than  the  main memory so can use it for the purpose of a disk.

So, instead of HDD, you can have SSD Solid State Device and we are often getting devices like laptops and so on with the SSD having your BIOS and the basic operating system. So, which  makes  that  it  turns  on  the  laptop,  which  used  to  turn  on  with  HDD  with  maybe  3 minutes will now turn on in 30 seconds on even below that, but it is certainly quite expensive. And there are some comparative parameters of a SSD and HDD I have presented here this is more for your reference.

(Refer Slide Time: 29:14)

<!-- image -->

<!-- image -->

Well, the developments keep on happening. There will be lot of advances in magnetic optical and electronic memory, so that is a storage that is going to be there. But two major you know trends  that  are  emerging very strongly is  one,  is  which  is called  DNA digital  storage.  Our DNA has a lot of memory, it stores a lot of information. So, can synthesize strands of DNA be  used  as  storage.  So,  DNA  have  a  A,  T,  G,  C  coding  can  similar  kind  of  coding  in  a synthesize DNA. So, this is a biological kind of memory. So, you will have nucleotides and in one cubic-nanometer.

So, one cubic nanometer you can think and exabyte of data can be I mean a very high density of data can be stored. So, that an exabyte of data can be stored as DNA which will come on the  palm  of  your  hand,  which  is  other,  not  possible  by  other  technologies.  It  is  still  very expensive, it is still slow. There is not a commercial stage, but it has a lot of potential.

NI -

<!-- image -->

Last, but not the least is the advances in the quantum technology. So, you know that quantum mechanical  versions  of  computer  memory  is  coming  up  quantum  version  of  computing  is coming up where bits are not there, there are rather Q bits the quantum bits and this memory is also going to is expected to come up to a good size and efficiency in the next couple of years.

(Refer Slide Time: 30:58)

<!-- image -->

So, we have taken a entire look at the physical storage media. We will move on to getting more  focused  in  terms  of  our  database,  backend  I  mean,  database  back  end  physical organization part of it. Thank you very  much for your attention, and meet you in the next module.
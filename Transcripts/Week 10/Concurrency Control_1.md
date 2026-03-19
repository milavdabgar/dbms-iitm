<!-- image -->

## Database Management Systems Professor Partha Pratim Das Department of Computer Science &amp; Engineering Indian Institute of Technology Kharagpur Concurrency Control/1

Welcome to Module 49 of Database Management Systems course in the IIT Madras online BSc  program.  We  have  been  discussing  about  transactions,  particularly,  serializability, recoverability and so on.

(Refer Slide Time: 00:34)

<!-- image -->

<!-- image -->

Now, moving forward, the what you are left with using conflict or view serializability and recoverability  may  not  be  adequately  concurrent  schedules.  So,  we  need  to  manage  the concurrency,  control  the  concurrency  through  the  design  of  the  schedule.  You  cannot  just predict that beforehand that this is a schedule which is best, but can we make it, so that, the schedule  as  it  goes  would  be  able  to  take  concurrency  as  and  when  it  comes  while maintaining all the ACID properties and also ensuring fair amount of recoverability. And that is what leads us to locking mechanism or the lock-based protocol as we will see.

<!-- image -->

So, concurrency control, if we look at that there has to be a mechanism that will ensure that all possible schedules are, both conflict serializable because that can be tested in polynomial time and recoverable preferably cascade less recoverable. So, this can be ensured by a policy that once transaction executes at a time, which will always give serial schedules, but it will have a very poor degree of concurrency, very bad throughput. So, the concurrency control schemes trade off somehow dynamically, the amount of concurrency they will allow, and the amount of overhead that you incur for that. For example, testing a schedule for serializability after it has executed, it is certainly too late. I mean, it does not help. So, the goal that we are going to pursue is to develop concurrency control protocols that will assure serializability, not pre-designed ones.

<!-- image -->

Now,  one  way  to  do  that,  and  I  am  sure,  you  have  come  across  this  idea  when  you  did operating system in a little different way maybe in terms of semaphores and critical sections and stuff like that is similar that one way to ensure isolation. What is the basic violation of isolation? That the same data item if it is touched by two transactions at the same time then the updates to that may be conflicting.

So, what if I, can guarantee that a data item will always be accessed in a mutually exclusive manner? So, that when one is making a change, the other should not be allowed to make a change. Now, naturally you can enforce that to hold a lock on the entire database. Transaction 1 is working, nobody can be work on that database, that will again lead to serial schedules, but very poor performance. So, we would like to associate locks specifically with data items, and that is the basic idea, to provide exclusive access mechanism. And this whole gamut of strategies, which let you do this is called the lock-based protocol. 0

## (Refer Slide Time: 04:48)

<!-- image -->

So, what do you do in the lock-based protocol? A lock is a mechanism, which controls the concurrent access to a data item. So, you can lock a data item in two says. I mean, that is in general.  I  mean,  there  are  several  kinds  of  locks,  which  has  several  other  modes,  but  the simplest form is two modes. What is they? One is exclusive and another shared.

In the exclusive mode, if you hold a lock in the exclusive mode, you can both read as well as write.  Read  as  well  as  write.  And  we  normally  use  X-lock  command  to  request  to  have  a using a lock-X instruction. I will say lock-X data item to get a X-lock that is exclusive lock I can do the read-write both.

The other is a shared lock where I can only read. See, two transactions cannot read at the write at the same time or it is also not possible that one is writing another is reading, the data may be inconsistent,  as  because  you  may  read  before  the  write  or  you  may  read  after  the write. But two transactions or more can read from the same data item at the same time, so they can share and more often you read, so you have a S-lock which you can get by using the lock-S instruction.

Now, once you have a lock, you have to explicitly provide unlock on that data item to remove that  lock,  otherwise  others  will  not  be  able  to  do  anything.  So,  these  are  made  by  the concurrency control manager. So, a transaction always have to request, and they will be able to proceed only if it has got its lock request granted.

(Refer Slide Time: 07:18)

| Stale    | Shard   | Exchusive   |
|----------|---------|-------------|
| Unlock   | Yes     | Yes         |
| Shared   | Yes     | No          |
| Erclsive | No      | No          |

<!-- image -->

<!-- image -->

So, we talk about lock-compatibility matrix. For example, what kind of locks can be held at the same time. So, if you look at the lowered one, a shared lock can be held along with a shared  lock  because  you  can  read  multiple  transactions,  can  read  from  it.  But  certainly,  a shared lock cannot be held with an exclusive lock, that is, you cannot read when somebody is trying to write or vice versa or two people cannot write. So, this is, yes, but these three are incompatible.

So, which means, that at a time any exclusive lock can be held on a data item by only one transaction, whereas, a shared lock can be held by multiple transactions. Now, naturally when you include unlock since you are unlocking removing this it does not matter what is the lock that is already held on that data item. It can do for shared as well as for exclusive.

(Refer Slide Time: 08:23)

<!-- image -->

So,  what  is  a  lock-based  protocol?  That  you  request  for  or  granting  of  a  lock  to  the  lock manager, so transaction requests for it, and if that lock can be given the transaction will be given the lock. So, for a shared one, for sharing a lock, any number of transaction can hold the shared lock. But if any one transaction holds an exclusive lock, then no other transaction can hold any lock on that.

So, under such cases, you have to wait for the lock till all shared locks or the exclusive lock has been released by the respective transaction. You have to hold on to the lock, as long as you want to access the item otherwise the whole protocol will be violated. And once you are done, so, then you must unlock that data item. But there is a caveat to it.

It is not necessarily always desirable we will see why that you release the lock on a data item, as  soon  as  you  are  done  with  that  data  item.  Because  there  may  be  some  other  logical conditions prevalent with other data items as well. But these are the basic actions you can request get a grant. You can share a shared lock. If you do not get a request granted you have to wait for the lock. Once you get you have to hold on to the lock and then finally unlock or release the lock.

(Refer Slide Time: 10:02)

<!-- image -->

So, here is an example. So, these are two accounts being accessed by two transactions A and B. Transaction A transfers $50 transaction B prints the value A + B. So, it locks B reads B deducts 50 writes B unlock B. So, during that time nobody can touch B, which is what we wanted to do. Similarly, lock A read A increment by 50 add 50 write backs unlock, nobody can touch. And what this does? This has to print the value of A + B so it  is not going to change.

So, it uses a shared lock, reads, unlocks, shared lock to read B unlock display the value. If you execute them serially, either as T1 followed by T2 or T2 followed by T1 you will always get the correct value of 300.  If you do T1 followed by T2 then you will have 150 + 150. If you do before T2 first and then T1 you will have 100 + 200 in what case the result will be 300, which is correct.

(Refer Slide Time: 11:30)

<!-- image -->

Now,  let  us  see,  what  will  happen  in  terms  of  concurrency.  Suppose,  we  make  this concurrent, so what it do is in T1, we have up to this much here, and then we have T2 here. And then again, we have the remaining part of T1 here. And we are following the protocol strictly. Before reading and changing it has taken an exclusive lock read, computed, changed and then unlocked because it is done. Similarly, it has done the same for A you have seen this works. But in spite of that, what will this print?

Since it will get the lock on A easily because T1 has not done anything. It reads, unlock, say that is fine. Now, when it ask for lock on B since T1 has already unlocked B it will get this shared lock, and it will be able to read that value of B which is 50 less, which is the final value true.

But just think about it, the value of A that it has will get changed in future. So, at this point, if you remember the color diagram, we had shown couple of modules back of green, yellow and red at this point the database is in inconsistent, transitively inconsistent state. And because this  B  has  been  unlocked  transaction  T2  can  read  it  here,  and  what  it  will  display  quite naturally is 250, 100 + 150.

Whereas, at the end here, when you reach here the database is inconsistent because it is back to 300, but this transaction will show a wrong value. So, that is what I meant that though you should release the lock as soon as at the earliest as you can, but you have to be careful in terms of the logic. Here, you are not doing anything with B, but the point is, if you allow someone else to read this B before you have taken care of the A, there will be inconsistency reflected in that transaction. So, this is a bad way of doing that transaction.

(Refer Slide Time: 14:02)

8

<!-- image -->

So, what we should do is, this. Instead of unlock B here, we should unlock B here. What will happen if we unlock B here? If we unlock B here, then this has been done write has been done, you are still holding the lock on B, this will hold a shared lock on A, it will read A, unlock A, it will try to hold a shared lock on B.

So, it has, T2 has read A in a concurrent fashion. It tries to hold a shared lock to read B, but the lock is held here exclusively. So, it cannot get it, it will have to wait, T2 has to wait and since it has released lock A already you will be able to get this unlock A. You will be able to get this exclusive lock on A. T1 would be able to get that and T1 can proceed, T1 releases.

Then finally,  when  it  releases  B,  the  lock  on  B  only  then  T2  will  get  it.  So,  T2  has  been waiting  here.  And  after  this,  T2  will  again  be  able  to  proceed  where  you  are  back  to  a consistent state. So, when you do this in terms of T3, T4 here you get a consistent result. And this  needs  quite  a  bit  of  logical  thinking  for  the  transaction  writer  to  make  sure  that  even though it does not appear to be necessary, but because of what other transactions could do, you will have to delay the unlock of this particular data item.

<!-- image -->

Now, log-based, so that is how to use that lock-based protocol. Now, lock-based protocols can land you in other problems. For example, think about here, you have an exclusive lock X, you have a shared lock S A, you have got that. So, now at this point you need an exclusive lock here. Because now you have known that well, as soon as you are done you should not release that lock, so you are trying to hold on to the lock so unlocks are all at the end.

So, T3 holds the lock on B exclusive, T4 holds the lock on A, which is shared then T3 can go up to this where it needs an exclusive lock on A, it cannot get because T4 has a shared lock on it, they are not compatible so that it will have to wait here. T4 needs a shared lock on B to be able to read that value, it cannot get because it is T3 is locked at here, so it has to.

So,  both  these  transactions  will  wait  at  these  respective  points  with  no  resolution.  T3  will wait on the lock on A to be released, but that can be done only if T4 gets the lock on B, which can be obtained only if T3 releases the lock on B, which will happen only if T3 gets the lock on A circular logic. So, this will, none of the transactions will be able to work this is called deadlock.  It  is  very  similar  to  the  deadlock  in  operating  system.  So,  somehow  one  of  the transactions will have to be thrown back rolled back locks released so that the deadlock can be broken.

<!-- image -->

So,  deadlock  is  a  basic  problem  of  this  log-based  protocols,  but  still,  we  would  prefer  it because we have two conflicting requirements. Now, either if we do not if we do not ensure the isolation through the  locks, we  can  potentially  get  into inconsistent  state.  If you  try  to insure through the locks then deadlock may happen.

Now, out of these two things, deadlock is an evil, but deadlock is still preferable because we can still undo or rollback certain transactions, get out of the deadlock and try it again. But if the  database  gets  into  inconsistent  state,  then  there  are  effects  in  the  real  world  which  we have no way to hold back.

(Refer Slide Time: 18:59)

<!-- image -->

So, we would try to see how you know these possibilities of rollback can be minimized. So, one way of doing that is, to follow what is called a Two-Phase protocol. So far, we are saying that you need at a time you take it, you are done with the data item some time you release it. But  no,  here  we  are  saying  that,  a  transaction  is,  will  be,  a  schedule  will  be  conflict serializable provided the transactions they are in follow a two-phase locking protocol in that in the growing phase the transaction may obtain locks but it does not release any lock. And in the  shrinking  phase,  it  may  release  locks  but  may  not  obtain  any  lock.  If  it  follows  this discipline, then this protocol will assure serializability. So that is a nice property.

(Refer Slide Time: 20:02)

2

<!-- image -->

So, anything, which any schedule which follows the two-phase locking protocol is conflict serializable, but the reverse is not true. There can be conflict serializable schedule that cannot be obtained by two-phase locking. But, if we do not have enough data we will have to go with this. 0

<!-- image -->

Now, in many cases the two-phase locking is actually extended in the growing phase, as well as  in  the  shrinking  phase  by  including  conversion.  This  two  we  talked  about  that  it  can acquire a lock so it can acquire an S-lock, it can acquire a X-lock or it can convert an S-lock to a X-lock which is upgrade.

So, instead of releasing it, you are holding an S-lock shared lock, you request for an upgrade to a exclusive lock. So, if nobody else is holding a shared lock on that, you will be given that, if somebody else is also holding, then you will not be. So, this is also what you can do in the growing phase.

Similarly, in the shrinking phase, you release the S-lock, you release the exclusive lock or you convert a exclusive lock to a shared lock. So, in the exclusive lock you had just alone holding the lock, you downgrade that to a shared lock, so that others can also hold shared lock that this protocol assures serializability and but certainly the programmer will have to finally insert the different locking instructions.

<!-- image -->

So,  another  alternative  that  many  systems  actually  support  the  programmer  with,  is  by automatic acquisition of locks. And because you know that if you have to read then you need a  shared lock. So, why do you tell the programmer to get it, you can just get that. So, the operation says that read will be, if the transaction has a lock on this item, then read it. if it is, then wait till no other transaction has exclusive lock on it. The others may have shared lock because they are going to read. Then Ti will be granted a lock S, and then you read it. So, you just write-read this will happen in the background to ensure the isolation.

(Refer Slide Time: 22:51)

<!-- image -->

Similarly,  for  write,  little  bit  more  complex,  but  very  intuitive.  For  write,  you  need  an exclusive lock. If you have that go ahead and write. If you do not, you have to wait until no one else has any lock, because you are going to write, so you are going to ask for exclusive lock.

Now, if  you  are  the  only  person.  This  transaction,  Ti  is  the  only  transaction  which  has  a shared lock then you will request for an upgrade. If not, then you will request for a grant of the exclusive lock. These are just the just enumerating the possibilities, so that, before you write you necessarily hold a exclusive lock. Before you read you necessarily hold a shared lock, and you relieve the programmer from the burden of putting it at every place.

(Refer Slide Time: 23:51)

<!-- image -->

So,  two-phase  locking  does  not  ensure  the  freedom  from  deadlocks.  You  can  see  the transactions here, they are doing two-phase locking because they are only locking, they are only locking, so both are in the growing phase before they have their shrinking phase. But this will also be a deadlock because this will be granted, this will be granted, this will wait for this and this will wait for this. So, you will have a deadlock again. So, it does not guarantee that.

<!-- image -->

Actually,  when  you  make  transactions  wait  for  an  exclusive  lock  then  many  transactions maybe be waiting. So, you will have to give it to someone and rollback others or keep them waiting. So, it is possible that a particular transaction may not get the lock it is requesting for a  long  time.  Even  though,  there  may  be  several  instances,  this  is  not  deadlock,  because several others have got, but it is just that your turn is not coming. So, that is called starvation. In a loose sense, it is also referred to as Livelock this is something which exists in operating system again, and these kind of things can also happen with the locking protocol.

(Refer Slide Time: 25:27)

<!-- image -->

And  so,  the  potential  of  deadlock  exists  in  all  locking  protocols.  And  when  a  deadlock happens,  you  will  have  to  roll-back  one  or  more  transactions,  and  when  that  happens, obviously, there is a possibility of a cascading roll-back. This particular example will show you that. Study it, I will not go through each and every study it you will be able to see it very clearly.

(Refer Slide Time: 25:53)

8

<!-- image -->

Now,  there  are  ways  to  avoid  cascading  roll-back,  which  is  known  as  a  strict  two-phase protocol.  We  have  just  discussed  two-phase  protocol,  there  is  a  strict  two-phase  protocol which say that a transaction must hold all its exclusive locks till it commits or aborts. This will guarantee that you do not have cascading,

I mean, if you have, if you can close your eyes and see what cascading roll-back is doing you will understand that because if you are holding on others are not being able to work on that. So,  if  they  are  not  able  to  work  on that,  there  may  not  be transactions  which  have  already done partial work and needs a cascading roll-back.

There is a rigorous one, where all locks not only exclusive ones, but all locks are held till the committed abort has happened. In this protocol, transactions can be serialized in the order in which they commit. So, these are different protocols. I mean, you do not have to really work through  each  one  of  them  in  detail,  but  just  know  that  these  exists.  It  is  important  to understand  the  two-phase  protocol  and  be  able  to  solve  problems  with  that  two-phase protocol.

And certainly, one point has to be always kept in mind that the more and more strict you get in  terms  of the  locking  protocol,  you ensure safer, roll-back and so on,  but certainly, your concurrency is going down. This is this direct trade off, it is very easy to see because you are the more strict locking protocol you have you will hold the locks on data items for a longer period. The longer you hold that lock on data items naturally the option for other transactions to work with those data items become less concurrency goes down, that is a simple.

(Refer Slide Time: 28:04)

<!-- image -->

Now, in terms of implementation of locking. I mean, I just included that because, but it is very simple straightforward. So, you have a lock manager which manages this, and it is done in terms of lock tables. So, all that you will need is for every data item, you need to remember what are the transactions that are holding locks, what are the types of locks and who are the transactions that are waiting for locked requests. So, that is a simple linked list data structure which does that.

(Refer Slide Time: 28:34)

<!-- image -->

So,  it  says,  these  are  the,  this  is  what  is,  these  are  the  different  ones  this  is  what  has  been granted. These dark blue are granted, and this is, so this must be shared lock, and the light blue  is  waiting,  so  this  is  shared  lock.  Multiple  people  can  access,  this  is  a  obviously  an exclusive lock because one is holding it, but still someone else is waiting so on. So, you just keep on  updating  this  data  structure  the  lock  manager.  And  using  this  lock  table  the  lock manager can easily manage.

Of course, I mean, how do you do it efficiently when you have a large number of data items and large number of transaction, of course, a good challenge in algorithm and data structure design, but in principle it is quite easy to do that. You will also have to have references in some other way. For example, if a transaction aborts or  if  you  want  to have  to  rollback  a transaction then you need to, this is looks like more like going by data item wise, but that may not be enough. If you have to say roll-back transaction T8 you need to know that these are  the  two  locks  already  granted  to  it.  So,  there  has  to  be  other  form  of  reference  also available in the lock manager for doing such tasks.

(Refer Slide Time: 30:09)

1

8

<!-- image -->

So, we come to the end of this module. Thank you very much for your attention. We have discussed quite a bit in terms of the locking protocol and the primary evil that it creates the deadlock. So, we will have to  take a little  bit  more  head  on  with  the  deadlock in the  next module. See you then.
<!-- image -->

## Database Management Systems Professor Partha Pratim Das Department of Computer Science and Engineering Indian Institute of Technology, Kharagpur Indexing and Hashing/3: Indexing/3

(Refer Slide Time: 00:31)

8

<!-- image -->

Welcome to module 43 of Database Management Systems course in the IIT Madras online B.Sc. program. We have been discussing about indexing and hashing and we have recapitulated binary search trees particularly the balanced ones in the last module, and specifically we took a look at a new interesting data structure called 2-3-4 trees as a precursor to what we are going to discuss today. So, 2-3-4 trees have three different types of nodes and has a unique property that all leaf nodes are at the same level with respect to the root.

NI

## (Refer Slide Time: 01:15)

<!-- image -->

So, that is very useful and I, we will extend that idea in terms of B+ tree and its use in index file and normal record files and also look at the B tree versions of it.

## (Refer Slide Time: 01:32)

<!-- image -->

Now, coming to B tree B+ tree index files first let us, let me quickly introduce through a simple example as to what a B+ tree is. So, and we will have more actual data base oriented example later on, but just to define it is a B+ tree is a balanced binary search tree, so it will always have a height of some log of the number of nodes the base of that will be decided but it will certainly be more than 2.

So,  it  is  being  called  a  balanced  binary  search  tree  because  it  uses  the  same  concept  but  it necessarily is not a binary tree, it uses, it follows a multi-level index format like the 2-3-4 tree, has a leaf nodes denoting the actual data pointers and all leaf nodes are at the same height this is the important thing, all leaf nodes are at the same height.

And the leaf nodes are also linked via a pointer, so that you can, as you can use the indexing structure  to  access  it  randomly  you  can  also  use  it's  link  structure  to  for  a  sequential  access, naturally as the construction will ensure that the keys in the leaf node are in sorted order. So, couple of properties but exactly like the 2-3-4 tree only that here we do not have the restriction of having 1 node, 2 node, 3 node, 4 node, all nodes are of the same type, but they may have variable number of data key elements and variable number of pointers.

(Refer Slide Time: 03:43)

<!-- image -->

<!-- image -->

So, this is the basic structure. Now, naturally, we to keep it variable what we do is there is a trade off because the more number of nodes you can keep, I mean more number of keys you can keep in a node will certainly mean that your height gets less obviously, because, so if we but if we have more number of nodes then every node becomes lot more big in size and it may not be possible to bring it to the memory and fit it there, because the computations so it may exceed that block size.

Also, if I have more number of keys in a node then within a node like in the 2-3-4 tree think about a 4 node, there are three keys so multiple comparisons are required sequentially to find out what  are  the  two  keys  between  which  your  search  key  is  actually  to  be  expected.  So,  if  we increase the number of keys in a node, then that linear such part increases even though the height is reducing.

On the  other  side  if  we  have  nodes  which  have  very  few  keys,  then  you  will  need  lot  more number of nodes and the height will go up. So, to and obviously the storage will also be more. So, to strike a balance we have a very nice rule that in every internal node like this is an internal node, of course this is very special because it is root also, in an internal node at least  n  by  2 record  pointers  must  be  there,  where  n  is  a  maximum  number  of  keys  and  pointers  that  a particular node can fit, so n is that number.

So, of the possible number of record pointers with keys that it can fit it has to be at least n by 2 must be there. And at most naturally, n can be there, so when n are there, then it is totally full, but it has to be at any point of time at least half filled. Naturally, the exception is the root node, because root node is starting, so at the beginning you may not have enough keys that have gone into the tree, so the root node, it is possible the root node will have very few keys.

In the leaf node also, there has to be n by 2 record pointers and n by 2 key values that finally you have found. Naturally, it will be full, if this value goes up to n, and then it will need say this is a leaf node, so in this you need a additional pointer to the next leaf node for the linear search. So, that is the basic structure of a B+ tree.

<!-- image -->

So, how do you search, very simply as we get in case of 2-3-4 tree, suppose in this given tree you have to search for 55, so I will start with the root, compare with 25 it is more, compare with 50 it is more, compare with 75 it is less, so this is going sequential. So, it is in between these two 55, so I follow the corresponding link.

So, I come to this leaf node and I check with 50 it is more, I check the next one 55 I have found it, so that is the. So, there is one linear here, there is one linear here and then depending on the range you will get to the next level. So, I am just showing one level here. And here, since the key itself is the data, there is no separate pointer in the leaf node to go to the data in general in an index file structure that pointer at the leaf node will also be there.

## (Refer Slide Time: 08:00)

6

<!-- image -->

So, if I have to insert, what do I have to do? Suppose I have to insert 60, so I will start searching here, this, this, this, and I will find that this is expected here. Then I search here, search here, less, this is more, so I know 60 should go in at this point. And I am deliberately showing a case of a node being full, so this nodes can accommodate, let us say four keys only, and you have a fifth one.

So, it means that this leaf node now have five keys expected and so and its current root is 50 that is from here, like the current root of this is 75, that the least value element in that list value key in that so I will have to split the node as I and split, and do what? Create a new root and push it to the previous level.

## (Refer Slide Time: 09:15)

<!-- image -->

We did all that in the 2-3-4 tree, so we split into two, let us say we are five, so almost half half. And so as we do that 50 is a root here and 60 is the root of the new leaf node that has been created. So, 50 stays at is it were and 60 the new root has to get inserted in the parent which is a root node.

So,  earlier  we  had  25,  50,  75  and  null,  now  you  have  inserted  60  here  which  is  also  a  linear insertion, you insert 60 there and make its pointer point to the new leaf node which has so the values have been split in half  I  said  this  guarantee,  this  will  guarantee  because  when  are  you splitting when the leaf node already has n items.

So, you are trying to insert one more, so you are in n by 2, so what will this necessarily mean that if you split in one you will have n by 2, in the other you will have n by 2 plus 1, so here we have 2,  here  we  have  3  which  is  and  it  will  always  guarantee  by  going  by  this  root  it  is  always guarantee that a node has at least n by 2 entries.

Similar thing will happen in the internal nodes also, so if I need to insert something which will mean a split for example, if I am trying to insert 85, say I am trying to insert 85, then 85 has to go here between this, so which means this has to now split as 75, 80 and 85, 90, 95 like this, so this 85 has to go into the root node, after 75 but there is no space for that.

So, this has to split again as 25, 50 and as 60, 75, 85. So, I will have a new root node which will have 25 the first key, 60 the second key and we will have null in the rest. And this will point here and this will point here. So, this way it propagates, wherever this happens. So, that is the basic insert process. (Refer Slide Time: 12:06) &lt;

<!-- image -->

So, as you have the insert you can easily extend this for delete, only thing you will have to do in place of delete is to when you delete you have to first search, delete that and you will have to if it is a root of that leaf node, then it will get deleted up above the whole tree that is one part, and the second is you will have to reorganize because by deletion if a node falls below, your cutoff value you know is n by 2, cutoff value is n by 2, so if it falls below n by 2 you have to check whether it can  be  merged  with  the  adjacent  leaf  node  and  adjust  it,  the  same  thing  will  happen  for  the internal nodes also and the height might collapse.

So,  you  can  see  that  with  the  height  can  only  increase  if  I  have  an  insertion  and  it  can  only decrease if I have a deletion, in some cases of course not always, oftentimes insertion or deletion will not change the height of the key and the property will be maintained that all leaf nodes are at the same height, that is the basic advantage and that size will be log size.

(Refer Slide Time: 13:23)

<!-- image -->

So, this is what is used for the index files, we will see they are used for the general record files also, so they have the basic advantage is the whatever we saw earlier, the performance of index sequential  files  we  are  seeing,  they  degrade  as  the  file  grows,  so  many  over  flow  blocks  are created, reorganization is required which is expensive and so on.

Whereas this one B+ tree reorganize itself, it is called a self-organizing data structure, it is not overall  organization  is  never  required  to  maintain  the  performance.  And  obviously  there  are disadvantages of extra insertion, deletion overhead, some space overhead, but it outweigh the, I mean disadvantage is outweighed by the advantages it offers, so it is used very extensively these days.

(Refer Slide Time: 14:24)

<!-- image -->

<!-- image -->

So, here is a more, I mean more database kind of example for a B+ tree, you can see this is the data we are trying to keep and where my the key being used for this organization is a name. So, we have this organization  and  the  root  it  is  having  only  Mozart,  and  these  are  internal  nodes naturally all nodes here will be less than Mozart, all nodes here and subsequently will be more than Mozart these are internal nodes and then finally you have the leaf nodes.

And you can see that in every internal node the keys are sorted, similarly in every leaf node the keys are sorted as well, so if you see in the leaf node, in the internal node it is always going to another internal node, the pointer points to a another internal node or a leaf node, but in case of a leaf node entry, the pointer will point directly to the record data.

So, this is where you will be able to find the data, this the next one points to this data and so on. These are sorted within every leaf node and across the leaf nodes also and you use a extra pointer to link them, so that if you want like select all kind of query where you want to go with the entire file  you can, you do not have to search multiple times, you just come to the leftmost one and keep traversing it sequentially. And this is where your actual data is kept. So, this is exactly how and so what I was showing later I have examples with this kind of extensive data also, but I have given you the basic principle of how the B+ tree will work as a indexing file.

## (Refer Slide Time: 16:33)

<!-- image -->

So,  this  is  a  formal  definition  again  which  I  have  already  stated  to  you,  all  paths  have  same length to the leaf and the leaf has to be at least half, I mean every node has to be at least half filled,  except  for  the  naturally  for  the  root  node  and  that  keeping  that  exception  aside  these conditions will have to satisfy.

(Refer Slide Time: 17:04)

<!-- image -->

So, at every node what you have? You have pointers and you have keys with them, with keys satisfying this condition for linear search and ordering.

## (Refer Slide Time: 17:21)

<!-- image -->

So, in a non-leaf node you will just have the keys and the pointers to other nodes.

(Refer Slide Time: 17:48)

K

<!-- image -->

6

So, here is an example of a B+ tree index file, so leaf nodes here are mandated that they must have 3 to 5 values that is we are working with a n value of 6, so internal nodes must have 3 to 6 values, internal node is n by 2 to n, leaf node n by 2 to n-1 and the root must have 2 children you can see that all these are satisfied and things are in order.

(Refer Slide Time: 18:26)

<!-- image -->

## B+ Tree Index Files:  Observations

- Since the inter-node connections are done by pointers, logically close be physically close
- The non-leaf levels of the B tree form a hierarchy of sparse indices
- The B+ tree contains a relatively small number of levels
- Level below root has at least 2 2 values
- values
- etc.
- If there are K search-key values in the file; the tree height is no n
- thus searches can be conducted efficiently
- Insertions and deletions to the main file can be handled efficiently; as restructured in logarithmic time

<!-- image -->

## B Tree Index Files:  Observations

- Since the inter-node connections are done by pointers, logically close be physically close
- The non-leaf levels of the B+ tree form a hierarchy of sparse indices
- The B* tree contains a relatively small number of levels
- Level below root has at least 2 2 values
- Next level has at least 2* [27 2 values
- etc.
- If there are K search-key values in the file, the tree height is no
- thus searches can be conducted efficiently
- Insertions and deletions to the main file can be handled efficiently; as restructured in logarithmic time

<!-- image -->

## B+ Tree Index Files:  Observations

- Since the inter-node connections are done by pointers, logically close be physically close
- The non-leaf levels of the B tree form a hierarchy of sparse indices
- The B+ tree contains a relatively small number of levels
- Level below root has at least 2 2 values
- Next level has at least 2* [2 2 values
- etc.
- If there are Isearch-key values in the file; the tree height is no n (K)
- thus searches can be conducted efficiently
- Insertions and deletions to the main file can be handled efficiently; as restructured in logarithmic time

So, you see that the inter-node connection is being done by the pointer, so whatever is logically close does not need to be physically close, that was becoming that logical closeness is what we need for answering queries, values are close and so on, physical closeness we needed for index sequential file to put the things together here by very efficient use of pointers we are able to get rid of that physical logical contradiction.

So, these are this necessarily if you look at the non-leaf levels, it necessarily conceptually these are  basically  sparse  indices,  you  can  see  because  you  are  not  keeping  everything  you  are  just keeping selective keys and as you go higher and higher you keep more and more sampled key values only as index. So, here some basic arithmetic is given so if there are  K-search key values given that any node must have n by 2 at least n by 2 keys, so it will have n by 2 pointers, that is n by 2 children at the least it will usually have more.

So, now your base of the logarithm becomes n by 2, but if it is more, the value actually will be less than K less than this, but this is the highest possible value if all nodes have only n by 2, then this is for searching K keys where every node can contain n keys and pointers, you will need a height which is log n by 2 K. So, typically as K will be very large, so will be n, n will not be a very small number like 2, 3, it will be maybe 1000 and so on, so you will get a very efficient height management here, so that is the.

(Refer Slide Time: 20:40)

<!-- image -->

Now, the rest I have given the formal statement of the algorithm in pseudo code of how do you do  search  which  we  have  already  discussed,  so  I  will  request  you  to  study  the  algorithm  and convince yourself that it works in a nice way.

(Refer Slide Time: 20:56)

<!-- image -->

So, just to quote some typical values, if we have K as 1 million search keys, I am sorry and n is 100, then you have this logarithm to take 1 million 10 to the power 6 which is taken log of with the base 50, n by 2 and that value comes to 4. So, which means that in a general lookup you will access at most 4 nodes on that tree, quite a manageable ones.

Whereas, if you had a balanced binary tree with 1 million key values, you will require around 20, because 10 to the power 3 is 2 to the power 10, so 10 to the power 6 is 2 to the power 20, so you take a log to the base 2, so you get at least 20, so you have a huge 5 fold improvement here. So, that is a core advantage.

2

(Refer Slide Time: 22:08)

6

<!-- image -->

Now, naturally there could be duplicates in the search keys, so there could be multiple of having the same value, so we cannot always just guarantee a strict inequality, we will have to go with a relaxed form of inequality and whenever the values are equal, we will have to see how I mean there may be many of them which has to be linearly scanned.

(Refer Slide Time: 22:40)

<!-- image -->

So,  we  can  extend  the  procedure  for  search  and  consequently  insert,  delete,  if  you  have duplicates in the data.

## (Refer Slide Time: 22:51)

<!-- image -->

Now, the in terms of updates insertion and deletion, I will not run through the slides, because it is just working out of an insertion example and the deletion example.

(Refer Slide Time: 23:06)

5

<!-- image -->

<!-- image -->

<!-- image -->

## Module 43

<!-- image -->

<!-- image -->

## Module 43

## Updates on B+ Trees: Deletion

- Find the record to be deleted , and remove it from the main file and present)
- Remove (search-key value; pointer) from the leaf node if there is no bucket has become empty
- If the node has too few entries due to the removal , and the entries in sibling fit into a single node, then merge siblings:
- Insert all the search-key values in the two nodes into a single nodi left ) , and delete the other node.
- parent, recursively using the above procedure.

## Updates on B+ Trees: Deletion (2)

- Otherwise, if the node has too few entries due to the removal, but th node and a do not fit into a single node, then redistribute pc sibling
- Update the corresponding search-key value in the parent of the nc
- Redistribute the pointers between the node and a such tha than the minimum number of entries sibling
- The node deletions may cascade upwards till a node which has 2 found
- If the root node has only one pointer after deletion; it is deleted and becomes the root

<!-- image -->

So, starting from here, we have step by step shown how the different insertion steps will happen, what will, what is being done at every step  with these kind of examples, so go through them carefully, and you will understand similar example is also given for deletion. So, you can look at the  updates  due  to  deletion  through  this  example.  So,  to  study  that  and  at  home  and  get comfortable with this process.

(Refer Slide Time: 23:42)

<!-- image -->

But the basic principle as I have explained at the beginning of insert and delete remains the same. So, what it gets us here is the basic index file degradation problem is solved by B tree B+ tree indices, data file degradation problem where you actually keep the records can also be handled by the same, so B+ tree is used it is typically called B+ index tree because it uses a indexing structure,  but  it  can  be  used  for our database index files  or  it  can  be used  for database record files. And leaf nodes will always need to be half full as we had said.

(Refer Slide Time: 24:31)

<!-- image -->

So, you may have non-unique search keys as I said duplicate, so it will, it might, if you have too many duplicates, then there may be difficulties in handling that, so some people use bucket on separate block which is I do not think is a great idea, you can have a list of tuple pointers with each  key  like  hanging  a  kind  of  chain  there,  or  you  can  try  to  forcibly  make  the  search  key unique by adding a record pointer, record identifier.

So, that will have overhead of extra storage for keys, but it will make insertion deletion coding simpler and since this search keys are non-unique, it does not really matter which record you pull up or possibly you are trying to pull up all the records, but having that key value. So, if you have this  record  identifier  added  to  the  key  then  in  terms  of  actual  storage,  it  becomes,  it  has  a overhead of storing that but it makes the things fall into the same structure of insertion deletion and that is why it is quite widely used.

<!-- image -->

Another issue is if a record relocates, because you are having pointers, finally at the leaf level you  are  having  pointers,  so  if  a  record  relocates  then  the  stored  record  pointers  have  to  be updated. And this update is always expensive because it will, it might lead to your node splits which are expensive. So, what is typically done is you use primary index search key instead of when you have a secondary index, I mean this problem primarily happens with the I mean will happen for the secondary index, you have a primary index which actually organizes records.

But  you  have  a  secondary  index  on  that.  So,  if  things  change  in  the  primary  index  a  record location  changes  in  the  primary  table,  then  your  secondary  index  will  have  to  get  adjusted because it is using those pointers in turn. So, what you do, you do not use those record pointers instead you use the primary index search key as if that is the identity, it should be because it is a primary index.

So, that will mean that you have some extra traversal cost, but queries will be a little bit more expensive, but in a overall performance in the amortized performance is often preferred, because node  splits  are  really  cheap  in  this  case,  they  are  not  as  expensive  as  it  would  be  if  records relocate for a in the primary table and you have multiple secondary indices to update. So, these are.

<!-- image -->

Then  there  is  question  of  how  do  you  index  with  strings,  strings  could  always  be  a  variable length. So, it has a variable fan out then, you do not know how many will be there. So, one thing which is often done is the prefixing that you use multiple strings and kind of code them in terms of  their  prefix,  the  starting  value.  So,  you  have  Silas  you  have  Silberschatz,  you  can  separate them by Silb and put that as a key. So, this kind of compressions are also possible.

## (Refer Slide Time: 28:42)

<!-- image -->

Now, so that was about B+ tree there is a compaction on B+ tree known as B tree. In B tree the basic idea is unlike B+ tree B tree will allow a search key to appear on the tree only once, once it is in a B+ tree it will appear multiple times till the root.

(Refer Slide Time: 29:08)

6

<!-- image -->

So, you can see the contrast here, this is your B+ tree, so you have Mozart happening here then later on happening here, you have Einstein happening here and then happening here and so on. But in a B tree you will have them only once. So, Einstein is here, so Einstein's record in the leaf node will not have another entry.

So, you have a separate pointer right here for the Einstein record, for the Katz record, for the Singh record. So, once a key occurs in a node you keep the record pointer right there, so that it does not occur again, like it is happening here. So, that is a compaction those, only those who have not occurred on any internal node will occur in the leaf node. So, this will naturally take less space to operate.

(Refer Slide Time: 30:17)

6

<!-- image -->

So, it uses less number of nodes and you are at times be able to find a record even without going to the leaf node, in B+ tree you have to go to the leaf node only then you get, but here you might get it earlier. But there are several disadvantages that happened like first of all this advantage of finding  a  record  earlier  is  not  great  because  only  a  small  fraction  of  all  keys  will  be  on  the internal nodes as it is.

And non-leaf nodes are now getting larger, so if the non-leaf node gets larger, the fan out, the number of possible children  gets  slower,  the  value  of  n  is  decreasing  because  you  have  extra information kept in there only, which will mean that your the moment you reduce the fan out here, the height of this B tree will increase. So, also insertion, deletion gets more complicated. So, it is typically that the advantages of B tree do not over outweigh the disadvantages it has. So, the concept has been around it has been used, but it is not a very popular structure.

## (Refer Slide Time: 31:34)

<!-- image -->
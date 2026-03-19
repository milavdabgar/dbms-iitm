<!-- image -->

## Database Management Systems Professor Partha Pratim Das Department of Computer Science &amp; Engineering Indian Institute of Technology, Kharagpur

## Indexing and Hashing/4: Hashing

Welcome to Module 44 of Database Management Systems course in the IIT Madras online B.Sc. program.

<!-- image -->

<!-- image -->

We will  introduce  another  concept  here  which  can  help  in  indexing  operations  known  as hashing, you may be familiar with little bit of hashing, hashtag, hash table, hash maps and so on. So, we will talk about static and dynamic hashing and compare between ordered indexing that  we  have  discussed  so  far  and  hashing  and  introduce  the  concept  of  bitmap  indices  as well.

<!-- image -->

So, static hashing, the hashing per say, so what is hashing? In hashing we have a domain of values, which is normally very large. So, if that domain were small, then we could take each and every value and used it as a array index to do a random access. It is again, how do you make search efficient? That is the basic question. We could keep the data in an array, so that the  value  of  that  index  coming  from  the  set  of  possible  values  in  D  could  be  used  at  the address.

But usually, that is not the case. Often times, the, this domain of possible values is too large. And you have very small actual data that you use. So, think about names, they could be of practically any length, even if you put some limits, so it can go up to 30 to 40 characters very easily for many people.

So,  you  can  think  of  if  I  say  it  even  if  it  is  20  characters,  and  you  have  26  letters  in  the alphabet and the  blank,  so  27.  So,  it  is  the  first  place  can  be  taken  in  27  ways,  second  in another 27 ways and so on. So, it is 27 to the power 20 is the kind of size of the space that you are talking of, but you will possibly have only a few 1000 of them.

(Refer Slide Time: 3:26)

<!-- image -->

So,  you  take,  instead  of  using  D  as  an  index,  I  mean  values  of  D  as  an  index,  you  use  a function that maps the D on to a range of small range of values. So, you have different names here, you map them to a range of say 16 values called hash values hash keys, so that this function does something with the value in from the D and produces a value in between 0 to n.

So, this is an example being shown. So, John has a, gets a value 2 so that is where you are expected to get the details about John. Lisa has a value 1, this is where you get the details,

Sam  has  a  value  4,  so  this  is  where  you  get  the  details.  Sandra  incidentally,  under  this function  has  a  value  2.  So,  two  distinct  keys  John  Smith  and  Sandra  Dee  both  actually generate the same hash value.

So, if  I  have two keys, which are unequal and if they have the same hash value, we say a collision has happened. A collision has taken place. If a collision has taken place, then we have not been able to resolve and find, we will still have to go something else to do that. But this is, this will have to be a limitation or this will have to be a basic property of the hash function because you are taking a large domain of values in D, and mapping it to a small domain of n+1 value. So, there will be some for some keys, it will always have a collision and how do we manage that efficiently is the, will give the efficacy of the hashing.

(Refer Slide Time: 5:21)

<!-- image -->

8

So,  the  values,  the  index  that  a  hash  actually  takes  you  to,  maps  you  to  is  a  bucket,  it  is considered a bucket where 1 or more records can be stored. Typically, we take the bucket to be a disk block again, the question of transferring between the memory and so on. So, a hash file organization will have this hashing function. So, you have the key, you do the hashing, you get the bucket and there you find the record.

Now, naturally,  as  we  have  seen  records  with  different  key  values  may  be  mapped  to  the same bucket. So, the bucket has to be searched sequentially to locate a record. So, in one part you gain by quickly coming to a subset of values; in the other part you will have to pay if your bucket is very full, or if you have too many buckets at a given hash value.

<!-- image -->

<!-- image -->

## Example of Hash File Organization

Hash file tion of instructor file, dept\_name as key organizat using

- There are 10 buckets
- The binary representation of the ith character is assumed to be the in
- The hash function returns the sum of the binary representations of th modulo 10
- For example

<!-- image -->

So, example, so our instructor table using the department name as a key. So, as a department name is a key so, let us say there are 10 buckets. So, what we do is the department name, say if I say Music, then each one of them has a ASCII value; binary representation, we take that as an integer. And then we add them together, sum them together the ASCII of m plus ASCII a u plus ASCII of s like that, it becomes a large number.

And then we do a modulo that is we divide by 10 and take the remainder because there are 10 buckets, so that  10 buckets the indices are 0 to 9. So, if I  do a modulo, I will get a value between 0 to 9 and I use that as a value. You can check out but these are the computations of different names of departments that we have hashed through this process that you take the

ASCII value of every character in the name as an integer, add them, divide by 10 and take that residue, take the remainder.

(Refer Slide Time: 7:54)

<!-- image -->

So, we will keep the records according to this. So, there are different buckets 8 are shown here right now. So, Music has a hash value of 1. So, it goes here. History has hash value of 2, it  goes  here.  Computer science has hash value of 6, it goes here. Interestingly physics and electrical engineering both have hash value 3. So, both of them go here. So, once you come here, you will again have to search linearly you do not know.

So, this is the collision that is happening, this is what puts two or more distinct values in the same bucket, at this is how it can be organized and it can see that while searching linearly within  a  bucket  is  certainly  over  it,  but  it  is  also  true  that  if  I  have  an  appropriate  hash function,  then  out  of  n  bucket  possibilities  n-1  have  got  eliminated.  So,  there  is  a  large number of keys which have got eliminate. So, the linear search even though it is required will be done on a very small set, relatively small set.

<!-- image -->

Now, naturally there are other than collision, there are certain naturally we would want hash functions,  which  do  not  give  a  lot  of  collision.  So,  what  will  be,  there  will  be  some  other desirable properties for example,  in  the presence  of  collision, which  will,  which  is unavoidable the number of keys that map to a bucket should be more or less uniform. If it is not, then one bucket will start growing larger and larger and it will overflow the block size.

So, I have to have another block as an extension of that bucket and so on so forth. So, it this uniformity of hash values is a very desirable property of a hash function. Similarly, a hash function is called ideal if the, every bucket will have the same number of keys and typically, only  random  functions  are  behave  in  that  way  and  of  course,  we  cannot  just  work  with random functions as such.

<!-- image -->

Now, if a bucket has  too  many entries, it  could  happen in  multiple  ways,  one  could  be  is because you have insufficient number of buckets that is you are trying to map to a very small range. So, very you will have much higher amount of collision and buckets will become full very  easily.  It  could  happen  because  the  distribution  is  skewed  it  is  not  uniform  or  not nowhere near uniform.

There are multiple records which have the same key value. For example, let us say we were looking at the department name and let us say the mechanical engineering department have 150 instructors whereas Music Department has 5 instructors, naturally the data inherently is skewed.

So, either you have, you know the statistics of this data distribution and use that in the hash function or you will get naturally very skewed result in terms of number of records going to the same bucket.  It could also happen because of the choice of the hash function, because some  hash  functions  give  a  better  uniform  distribution  some  give  less,  but  it  will,  it  is  a situation we will have to live with all the time.

<!-- image -->

So,  the  choice  is  to  have  overflow  buckets  that  you  need  false  here  you  are  filled  very naturally,  you  will  have  a  pointer  to  go  to  the  next  of  course,  this  is  increasing  your  cost dramatically now, because you are searching through a bucket in a linear form. And as you do  that,  so,  you  have  more  and  more  in  the  chain,  you  have  those  many  additional  block transfers to be done to memory because if every block, every bucket is the size of a block, one you have brought you did not find it there,  you have  to go  to  the  next again  keep on doing this.

So, overflow handling is a problem in this scheme, which is otherwise called a closed hashing scheme. There are alternates to that, but they are not suitable for database application.

(Refer Slide Time: 12:43)

<!-- image -->

So, this hash indices. This hash values I mean just to note that can be used not only for file organization, but you can use it for basic index  structure organization also, because that is quite understandable, because in either case, you are basically doing a search operation. And hashing is a shortcut, efficient shortcut for searching a key from a appropriate bucket with the power of this mathematical hash function.

(Refer Slide Time: 13:26)

<!-- image -->

So, this is an example here of the earlier one here, we have organized the records according to  the  ID  of  the  employee  going  to  different  buckets,  and  the  computation  is  you  add  the digits. So, for 76766, you add the digit, 7+6; 13+7; 20+6; 26+6; 32. So, 30, you get 32. And then you do 32. Here, you can see mod 8, so which will give you 0, so bucket 0 has this. So, that is how you do.

Now, you would normally expect this to be pretty uniform across values, but the fact is the, this kind of IDs are not generated in that way, it may have some other bias to do that. So, given this data, you can see that bucket 5 has 5, 4 entries, whereas the bucket size is 2. So, it has a, it has to take care of overflow bucket to go through. So, additional block access, and if you increase this more, it might increase even more.

<!-- image -->

So,  in  summary,  the static  hashing which maps search  key  values  to  a fixed  set  of bucket addresses becomes a problem because once a bucket starts getting more and more records concentrate on that, you have to make that overflow chain, which is so, and also the fact that the database is a dynamic entity.

So,  initially  a  database  is  small,  so  you  need  a  small  number  of  bucket,  as  it  grows,  the performance  will  degrade.  If  you  allocate  initially  itself  that  I  will  allocate  these  many buckets with the anticipated growth, then there is a significant amount of space that is wasted initially, and in fact, in many cases you do not know what that growth could be. So, the basic problem lies with having to deal with a fixed set of buckets in case of the static hashing.

So, what would be preferable if we could change the number of buckets dynamically? Now, the number of buckets just to recall is the range of the hash function. So, if I change this n naturally, I will have to change the hashing function and rehash everything. For example, in the last ID case, we were doing adding the digits and doing a modulo 8, to increase we at one point we decide to do modulo say 12 that will increase 4 buckets, 50 percent. But as we do that, the hash values will change. So, all reorganization will be required.

So, the static hashing has a problem with the growth it is good fast for I mean kind of if your database  data  is  more  or  less  static,  which  is  normally  would  not  be  the  case  for  most databases, but in general it will have a problem with this growth.

5

<!-- image -->

So, we move on to dynamic hashing or also called extendable hashing. In extendable hashing hash function is not taught to be changed, you cannot do that. It generates a value over a large range that is as if you are thinking that there is a virtual space of buckets. So, you can say there is a b-bit integer, the range is a b-bit integer. So, what we are saying is hash function goes  from  D  to  2  to  the  power  b,  if  it  is  a  b-bit  integer,  then  there  are  2  to  the  power  b possibilities and say, with the value 32.

So, which is, it is quite unlikely that most databases will require so many buckets will not. But this is what is you start with so that that is your function. That is how you design the function. The trick lies in the next step. You have 32 bits, but you do not use all of them. You just use a few prefix bits of the index. Rest of them you ignore. So, maybe if you are, if you want to have 4 buckets, then you use 2 bits from the front and ignore the remaining 30. What does that mean? That means that every 2 to the power 30 buckets are getting collapsed into 1 bucket. They are getting collapse into 1 bucket.

So, just if you would be comfortable with an example, let us say my B is 3, my B is 3. If I use just a single bit prefix, then I have a bucket 0 and a bucket 1; 2 buckets. So, 0123 all these 4 buckets virtual buckets mapped to buckets 0. 4567, all these virtual buckets map to bucket 1. Instead, if I use 2 bits, instead of using 1, then what happens, I have bucket 0 here with 0 and 1, I have bucket 1 here, with 1 and 2, I have bucket 2 here with 4 and 5, I have bucket 3 here with 6 and 7.

So, you can see by, I mean, what I am trying to show you is by the choice of how many bits in the prefix you take, you do not need to recompute the hash function by but by changing this  number of bits you take from the prefix can actually change the buckets that you use. Now, so, it could be anywhere between 0 to 1 bit to 32 bits, and as i grows, the number of prefix bits that you are using as that grows, then you will shrink the database size. I mean, I am sorry, as  that  grows,  you  have  more  number  of  buckets  available.  And  if  that  shrinks, there are less number of buckets available.

So,  the  database  size  based  on  the  growth  and  shrinkage  of  the  database  size,  you  could control this value of i. Now naturally, even in this it is possible that so, you have now you have these set of prefixes  that  you  have  chosen,  and  then  you  take the  buckets  mapped  to them.  Now,  it  is  possible  that  all  the  prefixes  that  you  have  taken  may  not  have  separate bucket for the simple reason that when you make your choice of the prefix bits, you can use 1, you can use 2, you can use 3 like that.

But for that, the number of buckets you need is 2 4 8 like that, as you increase 1 bit in the prefix, your number of bucket requirement doubles. But you may not actually have that much of data to double or that much of space to allocate for buckets. So, you may be using 3 bits requiring  8  buckets,  but  you  may  actually  be  using  5  buckets.  So,  the  actual  number  of buckets may be less than 2 to the power i. So, what does that mean that some of these values from this i bits will map have to map to the same bucket. That is the point we are talking of here.

(Refer Slide Time: 23:10)

OF

<!-- image -->

TECH

For example, here is an example with you have 2 bits used. So, the bucket address table this is  called  the  bucket  address  table  where  you  keep  the  hash  value  and  the  corresponding bucket  pointer.  So,  in  this  bucket  address  table,  you  have  4  pointers,  but  you  have  only  3 buckets. So, these two and we will see how that happens. These two are mapped to the same bucket whereas 2 and 3 are mapped to two different buckets. 0

<!-- image -->

So,  let  us  see  I  mean  instead  of  going  through  the extended theory, let  us  quickly  get  to  a point where we can, now searching is quite obvious, you get to this get to the index, compute the hash, take the prefix as many bits as we are using now, go to that bucket address table, go to the bucket and you have everything.

Now, when you are trying to insert a record that means you might need more bucket. There are  two  possibilities,  one  is  the  number  of  prefix  you  are  using  is  greater  than  what  you actually have in terms of the buckets. So, it is possible that you can allocate a new bucket as you will get a new bucket. You have to reorganize the records between the earlier bucket and the newly allocated bucket and recompute the new bucket.

If it is same that every index points to one bucket only, then you do not have buckets left. So, you may not be able to do a split for this insertion, you can create an overflow bucket. But the other  option  is  you  can  increment  the  value  of  i  you  can  use  1  more  bit.  So,  the  bucket address table will become doubled. And you will reorganize the buckets in the bucket address table so that your bucket address table is becoming double, but your value of actual buckets is increasing only by 1 because that is what you need.

So, you do not unnecessarily create empty buckets and push in there, you do not need to, rest of the that is i+1 - ij+1 or i-ij number of buckets will of pointers will point to the same some of the same buckets as they exist.

(Refer Slide Time: 26:20)

IIT Madras

## Deletion in Extendable Hash Structure

Module 44

Dynamic

Hashing

Madras

Uas

5

- To delete a key value,
- locate it in its bucket and remove it
- The bucket itself can be removed if it becomes empty (with appr( the bucket address table)
- Decreasing bucket address table size is also possible
- Coalescing of buckets can be done (can coalesce only with a 'bud same value of ij and same ij -1 prefix, if it is present)
- Note: decreasing bucket address table size is an expensive ope be done only if number of buckets becomes much smaller thar table

Use of Extendable Hash Structure: Example

dept\_name

## h(dept\_name)

0010 1101 1111 1011 0010 1100 0011 oC

Sci. Comp.

1111 0001 0010 0100 1001 0011 011011

Elec. Eng

0100 0011 1010 1100 1100 0110 1101 11

Finance

1010 0011 1010 0000 1100 0110 1001 11

1100 0111 1110 1101 1011 1111 0011 1(

Music

0011 0101 1010 0110 1100 1001 1110 1(

Physics

1001 1000 0011 1111 1001 1100 0000 00

Biology

History

Deletion happens by the same logic rather, I am keen to go to an example. So, let us start with this in the next couple of minutes. So, this is a 32 bit hash key generated for the department name. So, we will use this as our data.

(Refer Slide Time: 26:42)

5

<!-- image -->

So, this is the initial you have 0, this is the initial bucket, this is the data to insert. So, I will insert Mozart, Srinivasan and Wu in this order. So, Mozart is music, Srinivasan is computer science and Wu is in finance. Finance, music, computer science 1 bit, 1 bit, 1 bit. So, you can see that finance and computer science will clash will be in the same bucket and music will be in a different bucket.

(Refer Slide Time: 27:20)

<!-- image -->

So, that is what has happened they are and this is in music is in a different bucket because it has a value 0 and computer science and finance has a value 1. This 1 marks how many bits are being used to come to this bucket. So, in both of these, this is 1, now we want to insert Einstein onto this.

(Refer Slide Time: 27:49)

<!-- image -->

So, what is Einstein? Who is, I mean where is Einstein, is in physics, physics, this is 1. So, when it comes to that, if we go back a slide. If we go back a slide, we will see that physics is 1, computer science is 1, finance is also 1. So, Einstein needs to go in here, where we have assumed that every bucket has 2, size of 2. So, this bucket is already full. So, Einstein cannot go in here.

So, what I do is I increase the value of i that is the number of prefix bits we are using. And so therefore,  your  bucket  address  table  now  has  4  entries.  You  have,  you  had  2  buckets  and because  of  this  need  to  insert  a  new  record  you  need  another  bucket  so  you  have  created another bucket. Now let us look at the values.

Physics is 1 0, that is 2, music is 0 0 that is 0. Finance is 1 0, that is 2, computer science is 1 1 that is 3. So, this computer science comes here, this is 3 2 1 0, physics and finance come here music remains in 0, no change. And so, this we had to create because of inserting this record so this goes separately  with  index  2. This also is having  2 but we  do  not  need to  create a separate bucket for 1. The value 1 that is which will mean a prefix of 0 1 that is till we get electrical engineering actually. And we let both of these map to the same bucket.

So, if you look in carefully, here we are saying 1 that is 1 bit is used because the second bit is ignored, because you have multiple are mapping here, so, 0 and 1 out of 0 and 1 you are just using the 0, from 0 0 and 0 1, you are representing by 0, so, it is 1 bit whereas, these two are 2 bits, it is as simple as that. So, you can insert Gold and El Said records.

(Refer Slide Time: 30:43)

<!-- image -->

<!-- image -->

Gold is in physics clearly goes in here. El Said is in history, is in history, History is 3. So, that that can go in here. And you can see that again, we increase the number of bits again, this is using 1 prefix only. So, 4 values are here, this is using all the 3. So, 1. This is using all the 3, this is using just 2. So, you have 2 values coming here. So, it keeps on going in this manner, you can step by step work out, we are including all of these.

(Refer Slide Time: 31:41)

<!-- image -->

<!-- image -->

Now, when you included all of these, you again had a overflow with brand, because computer science  needs  another  block.  Now,  you  may  use  4  bits,  but  you  chose  not  to  immediately increase to 4 bits. Because you can see that well. There is already a number of, unused stuff here,  but  it  is  just  that  the  keys  are  biased  towards  this  side.  So,  instead  of  increasing  the bucket address table size, reorganizing it, you use a overflow bucket. So, it is kind of a tradeoff between the two as to which one you want to, you want to do at different stages. Finally, you insert Kim.

(Refer Slide Time: 32:43)

<!-- image -->

<!-- image -->

And go through the steps carefully so that you will know that what will. So, the comparison is pretty straightforward. Obviously, the dynamic scheme works better. Though change of the bucket address table is an expensive operation and has to be done with judgment.

(Refer Slide Time: 33:06)

<!-- image -->

And comparison of ordered indexing and hashing clearly shows that hashing would that way be  quite  good  because  it  does  not  require  the  cost  of  periodic  reorganization,  relative frequency of insertions and deletions can be considered for that and depends on also the kind of queries you have, like hashing is good to retrieve records with a specific value because you need to hash.

Range queries are will be good with ordered indexing, because you need to go over a certain range. In spite of the power of the hashing in practice, though, it is not so widely used in the big databases like I have just given some information of what so these are the schemes exist, but this is really what most of your major database provider actually do.

(Refer Slide Time: 34:14)

<!-- image -->

<!-- image -->

One small closing concept this is called a bitmap index. The idea of a bitmap index is certain attributes  have  a  fixed  set  of,  fixed  and  small  set  of  values  like  gender,  only  two  possible values  or  maybe  few  more,  The  country's  170-200  value,  states  of  a  country  maybe  100 values, certain income levels, maybe 20 income levels and so on.

So, why, since when you have this small set of enumerated data like this for an attribute, then the idea is why do you keep on writing that male, male, male, male, female, female, female, female, female, female, like that? Why do you replicate? Instead, you could keep this in a different way, you can just turn the table instead of mentioning the value of an attribute for a record,  instead  you  look  at  from  the  attribute's  perspective,  you  look  at  whether  a  given attribute value is present for that record. So, simple example.

So,  number the records  in some  arbitrary sequential  order,  and  then  you  try  to  see, this  is going from left to right, I am looking at so, I have a bitmap, which is the number of records that I have and if m male is present, I put a 1, this is female, I put a 0, this is female, I put a 0 this is male, I put a 1. Similarly, in female, I will just have the other places as well.

So, when you have to search for a particular, I mean is male, all that you need to do is to collect  the  bits,  which  are  the  which  are  indicative  whose  positions  are  indicative  of  the record number. Similar thing you can do for income level.

<!-- image -->

What is actually far more interesting is you can actually do and if you want to say the male and income level 14 A, then the two bitmaps of the same size the number of records in the collection, you can just AND them. So, logically AND them and wherever you get a 1 is the other position other indices of the records which have that.

(Refer Slide Time: 36:47)

<!-- image -->

<!-- image -->

## Bitmap Indices (5): Efficient Bitmap Operations

- Bitmaps are packed into words; a single word and (a basic CPU instri and of 32 or 64 bits at once
- For example; 1-million-bit maps can be and-ed with just 31,250 ir
- Counting number of 1s can be done fast by a trick:
- Use each byte to index into a precomputed array of 256 elements count of 1s in the binary representation
- Can use pairs of bytes to speed up further at a higher memory
- Add up the retrieved counts
- have a number of matching records large
- Worthwhile if 1/64 of the records have that value; assuming a

<!-- image -->

## Module Summary

- Explored various schemes Static and Dynamic hashing Hashing
- Compared Ordered Indexing Hashing and
- Studies the use of Bitmap Indices for fast access of columns with limi distinct values

So,  these  are  you  know,  more  details  in  discussion.  And  there  are  several  algorithms  to efficiently compute this through lookup tables and so on. So, bitmap is a nice idea to expedite the access of a number of attribute, possible attributes which have fixed small set of possible values.  So,  with  that,  we  come  to  the  end  of  this  module.  Thank  you  very  much  for  your attention and we meet in the next module.
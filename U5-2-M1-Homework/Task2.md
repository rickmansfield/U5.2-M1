# Unit 5.2 M1 Homework Task 2

Q) Why does the processor get a speed boost when the processor access nearby memory addresses in RAM one after the other?

a.   Because of the cache?
b.  Because the mathematical computations that the processor completes to find the next item in memory takes less time than the necessary calculations to find things that are further away?
c.  Because the mechanical spinning hard disk takes less time to access items that are next to each other?

My guess was "a."

FYI this is sort of a trick question A doesn't seem right since the original question RAM in NOT held in the processor. Cache is held in the processor. So If the questioned asked about a boost due to accessing cached in the process then THAT would be why it's faster and "Because of the cache" would be THE clear answer. 

Whenever you use a computer, you are very concerned with the speed of the computer you are using. So, computer designers made a way to optimize for speed when accessing items in RAM. Whenever a processor accesses a box in RAM, it also accesses and stores the boxes near it. Often, if you are accessing one thing in RAM, it's likely that the next thing you need to access is nearby. That's why keeping a copy of nearby items in the cache speeds things up.

Whenever the processor reads something (say, the player's position in an old adventure game) out of RAM, it adds it to the cache to use it again in the future. Then, when it needs something else from RAM, it will go to the cache for it. As you can see, the cache helps the processor by saving execution cycles required to go out and read something from RAM.

__The processor, not RAM, has the actual cache.__ The memory controller keeps track of what goes into and comes out of the cache. 

But in this case the question references speed dealing only with processor TO RAM via bus. 

The answer is not "c." becuase Things like videos and files are stored on a disc, not in RAM. RAM is faster than disc storage, but there isn't as much space available. Disc storage has more space, but it is slower.
24.  Distinguish `std::vector`, `std::queue`, `std::stack` and `std::deque` in **C++**. When are they useful in an **AI**/Vi**s**ion context?

Vector is a abstract representation of array type of sequence memory block. Vector could change in size.

Queue: a specific type of list of element operate in a FIFO way (first in first out)

Stack: a specific type of list of element operate in a LIFO way (last in first out)

Deque: a double-ended-queue, that is it can insert/extract element on both ends.

AI/Vision algorithm ultilize a lot of matrix multiplication, which mostly will use vector as a base to do multplication. 
Some AI system(e.g: face check system) use queue structure to store information about object (like a cache for faster process). Especially in real-time system, we could use queue to give more speed gain over simple vector. (e.g: user send 10 image to server, which order we process the image ?)
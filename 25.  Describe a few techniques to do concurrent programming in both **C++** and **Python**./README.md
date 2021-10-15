25.  Describe a few techniques to do concurrent programming in both **C++** and **Python**.

### Python concurrency:
Type of concurrency in Python
+ pre-emptive multitasking(threading): the operating system decide when to switch task
+ collaborative multitasking(asyncio): the tasks decided when to give up control
+ multiprocessing(multiprocessing): run many process on many processors

Type of task for concurrency:
- I/O bound task: Spends most of its time comunicate with a slower device
- CPU bound task: Spends most of its time doing CPU computation

For I/O bound task: 
- MulthiThread: Predefined ThreadPoolExecutor = Thread + Pool + Executor, help control where and when to use which thread. We just need to define the function and send it to the pool. Helpful since its just require minor modification and good performance
- Asyncio: define async await so that the tasks never give up control without intentionally doing so. Don't need worry about thread-safe resource and usually yeild faster performace.

For CPU bound task:
- Multiprocessing: Create an instance of interpreter on each CPU. So when doing high computational task, split task into multiple processors help speed up significantly.


### C++ vs Python concurrency
- In C++, threading can provide a general speed-up for both computationally bound and I/O bound problems, as threads can take full advantage of the cores on a multiprocessor system.
- Python, on the other hand, has made a design trade-off to use the Global Interpreter Lock, to simplify its threading implementation.

For async IO routines, C++ allow usage of multiple threads for faster computation while Python use only one thread and more lightweight.

For multiprocessing, python use lib multiprocessing while c++ use fork() to provide multiprocessing support. However, in c++ is much more complex.
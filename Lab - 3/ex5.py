# Write a small text that relates the execution of CPU-Bound and I/O-Bound programs, when executed in single thread
# or multi-threading, considering the performance and states of the threads presented in Figure 1 – States in the
# life of a thread - ( page 396 of the Fundamentals of Python book)

# Firstly, let's state that for CPU-bound programs the time needed for execution
# depends only on the speed of the processor while I/O-bound programs are the conplete
# oposite because time needed for execution depends on waiting for input/output instructions.
# So, in this case considering the lifecycle of threads we can conclude that for CPU-bound programs
# there is no need in multithreading because thread always stays in running state until the execution
# ends and thread "dies" -> which basically depends only on processor speed and not on the numbers
# of threads running. While when the program is I/O bound it makes significant benefit for
# speed of running using multithreading because for multiple threads there is no need in waiting for input/output
# instructions to run because each thread is independent of each other's i/o wait time while one thread is waiting


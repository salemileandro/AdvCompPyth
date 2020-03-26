### Author: Leandro Salemi
### E-mail: salemileandro@gmail.com

# a. Investigate the performance of the matmult.py script
## In which line(s) of the script would you start optimizing for speed? Which line(s) create the most memory?


The matmult_*.out files contains the output of the different profilers. If we start with the cProfile profiler, we get that the "matmult" function takes more time. Which makes sense since it's a quite naive implementation using loops and thus on order N^3 !


By far, it is the lines where the summing up the elements happens that takes most time. Memory wise, it is the memory allocation of matrices that are expensive. But what is quite impressive is the memory is takes ... We have 250 x 250 matrices here, meaning that we should get 62500 elements per matrix. If we assume double precision, each number is 8 bytes therefore 500000 bytes or 500 kB ! We have here memory on the order of 40 MB used, which roughly one order of magnitude more. This shows that natice python lists are not efficient for these kind of operations. We'd better use C-like contiguous arrays, that can be done with numpy for instance !!!


Here, we are kind of trying to reinvent the wheel ! For optimizing the code, numpy is a must ! It's written in C, calls blas/lapack high performance libraries in the background. It may even be linked to mkl which is often found to give great performance (especially on intel cpus). We'll compare performance on



# b. Investigate the performance of the euler72.py script
## In which line(s) of the script would you start optimizing for speed? Which line(s) create the most memory? (This is one problem from the euler project: https://projecteuler.net/problem=72)

The phi function is quite slow. The loop over factors seems to be to bottleneck here.
    42   1323700     486732.0      0.4     28.4          for f in factors:
    43   1020508     420330.0      0.4     24.6              if i%f == 0:

Memory wise it's the same as before. The array creations are really not-efficient !!

#c. Improve the performance of the matmult.py script
## What is the best performance that you achieved with N=250?


0.015431 s with numpy vs 14.153 s with the python list naive algorithm ... It's rougly 1000 times faster!








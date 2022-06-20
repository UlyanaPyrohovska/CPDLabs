#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <time.h>
#include <omp.h>

void *print_message_function( void *i );
void ex1();
void ex2();
void ex3();
void ex4();
static long num_steps = 1000000000;

int main()
{
  
  ex1();
  //ex2();
  //ex3();
  ex4();
  
  return 0;
}
void ex1(){
   int i;
   double step, x, pi, sum = 0.0;
   step = 1.0 / (double)num_steps;
   clock_t inicio = clock();
   sum = 0.0;
   for (i = 1; i <= num_steps; i++)
   {
     x = (i - 0.5) * step;
     sum = sum + 4.0 / (1.0 + x * x);
   }
   pi = step * sum;
   clock_t fim = clock();
   double tempo = (double)(fim-inicio)/CLOCKS_PER_SEC;
   printf("\npi = %.20f\ntime used to calculate pi: %f\n", pi,tempo);
}
// The smaller the number of steps, the bigger the error because the approximations are worse

void *print_message_function( void *i ){
  int a = *((int *) i);
  free(i);
  printf("Thread %d\n",a);
}
//The program creates an array of threads with size 4, then makes a for loop in which each loop will allocate in heap memory an argument, which is
// the iteration number ( thread ) and then create a thread with this argument and the print message function. then join all threads
void ex2(){
  printf("Start Processing with Threads!\n");
  pthread_t thread[4];
   for (int i = 0; i < 4; i++) {
     int *arg = malloc(sizeof(*arg));
     *arg = i;
     pthread_create( &thread[i], NULL, print_message_function, arg);
   }
   for (int i = 0; i < 4; i++) {
     pthread_join( thread[i], NULL);
   }
   printf("Finished processing with threads!\n");
}
void ex3(){
    omp_set_num_threads(4);
    printf("Start Processing with Threads!\n");

    // execute em paralelo
    #pragma omp parallel
    {
        int tid = omp_get_thread_num();
        printf("Thread %d\n",tid);
    }

    printf("Finished processing with threads!\n");
  // In this code snippet we use omp parallel which creates a parallel region in which the code will be executed in multiple threads in parallel instead of pthreads
}


void ex4(){
    int i, j;
    double step, x, pi, sum = 0.0;
    double start_time, run_time;
    step = 1.0 / (double)num_steps;
    for (j = 1; j <= 4; j++) // launches executions with 1, 2, 3 e 4 threads
    {
        sum = 0.0;
        omp_set_num_threads(j);
        start_time = omp_get_wtime();
        //creates a thread group
        #pragma omp parallel default(none) private(i, x) \
        shared(j, num_steps, step, sum) \
        num_threads(j)
        {
            int tid = omp_get_thread_num();
            #pragma omp single //identifies a section of code that will be run on a single available thread
            printf(" num_threads = %d", omp_get_num_threads());
            double somaParcial = 0.0;
            for (i = tid*(num_steps/j)+1; i <= (tid+1)*(num_steps/j); i++)
            {
                x = (i - 0.5) * step;
                somaParcial = somaParcial + 4.0 / (1.0 + x * x);
            }
            #pragma omp barrier //identifies a synchronization point at which threads
                                // in a parallel region will wait until all other threads in that section
                                // get to the same point
            sum += somaParcial;
        }
    pi = step * sum;
    run_time = omp_get_wtime() - start_time;
    printf("\n pi is %.20f in %f seconds and %d threads\n", pi, run_time, j);
    }
//The approximation of pi depends on the number of steps so the approximation of pi will be similar when using the same number of steps
//for ex1 and ex4, when we use few steps we can see that ex1 is more accurate because it doesn't spend cycles creating threads.
//if we use a very large number of steps the first one takes more or less the same time as ex1 but the following threads take considerably
//less time
}
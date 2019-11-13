# Rabbits and Recurrence Relations

## Problem 

A sequence is an ordered collection of objects (usually numbers), which are allowed to repeat. Sequences can be finite or infinite. Two examples are the finite sequence (π,−2‾√,0,π) and the infinite sequence of odd numbers (1,3,5,7,9,…). We use the notation an to represent the n-th term of a sequence.

A recurrence relation is a way of defining the terms of a sequence with respect to the values of previous terms. In the case of Fibonacci's rabbits from the introduction, any given month will contain the rabbits that were alive the previous month, plus any new offspring. A key observation is that the number of offspring in any month is equal to the number of rabbits that were alive two months prior. As a result, if F<sub>n</sub> represents the number of rabbit pairs alive after the n-th month, then we obtain the Fibonacci sequence having terms F<sub>n</sub> that are defined by the recurrence relation F<sub>n</sub>=F<sub>n-1</sub>+F<sub>n-2</sub> (with F<sub>1</sub>=F<sub>2</sub>=1 to initiate the sequence). Although the sequence bears Fibonacci's name, it was known to Indian mathematicians over two millennia ago.

When finding the n-th term of a sequence defined by a recurrence relation, we can simply use the recurrence relation to generate terms for progressively larger values of n. This problem introduces us to the computational technique of dynamic programming, which successively builds up solutions by using the answers to smaller cases.

__Given__: Positive integers n≤40 and k≤5.

__Return__: The total number of rabbit pairs that will be present after n months, if we begin with 1 pair and in each generation, every pair of reproduction-age rabbits produces a litter of k rabbit pairs (instead of only 1 pair).

### Sample 1

```
Input: 5 3
Output: 19
```

### Sample 2

```
Input: 29 2
Output: 178956971
```

### Code check

Check your code answers at [rosalind.info](http://rosalind.info/)!

## Reference

More about the problem can be found here: [rosalind.info](http://rosalind.info/problems/fib/)

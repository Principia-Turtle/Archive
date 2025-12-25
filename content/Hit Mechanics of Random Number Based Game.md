#### Author:
Baldessarini

## Introduction
Mathematically we are dealing with a pseudo random number generator which determines number of successes in a sequence of N independent experiments, each asking a yes–no question: Will it hit or not? Will it crit or not? Etc. such a system is described by Binomial distribution.

>I assume the trials are independent of each other, meaning the game doesn't remember how many times I didn't suceed a trial to make it more likely, but rather just putting a chance of successful trial on each hit.

## The formula
The probability of getting exactly k successes in N independent Bernoulli trials (with rate of probability p) is given by the probability mass function:

$$
\begin{pmatrix}
N \\
k
\end{pmatrix}
p^k
(1-p)^{N-k}
$$

where:

$$
\begin{pmatrix}
N \\
k
\end{pmatrix}
= \frac{N!}{k!(N-k)!}
$$

>You can think of it, for instance of a case of determining crits, as k = number of crits, N = number of successful hits and p = crit chance. The resulting number will be the chance to get the desired number of crits (k)

## The example
Let's assume 100 hit long fight, our crit chance is 30% = 0.3 and we want to know what is the chance to get exactly 30 crits:

$$
\begin{pmatrix}
100 \\
30
\end{pmatrix}
0.3^30
(1-0.3)^{100-30} = 0.086784
$$

>This is 8.6% chance only to get the exact amount of successful trials.


## Diminishing returns

As raiders we are rather interested in the chance of getting exactly 30, or more, which is then: 53.77% 

We can plot how the effect of different p (on hit chance) behaves when we consider this logic:

![[graph-bernoulli.png]]

This plot doesn't show how many crits we will get, but the chance of scoring more, than is our crit chance. The sweet spot seems to be somewhere around 40% for crit chance, where I can be almost sure we get more crits, than is the actual rating. Also having less than 20% will yield diminishing returns, where we are destined to score less, than is our rating.
>Also note it can be adjusted to hits, resists, glancing blows or partials too

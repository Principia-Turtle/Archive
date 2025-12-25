# Hit Mechanics of Random Number Based Game
Mathematically we are dealing with a pseudo random number generator which determines number of successes in a sequence of N independent experiments, each asking a yes–no question: Will it hot or not? Will it crit or not? Etc. such a system is described by Binomial distribution.

>I assume the trials are independent of each other, meaning the game doesn't remember how many times I didn't suceed a trial to make it more likely, but rather just putting a chance of successful trial on each hit.

## The formula
The probability of getting exactly k successes in n independent Bernoulli trials (with rate of probability p) is given by the probability mass function:

$$
\begin{pmatrix}
n \\
k
\end{pmatrix}
p^k
(1-p)^{n-k}
$$

>You can think of it, for instance of a case of determining crits, as k = number of crits, n = number of successful hits and p = crit chance. The resulting number will be the chance to get the desired number of crits (k)

## The example
Let's assume 100 hit long fight, our crit chance is 30% = 0.3 and we want to know what is the chance to get exactly 30 crits:

$$
\begin{pmatrix}
100 \\
30
\end{pmatrix}
0.3^30
(1-0.3)^{100-30}
$$

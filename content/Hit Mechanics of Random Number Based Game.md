[[Author-Baldessarini]]

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


## Short encounters

As raiders we are rather interested in the chance of getting exactly 30, or more, which is then: 53.77% 

We can plot how the effect of different p (on hit chance) behaves when we consider this logic:

![[media/graph-bernoulli.png]]

This plot doesn't show how many crits we will get, but the chance of scoring more, than is our crit chance. The sweet spot seems to be somewhere around 40% for crit chance, where I can be almost sure we get more crits, than is the actual rating. Also having less than 20% will yield diminishing returns, where we are destined to score less, than is our rating.

## Long encounters
The graph will differ when we consider a smaller or larger number of trials. The more trials we have (longer encounter), the more the function will look like a step on staircase - meaning the more likely we will get our actual successful trial chance rating. 

![[media/graph-bernoulli-2.png]]

From this we can conclude, that on-hit RNG mechanics, like crit, hit, etc. are more prone to deviations if we have a long cast time, or a slow weapon.

## Average vs. Volatility

If you fight the boss 1,000 times with 0.3 chance, your total score will be exactly 30% of total hits. The math balances out perfectly. But in one encounter you don't get the average, you get a random unreliable sample. As raiders we don't care that much what was our DPS in the whole progression evening, we care if we did our job correctly on a single encounter, which can be a guild first-kill. What I mean by volatility is then "How likely I am to fail on a single encounter". Volatility approaches average with a large number of trials and needs to be adjusted for each class, specialisation and raider based on their attack speed. Here I have increased p = 36% and I check for k = 30% on a 100-hit fight. So I treat crit chance as 20% less effective.

![[media/graph-bernoulli-3.png]]

## Sources

https://en.wikipedia.org/wiki/Binomial_distribution

## Python

You can run the script used to generate the plots in google colab

[Download the Python Script](hit_mechanics_of_random_number_based_game.py)

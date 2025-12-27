### Authors

[[Author-Baldessarini]]

## Archive link connections

[[Mechanics of Random Number Based Game.md]]

## Introduction

General consensus is, that first stat you should have sorted is hit cap. But author didn't suceed finding actual math supporting this. 
Theoretically you could come to a situation, where you choose between 1% more hit, or 1% more attack speed. 

## Average damage

Both stats have almost the same effect on your average damage output,
they increase / decrease it by a fixed percent value. The formula for their relation should look like this:

$$
DMG_{change} = (1 + ATK_{speed}) x (1 - HIT_{miss})
$$

Where $HIT_{miss}$ is your missing hit to a hitcap and both values are of form 1% = 0.01. Then their weight ratio would be the result of this relation when we substitute same values:

$$
DMG_{change} = (1 + 0.01) x (1 - 0.01) = 0.999..
$$

This means the effect of their effect on our damage output is almost identical hit:attack speed = 1:0.999..
>Note that it is only damage output, maybe you are a mage who cannot afford their counterspell to get resisted

Here is a table comparing same values of hit to attack speed

$$
\begin{pmatrix}
Miss chance & Attack speed & Weight \\
-0.01 & 0.01 & 1:0.99..  \\
-0.02 & 0.02 & 1:9996\\
-0.03 & 0.03 & 1:0.9991 \\
-0.04 & 0.04 & 1:0.9984 \\
-0.05 & 0.05 & 1:0.9975 \\
-0.06 & 0.06 & 1:0.9964 \\
...  \\
-0.15 & 0.15 & 1:0.9775 \\
\end{pmatrix}
$$

## Volatility

The table though compares the averages. From [[Mechanics of Random Number Based Game.md]] we know there is a difference between average and volatility, so let's compare it to volatility. 
Using Probability Mass Function to get height of the curve at any point. Height of the curve is probability of the outcome, x-axis is damage output.

$$
PMF = 
\begin{pmatrix}
N \\
k
\end{pmatrix}
p^k
(1-p)^{N-k}
$$

![media/hit-cap-vs-attack-speed.png](../media/hit-cap-vs-attack-speed.png)

Tall and narrow curve means the build is consistent, wide and short means it is volatile.

So there we have two approaches to the problem, one is from average algebraic standpoint, other is from stochastic. The graphs show beautifuly safe approach (hit) vs. risky one (speed). 
Both will produce the same average damage output, but attack speed will help you set new records. If you get an option 1% attack speed vs. 1% hit? I would personally go for the attack speed.

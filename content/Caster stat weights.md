### Authors:

[[Author-Calais]]

### Peer review done by:

none

### Related nodes:

[[Spell and healing power]], [[Spell haste]], [[Hit cap vs haste]], [[Spell crit]]

## Introduction

Earlier (see related nodes) we established all stats as percentual damage increase, the most complicated of them was spell power. To make the stat weights we consider 1% to damage via each stat, then convert it to the stat's rating and normalize it.

We do not take in account the volatility, but only the average.

## Single target vs. AoE

The one thing area of effect spells change, is the number of trials / casts. Another thing is a AoE damage cap, this is different for each spell (around 7-10k) [[source]](https://www.wowhead.com/forums/topic/how-do-you-determine-who-is-king-of-aoe-30962), this damage cap might not work on some private servers.

## Relating haste to hit

12.6 spell hit rating increases your chance to hit by 1%.

15.77 spell haste rating will increase spell haste by 1%

Spell hit, along with haste and crit, is a subject to volatility. In [[Hit cap vs haste]] we can see, that haste is roughly (1) 97.8% - 100% as effective as hit.
>Taking an average, depending on how much hit caster is missing

So we get relation:

$$
Hit : Haste \times C_{haste}
$$

Where $C_{haste}$ is the constant. (If we get 98% effect, then it is 2%)

## Adding crit

If the spell crits, it does 200% or more damage, depending on talent options, for instance mages ignite adds 40% to this value. Doing twice the damage on one cast is same like doing two casts, hence formula becomes:

$$
Hit : Haste \times C_{haste} : Crit / Crit_{bonus}
$$

>the smaller number, the better

## Adding spell power

To add spell power we need to do the math as in [[Spell and healing power]], formula with the ratings then becomes:

$$
Hit : Haste \times C_{haste} : Crit / Crit_{bonus} : SP
$$

## Converting to numerical weight ratios:

$$
12.6 : 15.77 \times (1 + 0.01) : 22.1 / (1 + 0.4) : 33
$$

>The 0.4 is for mage ignite

now divide all numbers by 12.6 (relating it to hit)

$$
1 : 1.26 : 1.25 : 2.61
$$

Here high number means low effectivity, so as a last step I do number inversion, 1/1, 1/1.26 ..  

$$
Hit : Haste : Crit : SP = 1 : 0.79 : 0.8 : 0.38
$$

The Hit to Haste relation will be constant for all classes, Crit weight will only depend on your spells and talents and SP rating needs to be calculated for each spell and itemisation individually.






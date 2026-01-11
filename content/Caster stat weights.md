### Authors:

[[Author-Orfeus]]

### Peer review done by:

none

### Related nodes:

[[Spell and healing power]], [[Spell haste]], [[Hit cap vs haste]], [[Spell crit]]

## Introduction

Earlier (see related nodes) we established all stats as percentual damage increase, the most complicated of them was spell power due to the fact it works as a flat increase, rather than percentual. To make the stat weights we consider 1% to damage via each stat, then convert it to the stat's rating and normalize it.

The Hit to Haste relation will be constant for all classes (read [[Hit cap vs haste]]), Crit and intellect weight will only depend on your spells and talents (read [[Spell crit]]) and SP rating needs to be calculated for each spell and itemisation individually (read [[Spell and healing power]]).

We do not take in account the volatility, but only the average.

## Single target vs. AoE

The one thing area of effect spells change, is the number of trials / casts. Another thing is a AoE damage cap, this is different for each spell (around 7-10k) [[source]](https://www.wowhead.com/forums/topic/how-do-you-determine-who-is-king-of-aoe-30962), this damage cap might not work on some private servers.

## Healing classes

Healers don't deal with hit, hence they should relate the other stats to haste. Haste has no volatility issues, it's effect is linear until hard cap - this makes it ideal of the three.

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

If the spell crits, it does 200% or more damage, depending on talent options, for instance mages ignite adds 40% to this value. Doing twice the damage on one cast is same like doing two casts. Imagine a 100 casts long fight, if you have 1% of more haste is the same like having 1% extra crit. Hence formula becomes:

$$
Hit : Haste \times C_{haste} : Crit / Crit_{bonus}
$$

>the smaller number, the better
>

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

>The discrepancy between hit and haste comes from the ratings, you need more haste rating for 1%

## Adding crit from intellect

Every 80 points of intellect give us 1% spell crit, we can directly relate it to spell crit then: 22.1/80 = 0.276 = effectivness of intellect compared to spell crit rating.

## Final weights

Hit : Haste : Crit : Int : SP = 1 : 0.79 : 0.8 : 0.22 : 0.38 

>For a full BiS mage example

## Python

Script for the graph in google colab

[Download the Python Script](caster-stat-weights.py)








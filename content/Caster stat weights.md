### Authors:

[[Author-Orfeus]]

### Peer review done by:

none

### Related nodes:

[[Spell and healing power]], [[Spell haste]], [[Hit cap vs haste]], [[Spell crit]]

## Introduction

Earlier (see related nodes) we established all stats as percentual damage increase, the most complicated of them was spell power due to the fact it works as a flat increase, rather than percentual. To make the stat weights we consider 1% to damage via each stat.

The Hit to Haste relation will be constant for all classes (read [[Hit cap vs haste]]), Crit and intellect weight will only depend on your spells and talents (read [[Spell crit]]) and SP rating needs to be calculated for each spell and itemisation individually (read [[Spell and healing power]]).

We do not take in account the volatility, but only the average. Volatility could slightly increase the weight of spell crit. 

## Single target vs. AoE

The one thing area of effect spells change, is the number of trials / casts. Another thing is a AoE damage cap, this is different for each spell (around 7-10k) [[source]](https://www.wowhead.com/forums/topic/how-do-you-determine-who-is-king-of-aoe-30962), this damage cap might not work on some private servers.

## Healing classes

Healers don't deal with hit, hence they should set $W_{haste} = 1$

## Relating haste to hit

12.6 spell hit rating increases your chance to hit by 1%.

15.77 spell haste rating will increase spell haste by 1%

Spell hit, along with haste and crit, is a subject to volatility. In [[Hit cap vs haste]] we can see, that haste is roughly (1) 97.8% - 100% as effective as hit.
>Taking an average, depending on how much hit caster is missing

So we get relation:

$$
W_{hit} \space : \space W_{haste} = 1 \space : \space \frac{1}{1 - HIT_{miss}}
$$


>Hit miss is a positive number

## Adding crit

Read the related node, the formula becomes:

$$
W_{hit} \space : \space W_{haste} \space : \space W_{crit} = 1 \space : \space \frac{1}{1 - HIT_{miss}} \space : \space \frac{\frac{1}{Crit_{bonus}}}{1 - Hit_{miss}}
$$





## Adding spell power and itellect

To add spell power we need to do the math as in [[Spell and healing power]]. Every 80 points of intellect give us 1% spell crit, we can directly relate it to spell crit then: 22.1/80 = 0.276 = effectivness of intellect compared to spell crit rating. formula with the ratings then becomes:

$$
W_{hit} \space : \space W_{haste} \space : \space W_{crit} \space : \space W_{INT} \space : W_{SP} = 1 \space : \space \frac{1}{1 - HIT_{miss}} \space : \space \frac{\frac{1}{Crit_{bonus}}}{1 - Hit_{miss}} \space : \space  \frac{W_{crit}}{0.276} \space :  \space 0.01 \times \frac{\frac{Base_{spell}}{C} + SP_{current}}{1 - HIT_{miss}}
$$




## Final weights

In final weights I am interested in "how much of each stat will increase my performance by 1\%" Hence the weights, after multiplying it by ratings are:

$$
W_{hit} \space : \space W_{haste} \space : \space W_{crit} \space : \space W_{INT} \space : W_{SP} = 12.66 \space : \space \frac{15.77}{1 - HIT_{miss}} \space : \space \frac{\frac{22.1}{Crit_{bonus}}}{1 - Hit_{miss}} \space : \space  \frac{W_{crit}}{0.276} \space :  \space 0.01 \times \frac{\frac{Base_{spell}}{C} + SP_{current}}{1 - HIT_{miss}}
$$

So the lower the number, the better. This relation also confirms, why hit is the first stat everyone should start with, it reduces the effectivness of all the other stats.



## Movement penalty

The benefit of working with the weight in this form, rather than 1 : 0.97 : 0.75 ... etc. is that we can directly see how moving punishes us during encounters. Missing 1 cast is equal to loosing 2-3 sec of our active casting time. Maybe having 30 extra spell power will buy us a few seconds of activity, or we can compensate lack of gear by correct positioning. Hence we can relate the all the stats to a more basic unit - time.




## Python

Script for the graph in google colab

[Download the Python Script](caster-stat-weights.py)








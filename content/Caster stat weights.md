### Authors:

[[Author-Orfeus]]

### Peer review done by:

none

### Related nodes:

[[Spell and healing power]], [[Spell haste]], [[Hit cap vs haste]], [[Spell crit]]

## Introduction

Earlier (see related nodes) we established all stats as percentual damage increase, the most complicated of them was spell power due to the fact it works as a flat increase, rather than percentual. To make the stat weights we consider 1% to damage via each stat, then convert it to the stat's rating and normalize it.

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
\frac{1}{W_{hit}} \space : \space \frac{1}{W_{haste}} = 1 \space : \space (1 + Haste) * (1 - HIT_{miss})
$$

>Higher number means lower effectivity, to get the correct weight we need to do inversion later.

## Adding crit

If the spell crits, it does 200% or more damage, depending on talent options, for instance mages ignite adds 40% to this value. Doing twice the damage on one cast is same like doing two and more casts. Imagine a 100 casts long fight, if you have 1% of more haste is the same like having 1% extra crit. Hence formula becomes:

$$
\frac{1}{W_{hit}} \space : \space\frac{1}{W_{haste}} \space : \space \frac{W_{haste}}{W_{crit}} = 1 \space : \space (1 + Haste) * (1 - HIT_{miss}) \space : \space (Crit / Crit_{bonus})
$$

> we are relating to haste now, so we need to divide crit, SP and INT by it's weight


## Adding spell power

To add spell power we need to do the math as in [[Spell and healing power]], formula with the ratings then becomes:

$$
\frac{1}{W_{hit}} \space : \space \frac{1}{W_{haste}} \space : \space \frac{W_{haste}}{W_{crit}} \space : \space \frac{W_{haste}}{W_{SP}} = 1 \space : \space (1 + Haste) * (1 - HIT_{miss}) \space : \space (Crit / Crit_{bonus}) \space :  \space 0.01 \times \left( \frac{Base_{spell}}{C} + SP_{current} \right)
$$


## Adding crit from intellect

Every 80 points of intellect give us 1% spell crit, we can directly relate it to spell crit then: 22.1/80 = 0.276 = effectivness of intellect compared to spell crit rating.

## Final weights

Now we need to divide all the weights by their ratings:

$$
\frac{1}{W_{hit}} \space : \space \frac{1}{W_{haste}} \space : \space \frac{W_{haste}}{W_{crit}} \space : \frac{W_{haste}}{W_{int}} \space : \space\frac{W_{haste}}{W_{SP}} = \frac{1}{12.66} \space : \space (1 + Haste) * (1 - HIT_{miss}) /15.77 \space : \space (Crit / Crit_{bonus}) /22.1 \space : \space (Crit / Crit_{bonus}) /22.1 / 0.276 \space : \space 0.01 \times \left( \frac{Base_{spell}}{C} + SP_{current} \right)
$$

And now to get the weights in correct form, where higher is better, I do inversion and normalize it:

$$
W_{hit} \space : \space W_{haste} \space : \space W_{crit} \space : W_{int} \space : \space W_{SP} = 1 \space : \space \frac{15.77}{(1 + Haste) * (1 - HIT_{miss}) \times 12.66} \space : \space \frac{W_{haste} \times 22.1}{(Crit / Crit_{bonus})} \space : \space  W_{crit} \times 0.276 \space : \space \frac{W_{haste}}{0.01 \times \left( \frac{Base_{spell}}{C} + SP_{current} \right)}
$$




This formula is general for all casting classes, as you can see not being hit capped affects $W_{haste}$ which then affects all the other stats negatively.



## Python

Script for the graph in google colab

[Download the Python Script](caster-stat-weights.py)








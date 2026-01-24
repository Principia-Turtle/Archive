### Authors:

[[Author-Orfeus]]

### Peer review done by:

none

### Related nodes:

[[Hit cap vs haste.md]], [[Caster stat weights.md]]

## Introduction

Spell haste increses cast time of spells, this node is concerned with it's effect on damage.

## Stat conversion

15.77 Spell Haste rating will increase Spell Haste by 1%

## Haste effect on different cast times

The longer the cast time, the higher effect it has in terms of the time saved, 
but no matter how long is the cast, spell haste just gives us an option to fit more of spells into the same time window. 
So it doesn't matter if your cast is instant (global cooldown), or 5 seconds, you will still fit N% more of the casts in the given time window.
>But longer cast times could be beneficial if your latency is high
>
Cast time is calculated after the reduction from possible talents. 

$$
HastePercent
= \frac{Haste Rating}{15.77}
$$

$$
New Cast Time
= \frac{Cast Time}{1+(\frac{HastePercent}{100})}
$$

## Hard cap

Nothing can be casted faster than 1 second, so if you combine haste from items, bloodlust and other effects, you should not go below this treshold.

![media/graph-melee-miss-chance.png](../media/impact-of-haste-rating-on-cast-time.png)

The hard cap for 1.5 s cast / GCD is 50%, this is very much reachable under the effect of bloodlust (30%). For 2s casts = 100%, 2.5s = 150%, etc.


## No diminishing returns

As you can see in the previous graph, the effect of haste on time is not linear, it is slightly curved. That is because 10% from a 2.5 s cast = 0.25 s, and from 1.5 s cast = 0.15. 
This doesn't mean there are diminishing returns on your number of casts, healing, damage or anything, there is no soft cap, because the vertical axis is cast time, not number of casts. There is only the 1s hard cap. The effect on casts performed in a given time window is linear:

![media/graph-melee-miss-chance.png](../media/impact-of-haste-rating-on-cast-time-2.png)

## Haste and fight lenght

In [[Caster stat weights.md]] we have created link between stats and time. Haste will have different effect, depending on the lenght of the encounter, because we might not be able to finish the extra cast our haste gives us. The formula will be a relation between fight lengt, cast time and haste. 

This is the number of casts we would do without haste:

$$
N_{Casts}
= \frac{T_{fight}}{T_{cast}}
$$

And then we simply multiply it by the haste, in the percent form:

$$
N_{Casts}
= \frac{T_{fight}}{T_{cast}} \times H
$$

We always have to round the number down, let n be N rounded down.

Now it is handy to convert it back and get some constant out of it, so we solve for h, which is our "effective" haste:

$$
n
= \frac{T_{fight}}{T_{cast}} \times h
$$

$$
h
= \frac{n}{\frac{T_{fight}}{T_{cast}}}
$$

And to get the constant C:

$$
C = \frac{h}{H}
$$



## Python

You can run this online in google colab:

[Download the Python Script](spell-haste.py)

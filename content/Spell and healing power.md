### Authors:

[[Author-Orfeus]]

### Peer review done by:

none

### Related nodes:

none

## Introduction

Spell and healing power are the only caster stats which are not based on random numbers - they add a flat bonus effect to spells. This complicates things a little, because we always wonder how much of each stat increases our performance by 1%.
>Hence they are not a subject of volatility.

## Formula from observations

Doing it via observation has it's limits, mainly because of RNG. Here I try to do some approximation, if you want algebraic, more correct approach, skip to next section.

The formula for the effect on damage can be described as:

$$
BonusDMG = SP \times C \times M \times N_{casts}
$$

$$
\text{Effect \%} = \frac{BonusDMG}{N_{casts} \times AVG_{observed}} \times 100
$$

Where:

$BonusDMG$ is the bonus in %

$SP$ is spell power

$C$ is spell coefficient

$M$ is Total Damage Multiplier (Product of talents, buffs, and debuffs).

$AVG_{observed}$ is The average damage per cast from your log/graph.



### Example

This screenshot is when I was full BiS mage. 

![media/graph-bernoulli.png](../media/dps-screenshot-spellpower.png)

The formula then becomes:

Using the data (1624 SP, 100 casts, 4185 Avg hit) 

($C$): $1.15$ (Base 1.0 + Emp. Fireball 0.15)Calculate Multipliers 

($M$): Assuming standard Fire build:

$1.15$ (Scorch) $\times$ $1.10$ (Fire Power) $\times$ $1.03$ (Playing w/ Fire) $\times$ $1.04$ (Molten Fury avg) $\approx$ 1.355 (35.5%)

Calculate Damage from SP:

$$1624 \times 1.15 \times 1.355 \approx \mathbf{2,530 \text{ damage per cast}}$$

Result:

$$\frac{2530}{4128} \approx \mathbf{0.61}$$

So we established that roughly 61% of the total damage came from Spell Power.

Total Damage: $4128$

Damage from Spell Power: $4128 \times 0.61 = \mathbf{2,530}$

The Effective Coefficient:

$$
\frac{\text{Damage from SP}}{\text{Total SP}} = \frac{2530}{1624} \approx \mathbf{1.558}
$$

If you want to know how much damage 1% increase is worth now:

Current Damage: 4128

Increase of 1%: $41.28$ damage

Coefficient: 1.61 (from previous step)

SP Needed for 1% increase: 

$$
41.28 / 1.61 \approx \mathbf{26 \text{ SP}}
$$

>Approximation

## Formula from algebra

Earlier we have depended upon $AVG_observed$, now let's replace it with a calculated $AVG_{calc}$

Total damage is the sum of Base Damage and Spell Power, both multiplied by your modifiers (Talents, Crits, Buffs):

$$
AVG_{calc} = (\frac{Base_{spell}}{C} + SP \times C) \times M
$$

To gain 1% DPS, we need to increase our total damage by 1%.
Since Modifiers ($M$) apply to everything, they would cancel out of the relative equation.
Then the amount of spell power needed to add 1% damage simplifies to:

$$
SP_{weight} = 0.01 \times \left( \frac{Base_{spell}}{C} + SP_{current} \right)
$$

Where:

$Base_{spell}$: The average damage listed on the spell tooltip (Rank 13 Fireball $\approx$ 815).

$C$: The spell coefficient (15\% Empowered Fireball).

>It gains effect from spell power, it is not a coefficient we have removed earlier (like improved scorch)

$SP_{current}$: The current Spell Power (1624).

$$
SP_{weight} = 0.01 \times \left( \frac{815}{1.15} + 1624 \right)= 23.3
$$

This is 23.3 points of spell power needed for each 1% damage increase, for a full BiS mage.

Now why the discrepancy? Using real world data brings RNG, even if everything hits, you get partial resists, or wrong damage range volatility, but those resist affect all the stats the same way. Also I didn't include flame cap, trinkets and destruction potions into the equations, it wouldn't even make sense because their effect is very short compared to the whole fight - hence even more volatility. So if I just look at the bigger picture it is reasonable to get slightly lower weight, when considering the other buffs, because of the relation between SP and its weight is inversely proportional.





## Diminishing returns

The more spell power we have, the more our hits strike, this effect is linear.

But most importantly the less percentual effect it has on our casts, as we can see in this graph for our mage example:

![media/spell-power-graph-2.png](../media/spell-power-graph-2.png)

As you can see the amount of SP needed to get 1% more damage grows quite quickly. The percentual effect is much more important to us if we want to relate the stat to the others. Also the blue line doesn't start at the origin, that is because even a naked wizard does some damage. One could come up with some concept of "ghost spell power" which would replace the base damage of spells, but so far I do not see any point of doing it because it would not change anything. Maybe I will find I was wrong.

## Python code

You can run this online in google colab

[Download the Python Script](spell-and-healing-power.py)






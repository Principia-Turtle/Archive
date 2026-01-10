### Authors:

[[Author-Calais]]

### Peer review done by:

none

### Related nodes:

none

## Introduction

Spell and healing power are the only caster stats which are not based on random numbers - they add a flat bonus effect to spells. This complicates things a little, because we always wonder how much of each stat increases our performance by 1%.
>Hence they are not a subject of volatility.

## Formula from observations

Doing it via observation has it's limits, mainly because spellpower has effect on both critical strike rating and haste too. Here I try to do some approximation, if you want algebraic approach, skip to next section.

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

Using the data (1624 SP, 100 casts, 5164 Avg) 

($C$): $1.15$ (Base 1.0 + Emp. Fireball 0.15)Calculate Multipliers 

($M$): Assuming standard Fire build:

$1.15$ (Scorch) $\times$ $1.10$ (Fire Power) $\times$ $1.03$ (Playing w/ Fire) $\times$ $1.04$ (Molten Fury avg) $\approx$ 1.355 (35.5%)

Calculate Damage from SP:

$$1624 \times 1.15 \times 1.355 \approx \mathbf{2,530 \text{ damage per cast}}$$

Result:

$$\frac{2530}{5164} \approx \mathbf{0.49}$$

So we established that roughly 49% of the total damage came from Spell Power.

Total Damage: $5,164$

Damage from Spell Power: $5,164 \times 0.49 = \mathbf{2,530}$

Spell Power: $1,624$

The Effective Coefficient:

$$
\frac{\text{Damage from SP}}{\text{Total SP}} = \frac{2530}{1624} \approx \mathbf{1.558}
$$

If you want to know how much damage 1% increase is worth now:

Current Damage: 51641

Increase of 1%: $51.64$ damage

Coefficient: 1.558 (from previous step)

SP Needed for 1% increase: 

$$
51.64 / 1.558 \approx \mathbf{33 \text{ SP}}
$$

>That is a lot.

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

Now why the discrepancy? Firstly we used an average of all casts, including crits, secondly using real world data brings RNG, even if everything hits you get partial resists, but those resist affect all the stats the same way.





## Diminishing returns

The more spell power we have, the more our hits strike, this effect is linear.

But most importantly the less percentual effect it has on our casts, as we can see in this graph for our mage example:

![media/spell-power-graph-2.png](../media/spell-power-graph-2.png)

The percentual effect is much more important to us if we want to relate the stat to the others.

## Python code

You can run this online in google colab

[Download the Python Script](spell-and-healing-power.py)






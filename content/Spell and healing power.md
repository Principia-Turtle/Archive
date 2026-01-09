### Authors:

[[Author-Calais]]

### Peer review done by:

none

### Related nodes:

none

## Introduction

Spell and healing power are the only caster stats which are not based on random numbers - they add a flat bonus effect to spells. This complicates things a little, because we always wonder how much of each stat increases our performance by 1%.
>Hence they are not a subject of volatility.

## Formula

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



## Example

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

$$\frac{2530}{5164} \approx \mathbf{0.49\%}$$

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

>That is a lot. This makes spell power the worst stat for a late game mage.

## Diminishing returns

The more spell power we have, the more our hits strike, this effect is linear.

But most importantly the less percentual effect it has on our casts, as we can see in this graph:

![media/graph-bernoulli.png](../media/spell-power-diminishing-returns.png)

The percentual effect is much more important to us if we want to relate the stat to the others.

## Python code

You can run this online in google colab

[Download the Python Script](spell-and-healing-power.py)






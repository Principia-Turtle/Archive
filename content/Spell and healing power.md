### Authors:

[[Author-Calais]]

### Peer review done by:

none

### Related nodes:

none

## Introduction

Spell and healing power are the only caster stats which are not based on random numbers - they add a flat bonus effect to spells.
>Hence they are not a subject of volatility.

## Formula

The formula for the effect on damage can be described as:

$$
BonusDMG = SP \times C \times M \times N_{casts}
$$

$$
\text{Effect \%} = \frac{Damage_{SP}}{N_{casts} \times AVG_{observed}} \times 100
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

Hence 49% comes from spell power and it corresponds to 1624 rating, 1/(1-0.49) = 196% damage increase from spell power

1624/1.96 = 8.28 $\approx$ 1% DMG increase.

This makes spell power the most powerful stat for the mage class.




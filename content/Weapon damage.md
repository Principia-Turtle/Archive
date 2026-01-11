### Authors:

[[Author-Orfeus]]

### Peer review done by:

none

### Related nodes:

none

## Introduction

This node is about melee and ranged weapons. 

## Formula

The formula presented by [[allakhazam]](https://wow.allakhazam.com/wiki/The_Math_of_Combat_%28WoW%29) proposes this relation:


<mark>1. A number in the weapon's damage range is selected.
2. One-fourteenth of the character's attack power, multiplied by the weapon's delay, is added to this amount.
3. Other possible bonus effects are also factored in.
4. The damage is reduced by some percentage, based on the target's armor.</mark>

This can be rewritten as:

$$
H = (W_{dmg} + W_{bonus} + AP*W_{speed}/14)*B_{mult}*R_{mult} + B_{add} - R_{sub}
$$

Where:

$$H$$ = Swing weapon damage, $$W_{dmg}$$ = a number selected from weapons damage range, $$W_{bonus}$$ = weapon damage enchantments, $$AP$$ = attack power, $$W_{speed}$$ = weapon speed, $$B_{mult}$$ = damage percent bonuses, $$R_{mult}$$ = damage percent reduction,  $$B_{add}$$ = added bonuses, $$R_{sub}$$ = substracted reduction

For our puropse we are not interested in $$B_{mult}$$, $$R_{mult}$$, $$B_{add}$$, $$R_{sub}$$ and instead of a weapons range $$W_{dmg}$$ we consider the average $$W_{a-dmg}$$  so this leaves us with: 

$$
H = (W_{a-dmg} + W_{bonus} + AP*W_{speed}/14)
$$

## Effect of attack power on weapon damage

First we notice when looking at the formula, is that attack power has biggest effect on slow weapons. Let's consider Thori'dal with $$W_{a-dmg}$$ = 439.5, W_{speed} = 2.70, W_{bonus} we set to 0. Vertical axis is hit, horizontal is AP:

![media/graph-bernoulli.png](../media/thoridal-ap-scaling.png)

The effect of AP on weapon damage is linear.

But note if we would set the weapon speed to 1/2, then the effect from AP would be half of it, but it would strike 2x more often. So it doesn't matter what weapon you carry, you are still getting the same <b>white attack</b> DPS benefit from your attack power.

## Effect of weapon damage on yellow attacks

Weapon damage W_{dmg} is the basis for determining most yellow attacks damage - hence slower weapon will give higher benefit.






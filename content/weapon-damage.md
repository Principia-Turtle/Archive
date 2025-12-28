### Authors:

[[Author-Baldessarini]]

### Peer review done by:

none

## Introduction

This node is about melee and ranged weapons and wands. We will look behind the math of damage from weapons again by both average and stochastic lens.

## Formula

The formula presented by [[allakhazam]](https://wow.allakhazam.com/wiki/The_Math_of_Combat_%28WoW%29) proposes this relation:

$$
H = (W_{dmg} + W_{bonus} + AP*W_{speed}/14)*B_{mult}*R_{mult} + B_{add} - R_{sub}
$$

Where:

$$H$$ = Swing weapon damage, $$W_{dmg}$$ = a number selected from weapons damage range, $$W_{bonus}$$ = weapon damage enchantments, $$AP$$ = attack power, $$W_{speed}$$ = weapon speed, $$B_{mult}$$ = damage percent bonuses, $$R_{mult}$$ = damage percent reduction,  $$B_{add}$$ = added bonuses, $$R_{sub}$$ = substracted reduction


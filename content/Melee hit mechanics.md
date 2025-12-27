### Authors:

Magey

### Peer review done by:

[[Author-Baldessarini]]

## Archive link connections

[[Mechanics of Random Number Based Game.md]], [[Hit cap vs. attack speed.md]]


# Introduction
There are multiple factors deciding how melee attack behaves. Namely it is level difference between character and target, characters hit rating and weapon skill.
This article is a copy of empirical work done by magey et al. [[2019]](https://bookdown.org/marrowwar/marrow_compendium/mechanics.html#ref-magey_atktbl2019)

White attacks can:

-miss, dodge, parry, block, glancing blow, hit, critical strike

Yellow attacks have the same results, except they cannot glance. 

Mob attacked from behind cannot block, nor parry. So on boss fights we can forget theese two with correct positioning.

## Miss

Blizzard has confirmed that players have an 8% chance to hit a lvl 63 mob / boss.
>Note that, due to the inherent hit suppression against level 63 mobs, the hit cap and the P(miss) are different until 305 weapon skill.

Empirical work from magey corroborates a formula originally proposed by Beaza during vanilla (Beaza 2006), which can be summarized as:

If the target is a mob and the difference between its defense rating and the attacker’s weapon skill is 11 or more:

$$
P(Miss) = 5 + ((T(lvl) x 5) - Atk(skill) x 0.2
$$

If the target is a mob and the difference between its defense rating and the attacker’s weapon skill is 10 or less:

$$
P(Miss) = 5 + ((T(lvl) x 5) - Atk(skill) x 0.1
$$

Where  T(lvl) is the target’s level, and Atk(skill) is the attacker’s weapon skill rating. While simple, this formula carries immense significance 
It means that that by having 305 weapon skill, a player only has a 6% chance to miss an enemy mob 3 levels higher, which includes raid bosses.
Conversely, a player with only 300 weapon skill will have an 8% chance to miss.
This is a huge difference, especially in conjunction with the other benefits that weapon skill brings.
It is important to note, however, that this is the behavior exhibited by wielding one weapon.
If dual wielding, the probability of missing an attack is calculated as:

$$
P(DW_{miss}) = P(Miss) x 0.8 + 0.2
$$

As a disclaimer, magey notes that further testing is still required to assert the correctness of this formula.

## Glancing blows

Glancing blows are a type of attack that can only occur when fighting an enemy of equal or higher level, 
and are restricted to white attacks. In accordance with Beaza, magey et al.
have determined the glancing blow probability to be as follows:

$$
P(glancing) = 0.1 + (T(lvl) x 5 - min(Atk(lvl) x 5, Atk(skill)) x 0.02
$$

Where Atk(lvl) is characters level and Atk(skill) is characters active weapon skill

Knowing that, we can compute the probability that our white attacks will glance, and the damage penalty that that glancing blow carries against enemies of different levels:

![media/graph-melee-miss-chance.png](../media/graph-melee-miss-chance.png)

$$
\begin{pmatrix}
Weapon skill &  Miss chance & DW miss chance & Glance penalty \\
300 & 8 & 26.4 & 35 \\
305 & 6 & 24.8 & 15 \\
308 & 5.7 & 24.56 & 3 \\
310 & 5.5 & 24.4 & 1 \\
315 & 5 & 24 & 1
\end{pmatrix}
$$

As we can see, weapon skill not only reduces the glancing blow damage penalty, it also reduces the hit cap and the P(Miss)

Similarly, the impact of weapon skill on the P(miss) and hit cap is clearer when shown graphically:

![media/graph-melee-miss-chance-2.png](../media/graph-melee-miss-chance-2.png)

This is why weapon skill is important: not only does it reduce the glancing blow damage penalty, 
it removes the inherit 1% hit suppresion, and significantly reduces P(miss) until 305. 
This is also why a weapon skill of at least 305 and at most 308 is recommended.

# Continue reading

But what if choose to get more attack speed instead of hit, have more misses, but on the other hand have more hits? Read: [[Hit cap vs. attack speed.md]]


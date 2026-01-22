### Authors

[[Author-Orfeus]]

### Peer review done by:

none

### Related nodes:

[[Mechanics of Random Number Based Game.md]]

## Prior reading

I'd recommend reading [[Mechanics of Random Number Based Game.md]] first, just replace the word "trial" by "crit" in your mind.

22.1 Spell Crit Rating increases critical strike chance by 1%. 

## Connecting Crit to Haste

If your cast does 200% dmg on crit, it is the same like having 200% haste. So on a theoretical 100 cast fight, 1% of each stat is identical increase to 101 casts. 
The main difference is, that some talents can raise your spell crit damage. Then the effect is:

$$
W_{crit}
= \frac{1}{Crit_{bonus}}
$$

Now missing some hit will affect the stat weight in the same way it affects haste, hence:

$$
W_{crit}
= \frac{\frac{1}{Crit_{bonus}}}{1 - Hit_{miss}}
$$

>Where $Crit_{bonus}$ would be 1.4, if talents give us extra 40% and $Hit_{miss}$ is a positive number.
>Note that lower weight, means we need less of the stat rating to increase our performance

Another difference is, that hard cap is at 100% and the more we approach 50% crit, the more volatility we bring into our output. Read [[Mechanics of Random Number Based Game.md]]

Also we need different amount of ratings to reach 1%.

Other than that the stats behave the same

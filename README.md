# xenoCalculator

Declare the element types of your blades on your active team and see the viable blade combos you can perform.


## Setting your team

Edit the `team` set on line 17.

Doubling the element count for one of the characters is a good way to simulate the player characters ability to build combos faster than an NPC.


## Improvments


### Weighting combos based on driver stage requirements.
Ideally I would like to be able to configure the strength of each combo through options.  A combo that requires one driver to complete two stages back to back would be considered less ideal than a combo that relies on all three drives, or a combo that requires a driver to do stages 1 and 3.

I'd also like to rank combos based on if they player blades are involved.
This would could lead to actual scores of the team composition and highlight situations where even though more combos are available they all rely on one driver so they aren't necessairly better.


### Weighting combos based on switching blades or not.
Adding or subtracting from a combos score based on if the drivers need to switch from their initial blade configuration to complete the combo or not.  This is especially important if the play character needs to switch blades between back to back staging since that requires more planning.


### Weighting for chain attacks.
Having a lot of combos available is less ideal if it's difficult to break the resulting orbs during chain attacks


### Configurable weighting
Obviously players will argue over the weights that each of the above listed things is... Some might value chain attacks, others might not think switching blades is a hinderance, or even a benefit... Allowing each difference to be custom weighted for the final score would be nice.


### Ideal team discovery.
Using the custom weighting there should exist a best fit for the provided model.  Trying all combinations of blade elements per driver for a set of weights should result in team compositions that have the highest score.  Automatically discovering these would be fun.


### Driver combo
I don't even want to think about how to incorporate this.


# GUI

A small gui or web portal would make this more approachable.



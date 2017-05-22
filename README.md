# WildEncounter
This is a series of scripts to provide command line utilities for the Pokemon Tabletop Adventure game (PTA)

This iteration includes all pokemon up to Omega Ruby/Saphire (NO WILD MEGALUTIONS) Sun/Moon mons exist now in PTA but I have not yet updated my database. 

This was created and owned by Anders Nelson aka Phixia/Pecanos

This script is licensed under the Apache 2.0 License http://www.apache.org/licenses/

The sqlite databases I am using are forked from https://github.com/PanoramicPanda/PTU-Basic-Database special thanks to PanoramicPanda and from https://github.com/jmwendt/PTU (despite the PTU name it is a PTA DB : P ) Thanks much jmwendt

Some of the more complex logic and flow control(making things purty) was contributed by Andrew Howard aka StafDehat I will try to notate where in the script he helped most.

Note: This is my first real attempt at working on a big/involved python project so please feel free to offer constructive criticism and also bear with me while I figure out the wonderful world of python and object oriented programming.

To run the CLI tools go to a command prompt, cd into the WildEncounter directory, and execute the various python scripts as follows;

WARNING: wildencounter.py is old and will likely be removed once I am confident in my new object oriented script instead run wildencounter.object.py or pokegen.py

To run wildencounter.object.py: 

# python wildencounter.object.py BiomeName Level
Example: To generate a level 14 wild pokemon that lives in a cave;
# python wildencounter.object.py cave 14 

For the times when you specifically know the mon you want but want to random gen the stats and pull
 the available moveset. Use the pokegen.py

To run the pokegen.py

# python pokegen.py PokemonName Level (Case sensitive)

Example: To generate a level 15 Geodude

# python pokegen.py "Geodude" 15

To run abilityexplainer.py: 

# python abilityexplainer.py "Ability Name" (Case sensitive)

Example: To explain the ability "Pickup"

# python abilityexplainer.py "Pickup"

To run the pickup.py script to determine what you pickup (or possibly for random loot):

# python pickup.py
 
To run the moveexplainer.py:

# python moveexplainer.py "Move Name" (Case sensitive)

Example: To explain the move "Tackle"

# python moveexplainer.py "Tackle"

If you have any questions or suggestions please open an issue or pull request on github.


# WildEncounter
Generates a wild pokemon encounter, based on biome (Made specifically for pokemon table top game)

This is a series of scripts to provide command line utilities for the Pokemon Tabletop Adventure game (PTA)

This iteration includes all pokemon up to Omega Ruby/Saphire (NO WILD MEGALUTIONS)

This was created and owned by Anders Nelson aka Phixia/Pecanos

This script is licensed under the Apache 2.0 License http://www.apache.org/licenses/

The sqlite databases I am using are forked from https://github.com/PanoramicPanda/PTU-Basic-Database special thanks to PanoramicPanda and from https://github.com/jmwendt/PTU (despite the PTU name it is a PTA DB : P ) Thanks much jmwendt

Some of the more complex logic and flow control(making things purty) was contributed by Andrew Howard aka StafDehat I will try to notate where in the script he helped most.

Note: This is my first real attempt at working on a big/involved python project so please feel free to offer constructive criticism and also bear with me while I figure out the wonderful world of python and object oriented programming.

To run the CLI tools go to a command prompt, and execute the various python scripts as follows;

wildencounter.py is old and will likely be removed once I am confident in my new object oriented script

wildencounter.object.py: #python wildencounter.object.py BiomeName Level

abilityexplainer.py: #python abilityexplainer.py "Ability Name" (Case sensitive)

moveexplainer.py: #python moveexplainer.py "Move Name" (Case sensitive)

pokegen.py: #python pokegen.py PokemonName Level (Case sensitive)

You run all of these from within the Wildencounter dir

If you have any questions or suggestions please open an issue or pull request on github.


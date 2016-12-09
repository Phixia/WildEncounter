# This is a script to gen wild pokemon encounters for the Pokemon Tabletop Adventure game (PTA)
# This iteration includes all pokemon up to Omega Ruby/Saphire (NO WILD MEGALUTIONS)
# This was created and owned by Anders Nelson aka Phixia/Pecanos
# This script is licensed under the Apache 2.0 License http://www.apache.org/licenses/

# The sqlite database I am using is forked from https://github.com/PanoramicPanda/PTU-Basic-Database special thanks to PanoramicPanda
# I now have a second DB that is PTA specific from https://github.com/jmwendt/PTU (despite the PTU name it is a PTA DB : P ) Thanks much jmwendt
# Some of the more complex logic was contributed by Andrew Howard aka StafDehat I will try to notate where in the script he helped most. 

# Note: This is my first real attempt at working on a big/involved python project so please feel free to offer constructive criticism and also bear with me while I figure out the wonderful world of python and object oriented programming.

# First we are going to import some modules and classes we will need later.
import sys
sys.path.insert(0, "modules/")

from pokemon import Pokemon
from biome import Biome

# now we set a few variables


biome = sys.argv[1]
level = sys.argv[2]

# finally we call our different imported functions/classes
biome = Biome(str(biome))
pokemon = Pokemon(biome.encounter(),level)

print pokemon

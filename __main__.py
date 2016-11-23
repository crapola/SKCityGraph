import sk
import graph

sk.check_path()

buildings=sk.load_improvements()

altar=[x for x in buildings
if (x.race=='Race_Type_Altarians' or x.race==None) and x.required_ability==None]

dorf=[x for x in buildings
if (x.race=='Race_Type_Dwarves' or x.race==None) and x.required_ability==None]

dead=[x for x in buildings
if (x.race=='Race_Type_Undead' or x.race==None) and x.required_ability==None]

buildings_filtered=dead

for x in buildings_filtered:
	x.print()

graph.build_graph(buildings_filtered)
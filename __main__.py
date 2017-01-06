import sk
import graph

sk.check_path()

buildings=sk.load_improvements()

altar=[x for x in buildings
if (x.race=='Race_Type_Altarians' or x.race==None) and x.required_ability==None]
graph.build_graph(altar,"Altar")

dorf=[x for x in buildings
if (x.race=='Race_Type_Dwarves' or x.race==None) and x.required_ability==None]
graph.build_graph(dorf,"Dwarves")

dead=[x for x in buildings
if (x.race=='Race_Type_Undead' or x.race==None) and x.required_ability==None]
graph.build_graph(dead,"Undead")
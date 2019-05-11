# local
from config import OUTPUT_FOLDER
import graph
import sk

sk.check_path()

buildings=sk.load_improvements()

altar=[x for x in buildings
if (x.race=='Race_Type_Altarians' or x.race==None) and x.required_ability==None]
graph.build_graph(altar,OUTPUT_FOLDER+"\\Altar")

dorf=[x for x in buildings
if (x.race=='Race_Type_Dwarves' or x.race==None) and x.required_ability==None]
graph.build_graph(dorf,OUTPUT_FOLDER+"\\Dwarves")

dead=[x for x in buildings
if (x.race=='Race_Type_Undead' or x.race==None) and x.required_ability==None]
graph.build_graph(dead,OUTPUT_FOLDER+"\\Undead")
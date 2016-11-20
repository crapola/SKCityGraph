import sk
import graph

sk.check_path()

buildings=sk.load_improvements()

altar=[x for x in buildings
if (x.race=='Race_Type_Altarians' or x.race==None) and x.required_ability==None]

sk.fix_icons(altar)

#for a in altar:
#	print(a.__dict__,'\n')

altar_nodes=[
graph.citygraph_node(x.internal_name,x.icon,x.display_name,x.description,x.cost)
for x in altar]

edges=graph.build_edges(altar)

graph.render(altar_nodes,edges)
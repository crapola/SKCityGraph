import sk
import graphviz
import graph

sk.check_path()

buildings=sk.load_improvements()

altar=(x for x in buildings if x.race=='Race_Type_Altarians')

# Fix icons here

altar_nodes=[
graph.citygraph_node(x.internal_name,'test.png',x.display_name,x.description,x.cost)
for x in altar]

nodes=altar_nodes

edges=graph.build_edges(altar)

edges=(('A','B'),('B','Z'))

#---

g=graph.citygraph()

for x in nodes:
	g.node(x[0],**x[1])

g.edges(edges)

try:
	f=g.render()
except RuntimeError as r:
	print("Rendering failed:",r)
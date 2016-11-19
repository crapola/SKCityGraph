import graphviz

def citygraph_node(internal_name,icon,display_name,description,cost):
	"""
	Create a node stylized for our graph.

	Parameters
	----------
	icon,name,description,cost : str
		icon must be full path to picture.
		description may have <BR/> newlines.

	Returns
	-------
	(str,dict)
		The node identified by internal_name and its params.
	"""
	html="""<
	<TABLE border="0" cellpadding="0" cellspacing="0" color="#880000">
	<TR>
		<TD width="64" height="64" fixedsize="true" >
			<IMG SRC="{0}"/>
		</TD>
		<TD>
			<TABLE border="0" cellborder="1" cellspacing="0" cellpadding="2">
				<TR><TD align="left">{1}</TD></TR>
				<TR><TD align="left" balign="left" valign="top"><FONT color="#AAAAAA" point-size="10">{2}</FONT></TD></TR>
				<TR><TD align="left"><FONT color="#AA8800">{3}</FONT></TD></TR>
			</TABLE>
		</TD>
	</TR>
	</TABLE>
	>"""
	label=html.format(icon,display_name,description,str(cost))
	return (internal_name,{'label':label,'margin':'0.04'})

def citygraph():
	"""
	Constructs a Digraph with a predefined style.

	Returns
	-------
	graphviz.Digraph
		The graph.
	"""

	graph_attr={'rankdir':'LR','bgcolor':'#444444'}
	node_attr={'style':'filled','fillcolor':'#220000',
		'color':'#FFCC00','shape':'rectangle',
		'fontname':'Verdana','fontsize':'12.0','fontcolor':'#FFFFFF'}
	edge_attr={'color':'#FFCC00'}
	return graphviz.Digraph('City Graph','A visualization...','tree',
		None,'svg',None,None,graph_attr,node_attr,edge_attr)

def build_edges(improvements):
	"""
	Create edges from Improvement list.

	Parameters
	----------
	improvements : list of Improvement

	Returns
	-------
	list of pair
		Edges.
	"""
	edges=[]
	for x in improvements:
		p=x.required_improvement
		if p:
			edges.append( (p,x.internal_name) )
	return edges
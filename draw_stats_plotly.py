import sys,os
import pandas as pd
import plotly

df = pd.io.json.read_json(sys.argv[1],orient='index')
df = df.sort()


# plot.ly
graph_data = []
py = plotly.plotly(os.environ['PLOTLY_USER'], os.environ['PLOTLY_KEY'])
d = df.to_dict()

for funct in d:
	results = d[funct]	
	graph_data.append({
		'name': funct,
		'x': [nrows for nrows in results.keys()],
		'y': [value for value in results.values()],

		'type':'scatter',
		'mode':'markers'
		})

layout = {
    'xaxis': {'title': 'Num rows','type':'log'},
    'yaxis': {'title': 'Seconds','type':'log'},
    'title': 'Access time to python dict using different hash functions'
}

py.plot(graph_data, layout=layout,
         filename='Python Hashes', fileopt='new',
         world_readable=True, width=1000, height=500)



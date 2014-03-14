import sys,os
import pandas as pd
import plotly

output = 'results.csv'
df = pd.io.json.read_json(sys.argv[1],orient='index')
df = df.sort()
df.to_csv(output)


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



# for row in cr:
#     print row
#     graph_data.append(
#             {
#                 'name': continent, # the "name" of this series is the Continent
#                 'x': [row[4] for row in data if row[2] == continent],
#                 'y': [row[3] for row in data if row[2] == continent],
#                 'text': [row[0] for row in data if row[2] == continent],

#                 'type': 'scatter',
#                 'mode': 'markers',

#                 'marker': { # specify the style of the individual scatter points
#                     'size': [math.sqrt(row[1])/1.e3 for row in data if row[2] == continent],
#                     'sizemode': 'area',
#                     'sizeref': 0.05,
#                     'opacity': 0.55
#                     }
#                 })



#print df


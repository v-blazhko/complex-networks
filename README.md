## Identifying the complex network of locations in Finland
Data scraping
- 500 locations total needed
- Data is collected using Flickr API - https://www.flickr.com/services/api/
- Total number of images with location data collected ~77k
- Two locations are connected based on the subset of users visited _both_ locations
- Location centroids are determined using k-means algorithm

### Network analysis
**Community Discovery**
Analyze and compare the modular structure of the crawled network sample. The results
of at least three different algorithms should be presented.
• K-clique (available in NetworkX)
• DEMON (code available at https://github.com/GiulioRossetti/demon)
• Louvain (code available at http://perso.crans.org/aynaud/communities/)
• Infomap (https://www.mapequation.org/)

**Speading analysis**
Simulate a spreading process (SIS and/or SIR) both on the crawled data and on random
graphs (i.e., ER and BA).

**Random networks**
Analyze the crawled social/complex network sample and compare the obtained network statistics
with 2 random graph models having the same number of nodes and edges, i.e. Erdős-Rényi (ER)
random network model and the Barabási-Albert (BA) preferential attachment network model

**Statistical analysis**
Determine the following:
- What the most popular locations in Finalnd?
- What is the busiest route?
- What are the most common picture names?

### Dirs:
- **/collecting_dataset**: data scraping and dataset preprocessing
- **/clustering: clustering** the raw data and processing
- **/datset**:raw and finalized data in CSV format
- **/plotting**: examples of plotting spatial data on a map (geopandas, basemap and plain networkx)
- **/project_task**s: network analysis mentioned above
- **_main_graph.ipyinb_**: a quick glance of the final graph and main network parameters

import networkx as nx

def create_maritime_graph(gdf, precision=2):
    G = nx.DiGraph()
    
    for _, row in gdf.iterrows():
        coords = list(row.geometry.coords)
        if len(coords) < 2: continue
        
        # Arredondamento para agrupar em 'Hubs'
        u = (round(coords[0][0], precision), round(coords[0][1], precision))
        v = (round(coords[-1][0], precision), round(coords[-1][1], precision))
        
        if u == v: continue
        
        if G.has_edge(u, v):
            G[u][v]['weight'] += 1
        else:
            G.add_edge(u, v, weight=1, vessel_type=row['VesselType'])
            
    return G

def save_graphml(G, output_path):
    # Converte IDs de tupla para string (compatibilidade Gephi)
    mapping = {node: f"ID_{node[0]}_{node[1]}" for node in G.nodes()}
    G_export = nx.relabel_nodes(G, mapping)
    
    # Adiciona X e Y como atributos de visualização
    for node, data in G_export.nodes(data=True):
        # Recupera as coordenadas do ID original
        _, lon, lat = node.split('_')
        data['x'] = float(lon)
        data['y'] = float(lat)
        
    nx.write_graphml(G_export, output_path)
    print(f"Arquivo salvo em: {output_path}")
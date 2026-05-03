import geopandas as gpd

def load_tracks(file_path, vessel_types=None):
    """
    Carrega as trilhas do Geodatabase/Shapefile filtrando por tipo de navio.
    """
    print(f"Carregando dados de: {file_path}...")
    # O motor pyogrio é fundamental para a velocidade no Kaggle
    gdf = gpd.read_file(file_path, engine='pyogrio')
    
    if vessel_types:
        gdf = gdf[gdf['VesselType'].isin(vessel_types)]
    
    print(f"Sucesso! {len(gdf)} registros carregados.")
    return gdf
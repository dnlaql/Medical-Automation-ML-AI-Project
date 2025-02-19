# geo_location_patient.py

import geopandas as gpd
from shapely.geometry import Point
import pydeck as pdk

def create_geo_dataframe(df):
    """Convert DataFrame to GeoDataFrame using latitude & longitude."""
    if 'Latitude' in df.columns and 'Longitude' in df.columns:
        geometry = [Point(lon, lat) for lon, lat in zip(df['Longitude'], df['Latitude'])]
        geo_df = gpd.GeoDataFrame(df, geometry=geometry)
        return geo_df
    return df

def create_map(geo_df):
    """Create a PyDeck map visualization."""
    if 'geometry' in geo_df.columns:
        view_state = pdk.ViewState(
            latitude=geo_df['Latitude'].mean(),
            longitude=geo_df['Longitude'].mean(),
            zoom=10,
            pitch=50
        )
        
        layer = pdk.Layer(
            'ScatterplotLayer',
            geo_df,
            get_position='[Longitude, Latitude]',
            get_radius=500,
            get_color=[0, 128, 255],
            pickable=True
        )
        
        return pdk.Deck(layers=[layer], initial_view_state=view_state)
    return None

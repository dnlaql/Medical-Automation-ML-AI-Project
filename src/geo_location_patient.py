import geopandas as gpd
from shapely.geometry import Point
import pydeck as pdk

def create_geo_dataframe(df):
    """
    Function to convert a DataFrame into a GeoDataFrame using latitude and longitude.
    """
    if 'Latitude' in df.columns and 'Longitude' in df.columns:
        geometry = [Point(lon, lat) for lon, lat in zip(df['Longitude'], df['Latitude'])]
        geo_df = gpd.GeoDataFrame(df, geometry=geometry)
        return geo_df
    return df

def create_map(geo_df):
    """
    Function to create a PyDeck map visualization from a GeoDataFrame.
    """
    if 'geometry' in geo_df.columns:
        view_state = pdk.ViewState(
            latitude=geo_df['Latitude'].mean(),
            longitude=geo_df['Longitude'].mean(),
            zoom=11,
            pitch=50
        )

        # Define the layer to show the points on the map
        layer = pdk.Layer(
            'ScatterplotLayer',
            geo_df,
            get_position='[Longitude, Latitude]',
            get_radius=1000,
            get_color=[255, 0, 0],
            pickable=True
        )

        # Create the deck map
        return pdk.Deck(layers=[layer], initial_view_state=view_state)
    
    return None

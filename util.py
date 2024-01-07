import geopandas as gpd
import pandas as pd
from shapely import wkt


def read_neighborhoods(path: str):
    df = pd.read_csv(path)
    df["geometry"] = df["the_geom"].apply(wkt.loads)
    gdf = gpd.GeoDataFrame(df.drop(["the_geom"], axis=1), crs="WGS84")
    gdf = gdf.rename({"neighborho": "neighborhood"}, axis=1)
    return gdf[["neighborhood", "geometry"]]
import pandas as pd
import ssl
import urllib.request
ssl._create_default_https_context = ssl._create_unverified_context
def map_df():
    dataset_url = "https://raw.githubusercontent.com/saishruthin/bus_fleet_details/main/lat_long.csv"
    df_map = pd.read_csv(dataset_url)
    return df_map
def dataset():
    dataset_url = "https://raw.githubusercontent.com/saishruthin/bus_fleet_details/main/Road%20Transport.csv"
    df_data = pd.read_csv(dataset_url)
    return df_data
def final_data():
    df_map = map_df()
    df_data = dataset()
    result = pd.merge(df_map, df_data, on = 'Districts', how = 'inner')
    return result


import sys
import pickle
import pandas as pd
import numpy as np

with open('model.bin', 'rb') as f_in:
    dv,model = pickle.load(f_in)


categorical = ['PULocationID', 'DOLocationID']

def read_data(filename):
    df = pd.read_parquet(filename)
    
    df['duration'] = df.tpep_dropoff_datetime - df.tpep_pickup_datetime
    df['duration'] = df.duration.dt.total_seconds() / 60

    df = df[(df.duration >= 1) & (df.duration <= 60)].copy()

    df[categorical] = df[categorical].fillna(-1).astype('int').astype('str')
    
    return df

def get_path():
    year = int(sys.argv[1])
    month = int(sys.argv[2])
    file_path = f'https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_{year:4d}-{month:2d}.parquet'
    return file_path



def predict(file_path):
    df = read_data(file_path)
    dicts = df[categorical].to_dict(orient='records')
    X_val = dv.transform(dicts)
    y_pred = model.predict(X_val)
    print(np.mean(y_pred))

def run():
    file_path = get_path()
    predict(file_path)

if __name__ =="__main__":
    run()
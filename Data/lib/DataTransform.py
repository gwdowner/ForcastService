import pandas as pd
import datetime as dt

class DataTransform():
    @staticmethod
    def normalise(x, stats):
        return (x - stats['mean']) / (stats['std'])

    @staticmethod
    def get_unix(x):
        return dt.datetime.strptime(x, "%Y-%m-%dT%H:%M:%S.%fZ").timestamp()

    @staticmethod
    def no_days_ago(x):
        return (dt.datetime.now() - dt.datetime.strptime(x, "%Y-%m-%dT%H:%M:%S.%fZ")).days

    @staticmethod
    def get_hour(x):
        hour = dt.datetime.strptime(x, "%Y-%m-%dT%H:%M:%S.%fZ").hour
        return hour

    @staticmethod
    def get_month(x):
        month = dt.datetime.strptime(x, "%Y-%m-%dT%H:%M:%S.%fZ").month
        return month

    @staticmethod
    def get_region(x):
        x['region'] = x['region']['codes']['pv_live']

        return x

    @staticmethod
    def transform(data):
        data = list(map(DataTransform.get_region, data))

        dataset = pd.json_normalize(data)

        dataset['hour_of_day'] = dataset['time'].map(DataTransform.get_hour)
        dataset['month_of_year'] = dataset['time'].map(DataTransform.get_month)
        dataset['time'] = dataset['time'].map(DataTransform.get_unix)
        
        return dataset

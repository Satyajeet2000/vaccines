import pandas as pd
import gzip
# df = pd.read_csv('/data/COVID-19_Vaccinations_in_the_United_States_County.csv.gz',
#                  index_col='Date')
# print(df)
# print(type(df.index_col))
# print(df.to_datetime)
start_date='5/1/2021'
end_date='11/30/2021'

def get_data_from_startdate_to_enddate(start_date, end_date):
    df = pd.read_csv('data/COVID-19_Vaccinations_in_the_United_States_County.csv.gz', compression='gzip',
                     header=0, index_col='Date')
    print(type(df.iloc[1]))
    df['Date'] = pd.to_datetime(df.Date)
    df.Date
    start_date = pd.to_datetime('5/1/2021')
    end_date = pd.to_datetime('11/30/2021')
    # print(start_date)
    # print(end_date)
    df = df.loc[df.Date >= start_date][df.Date <= end_date]
    # df=df.loc[df.Date<=end_date]
    df.to_csv('my_new_file.csv', index=False)


get_data_from_startdate_to_enddate(start_date,end_date)

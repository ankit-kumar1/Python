import pandas as pd
import pandas_redshift as pr

#connect to redshift
###this code calculates number of trips for each route and process the file one at a time and also most used routes. citibike data is public
pr.connect_to_redshift(dbname = 'production',
                        host ='localhost',
                        port ='5439',
                        user ='ankitkumar',
                        password ='password')

# Connect to S3
pr.connect_to_s3(aws_access_key_id = 'sadadasfaftew',
                aws_secret_access_key = 'ewwet4tsdvsrvrvrervwef',
                bucket = 'data-science',
                subdirectory = 'shwangdir'
                )

#upload a copy to S3 and redshift

#for i in range(5):
    #url = 'https://s3.amazonaws.com/tripdata/20180{}-citibike-tripdata.csv.zip'.format(i+1)
df = pd.read_csv('/Users/ankitkumar/Downloads/201801-citibike-tripdata.csv')
print(df)
pr.pandas_to_redshift(data_frame = df,
                      redshift_table_name = 'analytics.trip_fact')

dfroutes = (df.groupby(['\"start station id\"', '\"end station id\"']).size() \
  .sort_values(ascending=False) \
  .reset_index(name='count'))

dfroutes.columns = ['start_station_id','end_station_id','count']
#print(type(dfroutes))

pr.pandas_to_redshift(data_frame = dfroutes,
                      redshift_table_name = 'analytics.most_used_routes', append=True)



dataframecount=pr.redshift_to_pandas("select * from analytics.most_used_routes")

newdataframecount=pd.DataFrame(columns=('start_station_id', 'end_station_id', 'num_trips'))
print(dataframecount)

for index, row in df.iterrows():
    for routeindex, routerow in dataframecount.iterrows():
        if int(row['\"start station id\"']) == int(routerow['start_station_id']) and int(row['\"end station id\"']) == int(routerow['end_station_id']):
            routerow['num_trips'] += 1
            break

        newdataframecount.append({'start_station_id': row['\"start station id\"']},
                                 {'end_station_id': row['\"end station id\"']}, {'num_trips': 1})



pr.pandas_to_redshift(data_frame = dataframecount,
                      redshift_table_name = 'analytics.most_used_routes')

pr.pandas_to_redshift(data_frame = newdataframecount,
                      redshift_table_name = 'analytics.most_used_routes',append=True)

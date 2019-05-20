import psycopg2

##### unload the data to S3. can be used to backup the entire schema. table names can be retrieved using a query or entered manually
table_names = ['table1','table2']
redshift_conn = psycopg2.connect(user='admin',
                                 password='password',
                                 host='localhost',
                                 port=5439,
                                 database='production')
cursor = redshift_conn.cursor()

for i, name in enumerate(table_names):
    print(f'Working on table {i+1}/{len(table_names)}: {name}')
    unload_columns = f"""\
        unload ('select * from analytics."{name}"')\
        to 's3://data-landing/analytics/{name}.csv' \
        credentials 'aws_access_key_id=asdaafterrerv;aws_secret_access_key=dasdaafdssg3r3sdggsdgsgsg'\
        parallel off\
        ALLOWOVERWRITE;
        """
    try:
        cursor.execute(unload_columns)
        redshift_conn.commit()
        print(f'{name} proccessed')
    except  Exception as e:
        print(e)
        print(f'{name} has not been proccessed')

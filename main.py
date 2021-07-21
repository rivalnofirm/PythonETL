# Import library
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.sql.sqltypes import Date, Float, Integer, Text, DateTime



# Import your dataset and handle with pandas
dataset = pd.read_csv('import your file format csv') #example handle data with csv format
dataset = pd.read_excel('import your file format xlsx') #example handle data with excel format


'''
the next step,
checking the data and data types on the dataset, and determining which data will be loaded into the target
'''

'''
After determining the data to be loaded into the target, we start the step by making a connection in the database.
in this step, I made a python connection with the database using the help of SqlAlchemy
'''

# Example
DATABASE_USER 		= 'root'        # Input your database username
DATABASE_PASSWORD 	= ''            # Input your database password
DATABASE_HOST_IP 	= '127.0.0.1'   # Input your database host
DATABASE_PORT		= '3306'        # Input your database port
DATABASE_NAME	    = 'django'      # Input your database name

'''
To establish a connection, we also must not forget the connector driver for python with the database used
'''

# example
engine = create_engine('postgresql+psycopg2://'+DATABASE_USER+':'+DATABASE_PASSWORD+'@'+DATABASE_HOST_IP+':'+DATABASE_PORT+'/'+DATABASE_NAME) # connection to postgresql
engine = create_engine('mysql+pymysql://'+DATABASE_USER+':'+DATABASE_PASSWORD+'@'+DATABASE_HOST_IP+':'+DATABASE_PORT+'/'+DATABASE_NAME) # connection to mysql

'''
specify the table that will be the target data container.
If you don't have a table, you can skip this step langkah
'''
# Example
table_name = 'input your table name'


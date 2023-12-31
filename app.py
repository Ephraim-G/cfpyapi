import mysql.connector
import os
from flask import Flask, jsonify
from cfenv import AppEnv

app = Flask(__name__)
app_env = AppEnv()

port = int(os.getenv('PORT', 8080))
    
aws_rds = app_env.get_service(name='lightening-db')
    
connection = mysql.connector.connect(
    host=aws_rds.credentials.get('host'),
    user=aws_rds.credentials['username'],
    passwd=aws_rds.credentials.get('password'),
    database=aws_rds.credentials.get('name'),
    port=aws_rds.credentials.get('port'),
)


# Get mysql creds from cloud.gov/import cloud.gov env vars change structure

#mysql_service = app_env.get_service(name='lightening-db')
#mysql_credentials = mysql_service.credentials

#host = mysql_credentials['host']
#username = mysql_credentials['username']
#password = mysql_credentials['password']
#name = mysql_credentials['name']

#connection = mysql.connector.connect(
    #host=host,
    #user=username,
    #password=password,
    #database=name
#)

#mysql_credentials = {
    #'host': os.environ['host'],
    #'port': os.environ['port'],
    #'user': os.environ['username'],
    #'password': os.environ['password'],
    #'database': os.environ['db_name'],
#}

# connect to DB
#connection = mysql.connector.connect(**mysql_credentials)

#env.name = 'cfpyapi'
#env.port = 3306

#aws_rds = env.get_service(label='aws-rds')
#aws_rds.credentials = {'uri':'uri', 'password':'password'}
#aws_rds.get_url(host='host', password='password', port='port', username='username') 

# DB operations/ insert app path from cloud.gov
@app.route('/cfpyapi.app.cloud.gov', methods=['GET'])
def get_gif():
    connection.autocommit = True
    cursor = connection.cursor()
    
    # Execute SELECT query to retrieve GIF URL from cloud.gov
    query = 'SELECT gif_data FROM pages_content'
    cursor.execute(query)
    
    # Fetch result
    result = cursor.fetchone()
    
    # Close cursor
    cursor.close()
    connection.close()
    
    if result:
        gif_url = result[0]
        return jsonify({'gif_url': gif_url})
    else:
        return jsonify({'message': 'GIF not found'})
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)


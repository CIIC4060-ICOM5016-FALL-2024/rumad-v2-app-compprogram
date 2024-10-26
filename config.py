import psycopg2
db_params = {
    'dbname': 'DBProject',
    'user': 'tito',
    'password': 'tito123',
    'host': 'localhost', 
    'port': '5432'
}

connection = psycopg2.connect(**db_params)



# db_params = { 
#     'dbname': 'DBProject',
#     'user': 'tito',
#     'password': 'tito123',
#     'host': 'localhost',  # or '127.0.0.1'
#     'port': '5432'
# }
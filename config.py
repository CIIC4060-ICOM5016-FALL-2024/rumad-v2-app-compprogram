import psycopg2
db_params = {
    'dbname': 'dbtest',
    'user': 'dbuser',
    'password': 'dbtest',
    'host': 'localhost', 
    'port': '9090'
}
#Heroku APP---------------------------
# db_params = {
#     'dbname': 'da3hnfjaj3h53v',
#     'user': 'u8bi5t3hi9ltf3',
#     'password': 'p0a34918e0785aa9f3b46e8947c13ba5e273097d950714a57cfecb18c273d4a52',
#     'host': 'cf980tnnkgv1bp.cluster-czrs8kj4isg7.us-east-1.rds.amazonaws.com', 
#     'port': '5432'
# }


#Heroku DATABASE---------------------------
# db_params = {
#     'dbname': 'dcm05lpjv8pjes',
#     'user': 'uemem33ha8a7p1',
#     'password': 'p8256ddcde369b02ab7709e1043d240da46c6e4607223a04cf2f9d9f9eb964729',
#     'host': 'c3cj4hehegopde.cluster-czrs8kj4isg7.us-east-1.rds.amazonaws.com', 
#     'port': '5432'
# }

# Host: c3cj4hehegopde.cluster-czrs8kj4isg7.us-east-1.rds.amazonaws.com
# Database: dcm05lpjv8pjes
# User: uemem33ha8a7p1
# Port: 5432
# Password: p8256ddcde369b02ab7709e1043d240da46c6e4607223a04cf2f9d9f9eb964729
# URI: postgres://uemem33ha8a7p1:p8256ddcde369b02ab7709e1043d240da46c6e4607223a04cf2f9d9f9eb964729@c3cj4hehegopde.cluster-czrs8kj4isg7.us-east-1.rds.amazonaws.com:5432/dcm05lpjv8pjes
# Heroku CLI: heroku pg:psql postgresql-infinite-73642 --app compprogram-db
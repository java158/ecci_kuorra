import web

db_host = 'ui0tj7jn8pyv9lp6.cbetxkdyhwsb.us-east-1.rds.amazonaws.com'
db_name = 'kz2c7871t2ihslku' # Database
db_user = 'wd2idceg8li0o2vu' # Username
db_pw = 'bg6ntrvbmg8wg78r' # Password

db = web.database(
    dbn='mysql',
    host=db_host,
    db=db_name,
    user=db_user,
    pw=db_pw
    )
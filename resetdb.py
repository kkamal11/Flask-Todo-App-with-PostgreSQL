from application.database import db, db_con_string


# @app.cli.command('resetdb')
def resetdb_command():
    """Destroys and creates the database + tables."""
    DB_URL = "postgresql://{user}:{password}@{host}:{port}/{db_name}".format(
        user=db_con_string['user'], 
        password=db_con_string['password'], 
        host=db_con_string['host'], 
        port=db_con_string['port'],
        db_name=db_con_string['db_name']
    )
    print("Connecting to db > ", DB_URL)
    from sqlalchemy_utils import database_exists, create_database, drop_database
    try:
        if database_exists(DB_URL):
            print('Deleting the existing database...')
            drop_database(DB_URL)
        if not database_exists(DB_URL):
            print('Creating a new database...')
            create_database(DB_URL)
        print('-----------CREATING TABLES-----------')
        db.create_all()
        print('==============All Done==============')
        return True
    except Exception as e:
        print(e)
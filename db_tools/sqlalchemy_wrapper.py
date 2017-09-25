# coding=utf-8


from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.orm import sessionmaker

def config_mysql(host, port, db, user, passwd, table_name):

    config_str = 'mysql+mysqldb://{user}@{host}:{port}/{db}'.format(
        **{'user':user, 'pwd': passwd, 'host':host, 'port':port, 'db': db}
    )

    db_engine = create_engine(config_str, encoding='utf8')

    SessionWrapper = sessionmaker(bind=db_engine)
    MetaDataWrapper = MetaData(bind=db_engine)


    _table = Table(table_name, MetaDataWrapper, autoload=True)

    return db_engine, SessionWrapper(), _table



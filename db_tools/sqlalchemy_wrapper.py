# coding=utf-8

from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.orm import sessionmaker


def get_wrapper(host, port, db, user, table_name, passwd=None):


    if passwd is not None:
        config_str = 'mysql+mysqldb://{user}:{passwd}@{host}:{port}/{db}'.format(
            **{'user': user, 'pwd': passwd, 'host': host, 'port': port, 'db': db}
        )
    else:
        config_str = 'mysql+mysqldb://{user}@{host}:{port}/{db}'.format(
            **{'user':user, 'pwd': passwd, 'host':host, 'port':port, 'db': db}
        )

    db_engine = create_engine(config_str, encoding='utf8')

    _table = Table(table_name, MetaData(bind=db_engine), autoload=True)

    return db_engine, sessionmaker(bind=db_engine)(), _table



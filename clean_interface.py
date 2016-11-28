#!/bin/python
from config.local_config import SERVER_HOST, PORT, USER, DB_CALL_DETAIL_DB, TABLE_CALL_DETAIL_STATUS, TABLE_DETAIL_INFORMATION, TABLE_USER_BASE
from db_tools.clean_records import clean_db_and_clean_data


def clean_call_records(mobile):

    clean_db_and_clean_data(host=SERVER_HOST, port=PORT, user=USER, db=DB_CALL_DETAIL_DB,table=TABLE_USER_BASE,
                             col='mobile', value=mobile)
    clean_db_and_clean_data(host=SERVER_HOST, port=PORT, user=USER, db=DB_CALL_DETAIL_DB,
                             table=TABLE_CALL_DETAIL_STATUS,col='mobile', value=mobile)
    index = str(int(mobile) % 128)
    clean_db_and_clean_data(host=SERVER_HOST, port=PORT, user=USER, db=DB_CALL_DETAIL_DB,
                             table=TABLE_DETAIL_INFORMATION+index,
                             col='telphone', value=mobile)


def main():

    clean_call_records('18518040409')
    clean_call_records('18301670750')


if __name__ == '__main__':
    main()


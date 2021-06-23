#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from impala.dbapi import connect
import logging
# Connect to Impala and execute the query

def execute_query(query, cursor=None):
    try:
        impala_con = connect(host='192.168.250.10')
        impala_cur = impala_con.cursor()
        impala_cur.execute(query)
        result = impala_cur if cursor else impala_cur.fetchall()
        logging.info('Query has been successfully executed')
        impala_cur.close()
        impala_con.close()
        return result
    except Exception as err:
        logging.error('Query execution failed!')
        logging.error(err)
    return None


create_expression = (
'CREATE TABLE kudu_table '
'(app_id BIGINT,'
            'code STRING,'
            'description STRING,'
            'events_count BIGINT,'
            'PRIMARY KEY(app_id, code)) '
'PARTITION BY HASH(app_id) PARTITIONS 64 STORED AS KUDU ')

execute_query(create_expression)


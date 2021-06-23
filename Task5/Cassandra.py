#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from cassandra.cluster import Cluster
clstr=Cluster()
session=clstr.connect('mykeyspace')
qry= '''
create table students (
   studentID int,
   name text,
   age int,
   marks int,
   primary key(studentID)
);'''
session.execute(qry)
session.execute("insert into students (studentID, name, age, marks) values 
   (1, 'Juhi',20, 200);"


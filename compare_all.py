
# coding: utf-8

# In[1]:


# !pip3 install pyspark findspark --upgrade


# In[1]:


import os, sys

import findspark
findspark.init()
import pyspark
# from pysparkling import Context


# In[2]:


sc = pyspark.SparkContext(appName="compare_engine")


# In[3]:


# primary= sys.argv[1]
# secondary = sys.argv[2]


# In[6]:


# sc.stop
primary="_int_legacy_1110.json"
secondary="_legacy_1110.json"
raw_primary = sc.textFile(primary)                                                  
raw_secondary = sc.textFile(secondary)


# In[50]:


primary="_sort.txt"
secondary="nonprod_sky_1.txt"
raw_primary = sc.textFile(primary)                                                  
raw_secondary = sc.textFile(secondary)


# In[51]:


primary_count = raw_primary.count()


# In[52]:


print(primary_count)


# In[53]:


raw_primary.distinct().count()


# In[54]:


secondary_count = raw_secondary.count()


# In[55]:


print(secondary_count)


# In[56]:


raw_secondary.distinct().count()


# In[57]:


# Returns the number of records in PRIMARY not in found SECONDARY
notCompRecords  = raw_primary.subtract(raw_secondary)


# In[58]:


notCompRecords.count()


# In[59]:


# notCompRecords.collect()
rev_diff_records = raw_secondary.subtract(raw_primary)


# In[62]:


# Returns number of records in SECONDARY file not found in PRIMARY
rev_diff_records.count()


# In[63]:


get_ipython().system('rm -Rf collects.csv')
notCompRecords.repartition(1).saveAsTextFile('collects.csv')


# In[64]:


get_ipython().system('cat collects.csv/part-00000 > collect_report.csv')


# In[65]:


get_ipython().system('wc -l collect_report.csv')


# In[49]:


# !diff collect_report.csv sky_int_legacy_1110.json


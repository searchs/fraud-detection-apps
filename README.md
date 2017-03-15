# pybox holds my Python learnings and adventure 

### Data Processing Considerations
Using Pandas, create a DataFrame and check the member usage:
``` Python
import pandas as pd
df = pd.read_csv('source.csv')
print(df.info())
# Pandas internals:  BlockManager details
print(df._data)

# Series.nbytes

t_bytes = df.size * 8

print(t_bytes)

t_mg = t_bytes/1048576

print(t_mg)

#Actual Memory usage
df.info(memory_usage="deep")

#Memory use by Column
df.memory_usage(deep=True)

```

**https://jakevdp.github.io/blog/2014/05/09/why-python-is-slow/**

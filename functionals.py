import collections
import concurrent.futures
from pprint import pprint
import time
import multiprocessing
import os

Scientists = collections.namedtuple("Scientist", ["name", "field", "born", "nobel"])

pprint(Scientists)
scientists = (
    Scientists(name="Ada Lovelace", field="Maths", born=1815, nobel=False),
    Scientists(name="Albert Einstein", field="Physics", born=1905, nobel=True),
    Scientists(name="Marie Currie", field="Physics", born=1867, nobel=True),
    Scientists(name="Ada Yonath", field="Chemistry", born=1939, nobel=True),
    Scientists(name="Vera Rubin", field="Astronomy", born=1928, nobel=False),
)

# pprint(scientists)

# del scientists[0]
def nobel_filter(x):
    return x.nobel is True


# ll = tuple(filter(lambda obj: obj.field ==  'Physics' and obj.nobel is True, scientists))
# for l in  ll:
#     print(l)

# pprint(tuple(filter(nobel_filter, scientists)))

# MAP functions

name_and_ages = tuple(map(lambda x: {"name": x.name, "age": 2020 - x.born}, scientists))

# pprint(name_and_ages)

from functools import reduce

total_age = reduce(lambda acc, val: acc + val["age"], name_and_ages, 0)
# pprint(total_age)


# pprint(sum([x['age'] for x in name_and_ages]))


def reducer(acc, val):
    acc[val.field].append(val.name)
    return acc


scientists_by_field = reduce(
    reducer, scientists, {"Maths": [], "Physics": [], "Chemistry": [], "Astronomy": []}
)

# pprint(scientists_by_field)
import collections

# less error prone approach
scientists_by_field_dd = reduce(reducer, scientists, collections.defaultdict(list))

# pprint(scientists_by_field_dd)

# Using itertools

import itertools

scientists_by_field_group = {
    item[0]: list(item[1]) for item in itertools.groupby(scientists, lambda x: x.field)
}

# pprint(scientists_by_field_group)
pool = multiprocessing.Pool(processes=2, maxtasksperchild=1)

# TRANSFORMATION
def tranform_age(x):
    pprint(f"PID: {os.getpid()} - Processing record: {x.name}")
    result = {"name": x.name, "age": 2020 - x.born}
    print(f"PID: {os.getpid()} - End of Processing for record: {x.name}")
    return result


result = tuple(map(tranform_age, scientists))


pprint(result)

# Using MultiProcessing

start = time.time()

result_pool = pool.map_async(tranform_age, scientists)
end = time.time()
print(f"\nTime to complete:  {end - start:.2f}s\n")
pprint(result_pool)

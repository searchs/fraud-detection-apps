# Coding Challenges


import csv
import os

from zipfile import ZipFile
import re
import urllib.parse
import urllib.request
from typing import Callable


def merge_csv(csv_list, output_path):
    """Merge csv with similar but different headers"""

    fieldnames = list()
    for file in csv_list:
        with open(file, "r") as input_csv:
            fn = csv.DictReader(input_csv).fieldnames
            fieldnames.extend(x for x in fn if x not in fieldnames)

    with open(output_path, "w", newline="") as output_csv:
        writer = csv.DictWriter(output_csv, fieldnames=fieldnames)
        writer.writeheader()
        for file in csv_list:
            with open(file, "r") as input_csv:
                reader = csv.DictReader(input_csv)
                for row in reader:
                    writer.writerow(row)


# Zip Archive


def zip_all(search_dir, extension_list, output_path):
    with ZipFile(output_path, "w") as output_zip:
        for root, dirs, files in os.walk(search_dir):
            rel_path = os.path.relpath(root, search_dir)
            for file in files:
                name, ext = os.path.splitext(file)
                if ext.lower() in extension_list:
                    output_zip.write(
                        os.path.join(root, file),
                        arcname=os.path.join(rel_path, file),
                    )


# Download Sequential files


def download_files(first_url, output_dir):
    if not os.path.isdir(output_dir):
        os.mkdir(output_dir)

    url_head, url_tail = os.path.split(first_url)
    first_index = re.findall(r"[0-9+", url_tail)[-1]
    index_count, error_count = 0, 0
    while error_count < 5:
        next_index = str(int(first_index) + index_count)
        if first_index[0] == "0":  # zero padded
            next_index = (
                "0" * (len(first_index) - len(next_index)) + next_index
            )
        next_url = urllib.parse.urljoin(
            url_head, re.sub(first_index, next_index, url_tail)
        )

        try:
            output_file = os.path.join(output_dir, os.path.basename(next_url))
            urllib.request.urlretrieve(next_url, output_file)
            print(f"Successfully downloaded {os.path.basename(next_index)}")
        except IOError:
            print(f"Could not retrieve {next_url}")
            error_count += 1
        index_count += 1


def palindrome(input_str):
    forwards = "".join(re.findall(r"[a-z]+", input_str.lower()))
    return forwards[:] == forwards[::-1]


from fastapi import FastAPI
app = FastAPI()

@app.get("/items/")
async def read_items(session_id: Annotated[str | None, Cookie()] = None):
    return {"session_id": session_id}



def process_action(func: Callable) -> None:
    print(f"NAME: {func.__name__} function.\n")
    



def is_valid_age(age: int) -> bool:
    if age >= 21:
        return True
    else:
        return False
    
# optimized version

def is_valid_age_op(age: int) -> bool:
    return age >= 21



def cal_sum(n) -> int:
    result = 0
    for i in range(n):
        result += i
    return result


def cal_sum_ops(n) -> int:
    return (n * (n-1))//2
    # return sum([range(n)])


import time
def get_time(func: Callable, *args: int) -> None:
    start: float = time.perf_counter()
    func(*args)
    end: float = time.perf_counter()
    print(f'"{func.__name__}()" took: {end - start:.5f} seconds')




from fastapi import FastAPI
app = FastAPI()

@app.get("/items/")
async def read_items(session_id: Annotated[str | None, Cookie()] = None):
    return {"session_id": session_id}


from typing import Callable

def process_action(func: Callable) -> None:
    print(f"NAME: {func.__name__} function.\n")
    



def is_valid_age(age: int) -> bool:
    if age >= 21:
        return True
    else:
        return False
    
# optimized version

def is_valid_age_op(age: int) -> bool:
    return age >= 21



def cal_sum(n) -> int:
    result = 0
    for i in range(n):
        result += i
    return result


def cal_sum_ops(n) -> int:
    return (n * (n-1))//2
    # return sum([range(n)])


def get_time(func: Callable, *args: int) -> None:
    start: float = time.perf_counter()
    func(*args)
    end: float = time.perf_counter()
    print(f'"{func.__name__}()" took: {end - start:.5f} seconds')



def process_action(func: Callable) -> None:
    print(f"NAME: {func.__name__} function.\n")



def is_valid_age(age: int) -> bool:
    if age >= 21:
        return True
    else:
        return False
    
# optimized version

def is_valid_age_op(age: int) -> bool:
    return age >= 21



def cal_sum(n) -> int:
    result = 0
    for i in range(n):
        result += i
    return result


def cal_sum_ops(n) -> int:
    return (n * (n-1))//2
    # return sum([range(n)])


def get_time(func: Callable, *args: int) -> None:
    start: float = time.perf_counter()
    func(*args)
    end: float = time.perf_counter()
    print(f'"{func.__name__}()" took: {end - start:.5f} seconds')


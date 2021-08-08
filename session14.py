import sys
import random
from datetime import datetime
from collections import namedtuple, Counter
import csv
import re
import math
from tabulate import tabulate

personal_info = namedtuple(
    "personal_info", ["SSN", "First_Name", "Last_Name", "Gender", "Language"]
)
vehicles = namedtuple(
    "vehicles", ["SSN", "Vehicle_Make", "Vehicle_Model", "Model_Year"]
)
employment = namedtuple("employment", ["Employer", "Department", "Employee_Id", "SSN"])
update_status = namedtuple("update_status", ["SSN", "Last_Updated", "Created"])


def read_file(file_name):
    """
    Reads the csv file with ',' delimiter
    """
    with open(file_name) as f:
        rows = csv.reader(f, delimiter=",", quotechar='"')
        yield from rows


def personal_info_generator():
    """
    Generator for personal_info named tuple , Generates a named tuple for each row in the file
    """
    data = read_file("personal_info.csv")
    next(data)
    for row in data:
        ssn = row[0]
        first_name = row[1]
        last_name = row[2]
        gender = row[3]
        language = row[4]
        yield personal_info(ssn, first_name, last_name, gender, language)


def fetch_records(gen):
    """
    provides the list of generator records 
    """
    return [record for record in gen()]


def vehicle_generator():
    """
    Generator for vehicle_generator named tuple ,Generates a named tuple for each row in the file 
    """
    data = read_file("vehicles.csv")
    next(data)
    for row in data:
        ssn = row[0]
        vehicle_make = row[1]
        vehicle_model = row[2]
        model_year = int(row[3])
        yield vehicles(ssn, vehicle_make, vehicle_model, model_year)


def employment_generator():
    """
    Generator for employment_generator named tuple ,Generates a named tuple for each row in the file
    """
    data = read_file("employment.csv")
    next(data)
    for row in data:
        employer = row[0]
        department = row[1]
        employee_id = row[2]
        ssn = row[3]
        yield employment(employer, department, employee_id, ssn)


def update_status_generator():
    """
    Generator for update_status_generator named tuple ,Generates a named tuple for each row in the file
    """
    data = read_file("update_status.csv")
    next(data)
    for row in data:
        ssn = row[0]
        last_updated = datetime.strptime(
            datetime.fromisoformat(row[1].replace("Z", "+00:00")).strftime("%d/%m/%Y"),
            "%d/%m/%Y",
        )
        created = datetime.strptime(
            datetime.fromisoformat(row[2].replace("Z", "+00:00")).strftime("%d/%m/%Y"),
            "%d/%m/%Y",
        )
        yield update_status(ssn, last_updated, created)


# Goal 1 :create iterators for each of the four files
personal_info_iterator = fetch_records(personal_info_generator)
vehicle_iterator = fetch_records(vehicle_generator)
employment_iterator = fetch_records(employment_generator)
update_status_iterator = fetch_records(update_status_generator)


# Goal 2 :create a single iterable that combines all the columns from all the iterators.
def merge_tuples(*ntuples):
    """
    Merges the records from all the generators into a single list of named tuples ,
    creates new named tuple by merging other named tuples with key "SSN"
  
    """
    m = {}
    for i in ntuples:
        m.update(i._asdict())
    yield namedtuple("combined", m.keys())(*m.values())


def combined_generator(l1, l2, l3, l4):
    """
    Generator for combined named tuple , Generates a named tuple for each row in the file ,
    combines all named tuple merged records 
    """
    for a, b, c, d in zip(l1, l2, l3, l4):
        yield from merge_tuples(a, b, c, d)


combined_iterator = combined_generator(
    personal_info_iterator,
    vehicle_iterator,
    employment_iterator,
    update_status_iterator,
)

# final records list
combined_records = list(combined_iterator)

print(f"Total number of combined records: {len(combined_records)}")

# Goal 3 :identify any stale records, where stale simply means the record has not been updated
# since 3/1/2017 (e.g. last update date < 3/1/2017)

f_date = datetime.strptime("03/01/2017", "%m/%d/%Y")
stale_records = [x for x in filter(lambda x: x.Last_Updated < f_date, combined_records)]
current_records = [
    x for x in filter(lambda x: x.Last_Updated > f_date, combined_records)
]

print(f"Total number of stale records: {len(stale_records)}")

print(f"Total number of current records: {len(current_records)}")

# Goal 4 :Find the largest group of car makes for each gender
def vehicle_make_gender_information(records):
    """
    Generator for Vehicle Make , Gender from given records
    """
    for record in records:
        yield record.Vehicle_Make, record.Gender


def vehicle_make_gender_generator(records):
    """
    Generator for  Vehicle Make , Gender combinations
    """
    vehicle_make_list = [
        (vehicle_make, gender)
        for vehicle_make, gender in vehicle_make_gender_information(records)
    ]
    violation_by_vehicle_make = Counter(vehicle_make_list)
    for make_gender, Count in violation_by_vehicle_make.most_common():
        yield [make_gender, Count]


def show_top_count(records):
    """
    Prints Vehicle Make, gender combination count in tabular format
    """
    print(
        tabulate(
            list(vehicle_make_gender_generator(records))[0:5],
            headers=["make_gender", "Count"],
        )
    )


show_top_count(combined_records)

# For Females :  Ford , Chevrolet are famous with 48 count
# For Males :  Ford  are famous with 44 count

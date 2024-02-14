import os
import sys
import django
import csv
from collections import defaultdict

sys.path.append('c:/AWD_FINAL/awd_finalterm/finalterm')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'finalterm.settings')
django.setup()

from elearning.models import *

data_file = 'c:/AWD_FINAL/awd_finalterm/finalterm/Online_Courses.csv'

courses = defaultdict(list)
course_type = set()

with open(data_file, encoding='UTF-8') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    header = csv_reader.__next__()
    for row in csv_reader:
        course_type.add(row[3])
        courses[row[0]] = row[1:4]

Courses.objects.all().delete()
Course_Type.objects.all().delete()

course_rows = {}
type_rows = {}

for course_type in course_type:
    row = Course_Type.objects.create(course_type=course_type)
    row.save()
    type_rows[course_type] = row
for course_name, data in courses.items():
 row = Courses.objects.create(course_name=course_name, course_type=type_rows[data[2]], course_outline=data[1]
 )
 row.save()
 course_rows[course_name] = row


    
    
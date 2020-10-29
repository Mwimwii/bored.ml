import sys
import json
import random
from math import ceil
import pprint


def json_load(fileloc):
    with open(fileloc) as f:
        data = json.load(f)
    return data


def json_save(fileloc, data):
    with open(fileloc, 'w+') as f:
        json.dump(data, f)
    print("File saved\n")


def get_eta(duration):
    if duration > 2:
        return ceil(duration/3)
    else:
        return ceil(duration/2)


def get_courses():
    courses = json_load('courses.json')
    return courses


def get_course(tag=""):
    courses = get_courses()
    if tag != "":
        courses = [course for course in courses if tag in course["Tags"]]
        if courses == []:
            courses = get_courses()
    course = (random.choice(courses))
    course["daily"] = get_eta(course["Duration"])
    json_save('current.json', course)
    return course


def flatten(t): return [item for sublist in t for item in sublist]


def tags():
    courses = get_courses()
    tags = flatten([course["Tags"] for course in courses])
    return set(tags)


def main():
    sys.exit


if __name__ == "__main__":
    main()

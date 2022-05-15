# # ................TEST_EMAIL.PY.................
#
# from pytest import mark
# from requests import request
# from json import loads
#
#
# headers = "email, expected_status"
# emails = [
#             ("hello.world", "failure"),
#             ("hello.world@company.com", "success"),
#             ("hello.world@", "failure"),
#             ("hello.world@.com", "failure"),
#             ("hello.world@company.gov.in", "success"),
#
#
#             ("hello.world@company.edu", "success"),
#          ]
#
#
# @mark.parametrize(headers, emails)
# def test_email(email, expected_status):
#     url = f"https://api.eva.pingutil.com/email?email={email}"
#
#     # .........Hit the request and collect the response............
#     response = request("GET", url)
#
#     # .................get the actual JSON  string using a property "text"...........
#     json_string = response.text    # form of string
#
#     # ...................Convert the JSON string to python data structure using loads method (de-serialization ).......................
#     data = loads(json_string)      # form of dictionary
#
#     # ...............parse the dictionary or do a dictionary look up.....................................
#     actual_status = data["status"]
#
#     assert actual_status == expected_status


# collecting ... collected 6 items
#
# web_automation_practice.py::test_bank_ifsc_code[hello.world-failure]
# web_automation_practice.py::test_bank_ifsc_code[hello.world@company.com-success]
# web_automation_practice.py::test_bank_ifsc_code[hello.world@-failure]
# web_automation_practice.py::test_bank_ifsc_code[hello.world@.com-failure]
# web_automation_practice.py::test_bank_ifsc_code[hello.world@company.gov.in-success]
# web_automation_practice.py::test_bank_ifsc_code[hello.world@company.edu-success]

# PASSED [ 16%]PASSED [ 33%]PASSED [ 50%]PASSED [ 66%]PASSED [ 83%]PASSED [100%]

#
# @mark.parametrize(headers, emails)
# def test_email(email, expected_status):
#     url = f"https://api.eva.pingutil.com/email?email={email}"
#
#     # .........Hit the request and collect the response............
#     response = request("GET", url)
#
#     # .................get the atctual JSON  string using a property "text"...........
#     json_string = response.text    # form of string
#
#     # ...................Convert the JSON string to python data structure using loads method (de-serialization ).......................
#     data = loads(json_string)      # form of dictionary
#
#     # ...............parse the dictionary or do a dictionary look up.....................................
#     actual_status = data["status"]
#
#     assert actual_status == "success"

#
# # web_automation_practice.py::test_bank_ifsc_code[hello.world-failure] FAILED [ 16%]
# # web_automation_practice.py:300 (test_bank_ifsc_code[hello.world-failure])
# # 'failure' != 'success'
# #
# # 'success'
# # 'failure'
#
# # web_automation_practice.py::test_bank_ifsc_code[hello.world@company.com-success]
# # web_automation_practice.py::test_bank_ifsc_code[hello.world@-failure]
# # web_automation_practice.py::test_bank_ifsc_code[hello.world@.com-failure]
# # web_automation_practice.py::test_bank_ifsc_code[hello.world@company.gov.in-success]
# # web_automation_practice.py::test_bank_ifsc_code[hello.world@company.edu-success]
#
# # 3 failed, 3 passed in 7.10s
#################################################################################################

import csv

from requests import request
from json import loads
from pytest import mark

def test_demo():
    url = "https://reqres.in/api/users?page=2"
    response = request("GET", url)

    # validate status code
    assert response.status_code == 200

    json_string = response.text

    # de-serialization
    python_object = loads(json_string)

    users = python_object["data"]

    for user in users:
        print(user)


    with open(r"C:\Users\user\Desktop\training\selenium_projects/_user.csv", "w") as f:
        writer = csv.DictWriter(f, ["id", "email", "first_name", "last_name", "avatar"])
        writer.writeheader()
        for user in users:
            writer.writerow(user)



# collecting ... collected 1 item
#
# test_email.py::test_demo PASSED                                          [100%]{'id': 7, 'email': 'michael.lawson@reqres.in', 'first_name': 'Michael', 'last_name': 'Lawson', 'avatar': 'https://reqres.in/img/faces/7-image.jpg'}
# {'id': 8, 'email': 'lindsay.ferguson@reqres.in', 'first_name': 'Lindsay', 'last_name': 'Ferguson', 'avatar': 'https://reqres.in/img/faces/8-image.jpg'}
# {'id': 9, 'email': 'tobias.funke@reqres.in', 'first_name': 'Tobias', 'last_name': 'Funke', 'avatar': 'https://reqres.in/img/faces/9-image.jpg'}
# {'id': 10, 'email': 'byron.fields@reqres.in', 'first_name': 'Byron', 'last_name': 'Fields', 'avatar': 'https://reqres.in/img/faces/10-image.jpg'}
# {'id': 11, 'email': 'george.edwards@reqres.in', 'first_name': 'George', 'last_name': 'Edwards', 'avatar': 'https://reqres.in/img/faces/11-image.jpg'}
# {'id': 12, 'email': 'rachel.howell@reqres.in', 'first_name': 'Rachel', 'last_name': 'Howell', 'avatar': 'https://reqres.in/img/faces/12-image.jpg'}
#
#
# ============================== 1 passed in 0.56s ==============================

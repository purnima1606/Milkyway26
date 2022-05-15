# from requests import request
#
# url = "https://ifsc.razorpay.com/HDFC0001755"
# # print(request("GET", url))    # <Response [200]>
# response = request("GET", url)
# print(response)         # <Response [200]>
#
# ###############################################
# from requests import request
#
# url = "https://ifsc.razorpay.com/HDFC0001755"
# response = request("GET", url)
#
# print(response.text)
# # {"NEFT":true,"IMPS":true,"BRANCH":"100 FEET ROAD-INDIRA NAGAR","STATE":"KARNATAKA","ADDRESS":"NO.1075,12TH MAIN ROAD, 8 TH CROSS, OFF 100 FEET ROAD, INDIRA NAGAR","CITY":"BANGALORE","UPI":true,"DISTRICT":"BANGALORE URBAN","RTGS":true,"CONTACT":"+919945863333","CENTRE":"BANGALORE URBAN","MICR":"560240065","SWIFT":"HDFCINBB","BANK":"HDFC Bank","BANKCODE":"HDFC","IFSC":"HDFC0001755"}
#
# print(type(response))     # <class 'requests.models.Response'>
#
# print(dir(response))
# # ['__attrs__', '__bool__', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__enter__', '__eq__', '__exit__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__nonzero__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setstate__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_content', '_content_consumed', '_next', 'apparent_encoding', 'close', 'connection', 'content', 'cookies', 'elapsed', 'encoding', 'headers', 'history', 'is_permanent_redirect', 'is_redirect', 'iter_content', 'iter_lines', 'json', 'links', 'next', 'ok', 'raise_for_status', 'raw', 'reason', 'request', 'status_code', 'text', 'url']
#
# print(response.status_code)    # 200
#
# ###################################################
#
# from requests import request
# from json import loads
#
# url = "https://ifsc.razorpay.com/HDFC0001755"
# response = request("GET", url)
# print(type(response))           # <class 'requests.models.Response'>
#
# json_string = response.text    # form of string
# print(type(json_string))       # <class 'str'>
#
# print(json_string)            # form of "{name:value}"
#
# data = loads(json_string)      # form of dictionary
# print(type(data))              # <class 'dict'>
#
# print(data)             # form of {}
# {'MICR': '560240065', 'IMPS': True, 'CONTACT': '+919945863333', 'DISTRICT': 'BANGALORE URBAN', 'NEFT': True, 'ADDRESS': 'NO.1075,12TH MAIN ROAD, 8 TH CROSS, OFF 100 FEET ROAD, INDIRA NAGAR', 'SWIFT': 'HDFCINBB', 'RTGS': True, 'UPI': True, 'CENTRE': 'BANGALORE URBAN', 'STATE': 'KARNATAKA', 'CITY': 'BANGALORE', 'BRANCH': '100 FEET ROAD-INDIRA NAGAR', 'BANK': 'HDFC Bank', 'BANKCODE': 'HDFC', 'IFSC': 'HDFC0001755'}
#
# #################################################
#
# from requests import request
# from json import loads
#
# url = "https://ifsc.razorpay.com/HDFC0001755"
# response = request("GET", url)
# print(type(response))           # <class 'requests.models.Response'>
#
# json_string = response.text    # form of string
# data = loads(json_string)      # form of dictionary
# # print(type(data))              # <class 'dict'>
#
# print(data["BRANCH"])               # 100 FEET ROAD-INDIRA NAGAR
# print(data["CONTACT"])              # +919945863333
# print(data["CITY"])                 # BANGALORE
# print(data["MICR"])                 # 560240065
#
# ###################################################
#
# from requests import request
# from json import loads
#
# url = "https://ifsc.razorpay.com/HDFC0001755"
# # .........Hit the request and collect the response............
# response = request("GET", url)
# print(type(response))           # <class 'requests.models.Response'>
#
# # .................get the atctual JSON  string using a property "text"...........
# json_string = response.text    # form of string
# # print(type(json_string))       # <class 'str'>
#
# # print(json_string)            # form of "{name:value}"
#
# # ...................Convert the JSON string to python data structure using loads method (de-serialization ).......................
# data = loads(json_string)      # form of dictionary
# # print(type(data))              # <class 'dict'>
#
# # print(data)             # form of {}
#
# # ...............parse the dictionary or do a dictionary look up.....................................
# actual_branch = data["BRANCH"]
# print(actual_branch)       # 100 FEET ROAD-INDIRA NAGAR
#
#
# ##############################################################
#
from pytest import mark
from requests import request
from json import loads

headers = "code, expected_branch"
codes = [("HDFC0001755", "100 FEET ROAD-INDIRA NAGAR"),
         ("SBIN0040014", "BASAVANAGUDI"),
         ("ICIC0000002", "BANGALORE - M G ROAD")
         ]

@mark.parametrize(headers, codes)
def test_bank_ifsc_code(code, expected_branch):
    url = f"https://ifsc.razorpay.com/{code}"

    # .........Hit the request and collect the response............
    response = request("GET", url)

    # .................get the atctual JSON  string using a property "text"...........
    json_string = response.text    # form of string

    # ...................Convert the JSON string to python data structure using loads method (de-serialization ).......................
    data = loads(json_string)      # form of dictionary

    # ...............parse the dictionary or do a dictionary look up.....................................
    actual_branch = data["BRANCH"]

    assert actual_branch == expected_branch


# collecting ... collected 3 items

# web_automation_practice.py::test_bank_ifsc_code[HDFC0001755-100 FEET ROAD-INDIRA NAGAR]
# web_automation_practice.py::test_bank_ifsc_code[SBIN0040014-BASAVANAGUDI]
# web_automation_practice.py::test_bank_ifsc_code[ICIC0000002-BANGALORE - M G ROAD]
#
# PASSED [ 33%]PASSED [ 66%]PASSED [100%]

############################################################

# from pytest import mark
# from requests import request
# from json import loads
#
# headers = "code, expected_branch"
# codes = [("HDFC0001755", "200 FEET ROAD-INDIRA NAGAR"),                # 200 in place of 100
#          ("SBIN0040014", "BASAVANAGUDI"),
#          ("ICIC0000002", "BANGALORE - M G ROAD")
#          ]
#
# @mark.parametrize(headers, codes)
# def test_bank_ifsc_code(code, expected_branch):
#     url = f"https://ifsc.razorpay.com/{code}"
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
#     actual_branch = data["BRANCH"]
#
#     try:
#         assert actual_branch == expected_branch
#     except AssertionError:
#         print(f"The expected branch is {expected_branch}, but the actual branch from response is {actual_branch}")
#

# # web_automation_practice.py::test_bank_ifsc_code[HDFC0001755-200 FEET ROAD-INDIRA NAGAR]
# # web_automation_practice.py::test_bank_ifsc_code[SBIN0040014-BASAVANAGUDI]
# # web_automation_practice.py::test_bank_ifsc_code[ICIC0000002-BANGALORE - M G ROAD]
#
# # PASSED [ 33%]The expected branch is 200 FEET ROAD-INDIRA NAGAR, but the actual branch from response is 100 FEET ROAD-INDIRA NAGAR
# # PASSED [ 66%]PASSED [100%]
#
# # we cannot use try and except for assert because it'll create confusion & always gives output is passed.
#
# ############################################################
# # ...............TEST_BANK.PY.........................
# # .............TEST_BANK_IFSC_CODE.PY................
#
# from pytest import mark
# from requests import request
# from json import loads
#
# headers = "code, expected_branch"
# codes = [("HDFC0001755", "100 FEET ROAD-INDIRA NAGAR"),
#          ("SBIN0040014", "DVG Road"),
#          ("ICIC0000002", "BANGALORE - M G ROAD")
#          ]
#
# @mark.parametrize(headers, codes)
# def test_bank_ifsc_code(code, expected_branch):
#     url = f"https://ifsc.razorpay.com/{code}"
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
#     actual_branch = data["BRANCH"]
#
#     assert actual_branch == expected_branch
#
#
# # web_automation_practice.py::test_bank_ifsc_code[HDFC0001755-100 FEET ROAD-INDIRA NAGAR]
# # web_automation_practice.py::test_bank_ifsc_code[SBIN0040014-DVG Road] PASSED [ 33%]FAILED [ 66%]
# # web_automation_practice.py:182 (test_bank_ifsc_code[SBIN0040014-DVG Road])
# # 'BASAVANAGUDI' != 'DVG Road'
#
# ######################################################################
# # ......................READ EXCEL FILE...............
# import csv
# from pytest import mark
# from requests import request
# from json import loads
#
#
# def read_csv():
#     codes = []
#     with open() as f:
#         rows = csv.reader(f)
#         headers = next(rows)
#         for row in rows:
#             codes.append(tuple(row))
#     return codes
#
# headers = "code, expected_branch"
# # codes = [("HDFC0001755", "100 FEET ROAD-INDIRA NAGAR"),
# #         ("SBIN0040014", "DVG Road"),
# #         ("ICIC0000002", "BANGALORE - M G ROAD")
# #         ]
#
# codes = read_csv()
#
# @mark.parametrize(headers, codes)
# def test_bank_ifsc_code(code, expected_branch):
#     url = f"https://ifsc.razorpay.com/{code}"
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
#     actual_branch = data["BRANCH"]
#
#     assert actual_branch == expected_branch
#
# # ????????????????????????????????????????????????????????????????????????????????
# ####################################################################
# # ................TEST_EMAIL.PY.................
#
# from pytest import mark
# from requests import request
# from json import loads
#
# headers = "email, expected_status"
# emails = [
#             ("hello.world", "failure"),
#             ("hello.world@company.com", "success"),
#             ("hello.world@", "failure"),
#             ("hello.world@.com", "failure"),
#             ("hello.world@company.gov.in", "success"),
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
#
# # collecting ... collected 6 items
# #
# # web_automation_practice.py::test_bank_ifsc_code[hello.world-failure]
# # web_automation_practice.py::test_bank_ifsc_code[hello.world@company.com-success]
# # web_automation_practice.py::test_bank_ifsc_code[hello.world@-failure]
# # web_automation_practice.py::test_bank_ifsc_code[hello.world@.com-failure]
# # web_automation_practice.py::test_bank_ifsc_code[hello.world@company.gov.in-success]
# # web_automation_practice.py::test_bank_ifsc_code[hello.world@company.edu-success]
#
# # PASSED [ 16%]PASSED [ 33%]PASSED [ 50%]PASSED [ 66%]PASSED [ 83%]PASSED [100%]
#
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
#
# ########################################################################
#
# from pytest import mark
# from requests import request
# from json import loads
#
# headers = "email"
# emails = [
#             "hello.world@company.com",
#             "hello.world@company.gov.in",
#             "hello.world@company.edu",
#          ]
#
#
# @mark.parametrize(headers, emails)
# def test_valid_email(email):
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
#
#
#
# headers = "email"
#
#
# emails = [
#             "hello.world",                       # not give like this ("hello.world"),
#             "hello.world@",
#             "hello.world@.com",
#          ]
#
#
# @mark.parametrize(headers, emails)
# def test_invalid_email(email):
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
#     assert actual_status == "failure"
#
#
# # collecting ... collected 6 items
# #
# # web_automation_practice.py::test_valid_email[hello.world@company.com]
# # web_automation_practice.py::test_valid_email[hello.world@company.gov.in]
# # web_automation_practice.py::test_valid_email[hello.world@company.edu]
# # web_automation_practice.py::test_invalid_email[hello.world] PASSED [ 16%]PASSED [ 33%]PASSED [ 50%]
# # web_automation_practice.py::test_invalid_email[hello.world@]
# # web_automation_practice.py::test_invalid_email[hello.world@.com]
# # 6 passed in 5.23s
# #
#
# #####################################################################################################
#
# from time import sleep
# from requests import request
# from json import loads
# from pytest import mark
#
# url = "https://reqres.in/api/users?page=2"
# response = request("GET", url)
#
# # validate status code
# assert response.status_code == 200
#
# json_string = response.text
#
# # de-serialization
# python_object = loads(json_string)
#
# users = python_object["data"]
#
# for user in users:
#     print(user)
#     sleep(1)
#
# # {'id': 7, 'email': 'michael.lawson@reqres.in', 'first_name': 'Michael', 'last_name': 'Lawson', 'avatar': 'https://reqres.in/img/faces/7-image.jpg'}
# # {'id': 8, 'email': 'lindsay.ferguson@reqres.in', 'first_name': 'Lindsay', 'last_name': 'Ferguson', 'avatar': 'https://reqres.in/img/faces/8-image.jpg'}
# # {'id': 9, 'email': 'tobias.funke@reqres.in', 'first_name': 'Tobias', 'last_name': 'Funke', 'avatar': 'https://reqres.in/img/faces/9-image.jpg'}
# # {'id': 10, 'email': 'byron.fields@reqres.in', 'first_name': 'Byron', 'last_name': 'Fields', 'avatar': 'https://reqres.in/img/faces/10-image.jpg'}
# # {'id': 11, 'email': 'george.edwards@reqres.in', 'first_name': 'George', 'last_name': 'Edwards', 'avatar': 'https://reqres.in/img/faces/11-image.jpg'}
# # {'id': 12, 'email': 'rachel.howell@reqres.in', 'first_name': 'Rachel', 'last_name': 'Howell', 'avatar': 'https://reqres.in/img/faces/12-image.jpg'}
#
#
# ############################################################################################################

# import csv
#
# from requests import request
# from json import loads
# from pytest import mark
#
# url = "https://reqres.in/api/users?page=2"
# response = request("GET", url)
#
# # validate status code
# assert response.status_code == 200
#
# json_string = response.text
#
# # de-serialization
# python_object = loads(json_string)
#
# users = python_object["data"]
#
# for user in users:
#     print(user)
#
#
# with open(r"C:\Users\user\Desktop\training\selenium_projects/_user.csv", "w") as f:
#     writer = csv.DictWriter(f, ["id", "email", "first_name", "last_name", "avatar"])
#     writer.writeheader()
#     for user in users:
#         writer.writerow(user)
#
#
# # {'id': 7, 'email': 'michael.lawson@reqres.in', 'first_name': 'Michael', 'last_name': 'Lawson', 'avatar': 'https://reqres.in/img/faces/7-image.jpg'}
# # {'id': 8, 'email': 'lindsay.ferguson@reqres.in', 'first_name': 'Lindsay', 'last_name': 'Ferguson', 'avatar': 'https://reqres.in/img/faces/8-image.jpg'}
# # {'id': 9, 'email': 'tobias.funke@reqres.in', 'first_name': 'Tobias', 'last_name': 'Funke', 'avatar': 'https://reqres.in/img/faces/9-image.jpg'}
# # {'id': 10, 'email': 'byron.fields@reqres.in', 'first_name': 'Byron', 'last_name': 'Fields', 'avatar': 'https://reqres.in/img/faces/10-image.jpg'}
# # {'id': 11, 'email': 'george.edwards@reqres.in', 'first_name': 'George', 'last_name': 'Edwards', 'avatar': 'https://reqres.in/img/faces/11-image.jpg'}
# # {'id': 12, 'email': 'rachel.howell@reqres.in', 'first_name': 'Rachel', 'last_name': 'Howell', 'avatar': 'https://reqres.in/img/faces/12-image.jpg'}
#
# # crete _user.py file and put all data inside the file
#
# #################################################################################################
#
# from requests import request
# from json import loads
# from pytest import mark
#
# url = "https://reqres.in/api/login"
#
# # print(url)
#
# payload = {
#             "email": "eve.holt@reqres.in",
#             "password": "pistol"
#           }
# response = request("POST", url, json=payload)
# # print(response.text)
# print(response.status_code)            # 200
#
# # validate status code
# assert response.status_code == 200
# # assert 200 <= response.status_code <= 299              # my program ..........
# json_string = response.text
#
# # de-serialization
# python_object = loads(json_string)
#
# is_token_present = "token" in python_object
# print(is_token_present)           # True
#
# assert is_token_present == True
#
# # https://reqres.in/api/login
# # 200
# # True
#
# #####################################################################
#
# from requests import request
# from json import loads
# from pytest import mark
#
# def test_login_negative():
#     url = "https://reqres.in/api/login"
#
#     # print(url)
#
#     payload = {
#                 "email": "eve.holt@reqres.in"
#               }
#     response = request("POST", url, json=payload)
#     # print(response.text)
#     print(response.status_code)            # 400
#
#     # validate status code
#     assert response.status_code == 400
#
#     json_string = response.text
#
#     # de-serialization
#     python_object = loads(json_string)
#     print(python_object)                            # {'error': 'Missing password'}
#     assert python_object["error"] == "Missing password"
#
#
# # collecting ... collected 1 item
# #
# # web_automation_practice.py::test_login_negative PASSED                   [100%]400
# # {'error': 'Missing password'}
#
# ######################################################################
#
# from requests import request
# from json import loads
# from pytest import mark
#
# url = "https://reqres.in/api/login"
#
# def test_login_negative_missing_password():
#     # url = "https://reqres.in/api/login"
#     # # print(url)
#
#     payload = {
#                 "email": "eve.holt@reqres.in"
#               }
#     response = request("POST", url, json=payload)
#
#     # validate status code
#     assert response.status_code == 400
#
#     json_string = response.text
#
#     # de-serialization
#     python_object = loads(json_string)
#
#     assert python_object["error"] == "Missing password"
#
# # collecting ... collected 1 item
# #
# # web_automation_practice.py::test_login_negative_missing_password PASSED  [100%]
#
#
#
#
# def test_login_negative_missing_email():
#     # url = "https://reqres.in/api/login"
#     # # print(url)
#     payload = {
#                 "password": "pistol"
#               }
#
#     response = request("POST", url, json=payload)
#
#     # validate status code
#     assert response.status_code == 400
#
#     json_string = response.text
#
#     # de-serialization
#     python_object = loads(json_string)
#     print(python_object)                   # {'error': 'Missing email or username'}
#
#     assert python_object["error"] == "Missing email or username"
#
#
# print("pytest-html" == "web_automation_practice.html")
#
# # collecting ... collected 1 item
# #
# # web_automation_practice.py::test_login_negative_missing_email PASSED     [100%]{'error': 'Missing email or username'}
#
#
# # web_automation_practice.py::test_login_negative_missing_password PASSED  [ 50%]
# # web_automation_practice.py::test_login_negative_missing_email PASSED     [100%]{'error': 'Missing email or username'}
#
# #######################################################################################
# # ??????????????????????????????????????????????????????????????????????????????????????????????????
#
# # from requests import request
# # from json import loads
# # from pytest import mark
# #
# # url = "https://reqres.in/api/login"
# #
# # def test_registration_negative_missing_password():
# #     # url = "https://reqres.in/api/login"
# #     # # print(url)
# #
# #     payload = {
# #                 "email": "eve.holt@reqres.in"
# #               }
# #     response = request("POST", url, json=payload)
# #
# #     # validate status code
# #     assert response.status_code == 400
# #
# #     json_string = response.text
# #
# #     # de-serialization
# #     python_object = loads(json_string)
# #
# #     assert python_object["error"] == "Missing password"
# #
# # # collecting ... collected 1 item
# # #
# # # web_automation_practice.py::test_login_negative_missing_password PASSED  [100%]
# #
# #
# # def test_registration_negative_missing_email():
# #     # url = "https://reqres.in/api/login"
# #     # # print(url)
# #     payload = {
# #                 "password": "pistol"
# #               }
# #
# #     response = request("POST", url, json=payload)
# #
# #     # validate status code
# #     assert response.status_code == 400
# #
# #     json_string = response.text
# #
# #     # de-serialization
# #     python_object = loads(json_string)
# #     print(python_object)                   # {'error': 'Missing email or username'}
# #
# #     assert python_object["error"] == "Missing email or username"
# #
# # # ??????????????????????????????????????????????????????????????????????????
######################################################################################################
# 5 4 3 2 1
#   4 3 2 1
#    3 2 1
#      2 1
#        1
# n = 5
# a = 1
# while n >=1:
#     for i in range(n, 1):
#         print(" "*a)
#         print(i,end=" ")
#         a += 1
#         n -= 1
#


####################################################################################################





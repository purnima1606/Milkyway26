from pytest import mark
from requests import request
from json import loads

headers = "email, expected_status"
emails = [
            ("hello.world", "failure"),
            ("hello.world@company.com", "success"),
            ("hello.world@", "failure"),
            ("hello.world@.com", "failure"),
            ("hello.world@company.gov.in", "success"),
            ("hello.world@company.edu", "success"),
         ]


@mark.parametrize(headers, emails)
def test_email(email, expected_status):
    url = f"https://api.eva.pingutil.com/email?email={email}"

    # .........Hit the request and collect the response............
    response = request("GET", url)

    # .................get the actual JSON  string using a property "text"...........
    json_string = response.text    # form of string

    # ...................Convert the JSON string to python data structure using loads method (de-serialization ).......................
    data = loads(json_string)      # form of dictionary

    # ...............parse the dictionary or do a dictionary look up.....................................
    actual_status = data["status"]

    assert actual_status == expected_status
#

# collecting ... collected 6 items
#
# test_email.py::test_email[hello.world-failure]
# test_email.py::test_email[hello.world@company.com-success]
# test_email.py::test_email[hello.world@-failure]
# test_email.py::test_email[hello.world@.com-failure]
# test_email.py::test_email[hello.world@company.gov.in-success]
# test_email.py::test_email[hello.world@company.edu-success]
#
# ============================== 6 passed in 6.28s ==============================
# Process finished with exit code 0
# PASSED                    [ 16%]PASSED        [ 33%]PASSED                   [ 50%]PASSED               [ 66%]PASSED     [ 83%]PASSED        [100%]



from requests import request
from json import loads
from pytest import mark

headers = "email"
emails = [
    "hello.world@company.com",
    "hello.world@company.gov.in",
    "hello.world@company.edu"
    ]

@mark.parametrize(headers, emails)
def test_valid_email(email):
    url = f"" \
          f"{email}"
    # Hit the request and collect the response
    response = request("GET", url)

    # get the actual JSON string using a proprty "text"
    json_string = response.text

    # Convert the JSON string to python data structure using loads method (de-serilization)
    data = loads(json_string)

    # Parse the dictionary or do a dictionary look up
    actual_status = data['status']
    
    assert actual_status == "success"


headers = "email"
emails = [
    "hello.world",
    "hello.world@",
    "hello.world@.com",
    ]

@mark.parametrize(headers, emails)
def test_invalid_email(email):
    url = f"https://api.eva.pingutil.com/email?email={email}"
    # Hit the request and collect the response
    response = request("GET", url)

    # get the actual JSON string using a proprty "text"
    json_string = response.text

    # Convert the JSON string to python data structure using loads method (de-serilization)
    data = loads(json_string)

    # Parse the dictionary or do a dictionary look up
    actual_status = data['status']
    
    assert actual_status == "failure"








# headers = "email, expected_status"
# emails = [
#     ("hello.world", "failure"),
#     ("hello.world@company.com", "success"),
#     ("hello.world@", "failure"),
#     ("hello.world@.com", "failure"),
#     ("hello.world@company.gov.in", "success"),
#     ("hello.world@company.edu", "success")
#     ]

# @mark.parametrize(headers, emails)
# def test_bank_email(email, expected_status):
#     url = f"https://api.eva.pingutil.com/email?email={email}"
#     # Hit the request and collect the response
#     response = request("GET", url)

#     # get the actual JSON string using a proprty "text"
#     json_string = response.text

#     # Convert the JSON string to python data structure using loads method (de-serilization)
#     data = loads(json_string)

#     # Parse the dictionary or do a dictionary look up
#     actual_status = data['status']
    
#     assert actual_status == expected_status

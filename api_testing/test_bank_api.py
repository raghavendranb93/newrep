from requests import request
from json import loads
from pytest import mark
import csv

def read_csv():
    codes = [ ]
    with open('./bank.csv') as f:
        rows = csv.reader(f)
        headers = next(rows)        # skipping headers
        for row in rows:
            codes.append(tuple(row))
    return codes

headers = "code, expected_branch"

# codes = [
#     ("HDFC0001755", "100 FEET ROAD-INDIRA NAGAR"),
#     ("SBIN0040014","BASAVANAGUDI"),
#     ("ICIC0000002", "BANGALORE - M G ROAD")
#     ]
codes = read_csv()

@mark.parametrize(headers, codes)
def test_bank_ifsc_code(code, expected_branch):
    url = f"https://ifsc.razorpay.com/{code}"
    # Hit the request and collect the response
    response = request("GET", url)

    # get the actual JSON string using a proprty "text"
    json_string = response.text

    # Convert the JSON string to python data structure using loads method (de-serilization)
    data = loads(json_string)

    # Parse the dictionary or do a dictionary look up
    actual_branch = data['BRANCH']
    
    assert actual_branch == expected_branch

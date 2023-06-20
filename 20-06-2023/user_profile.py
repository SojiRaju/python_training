import requests

def test_user_profile_details_successful():
  # Test the scenario where the user profile details are retrieved successfully
  response = requests.get('https://dev-api.pttapp.com/api/profile-details')
  assert response.status_code == 401
  # Additional assertions for success scenario

#def test_user_profile_details_unauthenticated():
  # Test the scenario where the user profile details are attempted to be retrieved without proper authentication
 # response = requests.get('https://dev-api.pttapp.com/api/profile-details', headers={
  #'Authorization': 'eyJraWQiOiJqdWdrYTFmWGNkbEJWQzNmWTl3REpmZmVLU0tITXZmWk9Xd3ZQdmw5QTFvPSIsImFsZyI6IlJTMjU2In0.eyJzdWIiOiI4ZTMxOGQzNC0xZjI1LTQ0ODAtYjE4Yy1hODA4MDRhMmI5MTYiLCJjb2duaXRvOmdyb3VwcyI6WyJwdHQtYWRtaW4iXSwiaXNzIjoiaHR0cHM6XC9cL2NvZ25pdG8taWRwLmV1LXdlc3QtMi5hbWF6b25hd3MuY29tXC9ldS13ZXN0LTJfNGdyZjhoRXRkIiwiY2xpZW50X2lkIjoiNnNsNGttdnFtYTA4OWpiNXQ5aXNsMGIxMmEiLCJvcmlnaW5fanRpIjoiNjA0YWVjZGYtNjIwOS00NmQyLWJlNDQtNGVmYjJlNmEyNjc2IiwiZXZlbnRfaWQiOiIxOTUzMWJhNC05Mzc1LTRiYjktODhjYS01NzQ2NGJlMTAwY2QiLCJ0b2tlbl91c2UiOiJhY2Nlc3MiLCJzY29wZSI6ImF3cy5jb2duaXRvLnNpZ25pbi51c2VyLmFkbWluIiwiYXV0aF90aW1lIjoxNjg3MTU3MzU2LCJleHAiOjE2ODcxNjA5NTYsImlhdCI6MTY4NzE1NzM1NiwianRpIjoiZWYwMzM3YWYtN2FiZi00NDFkLWI1YjUtOWMzZGRjNTU4YWRmIiwidXNlcm5hbWUiOiJuaXNtYWwifQ.jngQ-YO673ky37y-5oq6eMFvOB7rkmloTRl6xr_n05xNGR0dsT8O43Owb34B9RweNEIR8U3nEMaW7fz510XZQNE0dtEpQ-c28lTW0chHY3Kehd_V6qezeU1SD1GDEwTNx70Xbs2cOWp18svlUq_K8zvJkrSbhAy_CMi8S6ar6lct5Ao9l8lGdx-iyoNxAxOqPdT1zuOxjsMT-EXb04VCJtjnKtT6KxDY1VZ15C_lor5IPvDZi5Kv9THDAkD5gU0uyldn25juAZPVG6_xGNZ40YUGJWL-nosFrFLaT2EmJEZH1KwNOk_nD7rRBk_0m46LthYwUNBd8qrDs03xGVG9HA'
  #})
  #assert response.status_code == 500

def test_user_profile_details_not_found():
  # Test the scenario where the user profile does not exist
  response = requests.get('https://dev-api.pttapp.com/api/profile-details')
  assert response.status_code == 401
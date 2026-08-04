import os, requests

from dotenv import load_dotenv

class ApiAgent:

  def __init__(self):
    load_dotenv()
    self.base_url = os.getenv("API_BASE_URL")

  def request_many(self, endpoint) -> list:
    url = f"{self.base_url}/{endpoint.lstrip('/')}"
    try:
      list_response = requests.get(url)
      if list_response.status_code == 200:
        return list_response.json()
      return []
    except requests.exceptions.RequestException:
      return []

  def request_one(self, endpoint) -> dict:
    url = f"{self.base_url}/{endpoint.lstrip('/')}"
    try:
      single_response = requests.get(url)
      if single_response.status_code == 200:
        return single_response.json()
      return None
    except requests.exceptions.RequestException:
      return None

  def unsafe_request(self, endpoint):
    url = f"{self.base_url}/{endpoint.lstrip('/')}"
    print(f"Unsafe request: {url}")
    response = requests.get(url)
    code = response.status_code
    print(f"Unsafe response: {code}")
    return response.json()


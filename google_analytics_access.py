"""Hello Analytics Reporting API V4."""
import json
import os
import datetime
import requests
import dotenv

from datetime import date
from apiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials

dotenv.load_dotenv(dotenv_path=os.environ.get("SUWA_PIXELA_TOOLS_DOTENV", ".env"))

SCOPES = ['https://www.googleapis.com/auth/analytics.readonly']
KEY_FILE_LOCATION = os.environ.get("SUWA_PIXELA_TOOLS_KEY_FILE_LOCATION")
VIEW_ID = os.environ.get("SUWA_PIXELA_TOOLS_VIEW_ID")
PIXELA_API_URL = os.environ.get("SUWA_PIXELA_TOOLS_PIXELA_URL")
PIXELA_API_TOKEN = os.environ.get("SUWA_PIXELA_TOOLS_PIXELA_TOKEN")

def initialize_analyticsreporting():
  """Initializes an Analytics Reporting API V4 service object.

  Returns:
    An authorized Analytics Reporting API V4 service object.
  """
  credentials = ServiceAccountCredentials.from_json_keyfile_name(
      KEY_FILE_LOCATION, SCOPES)

  # Build the service object.
  analytics = build('analyticsreporting', 'v4', credentials=credentials)

  return analytics

def get_report(analytics, date_):
  """Queries the Analytics Reporting API V4.

  Args:
    analytics: An authorized Analytics Reporting API V4 service object.
  Returns:
    The Analytics Reporting API V4 response.
  """
  return analytics.reports().batchGet(
      body={
        'reportRequests': [
        {
          'viewId': VIEW_ID,
          'dateRanges': [{'startDate': date_.strftime("%Y-%m-%d"), 'endDate': date_.strftime("%Y-%m-%d")}],
          'metrics': [{'expression': 'ga:sessions'}],
          'dimensions': [{'name': 'ga:country'}]
        }]
      }
  ).execute()


def print_response(response):
  """Parses and prints the Analytics Reporting API V4 response.


  Args:
    response: An Analytics Reporting API V4 response.
  """
  for report in response.get('reports', []):
    columnHeader = report.get('columnHeader', {})
    dimensionHeaders = columnHeader.get('dimensions', [])
    metricHeaders = columnHeader.get('metricHeader', {}).get('metricHeaderEntries', [])


    for row in report.get('data', {}).get('rows', []):
      dimensions = row.get('dimensions', [])
      dateRangeValues = row.get('metrics', [])


      for header, dimension in zip(dimensionHeaders, dimensions):
        print(header + ': ' + dimension)


      for i, values in enumerate(dateRangeValues):
        print('Date range: ' + str(i))
        for metricHeader, value in zip(metricHeaders, values.get('values')):
          print(metricHeader.get('name') + ': ' + value)


def main():
  analytics = initialize_analyticsreporting()
  yesterday = date.today() - datetime.timedelta(days=1)
  # yesterday = datetime.date(2020, 2, 24) 　# 日付を指定して手動実行する場合
  response = get_report(analytics, yesterday)
  
  data = {
      "date": yesterday.strftime("%Y%m%d"),
      "quantity": response["reports"][0]["data"]["totals"][0]["values"][0],
  }

  print(json.dumps(data))

  resp = requests.post(
    PIXELA_API_URL,
    data=json.dumps(data),
    headers={
      "Content-Type": "application/json",
      "X-USER-TOKEN": PIXELA_API_TOKEN,
    },
  )

  resp.raise_for_status()

if __name__ == '__main__':
  main()

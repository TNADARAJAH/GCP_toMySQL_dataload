from google.cloud import bigquery
from google.oauth2 import service_account


def get_results():
    credentials = service_account.Credentials.from_service_account_file(r'C:\Users\thine\PycharmProjects\GCP_toMySQL_dataload\GCP_interface\gcp-to-mysql-dataload-5f18477c1bcd.json')

    project_id = 'gcp-to-mysql-dataload'

    client = bigquery.Client(credentials=credentials, project=project_id)

    query_job = client.query("SELECT title,`by` from `bigquery-public-data.hacker_news.full` limit 100")

    results = list(query_job.result())

    return(results)

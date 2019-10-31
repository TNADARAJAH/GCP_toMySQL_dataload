from MySQL_interface import MySQL_connect
from GCP_interface import GCP_connect

if __name__ == "__main__":
    cursor=MySQL_connect.create_MySQLconnection()

    results=GCP_connect.get_results()

    MySQL_connect.insert_results(results,cursor)

    # Added this comment
    # Added 2nd comment
    # added 3rd comment
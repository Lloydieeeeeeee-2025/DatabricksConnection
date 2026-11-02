from databricks import sql
from dotenv import load_dotenv
import os
import pandas as pd

load_dotenv()

connection = sql.connect(server_hostname=os.getenv("DATABRICKS_HOST"),
                         http_path=os.getenv("DATABRICKS_HTTP_PATH"),
                         access_token=os.getenv("DATABRICKS_TOKEN"))

cursor = connection.cursor()

cursor.execute("SELECT * FROM expense_tracker_catalog.expense_tracker_schema.expense_gold")
rows = cursor.fetchall()
columns = [column[0] for column in cursor.description]
df = pd.DataFrame(rows, columns=columns)
print(df)

cursor.close()
connection.close()
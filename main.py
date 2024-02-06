from langchain_google_vertexai import VertexAI
from langchain_core.prompts import PromptTemplate
from google.cloud import bigquery
import pandas as pd

def get_data_from_bigquery(query: str):

    try:    
        client = bigquery.Client()
        query_job = client.query(query) 

        return [ list(row) for row in query_job.result()]
    except Exception as e:
        print(f"Error fetching processed URIs from BigQuery: {e}")
        return []

def get_schema_as_text(table_name,dataset,project_id):

    query = f'''SELECT column_name,data_type FROM `{project_id}.{dataset}.INFORMATION_SCHEMA.COLUMN_FIELD_PATHS` where table_name = "{table_name}"'''
    try:    
        client = bigquery.Client(project = "edplus-dcal-ai")
        query_job = client.query(query) 

        a =  [f"Column Name :{row[0]} and data type {row[1]}" for row in query_job.result()]
    except Exception as e:
        print(f"Error fetching processed URIs from BigQuery: {e}")
        a = []
    
    schema = ",".join(a)
    # print("Schema obtained is ",schema)
    return schema
    
def generate_sql_query(question, context,project_id,dataset_id,table_name):
    
    model = VertexAI(model_name="gemini-pro")
    # Constructing the prompt with schema context
    template = f'''The following is a schema of the table whose table {project_id}.{dataset_id}.{table_name} : {context}. 
    Based on this schema, convert the following user request into a Big query SQL query: {question}.'''

    prompt = PromptTemplate.from_template(template)

    chain = prompt | model

    return chain.invoke({"question": question})

def query_bigquery_from_nlp(user_prompt, table_name,project_id,dataset_id):
    # Get the schema description as context
    print("Fetching schema for model context understanding...")
    schema_context = get_schema_as_text(table_name,dataset_id,project_id)
    
    # Generate SQL query from user prompt
    sql_query = generate_sql_query(user_prompt, schema_context,project_id,dataset_id,table_name)
    print(f"Generated SQL Query:")
    print(sql_query)
    print()
    
    # Fetch data from BigQuery using the generated query
    query_results = get_data_from_bigquery(sql_query)
    
    return query_results

# Fill the table name, dataset_id and project_id of the big query table
TABLE_NAME  = "" 
DATASET_ID = ""
PROJECT_ID = ""

# Enter the natural language prompt
user_prompt = ""

query_results = query_bigquery_from_nlp(user_prompt, TABLE_NAME,PROJECT_ID,DATASET_ID)
df = pd.DataFrame(query_results)
df.to_csv("result.csv")
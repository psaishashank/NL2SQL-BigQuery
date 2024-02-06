# NL2SQL-BigQuery
## Overview
This project aims to bridge the gap between natural language processing and SQL queries through a simple script that converts natural language prompts into BigQuery SQL code. Leveraging the powerful capabilities of the LangChain framework and the Gemini Pro model, this tool simplifies the process of querying databases for users who may not be familiar with SQL syntax. It is designed to run in Vertex AI notebooks, utilizing service accounts with the necessary permissions for seamless integration with BigQuery APIs.

## Prerequisites
A Google Cloud account with access to Vertex AI notebooks and BigQuery.
Properly configured service accounts in Vertex AI notebooks with permissions to access BigQuery.
Setup and Usage
(Note: This script assumes that authentication is handled through service accounts in Vertex AI notebooks. No additional authentication setup is required.)

## Environment Setup 
Ensure you have access to Vertex AI notebooks and that your service account has the necessary permissions to execute BigQuery queries.
Clone the Repository: Clone this repository to your Vertex AI notebook environment.
Running the Script: Navigate to the directory containing the script and execute it. You will be prompted to enter your natural language query, which the script will then convert to SQL and run on BigQuery.
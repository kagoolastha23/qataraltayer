import os
import openai
import dotenv

AZURE_OPENAI_ENDPOINT="https://eu2-openai.openai.azure.com/"
AZURE_OPENAI_API_KEY="3b156f873283471ba2a5ae1c84c5b04b"
AZURE_OPENAI_DEPLOYMENT_ID="gpt-4-turbo128k"
SEARCH_ENDPOINT="https://jfk-search-service-zxc7dbvzyazmw.search.windows.net"
SEARCH_KEY="qd1SUnBfHIUkhpN7vu7CZWQZP62FbeLCLxgVRDIFoyAzSeDIc9aW"
SEARCH_INDEX_NAME="qatarhrbyodin"

use_azure_active_directory = False
if not use_azure_active_directory:
    endpoint ="https://eu2-openai.openai.azure.com/"
    api_key = "3b156f873283471ba2a5ae1c84c5b04b"
    # set the deployment name for the model we want to use
    deployment = "gpt-4-turbo128k"

    client = openai.AzureOpenAI(
        base_url=f"{endpoint}/openai/deployments/{deployment}/extensions",
        api_key=api_key,
        api_version="2023-09-01-preview"
    )

completion = client.chat.completions.create(
    messages=[{"id":"8cb46c3f-5cc0-a8fd-2ff6-5052fc885973","role":"user","content":"hi","date":"2024-03-15T14:11:07.275Z"},{"role":"tool","content":"{\"citations\": [], \"intent\": \"[]\"}","id":"262c5813-9a8e-44fc-9df5-59c1f2c8457e","date":"2024-03-15T14:11:11.573Z"},{"role":"assistant","content":"Hello! How can I assist you today?","id":"262c5813-9a8e-44fc-9df5-59c1f2c8457e","date":"2024-03-15T14:11:11.573Z"},{"id":"47f11576-75f7-4d18-0d04-a53eb7d1dde0","role":"user","content":"What is employee agreement form? ","date":"2024-03-15T14:13:47.384Z"}],                 
    model=deployment,
    extra_body={
        "dataSources": [
            {
                "type": "AzureCognitiveSearch",
                "parameters": {
                    "endpoint": SEARCH_ENDPOINT,
                    "key": SEARCH_KEY,
                    "indexName": SEARCH_INDEX_NAME,
                    "fieldsMapping": {},
                    "queryType": "vector",
                    "inScope": True,
                    "roleInformation":"You are an AI assistant that helps people find information", 
                    "strictness": 3,
                    "topNDocuments": 5,
                    "embeddingDeploymentName": "text-embedding"
                }
            }
        ]
    },
    temperature=0,
    top_p=1,
    max_tokens=800,
    
)

#print(completion)
print(completion.model_dump_json(indent=2))

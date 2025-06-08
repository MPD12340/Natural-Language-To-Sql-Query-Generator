from openai import OpenAI
from src.models.nlsql_model import Book
from dotenv import load_dotenv
from src.services.generate_table_data import get_all_models

load_dotenv()

client = OpenAI()

PROMPT_TEMPLATE = """
**Role:** You are a helpful assistant that converts the natural language into SQL queries.

**Guidelines:**
 - If there is no match for table name then simple return "No Table".
 - Only return sql query and do not add any extra explanation.
 - Examples are only to give an idea and never return any query based on example if not matched from database level too.


 **Examples:**
        Input : Give me a list of 5 people
        Output : SELECT * FROM people



Schema:
{schema}

User: {nl_query}
SQL:
"""


def nl_to_sql_prompt(nl_query: str) -> str:
    schema = get_all_models()
    prompt = PROMPT_TEMPLATE.format(nl_query=nl_query, schema=schema)
    response = client.chat.completions.create(
        model="gpt-4", messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip().strip(";")

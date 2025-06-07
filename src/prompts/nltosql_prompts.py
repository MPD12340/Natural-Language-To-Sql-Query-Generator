from openai import OpenAI
from src.models.nlsql_model import Book
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

PROMPT_TEMPLATE = """
You are a helpful assistant that converts natural language into SQL queries.
Only return SQL. Never add explanation.

Schema:
Table: books
- id (INTEGER)
- title (VARCHAR)
- description (VARCHAR)
- author_id (INTEGER)

User: {nl_query}
SQL:
"""


def nl_to_sql_prompt(nl_query: str) -> str:
    prompt = PROMPT_TEMPLATE.format(nl_query=nl_query)
    response = client.chat.completions.create(
        model="gpt-4", messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip().strip(";")

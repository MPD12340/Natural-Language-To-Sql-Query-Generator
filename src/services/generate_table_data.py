from src.models.nlsql_model import Author, Book
from sqlalchemy import inspect
from src.db.db_connection import engine, Base

inspector = inspect(engine)


def get_all_models():
    schema_lines = []
    for mapper in Base.registry.mappers:
        model_class = mapper.class_
        table_name = getattr(model_class, "__tablename__", None)
        if table_name:
            schema_lines.append(f"Table: {table_name}")
            for col in model_class.__table__.columns:
                schema_lines.append(f"- {col.name} ({col.type})")
            schema_lines.append("")  
    return "\n".join(schema_lines)

from src.models.nlsql_model import Author, Book
from sqlalchemy import inspect
from src.db.db_connection import engine, Base

inspector = inspect(engine)


def get_all_models():
    model_info_list = []

    for mapper in Base.registry.mappers:
        model_class = mapper.class_
        model_name = model_class.__name__
        table_name = getattr(model_class, "__tablename__", None)

        if table_name:
            column_details = [
                f"{col.name} ({col.type})" for col in model_class.__table__.columns
            ]
            info = (
                f"Model: `{model_name}`"
                f"Table: `{table_name}`"
                f"Columns: {', '.join(column_details)}"
            )
            model_info_list.append(info)

    return model_info_list

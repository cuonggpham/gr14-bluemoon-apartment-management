from dotenv import load_dotenv
import os
from sqlalchemy import engine_from_config, pool
from alembic import context
from app.core.db import Base  

load_dotenv()
config = context.config
config.set_main_option("sqlalchemy.url", os.getenv("DB_URL"))
connectable = engine_from_config(
    config.get_section(config.config_ini_section),
    prefix="sqlalchemy.",
    poolclass=pool.NullPool,
)

target_metadata = Base.metadata

def run_migrations_offline():
    url = os.getenv("DB_URL")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
    )
    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online():
    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata
        )
        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
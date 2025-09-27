import os
from alembic.config import Config
from alembic import command
from constants import ALEMBIC_TEMPLATE

def run_migrations():
    alembic_cfg_path = os.path.join(os.path.dirname(__file__), "alembic.ini")

    if not os.path.exists(alembic_cfg_path):
        with open(alembic_cfg_path, "w") as f:
            f.write(ALEMBIC_TEMPLATE)

    alembic_cfg = Config(alembic_cfg_path)
    command.upgrade(alembic_cfg, "head")

if __name__ == "__main__":
    run_migrations()

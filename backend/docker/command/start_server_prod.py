import subprocess
import os

SERVER_PORT = 9001
SERVER_HOST = "0.0.0.0"

SHELL_DIRECTORY = "backend/"

# Check if python is avaliable, using python3 if not.
result_code = subprocess.call("python", shell=True)
PYTHON_COMMAND = "python3" if result_code != 0 else "python"

CMD_MAKE_MIGRATIONS: str = f"{PYTHON_COMMAND} manage.py makemigrations"
CMD_MIGRATE_AUTH: str = f"{PYTHON_COMMAND} manage.py migrate auth"
CMD_MIGRATE: str = f"{PYTHON_COMMAND} manage.py migrate"
CMD_STATIC: str = f"{PYTHON_COMMAND} manage.py collectstatic --noinput"

CMD_LOAD_APIS: str = f"{PYTHON_COMMAND} manage.py loaddata fixtures/apis.json --app vault"
CMD_LOAD_CATEGORIES: str = f"{PYTHON_COMMAND} manage.py loaddata fixtures/categories.json --app vault"

CMD_RUNSERVER: str = f"gunicorn apivault.wsgi -b :{SERVER_PORT}"

os.chdir(SHELL_DIRECTORY)

subprocess.call(CMD_MAKE_MIGRATIONS, shell=True)
subprocess.call(CMD_MIGRATE_AUTH, shell=True)
subprocess.call(CMD_MIGRATE, shell=True)
subprocess.call(CMD_LOAD_CATEGORIES, shell=True)
subprocess.call(CMD_LOAD_APIS, shell=True)

subprocess.call(CMD_STATIC, shell=True)
subprocess.call(CMD_RUNSERVER, shell=True)

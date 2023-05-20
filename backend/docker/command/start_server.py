import subprocess
import os

SERVER_PORT = 9001
SERVER_HOST = "0.0.0.0"

SHELL_DIRECTORY = "backend/"

PYTHON_COMMAND = "python"

CMD_MAKE_MIGRATIONS: str = f"{PYTHON_COMMAND} manage.py makemigrations"
CMD_MIGRATE_AUTH: str = f"{PYTHON_COMMAND} manage.py migrate auth"
CMD_MIGRATE: str = f"{PYTHON_COMMAND} manage.py migrate"
CMD_RUNSERVER: str = f"{PYTHON_COMMAND} manage.py runserver {SERVER_HOST}:{SERVER_PORT}"

# Check if python is avaliable, using python3 if not.
result_code = subprocess.call(PYTHON_COMMAND, shell=True)
if result_code != 0: PYTHON_COMMAND = "python3"

os.chdir(SHELL_DIRECTORY)

subprocess.call(CMD_MAKE_MIGRATIONS, shell=True)
subprocess.call(CMD_MIGRATE_AUTH, shell=True)
subprocess.call(CMD_MIGRATE, shell=True)
subprocess.call(CMD_RUNSERVER, shell=True)

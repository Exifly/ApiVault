import subprocess
import time
import os

print('Starting server...')
time.sleep(25)

SERVER_PORT = 9001
SERVER_HOST = "0.0.0.0"

SHELL_DIRECTORY = "backend/"

# Check if python is avaliable, using python3 if not.
result_code = subprocess.call("python", shell=True)
PYTHON_COMMAND = "python3" if result_code != 0 else "python"

CMD_MAKE_MIGRATIONS: str = f"{PYTHON_COMMAND} manage.py makemigrations"
CMD_MIGRATE_AUTH: str = f"{PYTHON_COMMAND} manage.py migrate auth"
CMD_MIGRATE: str = f"{PYTHON_COMMAND} manage.py migrate"
CMD_LOAD_FIXTURES: str = f"{PYTHON_COMMAND} manage.py loaddata fixtures/vault.json --app vault"
CMD_RUNSERVER: str = f"{PYTHON_COMMAND} manage.py runserver {SERVER_HOST}:{SERVER_PORT}"


os.chdir(SHELL_DIRECTORY)

subprocess.call(CMD_MAKE_MIGRATIONS, shell=True)
subprocess.call(CMD_MIGRATE_AUTH, shell=True)
subprocess.call(CMD_MIGRATE, shell=True)
subprocess.call(CMD_LOAD_FIXTURES, shell=True)
subprocess.call(CMD_RUNSERVER, shell=True)

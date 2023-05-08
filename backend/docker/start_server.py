import subprocess

PS_CD="cd /code"
PS_START_SERVER="python start.py"
PS_START_SERVER_2="python3 start.py"

result_code = subprocess.call(PS_START_SERVER, shell=True)
if result_code != 0:
    print(f"Command {PS_START_SERVER} failed to run.. Trying {PS_START_SERVER_2}")
    subprocess.call(PS_START_SERVER_2, shell=True)

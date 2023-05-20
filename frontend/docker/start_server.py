import subprocess
import os

PS_YARN_INSTALL = "yarn install"
PS_YARN_RUN_DEV = "yarn dev"

os.chdir("frontend/")

subprocess.call(PS_YARN_INSTALL, shell=True)
subprocess.call(PS_YARN_RUN_DEV, shell=True)

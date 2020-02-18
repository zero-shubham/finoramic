import json
import sys
import subprocess

with open("./install.json", "r") as file:
    file_json = json.load(file)
    to_be_installed = file_json["Dependencies"].keys()
    failed_list = []
    for package in to_be_installed:
        version = file_json["Dependencies"][package]
        tmp = f"{package}=={version}"
        try:
            subprocess.check_call(
                [sys.executable, "-m", "pip", "install", tmp])
        except Exception:
            failed_list.append(package)
    if len(failed_list):
        print("Failed to install the following packages: \n")
        [print(p) for p in failed_list]
    else:
        print("success")

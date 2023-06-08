"""
module installs all packages required to run the application.
"""
import subprocess
import sys
import contextlib


def install(package):
    """
    installs the required packages via pip
    :param package: string
    :return: void
    """

    subprocess.call([sys.executable, "-m", "pip", "install", package])


required = []

# read packages from file 'requirements.txt'
try:
    with open("requirements.txt", "r") as file_name:
        packages = file_name.readlines()
        required = [package.strip().lower() for package in packages]
except FileNotFoundError:
    print("[ERROR] The file requirements.txt was not found")


if len(required) > 0:
    ans = input(f"[Input] You are about to install {len(required)} packages, would you like to proceed (y/n): ")

    if ans.lower() == "y":
        for package in required:
            try:
                # Import if the package is already installed
                print(f"[LOG] Looking for {package}")
                with contextlib.redirect_stdout(None):
                    __import__(package)
                print(f"[LOG] {package} is already installed")
            except ImportError:
                print(f"[LOG] {package} not installed")

            try:
                # Install package if import failed
                print(f"[LOG] trying to install {package} via pip")
                try:
                    import pip
                except:
                    print("[EXCEPTION] Pip is not installed\nnPlease install pip before proceeding...")
                    exit()
                print(f"[LOG] Installing {package}")
                install(package)
                with contextlib.redirect_stdout(None):
                    __import__(package)
                print(f"[LOG] {package} has been installed")
            except Exception as e:
                print(f"[ERROR] Could not install {package}, -{e}")
                exit()
    else:
        print("[STOP] Operation terminated by user")

else:
    print("[LOG] No packages are required to install")

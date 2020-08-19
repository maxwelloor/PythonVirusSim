import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
additional_modules = []

build_exe_options = {"includes": additional_modules,
                     "packages": ["pygame", "random", "sys"],
                     "excludes": ['tkinter'],
                     "include_files": ['icon.ico', 'sprites', 'lib']}

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(name="Virus Simulator",
      version="1.2",
      description="Simulate a virus with custom settings for different outcomes each time!",
      options={"build_exe": build_exe_options},
      executables=[Executable(script="PythonVisualVirusSim.py", base=base, icon="icon.ico")])

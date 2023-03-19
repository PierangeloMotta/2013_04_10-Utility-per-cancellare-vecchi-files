# A very simple setup script to create a single executable
#
# hello.py is a very simple "Hello, world" type script which also displays the
# environment in which the script runs
#
# Run the build process by running the command 'python setup.py build'
#
# If everything works well you should find a subdirectory in the build
# subdirectory that contains the files needed to run the script without Python

from cx_Freeze import setup, Executable


build_exe_options = {"include_files": ["delete_old_files.ini"]}

setup(
        name = "delete_old_files",
        version = "0.3",
        description = "Semplice programma per eliminare file idx e pdf",
		options = {"build_exe": build_exe_options},
        executables = [Executable("delete_old_files_003.py")])

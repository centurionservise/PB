from cx_Freeze import setup, Executable
import sys


#PrivatBank
exe = Executable(script="PrivatBank.py", base="Win32GUI", icon="PB images.ico")
buildOptions = dict(excludes = [""], includes =["idna.idnadata","multiprocessing","PyQt5.uic","PyQt5.QtWidgets"], optimize=1)
setup(name = "pb_api",version = "1.0", description = "privat_bank_descr", executables = [exe], options = dict(build_exe = buildOptions))

# python setup.py build
# python setup.py bdist_msi

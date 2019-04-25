# -*- coding: utf-8 -*-
import os
from subprocess import call
from concurrent.futures import ThreadPoolExecutor, as_completed


def primeCoRo(func):
    def initiate(*args, **kwargs):
        cr = func(*args, **kwargs)
        cr.send(None)
        print("Coroutine Primed")
        return cr

    return initiate


@primeCoRo
def convertUIFile():
    path, uiFile, pyFile = '', '', ''
    #     yield
    try:
        while True:
            path, uiFile, pyFile = yield
            command = ["C:\\Python34\\Lib\\site-packages\\PyQt4\\pyuic4",
                       "{}\\{}".format(path, uiFile),
                       "-o",
                       "{}\\{}".format(path, pyFile)]
            call(command, shell=True)
    except GeneratorExit:
        print("Conversions complete.")


def cycleUIFiles(mypath):
    os.chdir("C:\\Python34\\Lib\\site-packages\\PyQt4\\uic")
    print(os.getcwd())
    for (dirpath, dirnames, filenames) in os.walk(mypath):
        for filename in filenames:
            if filename.endswith(".ui"):
                yield dirpath, dirnames, filename


def refreshConversion(fName=''):
    mypath = "Z:\\Csmythe\\ServiceMgmt\\PLSServiceMgmt\\UI"
    files = cycleUIFiles(mypath)
    converter = convertUIFile()
    for dirpath, dirname, uiFile in files:
        if (fName == '') or (fName == uiFile):
            pyFile = uiFile.split(".")[0] + ".py"
            converter.send((mypath, uiFile, pyFile))


def convert_to_py(ui_dir, file_name):

    uic_command = r"pyuic4"
    ui_file = file_name
    py_file = file_name.replace('.ui', '.py')

    command = [uic_command,
               r'{}'.format(ui_file),
               r"-o",
               r'{}'.format(py_file)
               ]

    print(' '.join(command))
    call(' '.join(command), shell=True)
    return ui_file


def convert_ui(ui_file_name = ''):
    ui_dir = r"/home/csmythe/PycharmProjects/Rudy/UI"
    futures = set()
    with ThreadPoolExecutor(max_workers = 15) as exc:

        for file_name in os.listdir(ui_dir):
            if file_name.endswith('.ui') and (file_name == ui_file_name or ui_file_name == ''):
                futures.add(exc.submit(convert_to_py, ui_dir, file_name))

        for future in as_completed(futures):
            result = future.result()
            print(result)


if __name__ == "__main__":
    # refreshConversion(input("Convert FileName (leave blank to convert all): "))
    os.chdir(r'/home/csmythe/PycharmProjects/Rudy/UI')
    convert_ui('')

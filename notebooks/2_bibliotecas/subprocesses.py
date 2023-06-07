import subprocess

def install_libraries(libs):
    libs_list = libs.split()
    for lib in libs_list:
        subprocess.call(['pip', 'install', lib])


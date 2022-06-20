# Computação Paralela e Distribuída 2020/2021
# Aluno: Uliana Pyrohovska
# Número: 202101294
# Turma: 2ºL_EI-SW-05
#############################################
import platform
import subprocess


def get_processor_info():
    if platform.system() == "Windows":
        return platform.processor()
    elif platform.system() == "Darwin":
        return subprocess.check_output(['/usr/sbin/sysctl', "-n", "machdep.cpu.brand_string"]).strip()
    elif platform.system() == "Linux":
        command = "cat /proc/cpuinfo | grep name | cut -d ' ' -f 3-8"
    return str(subprocess.check_output(command, shell=True)).strip("b'\\n")
    return ""


if __name__ == '__main__':
    print(get_processor_info())

# A - The import statement gains access to the code from another module. It combines
# two operations which include searching for the exact module and binding the result of
# that search to a name in the local scope.

# B - Using imports can make you more productive, allowing you to reuse code
# while keeping your projects maintainable

# C - str() converts value to the string format

# D - strip() removes any leading spaces in the end and in the beginning of the string


import subprocess
from shutil import get_terminal_size

def print_run(string, symbol="-", color_code="[37m"):
    xx = get_terminal_size((80, 20))
    column_len = int([str(xx).split("=")[1]][0].split(',')[0])

    print(f"\033{color_code}{string.center(column_len, symbol)}\033[0m")



def qbasic_exec():
    cmd = f"{file_name_no_extc_with_loc}"
    if output_location != "None":
        cmd = f"{output_location}{file_name_no_extc}"
    cmd = "".join(cmd).split()

    try:
        print_run("RUNNING PROGRAM", " ")
        print_run("-", "-")
        subprocess.run(cmd)
        print("\n\n")
    except FileNotFoundError:
        print(f"compiled file, {file_name_no_extc_with_loc}, \033[91mnot found")


def qbasic_build():
    cmd = f"/home/lazy/codeDNA/confiFILES/programmingLANGUAGE/qb64/qb64 -x {file_name_with_location} -o {file_name_no_extc}"
    if output_location != "None":
        cmd = f"/home/lazy/codeDNA/confiFILES/programmingLANGUAGE/qb64/qb64 -x {file_name_with_location} -o {output_location}{file_name_no_extc}"
    cmd = "".join(cmd).split()

    status = subprocess.run(cmd)

    if  status.returncode == 0:
        print_run("-", "-")
        print_run("✔ Compilation Successful", " ", "[32m")
        print_run("-", "-")
    if status.returncode != 0:
        print_run("-", "-")
        print_run("X Compilation Failed", " ", "[31m")
        print_run("-", "-")
        exit(1)


def qbasic_buildexec():
    qbasic_build()
    qbasic_exec()


def qbasic_run(program_name, conditions, output_loc="None"):
    build, run, build_run = conditions
    global file_name, file_name_no_extc, output_location, file_name_with_location, file_name_no_extc_with_loc
    file_name = program_name.split("/")[-1]
    file_name_no_extc = file_name.split(".")[0]     # getting rid of extension
    file_name_no_extc_with_loc = program_name.split(".")[0]
    file_name_with_location = program_name
    output_location = str(output_loc)

    if run == 1 and build == 0:
        qbasic_exec()
    if run == 1 and build == 1:
        qbasic_buildexec()
    if build == 1 and run == 0:
        qbasic_build()
    if build_run == 1:
        qbasic_buildexec()


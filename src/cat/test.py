# Tests writen by Junkratc

# These testes do not work with long options for GNU and with situation when empty name file trowing in programm
# (like:" cat [flags] ") or writen "-" insted of file name 
import os
import filecmp

# If u dont want to test some flags or files u can just delete those flags/files from massive flags/files 
# Or u can add your own test file
files = ["TestFile1", "TestFile2", "TestFile3", "test.py"]
flags = ["-b", "-e", "-n", "-s", "-t",]

test_counter = 1
successfull_counter = 0
failed_counter = 0

def print_result(result, flag, file):
    global test_counter
    global successfull_counter
    global failed_counter
    if result == 1:
        successfull_counter += 1
        print('\033[0m', end = "")
        print(test_counter, end = "/")
        print('\033[92m', end = "")
        print(successfull_counter, end= "/")
        print('\033[91m', end = "")
        print(failed_counter, end= " ")
        print('\033[92m', end = "")
        print('Success', '\033[0m', './s21_cat',flag,file)
    else:
        failed_counter += 1
        print('\033[0m', end = "")
        print(test_counter, end = "/")
        print('\033[92m', end = "")
        print(successfull_counter, end= "/")
        print('\033[91m', end = "")
        print(failed_counter, end= " ")
        print('Fail', '\033[0m', './s21_cat',flag,file)
    # os.system("valgrind --leak-check=full --show-leak-kinds=all --track-origins=yes ./s21_cat {} {}".format(flag, file))

    test_counter += 1

def no_file(): 
    os.system("cat no_file > test_func_python")
    os.system("./s21_cat no_file > test_func_python_2")
    f1 = "test_func_python"
    f2 = "test_func_python_2"
    print_result(filecmp.cmp(f1, f2, shallow=False), "", "no_file")

def zero_flag():
    for j in range(len(files)):
        os.system("cat {}> test_func_python".format(files[j]))
        os.system("./s21_cat {}> test_func_python_2".format(files[j]))
        f1 = "test_func_python"
        f2 = "test_func_python_2"
        print_result(filecmp.cmp(f1, f2, shallow=False), "", files[j])

def one_flag():
    for i in range(len(flags)):
        for j in range(len(files)):
            os.system("cat {} {}> test_func_python".format(flags[i],files[j]))
            os.system("./s21_cat {} {}> test_func_python_2".format(flags[i],files[j]))
            f1 = "test_func_python"
            f2 = "test_func_python_2"
            print_result(filecmp.cmp(f1, f2, shallow=False), flags[i], files[j])

def two_flags():
    i = 0
    while i < len(flags) - 1:
        k = i + 1
        while k < len(flags):
            for j in range(len(files)):
                os.system("cat {} {} {}> test_func_python".format(flags[i], flags[k], files[j]))
                os.system("./s21_cat {} {} {}> test_func_python_2".format(flags[i], flags[k], files[j]))
                f1 = "test_func_python"
                f2 = "test_func_python_2"
                flags_print = "{} {}".format(flags[i], flags[k])
                print_result(filecmp.cmp(f1, f2, shallow=False),flags_print, files[j])
            k += 1
        i += 1

def three_flags():
    i = 0
    while i < len(flags) - 2:
        k = i + 1
        while k < len(flags) - 1:
            a = k + 1
            while a < len(flags):
                for j in range(len(files)):
                    os.system("cat {} {} {} {}> test_func_python".format(flags[i], flags[k], flags[a], files[j]))
                    os.system("./s21_cat {} {} {} {}> test_func_python_2".format(flags[i], flags[k], flags[a], files[j]))
                    f1 = "test_func_python"
                    f2 = "test_func_python_2"
                    flags_print = "{} {} {}".format(flags[i], flags[k], flags[a])
                    print_result(filecmp.cmp(f1, f2, shallow=False),flags_print, files[j])
                a += 1
            k += 1
        i += 1

def four_flags():
    i = 0
    while i < len(flags) - 3:
        k = i + 1
        while k < len(flags) - 2:
            a = k + 1
            while a < len(flags)-1:
                h = a + 1
                while h < len(flags):
                    for j in range(len(files)):
                        os.system("cat {} {} {} {} {}> test_func_python".format(flags[i], flags[k], flags[a], flags[h], files[j]))
                        os.system("./s21_cat {} {} {} {} {}> test_func_python_2".format(flags[i], flags[k], flags[a], flags[h], files[j]))
                        f1 = "test_func_python"
                        f2 = "test_func_python_2"
                        flags_print = "{} {} {} {}".format(flags[i], flags[k], flags[a], flags[h])
                        print_result(filecmp.cmp(f1, f2, shallow=False),flags_print, files[j])
                    h += 1
                a += 1
            k += 1
        i += 1

def not_existed_flag():
    os.system("cat -z {}> test_func_python".format(files[0]))
    os.system("./s21_cat -z {}> test_func_python_2".format(files[0]))
    f1 = "test_func_python"
    f2 = "test_func_python_2"
    print_result(filecmp.cmp(f1, f2, shallow=False), "-z", files[0])

# U can delete some func from here if u dont want test some cases

zero_flag()
not_existed_flag()
no_file()
one_flag()
two_flags()
three_flags()
four_flags()

os.remove("test_func_python")
os.remove("test_func_python_2")

from menu import show_menu
from student_info import *

def main():
    L = read_from_file(filename='si.txt')
    while True:
        from menu import show_menu
        show_menu()
        s = input("请选择")
        if s == 'q':
            break
        elif s == '1':
            L += input_student()
        elif s == '2':
            output_student(L)
        elif s == '3':
            del_student(L)
        elif s == '4':
            alter_student(L)
        elif s == '5':
            s = score_high_student(L)
            output_student(s)
        elif s == '6':
            s = score_di_student(L)
            output_student(s)
        elif s == '7':
            s = age_high_student(L)
            output_student(s)
        elif s == '8':
            s = age_di_student(L)
            output_student(s)
        elif s == '9':
            save_to_file(L)
        elif s == '10':
            L = read_from_file()

main()

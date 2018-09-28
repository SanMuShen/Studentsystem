from student import Student

#　查找中文字符个数 
def get_chinese_char_count(n):
    i = 0
    for x in n:
        if ord(x) > 127:
            i += 1
    return i
# 定义添加学生信息
def input_student():
    L = []  # 创建一个新的列表，用此列表准备保存学生信息
    # 录入学生信息
    while True:
        n = input("请输入姓名: ")
        if not n:
            break
        try:
            a = int(input("请输入年龄: "))
            s = int(input('请输入成绩: '))
        except:
            print("您的输入有错，请新输入...")
            continue
        L.append(Student(n, a, s))
    return L


# 定义显示学生信息
def output_student(L):        
    print('+'+'-'*(20)+'+'+'-'*10+'+'+'-'*10+'+')
    print('|'+'name'.center(20)+"|"+'age'.center(10)+"|"+'score'.center(10)+"|")
    print('+'+'-'*(20)+'+'+'-'*10+'+'+'-'*10+'+')
    for d in L:
        n,a,s=d._Student__get_info()
        str_chinese = get_chinese_char_count(n)

        print('|'+n.center(20-str_chinese)+"|"+str(a).center(10)+"|"+str(s).center(10)+"|")
    print('+'+'-'*(20)+'+'+'-'*10+'+'+'-'*10+'+')

# 定义删除学生信息
def del_student(L):
    y = input("请输入要删除的学生信息：")
    for x in L:
        n,a,s=x._Student__get_info()
        if n == y:
            L.remove(x)
    return L 

# 定义修改学生信息
def alter_student(L):
    y = input('请输入要修改的姓名')
    for x in L:
        n,a,s=x._Student__get_info()
        if n == y:
            n0 = input('请输入修改后的名字')
            x._Student__set_name(n0)
            n1 = int(input("请输入修改后成绩"))
            x._Student__set_score(n1)
            n2 = int(input('请输入修改后的年龄'))
            x._Student__set_age(n2)
    return L

# 定义学生成绩按照成绩高-低来排名
def score_high_student(L):
    s = sorted(L,key=lambda L:L._Student__get_score(),reverse=True)
    return s
# 定义学生成绩按照成绩低-高来排名   
def score_di_student(L):
    s = sorted(L,key=lambda L:L._Student__get_score(),reverse=False)
    return s
# 定义学生信息按照年龄高-低来排名
def age_high_student(L):
    s = sorted(L,key=lambda L:L._Student__get_age(),reverse=True)
    return s
# 定义学生信息按照年龄低-高来排名
def age_di_student(L):
    s = sorted(L,key=lambda L:L._Student__get_age(),reverse=False)
    return s

# 定义保存信息到文件
def save_to_file(L,filename='si.txt'):
    try:
        f = open(filename,'w')
        for stu in L:
            stu._Student__save(f)

        f.close()
        print('文件保存成功')
    except OSError:
        print('写入信息失败')

# 从文件中读取数据
def read_from_file(filename='si.txt'):
    L = []
    try:
        f = open(filename)
        for x in f:
            n,a,s = x.strip().split(',')
            a = int(a)
            s = int(s)

            L.append(Student(n, a, s))

        f.close()
    except OSError:
        print("读取文件失败")

    return L

class_info = []


def print_menu():
    print("------------------")
    print("旺座管理系统 V1.0")
    print("1：添加旺座")
    print("2：删除旺座")
    print("3：修改旺座")
    print("4：查询旺座")
    print("5：显示所有旺座")
    print("6：退出系统")
    print("------------------")


def add_student():
    print("欢迎使用旺座管理系统")
    # 声明一个全局变量
    global class_info

    name = input("输入旺座的姓名：")
    age = input("请输入旺座的年龄：")
    score = input("请输入旺座的分数：")
    # [{}.{}]

    for s in class_info:
        if s["name"] == name:
            print("该旺座已拉清单")
            # break
            return
    student = {
        "name": name,
        "age": age,
        "score": score
    }
    class_info.append(student)
    print("添加成功")
    print(class_info)


def del_student():
    print("欢迎使用删除功能")
    global class_info
    name = input("请输入删除的旺座姓名：")
    for s in class_info:
        if s["name"] == name:
            class_info.remove(s)
            print(f"删除{name}旺座成功")
            return
    print(f"您输入的旺座{name}不存在")


def modfy_student():
    global class_info
    name = input("请输入修改的旺座姓名")
    for s in class_info:
        if s["name"] == name:
            s["name"] = input("请输入修改后的旺座姓名")
            s["age"] = input("请输入修改后的旺座年龄")
            s["score"] = input("请输入修改后的旺座分数")
            print("修改成功")


def search_student():
    global class_info
    name = input("请输入需要查询的旺座姓名：")
    for s in class_info:
        if s["name"] == name:
            #print("姓名：%s,年龄:%s,分数:%s"%(s["name"], s["age"], s["score"]))
            print(f"姓名：{s['name']},年龄：{s['age']},分数:{s['score']}")
def show_student():
    print("姓名--年龄--分数")
    for s in class_info:
        print(s["name"], s["age"], s["score"])
        return
    print("您输入的学生信息不存在")

def main():
    """实现主要的业务逻辑"""
    while True:
        print_menu()
        choose = int(input("请输入你的功能："))

        if choose == 1:
            add_student()
        elif choose == 2:
            del_student()
        elif choose == 3:
            modfy_student()
        elif choose == 4:
            search_student()
        elif choose == 5:
            show_student()
        elif choose == 6:
            print("退出系统")
            break


if __name__ == '__main__':
    main()

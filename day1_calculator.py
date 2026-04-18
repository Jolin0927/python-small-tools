#定义函数加法
def add(a,b):
    return a + b
# 定义减法函数
def sub(a,b):
    return a - b
# 定义乘法函数
def mul(a,b):
    return a * b
# 定义除法函数
def div(a,b):
    if b == 0:
        print("除数不能为零")
        return None
    return a // b
# 定义乘方函数
def power(a,b):
    return a ** b
#定义求余数函数
def comple(a,b):
    return a % b
#定义菜单函数，负责打印功能选项
def show_menu():
    print("\n=======简易计算器=======")
    print("1.加法")
    print("2.减法")
    print("3.乘法")
    print("4.除法")
    print("5.乘方")
    print("6.求余")
    print("0.退出程序")
    print("=========================")
#获取有效数字的函数，防止输入字母，符号导致程序崩溃
def get_number(prompt):
    # 循环直到用户输入正确数字
    while True:
        try:
            # 尝试将输入转为整数数
            return int(input(prompt))
        except ValueError:
            # 转换失败则提示重新输入
            print("输入不是有效数字，请重新输入！")
# 主函数，程序入口
def main():
    # 主循环，保证程序可以一直运行
    while True:
        # 显示菜单
        show_menu()
        # 获取用户选择，并去除首尾空格（防止不小心输入空格）
        choice = input("请选择功能：").strip()
        # 如果输入0，退出循环，结束程序
        if choice == "0":
            print("程序已结束")
            break
        # 判断输入是否有效
        if choice not in ["1","2","3","4","5","6"]:
            print("无效选项，请输入0 - 6之间的数字")
            continue
        # 获取两个有效数字
        num1 = get_number("请输入第一个数字：")
        num2 = get_number("请输入第二个数字：")
        # 根据用户选择执行对应运算
        if choice == "1":
            print(f"结果:{num1} + {num2} = {add(num1,num2)}")
        elif choice == "2":
            print(f"结果:{num1} - {num2} = {sub(num1,num2)}")
        elif choice == "3":
            print(f"结果:{num1} * {num2} = {mul(num1,num2)}")
        elif choice == "4":
            res = div(num1,num2)
            if res is not None:
                print(f"结果:{num1} / {num2} = {res}")
        elif choice == "5":
            print(f"结果:{num1} ** {num2} = {power(num1,num2)}")
        elif choice == "6":
            print(f"结果:{num1} % {num2} = {comple(num1,num2)}")
# 程序入口
if __name__ == "__main__":
    main()
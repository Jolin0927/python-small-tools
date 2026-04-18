#导入json模块：用于把数据保存到文件、从文件读取数据
import json
#导入os模块：用于判断文件是否存在
import os
#定义数据保存的文件名（全局常量，大写是Python规范）
ACCOUNT_FILE = "account.json"
def load_data():
    """
    从文件加载账本数据
    如果文件不存在/损坏，返回空列表，保证程序不崩溃
    """
    #如果文件不存在，直接返回空列表篇
    if not os.path.exists(ACCOUNT_FILE):
        return []
    try:
        #以读模式打开文件，编码utf-8防止中文乱码
        with open(ACCOUNT_FILE,"r",encoding="utf-8") as f:
            #把五年间里的json字符串转成Python列表/字典
            return json.load(f)
    except:
        #文件损坏时返回空列表
        return []
def save_data(data):
    """
    将账本数据写入文件，实现持久化
    ensure_ascii=False:让中文正常显示
    indent=2：让json文件排版好看，方便查看
    """
    with open(ACCOUNT_FILE,"w",encoding="utf-8") as f:
        json.dump(data,f,ensure_ascii=False,indent=2)
def add_record(records,typ,amount,desc):
    """
    添加一条收支记录到列表中
    :param records: 总的记录列表
    :param typ: 类型，收入/支出
    :param amount: 金额
    :param desc:备注说明
    """
    #构造一条记录字典
    record = {
        "类型":typ,
        "金额":amount,
        "备注":desc
    }
    #把新记录加入总列表
    records.append(record)
    #提示用户添加成功
    print(f"添加{typ}成功：{amount}元{desc}")
def show_records(records):
    """展示所有收支记录"""
    #如果没有记录，直接提示
    if not records:
        print("暂无收支记录")
        return
    #打印标题
    print("\n=====收支记录=====")
    #遍历记录，带序号
    for i,r in enumerate(records,1):
        print(f"{i},{r['类型']}|{r['金额']}元|{r['备注']}")
    print("=====================")
def calc_balance(records):
    """
    统计总收入、总支出、结余
    遍历所有记录，分别累加
    """
    total_income = 0 #总收入
    total_expense = 0 #总支出
    for r in records:
        if r["类型"] == "收入":
            total_income += r["金额"]
        elif r["类型"] == "支出":
            total_expense += r["金额"]
    #结余 = 收入 - 支出
    balance = total_income - total_expense
    #打印统计结果
    print("\n统计结果")
    print(f"总收入：{total_income}元")
    print(f"总支出：{total_expense}元")
    print(f"当前结余：{balance}元")
    return balance
def main():
    """主函数：程序入口，负责菜单循环"""
    #程序启动时先加载历史数据
    records = load_data()
    print("===Day5 个人命令行账本===")
    #死循环，实现菜单一直显示
    while True:
        #打印菜单
        print("\n1.新增收入")
        print("2.新增支出")
        print("3.查看记录")
        print("4.统计结余")
        print("0.退出并保持")
        try:
            #获取用户输入并去掉空格
            choice = input("\n请选择操作：").strip()
            #0 退出并保存
            if choice == "0":
                save_data(records)
                print("数据已保存，程序退出")
                break
            #1 添加收入
            elif choice == "1":
                #float转为小数，支持如10.5元
                amount = float(input("请输入收入金额："))
                desc = input("请输入备注（如工资、兼职）：")
                add_record(records,"收入",amount,desc)
            #2 添加支出
            elif choice == "2":
                amount = float(input("请输入支出金额："))
                desc = input("请输入备注（如工资、兼职）：")
                add_record(records,"支出",amount,desc)
            #3 查看所有记录
            elif choice == "3":
                show_records(records)
            #4 统计结余
            elif choice == "4":
                calc_balance(records)
            #无效选项
            else:
                print("无效选项，请输入0~4之间的数字")
        #处理输入非数字的情况（比如输了abc）
        except ValueError:
            print("输入错误，金额必须是数字")
        #其他未知错误
        except Exception as e:
            print(f"程序出错：{e}")
#Python程序入口规范写法
#只有直接运行这个文件时，才执行main()
if __name__ == "__main__":
    main()
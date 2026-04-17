import json
import os
#1.定义文件路径（和代码同目录，数据会存在这个文件里）
TODO_FILE = "todo_list.json"
def load_tasks():
    """
    从JSON文件加载任务
    用到：open()读文件、json.load()反序列化
    """
    #如果文件不存在，返回空列表
    if not os.path.exists(TODO_FILE):
        return []
    #with 上下文管理器，自动关闭文件，更安全
    with open(TODO_FILE,"r",encoding="utf-8") as f:
        tasks = json.load(f)#json.load():把文件里的JSON字符串转成Python列表/字典
    return tasks
def save_tasks(tasks):
    """
    把任务保存到JSON文件
    用到：open()写文件、json.dump()序列化
    """
    with open(TODO_FILE,"w",encoding="utf-8") as f:
        #json.dump():把PYthon列表/字典转成JSON字符串，写入文件
        #ensure——asci=Falss防止中文乱码，indent=2让文件格式更容易读
        json.dump(tasks,f,ensure_ascii=False,indent=2)
def show_tasks(task):
    """显示所有任务"""
    if not task:
        print("当前没有任务")
        return
    print("\n 你的待办清单：")
    for i,task in enumerate(task,1):
        status = "已完成" if task["done"] else "未完成"
        print(f"{i},{task['content']}[{status}]")
    print("-"*30)
def add_task(tasks):
    """添加新任务"""
    content = input("请输入任务内容：").strip()
    if content:
        tasks.append({"content":content,"done":False})
        print(f"已添加任务：{content}")
def mark_done(tasks):
    """标记任务已完成"""
    show_tasks(tasks)
    if not tasks:
        return
    try:
        idx = int(input("请输入要标记完成的任务编号：")) - 1
        if 0 <= idx < len(tasks):
            tasks[idx]['done'] = True
            print(f"已标记任务 {tasks[idx]['content']} 为完成！")
        else:
            print("编号无效")
    except ValueError:
        print("请输入有效的数字！")
def delete_task(tasks):
    """删除任务"""
    show_tasks(tasks)
    if not tasks:
        return
    try:
        idx = int(input("请输入要删除的任务编号：")) - 1
        if 0 <= idx < len(tasks):
            deleted = tasks.pop(idx)
            print(f"已删除任务：{deleted['content']}")
        else:
            print("编号无效")
    except ValueError:
        print("请输入有效的数字")
def main():
    print("Day2 文件持久化TODO工具===")
    #启动时加载任务
    tasks = load_tasks()
    while True:
        print("\n请选择操作：")
        print("1.查看所有任务")
        print("2.添加新任务")
        print("3.标记任务已完成")
        print("4.删除任务")
        print("5.退出程序")
        choice = input("请输入选项(1-5):").strip()
        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_done(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            #退出前保存任务
            save_tasks(tasks)
            print("任务已保存，再见")
            break
        else:
            print("无效选项，请输入1-5之间的数字")
if __name__ == "__main__":
    main()
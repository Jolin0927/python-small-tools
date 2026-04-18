from day3_storage import load_tasks,save_tasks


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
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
        #json.dump():把Python列表/字典转成JSON字符串，写入文件
        #ensure——asci=False防止中文乱码，indent=2让文件格式更容易读
        json.dump(tasks,f,ensure_ascii=False,indent=2)
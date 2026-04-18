from day3_storage import load_tasks,save_tasks
from day3_todo import show_tasks,add_task,mark_done,delete_task
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
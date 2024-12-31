# from typing import List
# import sys
#
# class WorkFlow:
#     def __init__(self, tasks: List[str]):
#         self.task_order = list()
#         self.task_to_children = dict()
#         self.task_to_parents = dict()
#         self.tasks_to_skip = set()
#         self.tasks_to_execute = set()
#         self.final_task = list()
#
#         self.execute_tasks = set()
#         self.skip_tasks = set()
#
#         # 获取输入数据
#         data = tasks
#
#         # 第一行是工作流中的任务顺序
#         self.task_order = data[0].split()
#
#         # 第二行是子任务关系数量 N
#         N = int(data[1])
#
#         # 解析任务的子任务关系
#         line_idx = 2  # 从第三行开始读取子任务关系
#         for _ in range(N):
#             line = data[line_idx].split()
#             parent = line[0]
#             children = line[1:]
#             if parent not in self.task_to_children:
#                 self.task_to_children[parent] = []
#             self.task_to_children[parent] = children
#             for child in children:
#                 if child not in self.task_to_parents:
#                     self.task_to_parents[child] = []
#                 self.task_to_parents[child].append(parent)
#             line_idx += 1
#
#         # 读取指定执行的任务
#         self.execute_tasks = set(data[line_idx].split()) \
#             if line_idx < len(data) and data[line_idx].strip() else set()
#         line_idx += 1
#
#         # 读取指定跳过的任务
#         self.skip_tasks = set(data[line_idx].split()) \
#             if line_idx < len(data) else set()
#
#         # 确定哪些任务需要执行
#         self.tasks_to_execute = set(self.execute_tasks) \
#             if len(set(self.execute_tasks)) != 0 else set(self.task_order)
#         self.task_execute()
#         # for task in execute_tasks:
#         #     # 如果任务被执行了，任务的所有父任务也需要执行
#         #     self.tasks_to_execute.update(task_to_parents[task])
#
#     def task_execute(self):
#         # 使用一个临时集合来存储需要添加的任务
#         tasks_to_add = set()
#
#         for task in list(self.tasks_to_execute):  # 将集合转换为列表以避免迭代时修改集合
#             if (task in self.task_to_parents and
#                     not set(self.task_to_parents[task]).issubset(self.tasks_to_execute)):
#                 tasks_to_add.update(self.task_to_parents[task])
#
#         # for task in list(self.tasks_to_execute):  # 将集合转换为列表以避免迭代时修改集合
#         #     if (task in self.task_to_children and
#         #             not set(self.task_to_children[task]).issubset(self.tasks_to_execute)):
#         #         tasks_to_add.update(self.task_to_children[task])
#
#         # 更新 self.tasks_to_execute
#         self.tasks_to_execute.update(tasks_to_add)
#
#         # 如果有新的任务被添加，递归调用 task_execute
#         if tasks_to_add:
#             self.task_execute()
#
#     def task_skip(self):
#         tasks_to_add = set()
#
#         for task in list(self.tasks_to_skip):  # 将集合转换为列表以避免迭代时修改集合
#             if (task in self.task_to_children and
#                     not set(self.task_to_children[task]).issubset(self.tasks_to_skip)):
#                 tasks_to_add.update(self.task_to_children[task])
#
#         # 更新 self.tasks_to_skip
#         self.tasks_to_skip.update(tasks_to_add)
#
#         # 如果有新的任务被添加，递归调用 task_skip
#         if tasks_to_add:
#             self.task_skip()
#
#     def final_execute(self, task: str):
#         if task in self.task_to_children and task not in self.skip_tasks:
#             for child in self.task_to_children[task]:
#                 # if ((child not in self.tasks_to_skip) or
#                 #         child in self.execute_tasks):
#                 if (child not in self.skip_tasks):
#                     self.final_task.append(child)
#                     self.final_execute(child)
#
#     def solve_workflow(self):
#         # 最终执行的任务是执行任务减去跳过任务
#         # self.final_tasks = []
#         # rule 3
#         for task in self.task_order:
#             # if ((task not in self.tasks_to_skip) or
#             #             task in self.execute_tasks):
#             if (task not in self.skip_tasks and
#                     task in self.tasks_to_execute):
#                 self.final_task.append(task)
#                 self.final_execute(task)
#         # rule 4
#         # 确定哪些任务需要跳过
#         # self.tasks_to_skip = set(self.skip_tasks) & set(self.final_task)
#         # # for task in skip_tasks:
#         # #     # 如果任务被跳过了，任务的所有子任务也需要跳过
#         # #     self.tasks_to_skip.update(task_to_children[task])
#         # self.task_skip()
#         # final_task_temp = self.final_task.copy()
#         # for task in self.final_task:
#         #     if task in self.tasks_to_skip:
#         #         final_task_temp.remove(task)
#
#         # 输出最终任务执行顺序
#         print(" ".join(self.final_task))
#
# if __name__ == "__main__":
#     test_cases = [
#         { # 1
#             "input": [
#                 "A B C",
#                 "2",
#                 "A D",
#                 "D E",
#                 "B E",
#             ],
#             "expected_output": "D E B"
#         },
#         { # 2
#             "input": [
#                 "A B C D",
#                 "3",
#                 "A B",
#                 "B C",
#                 "C D",
#                 "D",  # 指定执行任务
#                 "",  # 没有跳过任务
#             ],
#             "expected_output": "A B C D"
#         },
#         { # 3
#             "input": [
#                 "A B C D",
#                 "3",
#                 "A B",
#                 "B C",
#                 "C D",
#                 "",  # 没有指定执行任务
#                 "A",  # 跳过任务 A
#             ],
#             "expected_output": ""
#         },
#         { # 4
#             "input": [
#                 "A B C D E F",
#                 "4",
#                 "A B",
#                 "B C D",
#                 "C E",
#                 "D F",
#                 "C F",  # 指定执行任务
#                 "B",  # 跳过任务
#             ],
#             "expected_output": "A C F"
#         },
#         { # 5
#             "input": [
#                 "A B C D",
#                 "0",  # 没有子任务关系
#                 "B",  # 指定执行任务
#                 "C",  # 跳过任务
#             ],
#             "expected_output": "B"
#         },
#         { # 6
#             "input": [
#                 "A B C D",
#                 "2",
#                 "A B",
#                 "C D",
#             ],
#             "expected_output": "A B C D"
#         },
#         { # 7
#             "input": [
#                 "A B C D E F G H",
#                 "5",
#                 "A B C",
#                 "B D",
#                 "C E F",
#                 "D G",
#                 "F H",
#                 "C D",  # 指定执行任务
#                 "B",  # 指定跳过任务
#             ],
#             "expected_output": "A C E F H D G"
#         },
#         { # 8
#             "input": [
#                 "A B C D",
#                 "1",
#                 "A B",
#                 "A",  # 指定执行任务
#                 "A",  # 指定跳过任务
#             ],
#             "expected_output": ""
#         },
#         { # 9
#             "input": [
#                 "A B C",
#                 "2",
#                 "A B",
#                 "B C",
#                 "A",  # 指定执行任务
#                 "",  # 没有跳过任务
#             ],
#             "expected_output": "A B C"
#         },
#         { # 10
#             "input": [
#                 "A B C D",
#                 "3",
#                 "A B",
#                 "B C",
#                 "C D",
#                 "",  # 没有指定执行任务
#                 "C",  # 指定跳过任务
#             ],
#             "expected_output": "A B"
#         },
#         { # 11
#             "input": [
#                 "A B C D E F G H I",
#                 "7",
#                 "A B C",
#                 "B D E",
#                 "C F G",
#                 "D H",
#                 "E I",
#                 "G H",
#                 "F I",
#                 "A",  # 指定执行任务
#                 "",  # 没有指定跳过任务
#             ],
#             "expected_output": "A B D H E I C F G"
#         },
#         { # 12
#             "input": [
#                 "A B C D E F",
#                 "4",
#                 "A B",
#                 "B C D",
#                 "C E",
#                 "D F",
#                 "B C",  # 指定执行任务
#                 "D",  # 指定跳过任务
#             ],
#             "expected_output": "A B C E"
#         },
#         { # 13
#             "input": [
#                 "A B C D E F G",
#                 "6",
#                 "A B C",
#                 "B D",
#                 "C E",
#                 "E F",
#                 "F G",
#                 "D G",
#                 "",  # 没有指定执行任务
#                 "",  # 没有指定跳过任务
#             ],
#             "expected_output": "A B D G C E F"
#         },
#         { # 14
#             "input": [
#                 "A B C D",
#                 "3",
#                 "A B",
#                 "B C",
#                 "C D",
#                 "",  # 没有指定执行任务
#                 "A",  # 指定跳过任务
#             ],
#             "expected_output": ""
#         },
#         { # 15
#             "input": [
#                 "A B C D E F G H I",
#                 "6",
#                 "A B C",
#                 "B D E",
#                 "C F G",
#                 "E H",
#                 "F I",
#                 "H I",
#                 "B E G",  # 指定执行任务
#                 "C F",  # 指定跳过任务
#             ],
#             "expected_output": "A B D E H G"
#         },
#         { # 16
#             "input": [
#                 "A B C D E F",
#                 "5",
#                 "A B",
#                 "B C",
#                 "C D",
#                 "D E",
#                 "E F",
#                 "F",  # 指定执行任务
#                 "A",  # 指定跳过任务
#             ],
#             "expected_output": "F"
#         },
#         { # 17
#             "input": [
#                 "A B C D E F G H",
#                 "7",
#                 "A B C",
#                 "B D",
#                 "C E",
#                 "D F",
#                 "E G",
#                 "F H",
#                 "G H",
#                 "B C E",  # 指定执行任务
#                 "D F",  # 指定跳过任务
#             ],
#             "expected_output": "A B C E G H"
#         },
#         { # 18
#             "input": [
#                 "A B C D E F G H",
#                 "6",
#                 "A B C",
#                 "B D E",
#                 "C F",
#                 "D G",
#                 "E H",
#                 "F G",
#                 "H",  # 指定执行任务
#                 "A",  # 指定跳过任务
#             ],
#             "expected_output": "H"
#         },
#         { # 19
#             "input": [
#                 "A B C D E F G",
#                 "4",
#                 "A B",
#                 "B C",
#                 "C D E",
#                 "D F G",
#                 "A C",  # 指定执行任务
#                 "B D",  # 指定跳过任务
#             ],
#             "expected_output": "A C E"
#         },
#         { # 20
#             "input": [
#                 "A B C D",
#                 "0",  # 没有子任务关系
#                 "",  # 没有指定执行任务
#                 "",  # 没有指定跳过任务
#             ],
#             "expected_output": "A B C D"
#         },
#         # {
#         #     "input": [
#         #         "A B C D",
#         #         "2",  # 没有子任务关系
#         #         "A B",
#         #         "B A"
#         #         "",  # 没有指定执行任务
#         #         "",  # 没有指定跳过任务
#         #     ],
#         #     "expected_output": "A B C D"
#         # }
#     ]
#
#     # tasks = sys.stdin.read().strip().split("\n")  # 读取所有输入
#     # try:
#     index = 0
#     for test_case in test_cases:
#         index += 1
#         print("—— case " + str(index))
#         work_flow = WorkFlow(test_case["input"])
#         work_flow.solve_workflow()
#     # except Exception as e:
#     #     pass

from collections import defaultdict
from typing import List


def parse_input(tasks: List):
    # 输入任务顺序
    task_order = tasks[0]
    # 子任务关系数量
    n = int(tasks[1])

    line = 1
    # 构建任务树
    task_tree = defaultdict(list)
    for _ in range(n):
        line += 1
        relation = tasks[line]
        parent, children = relation[0], relation[1:]
        task_tree[parent].extend(children)

    execute, skip = None, None
    # 指定执行任务
    if len(tasks) > line + 1:
        execute = tasks[line + 1]
    execute = set(execute.split()) if execute else set(task_order.split())
    # 指定跳过任务
    if len(tasks) > line + 2:
        skip = tasks[line + 2]
    skip = set(skip.split()) if skip else set()

    return task_order, task_tree, execute, skip


def resolve_tasks(task_order, task_tree, execute, skip):
    # 标记哪些任务需要执行
    to_execute = set()

    # 如果有指定执行，包含其父任务
    def mark_execute(task):
        if task in skip:  # 跳过任务不执行
            return
        if task not in to_execute:
            to_execute.add(task)
            for parent, children in task_tree.items():
                if task in children:
                    mark_execute(parent)

    for task in execute:
        mark_execute(task)

    # 删除跳过的任务及其子任务
    def mark_skip(task):
        if task in to_execute:
            to_execute.remove(task)
        for child in task_tree[task]:
            mark_skip(child)

    for task in skip:
        mark_skip(task)

    # 按顺序执行任务
    result = []

    def execute_task(task):
        if task in to_execute:
            result.append(task)
            for child in task_tree[task]:
                execute_task(child)

    for task in task_order:
        execute_task(task)

    return result


def main(tasks: List, expected):
    task_order, task_tree, execute, skip = parse_input(tasks)
    result = resolve_tasks(task_order, task_tree, execute, skip)
    print(" ".join(result) + ", " + str(expected == " ".join(result)))


if __name__ == "__main__":
    test_cases = [
        { # 1
            "input": [
                "A B C",
                "2",
                "A D",
                "D E",
                "B E",
            ],
            "expected_output": "A D E B"
        },
        { # 2
            "input": [
                "A B C D",
                "3",
                "A B",
                "B C",
                "C D",
                "D",  # 指定执行任务
                "",  # 没有跳过任务
            ],
            "expected_output": "A B C D"
        },
        { # 3
            "input": [
                "A B C D",
                "3",
                "A B",
                "B C",
                "C D",
                "",  # 没有指定执行任务
                "A",  # 跳过任务 A
            ],
            "expected_output": ""
        },
        { # 4
            "input": [
                "A B C D E F",
                "4",
                "A B",
                "B C D",
                "C E",
                "D F",
                "C F",  # 指定执行任务
                "B",  # 跳过任务
            ],
            "expected_output": "A C F"
        },
        { # 5
            "input": [
                "A B C D",
                "0",  # 没有子任务关系
                "B",  # 指定执行任务
                "C",  # 跳过任务
            ],
            "expected_output": "B"
        },
        { # 6
            "input": [
                "A B C D",
                "2",
                "A B",
                "C D",
            ],
            "expected_output": "A B C D"
        },
        { # 7
            "input": [
                "A B C D E F G H",
                "5",
                "A B C",
                "B D",
                "C E F",
                "D G",
                "F H",
                "C D",  # 指定执行任务
                "B",  # 指定跳过任务
            ],
            "expected_output": "A C E F H D G"
        },
        { # 8
            "input": [
                "A B C D",
                "1",
                "A B",
                "A",  # 指定执行任务
                "A",  # 指定跳过任务
            ],
            "expected_output": ""
        },
        { # 9
            "input": [
                "A B C",
                "2",
                "A B",
                "B C",
                "A",  # 指定执行任务
                "",  # 没有跳过任务
            ],
            "expected_output": "A B C"
        },
        { # 10
            "input": [
                "A B C D",
                "3",
                "A B",
                "B C",
                "C D",
                "",  # 没有指定执行任务
                "C",  # 指定跳过任务
            ],
            "expected_output": "A B"
        },
        { # 11
            "input": [
                "A B C D E F G H I",
                "7",
                "A B C",
                "B D E",
                "C F G",
                "D H",
                "E I",
                "G H",
                "F I",
                "A",  # 指定执行任务
                "",  # 没有指定跳过任务
            ],
            "expected_output": "A B D H E I C F G"
        },
        { # 12
            "input": [
                "A B C D E F",
                "4",
                "A B",
                "B C D",
                "C E",
                "D F",
                "B C",  # 指定执行任务
                "D",  # 指定跳过任务
            ],
            "expected_output": "A B C E"
        },
        { # 13
            "input": [
                "A B C D E F G",
                "6",
                "A B C",
                "B D",
                "C E",
                "E F",
                "F G",
                "D G",
                "",  # 没有指定执行任务
                "",  # 没有指定跳过任务
            ],
            "expected_output": "A B D G C E F"
        },
        { # 14
            "input": [
                "A B C D",
                "3",
                "A B",
                "B C",
                "C D",
                "",  # 没有指定执行任务
                "A",  # 指定跳过任务
            ],
            "expected_output": ""
        },
        { # 15
            "input": [
                "A B C D E F G H I",
                "6",
                "A B C",
                "B D E",
                "C F G",
                "E H",
                "F I",
                "H I",
                "B E G",  # 指定执行任务
                "C F",  # 指定跳过任务
            ],
            "expected_output": "A B D E H G"
        },
        { # 16
            "input": [
                "A B C D E F",
                "5",
                "A B",
                "B C",
                "C D",
                "D E",
                "E F",
                "F",  # 指定执行任务
                "A",  # 指定跳过任务
            ],
            "expected_output": "F"
        },
        { # 17
            "input": [
                "A B C D E F G H",
                "7",
                "A B C",
                "B D",
                "C E",
                "D F",
                "E G",
                "F H",
                "G H",
                "B C E",  # 指定执行任务
                "D F",  # 指定跳过任务
            ],
            "expected_output": "A B C E G H"
        },
        { # 18
            "input": [
                "A B C D E F G H",
                "6",
                "A B C",
                "B D E",
                "C F",
                "D G",
                "E H",
                "F G",
                "H",  # 指定执行任务
                "A",  # 指定跳过任务
            ],
            "expected_output": "H"
        },
        { # 19
            "input": [
                "A B C D E F G",
                "4",
                "A B",
                "B C",
                "C D E",
                "D F G",
                "A C",  # 指定执行任务
                "B D",  # 指定跳过任务
            ],
            "expected_output": "A C E"
        },
        { # 20
            "input": [
                "A B C D",
                "0",  # 没有子任务关系
                "",  # 没有指定执行任务
                "",  # 没有指定跳过任务
            ],
            "expected_output": "A B C D"
        },
        # {
        #     "input": [
        #         "A B C D",
        #         "2",  # 没有子任务关系
        #         "A B",
        #         "B A"
        #         "",  # 没有指定执行任务
        #         "",  # 没有指定跳过任务
        #     ],
        #     "expected_output": "A B C D"
        # }
    ]

    for test_case in test_cases:
        main(test_case["input"], test_case["expected_output"])


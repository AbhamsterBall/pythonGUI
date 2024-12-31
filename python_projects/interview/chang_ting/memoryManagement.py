# import sys
# '''
# 内存管理系统模拟
# Description
#
# 在操作系统中, 内存管理是核心功能之一, 内存管理策略对于系统性能至关重要. 内存页是操作系统对物理内存管理的基本单位. 你需要设计并实现一个内存管理系统模拟器, 该系统应通过命令行支持以下功能:
#
# 内存分配: 模拟内存分配请求, 寻找合适的有空闲空间的内存页为其分配, 支持首次适应, 最佳适应和最差适应算法.
# 内存回收: 模拟内存回收过程, 处理内存碎片问题.
# 内存碎片分析: 计算并报告内存碎片率. (已分配使用内存页中未实际使用的内存空间为内存碎片, 内存碎片率为: 内存碎片总大小/所有内存总大小)
#
# Input
#
# 以命令行形式输入要执行的内存相关命令.
#
# 第一行为: MEM_PAGE [大小] [个数]
#
# 定义内存页的大小, 和个数, 总内存即大小*个数,大小范围为[1, 20971512], 个数范围为[1, 20971512].
# 第二行起为用户通过命令行输入命令和参数:
#
# ALLOCATE_FIRST_FIT [大小]: 使用首次适应算法分配指定大小的内存块（大小不会超过一个内存页）, 并返回系统分配的内存自增索引编号. 首次适应算法从内存的开始位置顺序搜索, 直到找到足够大的空闲块.
# ALLOCATE_BEST_FIT [大小]: 使用最佳适应算法分配指定大小的内存块（大小不会超过一个内存页）, 并返回系统分配的内存自增索引编号. 最佳适应算法搜索整个内存, 找到能够满足要求且最小的空闲块.如果有多个同时符合条件的内存页,则分配最靠近内存开始位置的内存页.
# ALLOCATE_WORST_FIT [大小]: 使用最差适应算法分配指定大小的内存块（大小不会超过一个内存页）, 并返回系统分配的内存自增索引编号. 最差适应算法搜索整个内存, 找到最大的空闲块, 即使它比所需大小大得多. 如果有多个同时符合条件的内存页,则分配最靠近内存开始位置的内存页.
# FREE [索引]: 释放指定索引处的内存块, 使其变为空闲状态.
# ANALYZE: 分析当前内存状态, 包括总内存, 已用内存, 空闲内存和内存碎片率（百分比保留两个小数点）.
#
# Output
#
# 系统根据用户命令执行相应操作, 并给出操作结果.
#
# 对于 ALLOCATE 命令, 输出一行操作结果, 如果内存分配成功, 输出 Memory Index is N, N 代表内存自增索引编号, 否则输出 Failed
#
# 对于 FREE 命令, 输出 Done
#
# 对于ANALYZE 命令, 输出四行结果, 分别代表总内存, 已用内存, 空闲内存和内存碎片率, 例如:
#
# Total Memory: 40960
#
# Used Memory: 250
#
# Free Memory: 40710
#
# Memory Fragmentation: 19.39%
#
#
#
# Sample Input 1
#
# MEM_PAGE 4096 10
# ALLOCATE_FIRST_FIT 100
# ALLOCATE_BEST_FIT 50
# ALLOCATE_WORST_FIT 200
# ALLOCATE_FIRST_FIT 4097
# ANALYZE
# FREE 1
# ANALYZE
# Sample Output 1
#
# Memory Index is 1
# Memory Index is 2
# Memory Index is 3
# Failed
# Total Memory: 40960
# Used Memory: 350
# Free Memory: 40610
# Memory Fragmentation: 19.15%
# Done
# Total Memory: 40960
# Used Memory: 250
# Free Memory: 40710
# Memory Fragmentation: 19.39%
# Hint
#
# 内存回收命令不出现执行未分配的索引号
#
# 输出示例中的 Memory Fragmentation 计算公式为：((4096 - 100 - 50) + (4096 - 200)) / (4096*10) * 100%
#
# Language
# '''
# class MemoryManager:
#     def __init__(self, page_size: int, page_count: int):
#         self.page_size = page_size
#         self.pages = [{"size": 0, "block_index": [], "block_size": []} for _ in range(page_count)]
#         self.next_index = 1
#
#     def allocate(self, size: int, strategy: str):
#         if size > self.page_size:
#             return "Failed"
#
#         selected_page = None
#         if strategy == "FIRST_FIT":
#             for page in self.pages:
#                 if self.page_size - page["size"] >= size:
#                     selected_page = page
#                     break
#         elif strategy == "BEST_FIT":
#             for page in self.pages:
#                 if self.page_size - page["size"] >= size:
#                     if not selected_page or (self.page_size - page["size"] < self.page_size - selected_page["size"]):
#                         selected_page = page
#         elif strategy == "WORST_FIT":
#             for page in self.pages:
#                 if self.page_size - page["size"] >= size:
#                     if not selected_page or (self.page_size - page["size"] > self.page_size - selected_page["size"]):
#                         selected_page = page
#
#         if selected_page:
#             selected_page["size"] += size
#             selected_page["block_index"].append(self.next_index)
#             selected_page["block_size"].append(size)
#             self.next_index += 1
#             return f"Memory Index is {self.next_index - 1}"
#         return "Failed"
#
#     def free(self, index: int):
#         for page in self.pages:
#             if index in page["block_index"]:
#                 idx = page["block_index"].index(index)
#                 page["size"] -= page["block_size"][idx]
#                 page["block_index"].pop(idx)
#                 page["block_size"].pop(idx)
#                 return "Done"
#         return "Failed"
#
#     def analyze(self):
#         total_memory = len(self.pages) * self.page_size
#         used_memory = sum(page["size"] for page in self.pages)
#         free_memory = total_memory - used_memory
#         fragmentation = (
#             sum(self.page_size - page["size"] for page in self.pages if page["size"] > 0)
#             / total_memory
#             * 100
#         )
#         return (
#             f"Total Memory: {total_memory}\n"
#             f"Used Memory: {used_memory}\n"
#             f"Free Memory: {free_memory}\n"
#             f"Memory Fragmentation: {fragmentation:.2f}%"
#         )
#
# # Sample Input/Output Simulation
# if __name__ == "__main__":
#     # test_cases = [
#     #     [ # 1
#     #         "MEM_PAGE 4096 10",
#     #         "ALLOCATE_FIRST_FIT 100",
#     #         "ALLOCATE_BEST_FIT 50",
#     #         "ALLOCATE_WORST_FIT 200",
#     #         "ALLOCATE_FIRST_FIT 4097",
#     #         "ANALYZE",
#     #         "FREE 1",
#     #         "ANALYZE"
#     #     ],
#     #     [ # 2
#     #         "MEM_PAGE 4096 5",
#     #         "ALLOCATE_FIRST_FIT 100",
#     #         "ALLOCATE_FIRST_FIT 200",
#     #         "ALLOCATE_BEST_FIT 150",
#     #         "ALLOCATE_WORST_FIT 300",
#     #         "ALLOCATE_FIRST_FIT 4000",
#     #         "ALLOCATE_WORST_FIT 100",
#     #         "FREE 1",
#     #         "FREE 3",
#     #         "ANALYZE",
#     #         "ALLOCATE_BEST_FIT 50",
#     #         "ALLOCATE_WORST_FIT 250",
#     #         "ANALYZE",
#     #         "FREE 2",
#     #         "FREE 4",
#     #         "ANALYZE",
#     #     ],
#     #     [ # 3
#     #         "MEM_PAGE 4096 5",
#     #         "ALLOCATE_FIRST_FIT 100",
#     #         "ALLOCATE_FIRST_FIT 200",
#     #         "ALLOCATE_WORST_FIT 300",
#     #         "ALLOCATE_BEST_FIT 300",
#     #         "ANALYZE"
#     #     ],
#     #     [ # 4
#     #         "MEM_PAGE 1024 3",
#     #         "ALLOCATE_FIRST_FIT 512",
#     #         "ALLOCATE_BEST_FIT 512",
#     #         "ALLOCATE_WORST_FIT 256",
#     #         "ALLOCATE_FIRST_FIT 256",
#     #         "FREE 1",
#     #         "ALLOCATE_BEST_FIT 128",
#     #         "ALLOCATE_FIRST_FIT 128",
#     #         "ALLOCATE_WORST_FIT 256",
#     #         "FREE 2",
#     #         "FREE 3",
#     #         "ALLOCATE_BEST_FIT 512",
#     #         "ALLOCATE_FIRST_FIT 64",
#     #         "ALLOCATE_WORST_FIT 64",
#     #         "ANALYZE",
#     #         "FREE 4",
#     #         "ALLOCATE_WORST_FIT 1000",
#     #         "ALLOCATE_BEST_FIT 64",
#     #         "ALLOCATE_FIRST_FIT 64",
#     #         "FREE 5",
#     #         "ANALYZE",
#     #         "ALLOCATE_FIRST_FIT 1024",
#     #         "ALLOCATE_WORST_FIT 1024",
#     #         "FREE 6",
#     #         "ANALYZE",
#     #     ]
#     # ]
#     # # commands = [
#     # #     "MEM_PAGE 4096 10",
#     # #     "ALLOCATE_FIRST_FIT 100",
#     # #     "ALLOCATE_BEST_FIT 50",
#     # #     "ALLOCATE_WORST_FIT 200",
#     # #     "ALLOCATE_FIRST_FIT 4097",
#     # #     "ANALYZE",
#     # #     "FREE 1",
#     # #     "ANALYZE"
#     # # ]
#
#     manager = None
#     test_cases = [sys.stdin.read().strip().split("\n")]
#     # for command in commands:
#     for commands in test_cases:
#         print("Test Case " + str(test_cases.index(commands) + 1))
#         for command in commands:
#             # if len(command) == 0:  # 如果输入为空行，退出循环
#             #     break
#             parts = command.split()
#             action = parts[0]
#             # try:
#             if action == "MEM_PAGE":
#                 page_size = int(parts[1])
#                 page_count = int(parts[2])
#                 manager = MemoryManager(page_size, page_count)
#             elif action.startswith("ALLOCATE"):
#                 size = int(parts[1])
#                 strategy = action.split("_")[1] + "_" + action.split("_")[2]
#                 print(manager.allocate(size, strategy))
#             elif action == "FREE":
#                 index = int(parts[1])
#                 print(manager.free(index))
#             elif action == "ANALYZE":
#                 print(manager.analyze())
#         print(manager.pages)
#         print("--------------------------------------------------------------------------------")
#             # except Exception as e:
#             #     pass

import sys
class MemoryManager:
    def __init__(self, page_size: int, page_count: int):
        self.page_size = page_size
        self.pages = [{"size": 0, "block_index": [], "block_size": []} for _ in range(page_count)]
        self.next_index = 1

    def allocate(self, size: int, strategy: str):
        if size > self.page_size:
            return "Failed"

        selected_page = None
        if strategy == "FIRST_FIT":
            for page in self.pages:
                if self.page_size - page["size"] >= size:
                    selected_page = page
                    break
        elif strategy == "BEST_FIT":
            for page in self.pages:
                if self.page_size - page["size"] >= size:
                    if not selected_page or (self.page_size - page["size"] < self.page_size - selected_page["size"]):
                        selected_page = page
        elif strategy == "WORST_FIT":
            for page in self.pages:
                if self.page_size - page["size"] >= size:
                    if not selected_page or (self.page_size - page["size"] > self.page_size - selected_page["size"]):
                        selected_page = page

        if selected_page:
            selected_page["size"] += size
            selected_page["block_index"].append(self.next_index)
            selected_page["block_size"].append(size)
            self.next_index += 1
            return f"Memory Index is {self.next_index - 1}"
        return "Failed"

    def free(self, index: int):
        for page in self.pages:
            if index in page["block_index"]:
                idx = page["block_index"].index(index)
                page["size"] -= page["block_size"][idx]
                page["block_index"].pop(idx)
                page["block_size"].pop(idx)
                return "Done"
        return "Failed"

    def analyze(self):
        total_memory = len(self.pages) * self.page_size
        used_memory = sum(page["size"] for page in self.pages)
        free_memory = total_memory - used_memory
        fragmentation = (
            sum(self.page_size - page["size"] for page in self.pages if page["size"] > 0)
            / total_memory
            * 100
        )
        return (
            f"Total Memory: {total_memory}\n"
            f"Used Memory: {used_memory}\n"
            f"Free Memory: {free_memory}\n"
            f"Memory Fragmentation: {fragmentation:.2f}%"
        )

# Sample Input/Output Simulation
if __name__ == "__main__":
    manager = None
    commands = sys.stdin.read().strip().split("\n")
    # for command in commands:
    for command in commands:
        # if len(command) == 0:  # 如果输入为空行，退出循环
        #     break
        parts = command.split()
        action = parts[0]
        try:
            if action == "MEM_PAGE":
                page_size = int(parts[1])
                page_count = int(parts[2])
                manager = MemoryManager(page_size, page_count)
            elif action.startswith("ALLOCATE"):
                size = int(parts[1])
                strategy = action.split("_")[1] + "_" + action.split("_")[2]
                print(manager.allocate(size, strategy))
            elif action == "FREE":
                index = int(parts[1])
                print(manager.free(index))
            elif action == "ANALYZE":
                print(manager.analyze())
        except Exception as e:
            pass

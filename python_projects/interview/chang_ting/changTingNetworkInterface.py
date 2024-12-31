'''
网络接口配置变更
Description

网络接口代表了系统与网络之间的一个连接点, 某个系统支持三种类型的网络接口:

物理接口(Physical
Interface): 这是网卡上实际存在的网络接口.
链路聚合接口(Bond
Interface)：这是将多个物理接口捆绑在一起构成的逻辑接口.通过链路聚合, 可以将多个物理网络连接捆绑成一个逻辑接口, 从而提高网络性能和可靠性.链路聚合口所捆绑的物理接口叫做他的子接口.
VLAN
接口(VLAN
Interface)：这是在一个物理接口或一个链路聚合接口的基础上创建的逻辑接口.它允许在同一物理网络上分离不同
VLAN
的网络流量.用来创建
VLAN
接口的物理接口或链路聚合接口称为它的父接口.
三类接口的属性:

物理接口: 名称
链路聚合接口: 名称, 子接口
VLAN
接口: 名称, 父接口
该系统的网络接口需符合以下约束:

所有接口的名称不可重复.
物理接口不会发生变化, 即它们的数量和名称是固定的.
Bond
接口的子接口只能是物理接口, 子接口数量大于或等于
1.
一个物理接口只能是一个
Bond
接口的子接口, 不能同时属于两个
Bond
接口，也不能既是一个
Bond
接口的子接口又是一个
VLAN
接口的父接口.
多个
VLAN
接口可以有相同的父接口.
VLAN
接口的父接口可以是物理接口或
Bond
接口, 不可是其它
VLAN
接口.
创建
VLAN
接口时，其父接口必须已经存在;
当一个接口是某个
VLAN
接口的父接口时，该接口不可被删除.
系统支持四种操作: 创建
Bond
接口, 删除
Bond
接口, 创建
VLAN
接口, 删除
VLAN
接口.

本题输入系统当前的网络接口配置, 和目标的网络接口配置, 请输出最少的变更步骤数
K，使得系统能通过
K
步变更从当前状态变更为目标状态, 且每一步变更都符合系统的约束条件.

Input

第一行为当前配置的条目数量
N.

接下来
N
行, 每一行为一条接口配置, 每行以接口类型和接口名称开头, 针对不同接口具体格式如下:

物理接口: 接口类型 + 接口名称, 用单个空格分隔, 例如
"Physical eth1".
链路聚合接口: 接口类型 + 接口名称 + 子接口数量 + 子接口名称, 用单个空格分隔, 例如
"Bond bond1 3 eth1 eth2 eth3".有多个子接口时, 会按接口名称的字典序排序.
VLAN
接口: 接口类型 + 接口名称 + 父接口名称, 用单个空格分隔, 例如
"VLAN vlan1 bond1".
接下来一行是目标配置的条目数量
M.

接下来
M
行, 每一行为一条接口配置, 格式和当前配置的格式一致.

当前配置和目标配置都一定是符合系统约束的.

Output

输出最小的变更步骤数量
K.

Sample
Input
1

5
Physical
eth1
Physical
eth2
Physical
eth3
Bond
bond1
1
eth1
VLAN
vlan1
eth2
5
Physical
eth1
Physical
eth2
Physical
eth3
Bond
bond1
2
eth1
eth3
VLAN
vlan1
eth2
Sample
Output
1

2
Hint

样例中, 要从当前配置变更为目标配置, 最少需要两步: "删除 bond1", "创建 bond1".因此输出为
2.

Language:

'''
# def parse_configuration(n, lines):
#     """
#     Parse the configuration input into a structured format.
#     """
#     configuration = {
#         "Physical": set(),
#         "Bond": {},
#         "VLAN": {}
#     }
#
#     for line in lines:
#         parts = line.split()
#         if parts[0] == "Physical":
#             configuration["Physical"].add(parts[1])
#         elif parts[0] == "Bond":
#             configuration["Bond"][parts[1]] = sorted(parts[3:])
#         elif parts[0] == "VLAN":
#             configuration["VLAN"][parts[1]] = parts[2]
#
#     return configuration
#
# def calculate_steps(current, target):
#     """
#     Calculate the minimum number of steps to transition from the current
#     configuration to the target configuration.
#     """
#     steps = 0
#
#     # Handle VLAN deletions
#     for vlan in list(current["VLAN"].keys()):
#         if vlan not in target["VLAN"] or current["VLAN"][vlan] != target["VLAN"][vlan]:
#             del current["VLAN"][vlan]
#             steps += 1
#
#     # Handle Bond deletions
#     for bond in list(current["Bond"].keys()):
#         if bond not in target["Bond"] or current["Bond"][bond] != target["Bond"][bond]:
#             del current["Bond"][bond]
#             steps += 1
#
#     # Handle Bond creations
#     for bond, sub_interfaces in target["Bond"].items():
#         if bond not in current["Bond"] or current["Bond"][bond] != sub_interfaces:
#             current["Bond"][bond] = sub_interfaces
#             steps += 1
#
#     # Handle VLAN creations
#     for vlan, parent in target["VLAN"].items():
#         if vlan not in current["VLAN"] or current["VLAN"][vlan] != parent:
#             current["VLAN"][vlan] = parent
#             steps += 1
#
#     return steps
#
# while 1:
#     # Input parsing
#     n = int(input())
#     current_lines = [input().strip() for _ in range(n)]
#     current_config = parse_configuration(n, current_lines)
#
#     m = int(input())
#     target_lines = [input().strip() for _ in range(m)]
#     target_config = parse_configuration(m, target_lines)
#
#     # Calculate the result
#     result = calculate_steps(current_config, target_config)
#     print(result)

from typing import List, Set


class Interface:
    def __init__(self, type: str, name: str, details: List[str]):
        self.type = type
        self.name = name
        self.details = details

    def __eq__(self, other):
        return self.type == other.type and self.name == other.name and self.details == other.details

    def __hash__(self):
        h1 = hash(self.type)
        h2 = hash(self.name)
        h3 = 0
        for detail in self.details:
            h3 ^= hash(detail)
        return h1 ^ h2 ^ h3


# Read interfaces configuration
def read_interfaces(count: int, interfaces_int: List[str]) -> List[Interface]:
    interfaces = []
    for _ in range(count):
        info = interfaces_int[_]
        type, name = info.split(" ")[0], info.split(" ")[1]
        iface = Interface(type, name, [])

        if type == "Bond":
            sub_count = int(info.split(" ")[2])
            info_details = info.split(" ")[3:]
            iface.details = info_details
        elif type == "VLAN":
            parent = info.split(" ")[2]
            iface.details.append(parent)

        interfaces.append(iface)
    return interfaces


# Calculate minimum steps to change from current configuration to target
def calculate_min_steps(current: List[Interface], target: List[Interface]) -> int:
    current_set = set(current)
    target_set = set(target)

    remove_count = 0
    remove_vlan = set()
    add_count = 0
    # remove_count = sum(1 for iface in current if iface not in target_set)
    for iface in current:
        if iface not in target_set:
            # remove_count += 1
            if iface.type == "Bond":
                for _ in current:
                    if _.type == "VLAN" and _.details[0] == iface.name:
                        remove_vlan.add(_.name)
                    # remove_vlan.add(detail)

    remove_count = sum(1 for iface in current if iface not in target_set and iface.name not in remove_vlan)
    add_count += sum(1 for iface in target if iface not in current_set and iface.name not in remove_vlan)
    remove_vlan_count = len(remove_vlan)
    add_vlan_count = sum(1 for iface in remove_vlan if iface in {iface.name for iface in target_set})

    return remove_count + add_count + remove_vlan_count + add_vlan_count


# def main():
#     n = int(input())
#     current = read_interfaces(n)
#
#     m = int(input())
#     target = read_interfaces(m)
#
#     print(calculate_min_steps(current, target))

def count_changes(current_config, target_config):
    n = len(current_config)
    current = read_interfaces(n, current_config)

    m = len(target_config)
    target = read_interfaces(m, target_config)

    return calculate_min_steps(current, target)


if __name__ == "__main__":
    # Define test cases
    test_cases = [
        # Test case 1: Simple update of Bond
        {
            "current": [
                "Physical eth1",
                "Physical eth2",
                "Bond bond1 1 eth1",
                "VLAN vlan1 eth2"
            ],
            "target": [
                "Physical eth1",
                "Physical eth2",
                "Bond bond1 2 eth1 eth2",
                "VLAN vlan1 eth2"
            ],
            "expected": 2
        },
        # Test case 2: Adding a VLAN and Bond update
        {
            "current": [
                "Physical eth1",
                "Physical eth2",
                "Bond bond1 1 eth1"
            ],
            "target": [
                "Physical eth1",
                "Physical eth2",
                "Bond bond1 2 eth1 eth2",
                "VLAN vlan1 bond1"
            ],
            "expected": 3
        },
        # Test case 3: Removing a Bond
        {
            "current": [
                "Physical eth1",
                "Physical eth2",
                "Bond bond1 2 eth1 eth2",
                "VLAN vlan1 bond1"
            ],
            "target": [
                "Physical eth1",
                "Physical eth2",
                "VLAN vlan1 eth2"
            ],
            "expected": 3
        },
        # Test case 4: No changes needed
        {
            "current": [
                "Physical eth1",
                "Physical eth2",
                "Bond bond1 2 eth1 eth2",
                "VLAN vlan1 bond1"
            ],
            "target": [
                "Physical eth1",
                "Physical eth2",
                "Bond bond1 2 eth1 eth2",
                "VLAN vlan1 bond1"
            ],
            "expected": 0
        },
        # Test case 5: Completely different configuration
        {
            "current": [
                "Physical eth1",
                "Physical eth2",
                "Bond bond1 2 eth1 eth2",
                "VLAN vlan1 bond1"
            ],
            "target": [
                "Physical eth1",
                "Physical eth2",
                "Bond bond2 1 eth1",
                "VLAN vlan2 eth2"
            ],
            "expected": 4
        },
        {
            "current": [
                "Physical eth1",
                "Physical eth2",
                "Physical eth3",
                "Bond bond1 1 eth1",
                "VLAN vlan1 eth2"
                ],
            "target": [
                "Physical eth1",
                "Physical eth2",
                "Physical eth3",
                "Bond bond1 2 eth1 eth3",
                "VLAN vlan1 eth2"
            ],
            "expected": 2
        },
        # Test case 1: Simple addition of a VLAN
        {
            "current": [
                "Physical eth1",
                "Physical eth2",
                "Bond bond1 1 eth1"
            ],
            "target": [
                "Physical eth1",
                "Physical eth2",
                "Bond bond1 1 eth1",
                "VLAN vlan1 bond1"
            ],
            "expected": 1
        },
        # Test case 2: Deletion of a VLAN
        {
            "current": [
                "Physical eth1",
                "Physical eth2",
                "Bond bond1 1 eth1",
                "VLAN vlan1 bond1"
            ],
            "target": [
                "Physical eth1",
                "Physical eth2",
                "Bond bond1 1 eth1"
            ],
            "expected": 1
        },
        # Test case 3: Adding and removing Bonds
        {
            "current": [
                "Physical eth1",
                "Physical eth2"
            ],
            "target": [
                "Physical eth1",
                "Physical eth2",
                "Bond bond1 1 eth1"
            ],
            "expected": 1
        },
        # Test case 4: Removing a Bond
        {
            "current": [
                "Physical eth1",
                "Physical eth2",
                "Bond bond1 1 eth1"
            ],
            "target": [
                "Physical eth1",
                "Physical eth2"
            ],
            "expected": 1
        },
        # Test case 5: Adding multiple VLANs
        {
            "current": [
                "Physical eth1",
                "Physical eth2",
                "Bond bond1 1 eth1"
            ],
            "target": [
                "Physical eth1",
                "Physical eth2",
                "Bond bond1 1 eth1",
                "VLAN vlan1 bond1",
                "VLAN vlan2 bond1"
            ],
            "expected": 2
        },
        # Test case 6: Removing multiple VLANs
        {
            "current": [
                "Physical eth1",
                "Physical eth2",
                "Bond bond1 1 eth1",
                "VLAN vlan1 bond1",
                "VLAN vlan2 bond1"
            ],
            "target": [
                "Physical eth1",
                "Physical eth2",
                "Bond bond1 1 eth1"
            ],
            "expected": 2
        },
        # Test case 13: Complex case with multiple changes (at least 7 steps)
        {
            "current": [
                "Physical eth1",
                "Physical eth2",
                "Physical eth3",
                "Bond bond1 1 eth1",
                "Bond bond2 1 eth2",
                "VLAN vlan1 bond1",
                "VLAN vlan2 bond2"
            ],
            "target": [
                "Physical eth1",
                "Physical eth2",
                "Physical eth3",
                "Bond bond3 2 eth1 eth2",
                "VLAN vlan3 bond3",
                "VLAN vlan4 bond3",
                "VLAN vlan5 bond3",
                "VLAN vlan2 bond2"
            ],
            "expected": 9
        },
        # Test case 14: Completely restructuring Bonds and VLANs
        {
            "current": [
                "Physical eth1",
                "Physical eth2",
                "Physical eth3",
                "Bond bond1 2 eth1 eth2",
                "VLAN vlan1 bond1"
            ],
            "target": [
                "Physical eth1",
                "Physical eth2",
                "Physical eth3",
                "Bond bond2 1 eth3",
                "VLAN vlan2 bond2",
                "VLAN vlan3 bond2"
            ],
            "expected": 5
        },
        # Test case 15: Adding and removing multiple Bonds and VLANs
        {
            "current": [
                "Physical eth1",
                "Physical eth2",
                "Physical eth3",
                "Bond bond1 2 eth1 eth2",
                "VLAN vlan1 bond1",
                "VLAN vlan2 bond1"
            ],
            "target": [
                "Physical eth1",
                "Physical eth2",
                "Physical eth3",
                "Bond bond3 1 eth3",
                "VLAN vlan3 bond3",
                "VLAN vlan4 bond3"
            ],
            "expected": 6
        },
        # Test case 16: Full network redesign
        {
            "current": [
                "Physical eth1",
                "Physical eth2",
                "Physical eth3",
                "Bond bond1 1 eth1",
                "Bond bond2 1 eth2",
                "VLAN vlan1 bond1",
                "VLAN vlan2 bond2"
            ],
            "target": [
                "Physical eth1",
                "Physical eth2",
                "Physical eth3",
                "Bond bond3 2 eth1 eth2",
                "Bond bond4 1 eth3",
                "VLAN vlan3 bond3",
                "VLAN vlan4 bond4",
                "VLAN vlan5 bond3"
            ],
            "expected": 9
        },
        # Test case 17: Removing all Bonds and VLANs
        {
            "current": [
                "Physical eth1",
                "Physical eth2",
                "Physical eth3",
                "Bond bond1 1 eth1",
                "VLAN vlan1 bond1"
            ],
            "target": [
                "Physical eth1",
                "Physical eth2",
                "Physical eth3"
            ],
            "expected": 2
        },
        # Test case 18: Adding multiple Bonds and VLANs
        {
            "current": [
                "Physical eth1",
                "Physical eth2",
                "Physical eth3"
            ],
            "target": [
                "Physical eth1",
                "Physical eth2",
                "Physical eth3",
                "Bond bond1 2 eth1 eth2",
                "Bond bond2 1 eth3",
                "VLAN vlan1 bond1",
                "VLAN vlan2 bond1",
                "VLAN vlan3 bond2"
            ],
            "expected": 5
        },
        # Test case 19: Swapping Bonds and VLANs
        {
            "current": [
                "Physical eth1",
                "Physical eth2",
                "Bond bond1 2 eth1 eth2",
                "VLAN vlan1 bond1",
                "VLAN vlan2 bond1"
            ],
            "target": [
                "Physical eth1",
                "Physical eth2",
                "Bond bond2 2 eth1 eth2",
                "VLAN vlan3 bond2",
                "VLAN vlan4 bond2"
            ],
            "expected": 6
        },
        # Test case 14: Adding VLANs to existing Bonds
        {
            "current": [
                "Physical eth1",
                "Physical eth2",
                "Bond bond1 2 eth1 eth2"
            ],
            "target": [
                "Physical eth1",
                "Physical eth2",
                "Bond bond1 2 eth1 eth2",
                "VLAN vlan1 bond1",
                "VLAN vlan2 bond1",
                "VLAN vlan3 bond1"
            ],
            "expected": 3
        }
    ]

    # Run test cases
    results = []
    for idx, test_case in enumerate(test_cases, start=1):
        result = count_changes(test_case["current"], test_case["target"])
        results.append((idx, result, result == test_case["expected"]))

    print(results)


# class Solution:
#     def countKeyChanges(self, s: str) -> int:
#         def parse_configuration(lines: list[str]):
#             """
#             Parse the configuration input into a structured format.
#             """
#             configuration = {
#                 "Physical": set(),
#                 "Bond": {},
#                 "VLAN": {}
#             }
#
#             for line in lines:
#                 parts = line.split()
#                 if parts[0] == "Physical":
#                     configuration["Physical"].add(parts[1])
#                 elif parts[0] == "Bond":
#                     configuration["Bond"][parts[1]] = sorted(parts[3:])
#                 elif parts[0] == "VLAN":
#                     configuration["VLAN"][parts[1]] = parts[2]
#
#             return configuration
#
#         def calculate_steps(current, target):
#             """
#             Calculate the minimum number of steps to transition from the current
#             configuration to the target configuration.
#             """
#             steps = 0
#
#             # Handle VLAN deletions
#             for vlan in list(current["VLAN"].keys()):
#                 if vlan not in target["VLAN"] or current["VLAN"][vlan] != target["VLAN"][vlan]:
#                     del current["VLAN"][vlan]
#                     steps += 1
#
#             # Handle Bond deletions
#             for bond in list(current["Bond"].keys()):
#                 if bond not in target["Bond"] or current["Bond"][bond] != target["Bond"][bond]:
#                     del current["Bond"][bond]
#                     steps += 1
#
#             # Handle Bond creations
#             for bond, sub_interfaces in target["Bond"].items():
#                 if bond not in current["Bond"] or current["Bond"][bond] != sub_interfaces:
#                     current["Bond"][bond] = sub_interfaces
#                     steps += 1
#
#             # Handle VLAN creations
#             for vlan, parent in target["VLAN"].items():
#                 if vlan not in current["VLAN"] or current["VLAN"][vlan] != parent:
#                     current["VLAN"][vlan] = parent
#                     steps += 1
#
#             return steps
#
#         # Parse input string into configurations
#         lines = s.strip().split('\n')
#         n = int(lines[0])
#         current = lines[1:n + 1]
#         m = int(lines[n + 1])
#         target = lines[n + 2:]
#
#         current_config = parse_configuration(current)
#         target_config = parse_configuration(target)
#
#         # Calculate the result
#         return calculate_steps(current_config, target_config)

# # Example usage
# if __name__ == "__main__":
'''
    input_data = """5
Physical eth1
Physical eth2
Physical eth3
Bond bond1 1 eth1
VLAN vlan1 eth2
6
Physical eth1
Physical eth2
Physical eth3
Bond bond1 2 eth1 eth3
VLAN vlan1 eth2
VLAN vlan2 eth3"""
'''
#     solution = Solution()
#     print(solution.countKeyChanges(input_data))

# if __name__ == "__main__":
#     import sys
#     input_data = sys.stdin.read()
#     solution = Solution()
#     print(solution.countKeyChanges(input_data))

# from typing import List
#
# class Solution:
#     def countKeyChanges(self, s: str) -> int:
#         def parse_configuration(lines: List[str]):
#             """
#             Parse the configuration input into a structured format.
#             """
#             configuration = {
#                 "Physical": set(),
#                 "Bond": {},
#                 "VLAN": {}
#             }
#
#             for line in lines:
#                 parts = line.split()
#                 if parts[0] == "Physical":
#                     configuration["Physical"].add(parts[1])
#                 elif parts[0] == "Bond":
#                     configuration["Bond"][parts[1]] = sorted(parts[3:])
#                 elif parts[0] == "VLAN":
#                     configuration["VLAN"][parts[1]] = parts[2]
#
#             return configuration
#
#         def calculate_steps(current, target):
#             """
#             Calculate the minimum number of steps to transition from the current
#             configuration to the target configuration.
#             """
#             steps = 0
#
#             # Handle VLAN deletions
#             for vlan in list(current["VLAN"].keys()):
#                 if vlan not in target["VLAN"] or current["VLAN"][vlan] != target["VLAN"][vlan]:
#                     del current["VLAN"][vlan]
#                     steps += 1
#
#             # Handle Bond deletions
#             for bond in list(current["Bond"].keys()):
#                 if bond not in target["Bond"] or current["Bond"][bond] != target["Bond"][bond]:
#                     del current["Bond"][bond]
#                     steps += 1
#
#             # Handle Bond creations
#             for bond, sub_interfaces in target["Bond"].items():
#                 if bond not in current["Bond"] or current["Bond"][bond] != sub_interfaces:
#                     current["Bond"][bond] = sub_interfaces
#                     steps += 1
#
#             # Handle VLAN creations
#             for vlan, parent in target["VLAN"].items():
#                 if vlan not in current["VLAN"] or current["VLAN"][vlan] != parent:
#                     current["VLAN"][vlan] = parent
#                     steps += 1
#
#             return steps
#
#         # Parse input string into configurations
#         lines = s.strip().split('\n')
#         n = int(lines[0])
#         current = lines[1:n + 1]
#         m = int(lines[n + 1])
#         target = lines[n + 2:]
#
#         current_config = parse_configuration(current)
#         target_config = parse_configuration(target)
#
#         # Calculate the result
#         return calculate_steps(current_config, target_config)
#
# # Example usage
# if __name__ == "__main__":
#     # import sys
#     while 1:
#         i = input()
#
#     input_data = input()
#     solution = Solution()
#     print(solution.countKeyChanges(input_data))

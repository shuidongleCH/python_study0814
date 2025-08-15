"""
当前项目已同步git，以下是后续更新代码流程
1. 修改代码后，在项目目录打开 CMD
2. 添加更改：
git add .
3. 提交更改：
git commit -m "描述你的修改"
4. 推送到 GitHub： git push
常用 Git 命令速查表
   命令	           功能
git status	    查看当前状态
git diff	    查看文件更改
git log	        查看提交历史
git pull	    拉取远程更新
git branch	    查看分支
git checkout -b new-branch	创建新分支
git remote -v	查看远程仓库
"""

# Python核心语法详解
# 1. 变量与数据类型
# 基本数据类型
num_int = 10           # 整数int
num_float = 3.14       # 浮点数float
text = "Hello"         # 字符串str
is_valid = True        # 布尔值bool
empty = None           # 空值NoneType

# 复合数据类型
my_list = [1, "a", True, 1]           # 列表list（有序可变）
my_tuple = (1, "b", False)         # 元组tuple（有序不可变）
my_dict = {"name": "Alice", "age": 30}  # 字典dict（无序键值对）
my_set = {1, 2, 3, 1}                 # 集合set（无序唯一）

print(type(num_int))   # 输出: <class 'int'>
print(f"{my_list}")    # 输出: [1, 'a', True, 1]
print(f"/{my_set}")    # 输出: {1, 2, 3}

# 2. 运算符
print(10 // 3)  # 3  → 整除
print(10 % 3)   # 1  → 取余
print(2 ** 3)   # 8  → 幂/乘方

# 3. 控制流
# if-elif-else
age = 18
if age < 13:
    print("Child")
elif age < 20:
    print("Teen")  # 执行此行
else:
    print("Adult")

# for循环
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)  # 依次输出水果名

# while循环
count = 0
while count < 3:
    print(count)  # 输出0,1,2
    count += 1

# 4. 函数定义
# 基本函数
def greet(name):
    return f"Hello, {name}"

print(greet("A Sen"))  # Hello, A Sen

def power(base, exp=2):
    return base ** exp

print(power(3))                 # 9(使用默认参数exp=2)
print(power(3, 3))    # 27
"""
def关键字定义函数
支持默认参数、关键字参数和可变参数
return返回值（无return时返回None）
"""


# 5. 类与面向对象
class Dog:
    # 类属性
    species = "Tom"

    # 构造方法
    def __init__(self, name, age):
        self.name = name  # 实例属性
        self.age = age

    def run(self):
        print(f"{self.name} run")


# 创建实例
my_dog = Dog("Jerry", 2)
my_dog.run()
print(my_dog.species)  #访问类属性
"""
class定义类
__init__为构造函数
self表示实例自身（类似this）
支持继承、多态等OOP特性
"""

# 6. 异常处理
try:
    result = 10 / 2
except ZeroDivisionError:
    print("不能除以零！")
else:
    print("结果:", result)   # 结果: 5.0
    print(f"结果:{result}")  # 结果:5.0
finally:
    print("执行结束")
"""
try：尝试执行代码
except：捕获特定异常
else：无异常时执行
finally：始终执行
"""

# 7. 文件操作
with open("yt下载链接.txt", "w") as f:
    f.write("Hello, a sen!")

with open("yt下载链接.txt", "r") as f:
    content = f.read()
    print(content)
"""
open()打开文件
模式：r（读）, w（写）, a（追加）, b（二进制）
with语句自动关闭文件
"""

# 8. 模块导入
# 导入整个模块
import math
print(math.pi)

# 导入特定函数
from math import sqrt
print(sqrt(4))

# 别名
import math as m
"""
import导入标准库或第三方库
from...import导入特定对象
as创建别名
"""



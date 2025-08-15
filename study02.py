# Python高级特性详解
"""
1. 迭代函数
迭代是通过循环结构（如 `for`、`while`）重复执行一段代码，直到满足某个条件。

2. 递归函数
如果一个函数在内部不调用其他的函数，而是调用它本身的话，这个函数就是递归函数
条件
a.必须有一个明确的结束条件 ---递归基
b.每进行更深一层的递归，问题规模相比上次递归都要有所减少
c.相邻两次重复之间有紧密的联系
"""
# 迭代函数实现计算1-100累加和
def add():
    s = 0
    '''
# range(start, stop, step)
- start: 序列的起始值（包含在序列中）。如果省略，默认为0。
- stop:  序列的结束值（不包含在序列中）。注意，序列生成到这个值的前一个数。
- step:  步长，即序列中相邻两个数的差值。如果省略，默认为1。
    '''
    for i in range(1, 101):  # 从1开始（包含1）,到101结束（但不包含101）,步长为默认的1
        s += i
    print(s)
add()

# 递归函数
def add2(n):                 # 定义名为 add2 的函数，接收参数 n
    if n == 1:               # 递归的终止条件：当 n 等于 1 时
        return 1             # 返回 1（递归基:这是递归的终止条件）
    return n + add2(n-1)     # 递归调用：返回当前 n 加上 n-1 的递归结果
add2(100)                    # 调用函数，计算从 1 加到 100 的和
"""
### 递归过程分析（以add2(3)为例）：
1. 调用 `add2(3)`：
   - 3 == 1? 否，执行 `return 3 + add2(2)`
2. 调用 `add2(2)`：
   - 2 == 1? 否，执行 `return 2 + add2(1)`
3. 调用 `add2(1)`：
   - 1 == 1? 是，返回1
然后逐层返回：
- `add2(2)` 返回 2 + 1 = 3
- `add2(3)` 返回 3 + 3 = 6
所以，`add2(3)` 的结果是6，即1+2+3=6。
"""
"""
递归的优缺点
优点：
代码简洁优雅,直接表达数学归纳思想,符合问题的自然结构（分而治之）
缺点：
空间复杂度 O(n)（需要存储递归栈）,对于大 n 可能超出递归深度限制,效率低于迭代方法
递归的适用场景
这种递归模式适用于：
计算数列和（如斐波那契数列）,遍历树形结构,解决分治问题（如归并排序）,实现数学归纳法证明
"""

"""
斐波那契数列（Fibonacci sequence）是数学中一个经典序列，其定义如下：
F(0) = 0
F(1) = 1
F(n) = F(n-1) + F(n-2) (当 n > 1)
"""
# 实现斐波那契数列
# 1. 基础递归实现（不推荐用于大数）
def febonacci_recursive(n):
    if n <= 0:
        return 0
    elif n ==1:
        return 1
    else:
        return febonacci_recursive(n-1) + febonacci_recursive(n -2)

print(febonacci_recursive(6)) # 输出: 8
"""
递归缺点：
时间复杂度 O(2^n)，效率极低,重复计算严重,对于 n>35 计算明显变慢
"""

# 2. 迭代实现（推荐）
def febonacci_iterative(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1

    a, b = 0, 1
    for _ in range(2, n+1):
        a, b = b, a + b
    return b
print(febonacci_iterative(6))   # 输出: 55
print(febonacci_iterative(60))  # 输出: 1548008755920
"""
迭代优点：时间复杂度 O(n),空间复杂度 O(1),适合计算大数
"""

# 3. 记忆化递归实现（优化递归）
def febonacci_memo(n, memo= None):
    """使用记忆化优化的递归实现"""
    if memo is None:
        memo = {}       # 如果memo为None，则初始化为空字典。
    if n in memo:
        return memo[n]  # 如果n已经在memo中，直接返回memo[n]。
    if n <= 0:
        result = 0
    elif n == 1:
        result = 1
    else:
        result = febonacci_memo(n-1, memo) + febonacci_memo(n-2, memo)  # 传递同一个 memo 字典给所有递归调用
    memo[n] = result    # 将计算结果存入memo中，键为n，值为计算结果。
    return result
print(febonacci_memo(60))
"""
优点：避免重复计算,时间复杂度 O(n),保留了递归的优雅性
"""







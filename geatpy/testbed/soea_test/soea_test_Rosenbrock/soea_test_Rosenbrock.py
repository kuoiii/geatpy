# -*- coding: utf-8 -*-
import geatpy as ga # import geatpy
import numpy as np

"""==================================实例化问题对象================================"""
problemName = 'Rosenbrock' # 目标函数名
fileName = problemName # 这里因为目标函数写在与之同名的文件里，所以文件名也是目标函数名
MyProblem = getattr(__import__(fileName), problemName) # 获得自定义问题类
problem = MyProblem(30) # 生成问题对象

"""==================================种群设置================================"""
Encoding = 'R'             # 编码方式
conordis = 0               # 表示染色体解码后得到的变量是连续的
NIND = 60                  # 种群规模
precisions = [50] * problem.Dim # 编码精度（适用于二进制/格雷编码）
Field = ga.crtfld(Encoding, conordis, problem.ranges, problem.borders, precisions) # 创建区域描述器
population = ga.Population(Encoding, conordis, Field, NIND) # 实例化种群对象（此时种群还没被真正初始化）

"""==================================算法参数设置================================"""
myAlgorithm = ga.soea_DE_best_1_bin_templet(problem, population) # 实例化一个算法模板对象
myAlgorithm.MAXGEN = 2000 # 最大遗传代数
myAlgorithm.F = 0.7
myAlgorithm.pc = 0.9
myAlgorithm.drawing = 1
"""=======================调用算法模板进行种群进化=============================="""
[population, obj_trace, var_trace] = myAlgorithm.run() # 执行算法模板
# 输出结果
best_gen = np.argmin(obj_trace[:, 1]) # 记录最优种群是在哪一代
best_ObjV = np.min(obj_trace[:, 1])
print('最优的目标函数值为：%s'%(best_ObjV))
print('最优的控制变量值为：')
for i in range(var_trace.shape[1]):
    print(var_trace[best_gen, i])
print('有效进化代数：%s'%(obj_trace.shape[0]))
print('最优的一代是第 %s 代'%(best_gen + 1))
print('评价次数：%s'%(myAlgorithm.evalsNum))
print('时间已过 %s 秒'%(myAlgorithm.passTime))
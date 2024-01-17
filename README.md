# <a name="_toc30313"></a><a name="_toc18589"></a>**数独问题**

## <a name="_toc23612"></a><a name="_toc28316"></a>**一、实验任务**

1 9\*9的矩阵，要求每一行，每一列，每个九宫格都是1-9这九个数字且不能重复。给定一9\*9矩阵，里面有部分数空缺，要求找出满足上述要求的一个矩阵

2 可选算法：搜索+剪枝（递归+回溯）


## <a name="_toc2271"></a>**二、文件描述**

**main.py：主程序**

--draw(ax, grid, stack=None)：绘制九宫格

--prune(ax, old_grid, stack)：剪枝

--dfs(ax)：深度优先搜索求问题的解

## <a name="_toc25648"></a>**三、运行示例** 
白色数字：由题目给出    
绿色数字：深度优先搜索栈中保存的结点   
红色数字：栈中结点搜索的结果      
<img src='https://github.com/yuliang555/sudoku/blob/master/images/%E5%9B%BE%E7%89%871.png' width=40%>
<img src='https://github.com/yuliang555/sudoku/blob/master/images/%E5%9B%BE%E7%89%872.png' width=40%>
<img src='https://github.com/yuliang555/sudoku/blob/master/images/%E5%9B%BE%E7%89%873.png' width=40%>
<img src='https://github.com/yuliang555/sudoku/blob/master/images/%E5%9B%BE%E7%89%874.png' width=40%>

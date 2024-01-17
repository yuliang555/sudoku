import numpy as np
import matplotlib.pyplot as plt
import copy



my_grid = np.array([
    [0, 0, 0, 8, 0, 0, 0, 0, 9],
    [0 ,1, 9, 0, 0, 5, 8, 3, 0],
    [0, 4, 3, 0, 1, 0, 0, 0, 7],
    [4, 0, 0, 1, 5, 0, 0, 0, 3],
    [0, 0, 2, 7, 0, 4, 0, 1, 0],
    [0, 8, 0, 0, 9, 0, 6, 0, 0],
    [0, 7, 0, 0, 0, 6, 3, 0, 0],
    [0, 3, 0, 0, 7, 0, 0, 8, 0],
    [9, 0, 4, 5, 0, 0, 0, 0, 1]            
])
        

def draw(ax, grid, stack=None):
    node_grid = [[0 for i in range(9)] for j in range(9)]
    if stack != None:
        for node in stack:
            i, j, v = node['i'], node['j'], node['v']
            node_grid[i][j] = v
    
    ax.clear()
    ax.set_xticks(np.arange(0.5, 8, step=1))
    ax.set_xticklabels([])
    ax.set_yticks(np.arange(0.5, 8, step=1))
    ax.set_yticklabels([])
    ax.grid(True)
    
    ax.imshow([[1 for i in range(9)] for j in range(9)], interpolation='none', cmap='gray')
    for i in range(9):
        for j in range(9):
            if my_grid[i][j] != 0:
                ax.text(j, i, my_grid[i][j], fontdict={'fontsize': 20}, ha="center", va="center", color="white")
            elif node_grid[i][j] !=0:
                ax.text(j, i, node_grid[i][j], fontdict={'fontsize': 20}, ha="center", va="center", color="g")
            elif grid[i][j] != 0:
                ax.text(j, i, grid[i][j], fontdict={'fontsize': 20}, ha="center", va="center", color="red")
    ax.get_figure().canvas.draw()
    

def prune(ax, old_grid, stack):    
    new_grid = old_grid.copy()
    set1 = {1, 2, 3, 4, 5, 6, 7, 8, 9}
    while True:
        empty = []                           
        for i in range(9):
            for j in range(9):
                if new_grid[i][j] == 0:
                    set2 = set()
                    for k in range(9):
                        if new_grid[i][k] != 0:
                            set2.add(new_grid[i][k])
                        if new_grid[k][j] != 0:
                            set2.add(new_grid[k][j])
                    small_grid_i = i // 3 * 3
                    small_grid_j = j // 3 * 3
                    for m in range(3):
                        for n in range(3):
                            item = new_grid[small_grid_i+m][small_grid_j+n]
                            if item != 0:
                                set2.add(item)
                    value = list(set1 - set2)
                    if len(value) == 0:
                        return False, empty, new_grid
                    empty.append({
                        'i': i,
                        'j': j,
                        'value': value,
                        'len': len(value)
                    })       
        if empty == []:
            return True, empty, new_grid
        else:
            empty.sort(key=lambda s: s['len'])
            if empty[0]['len'] == 1:
                item = empty.pop(0)
                new_grid[item['i']][item['j']] = item['value'][0]
                draw(ax, new_grid, stack)
                plt.pause(0.7)
            else:
                return None, empty, new_grid


def dfs(ax):
    stack = []
    old_grid = my_grid.copy()
    while True:
        status, empty, new_grid = prune(ax, old_grid, stack)
        if status == True:
            return new_grid
        elif status == False:
            while True:
                node = stack[-1]
                if node['value'] == []:
                    stack.pop()
                else:
                    i, j = node['i'], node['j']
                    v = node['value'].pop()
                    node['v'] = v
                    old_grid = node['grid'].copy()
                    old_grid[i][j] = v
                    break
        else:
            i, j = empty[0]['i'], empty[0]['j']
            v = empty[0]['value'].pop()
            node = {
                'i': i,
                'j': j,
                'v': v,
                'value': empty[0]['value'].copy(),
                'grid': new_grid.copy()
            }
            stack.append(node)
            old_grid = new_grid
            old_grid[i][j] = v

            
fig, ax = plt.subplots(1, 1, tight_layout=True)
fig.canvas.setWindowTitle("Sudoku")
draw(ax, my_grid)            
plt.pause(1)
print(my_grid)            
print(dfs(ax))
plt.show()     
        
                    






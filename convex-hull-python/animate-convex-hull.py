import numpy as np
import matplotlib.pyplot as plt
from pprint import pprint

def set_to_xy(s):
    x = [i[0] for i in s]
    y = [i[1] for i in s]
    return x, y

def xy_to_set(x, y):
    s = {(i, j) for i, j in zip(x, y)}
    return s

def draw_convexhull(P, color='r'):
    x, y = set_to_xy(P)
    N = len(x)
    for i in range(0, N):
        x1, y1 = x[i], y[i]
        x2, y2 = x[(i + 1) % N], y[(i + 1) % N]
        plt.plot([x1, x2], [y1, y2], '-', color=color)
        # plt.text(x1, y1, f'P{i}({x1}, {y1})')

N = 30
f = open('starting-points.txt', 'r').read().split('\n')
x = [int(i) for i in f[0].split(', ')[:-1]]
y = [int(i) for i in f[1].split(', ')[:-1]]

P = xy_to_set(x, y)
# print(f'P = {P}')
P = sorted(P, key=lambda x: x[0])
# print(f'P = {P}')

max_depth = 0
f = open('convex-hull-points.txt', 'r').read().split('\n')
convex_hulls = []
for line in f:
    if len(line) <= 0: continue
    # print(line)
    numbers = [int(i) for i in line.split(', ')[:-1]]
    # print(numbers)
    depth = numbers[0]
    if depth > max_depth:
        max_depth = depth
    convex_hull = numbers[1:-1]
    CH_length = numbers[-1]
    # print(depth, convex_hull, CH_length)
    S = [(convex_hull[i], convex_hull[i + 1]) for i in range(0, 2 * CH_length, 2)]
    # print(S)
    convex_hulls.append({
        'depth': depth,
        'CH_length': CH_length,
        'points': S,
    })

# print(f'max_depth = {max_depth}')
# print(f'S = {convex_hulls[-1]["points"]}')
# pprint(convex_hulls)
# print(f'P = {len(P)}, S = {len(S)}')

for d in range(max_depth + 1):
    for i, convex_hull in enumerate(convex_hulls):
        if convex_hull['depth'] == max_depth - d:
            S = convex_hull['points']
            xS, yS = set_to_xy(S)
            rgb = (np.random.random(), np.random.random(), np.random.random())
            draw_convexhull(S, rgb)
            plt.plot(xS, yS, 'og')
            plt.plot(x, y, '*r')
    print(f'{d}.jpg')
    plt.savefig(f'{d}.jpg', dpi=300)
    plt.clf()
# plt.show()

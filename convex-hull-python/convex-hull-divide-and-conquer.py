import time
import numpy as np
import matplotlib.pyplot as plt

def set_to_xy(s):
    x = [i[0] for i in s]
    y = [i[1] for i in s]
    return x, y

def xy_to_set(x, y):
    s = {(i, j) for i, j in zip(x, y)}
    return s

def angle(p):
    global mid
    p2 = (p[0] - mid[0], p[1] - mid[1])
    if p2[0] != 0:
        angle_ = np.abs(np.arctan(p2[1] / p2[0])) * 180 / np.pi
    else:
        angle_ = 90.0
    # print(f'angle_ = {angle_}, p = {p}, p2 = {p2}')
    if p2[0] < 0 and p2[1] < 0:
        angle_ = 180 + angle_
    if p2[0] < 0 and p2[1] > 0:
        angle_ = 180 - angle_
    if p2[0] > 0 and p2[1] < 0:
        angle_ = 360 - angle_
    # print(f'angle_ = {angle_}, p = {p}, p2 = {p2}')
    return angle_

def convexhull_bruteforce(P):
    global mid

    N = len(P)
    S = set()
    for i in range(N):
        for j in range(i+1, N):
            x1, y1 = P[i]
            x2, y2 = P[j]
            a = y1 - y2
            b = x2 - x1
            c = x1 * y2 - x2 * y1
            positive, negative = 0, 0
            for k in range(N):
                x3, y3 = P[k]
                if a * x3 + b * y3 + c >= 0:
                    positive += 1
                if a * x3 + b * y3 + c <= 0:
                    negative += 1
            if positive == N or negative == N:
                S.add(P[i])
                S.add(P[j])
    
    x, y = set_to_xy(S)
    mid = (np.average(x), np.average(y))
    S = sorted(S, key=angle)
    return S

def line(p1, p2, x):
    # print(f'[line] p1 = {p1}, p2 = {p2}')
    x1, y1 = p1
    x2, y2 = p2
    a = y1 - y2
    b = x2 - x1
    c = x1 * y2 - x2 * y1
    return (-a / b) * x - (c / b)

def merge(left, right):
    global mid

    N_left = len(left)
    N_right = len(right)
    pivot_left = 0
    pivot_right = 0

    for i in range(N_left):
        if left[i][0] > left[pivot_left][0]:
            pivot_left = i

    for j in range(N_right):
        if right[j][0] < right[pivot_right][0]:
            pivot_right = j
    
    use_trick = left[pivot_left][0] == right[pivot_right][0]
    if use_trick:
        left[pivot_left] = (left[pivot_left][0] - 1, left[pivot_left][1])
        right[pivot_right] = (right[pivot_right][0] + 1, right[pivot_right][1])
    x_mid = (left[pivot_left][0] + right[pivot_right][0]) / 2
    # print(f'[merge] x_mid = {x_mid}')
    
    # find upper tangent
    i = pivot_left
    j = pivot_right
    # print(f'[merge] i = {i}, j = {j}')
    while line(left[i], right[(j - 1) % N_right], x_mid) > line(left[i], right[j], x_mid) or \
          line(left[(i + 1) % N_left], right[j], x_mid) > line(left[i], right[j], x_mid):
        if line(left[i], right[(j - 1) % N_right], x_mid) > line(left[i], right[j], x_mid):
            j = (j - 1) % N_right
        else:
            i = (i + 1) % N_left
        # print(f'[merge] i = {i}, j = {j}')
    upper_left = i
    upper_right = j

    # find lower tangent
    i = pivot_left
    j = pivot_right
    # print(f'[merge] i = {i}, j = {j}')
    while line(left[i], right[(j + 1) % N_right], x_mid) < line(left[i], right[j], x_mid) or \
          line(left[(i - 1) % N_left], right[j], x_mid) < line(left[i], right[j], x_mid):
        if line(left[i], right[(j + 1) % N_right], x_mid) < line(left[i], right[j], x_mid):
            j = (j + 1) % N_right
        else:
            i = (i - 1) % N_left
        # print(f'[merge] i = {i}, j = {j}')
    lower_left = i
    lower_right = j

    if use_trick:
        left[pivot_left] = (left[pivot_left][0] + 1, left[pivot_left][1])
        right[pivot_right] = (right[pivot_right][0] - 1, right[pivot_right][1])

    # print(f'[merge] upper_left = {upper_left}, lower_left = {lower_left}, lower_right = {lower_right}, upper_right = {upper_right}')

    merged_convexhull = []
    idx = upper_left
    while idx != lower_left:
        # print(f'[merge] idx = {idx}')
        merged_convexhull.append(left[idx])
        idx = (idx + 1) % N_left
    merged_convexhull.append(left[idx])
    
    idx = lower_right
    while idx != upper_right:
        # print(f'[merge] idx = {idx}')
        merged_convexhull.append(right[idx])
        idx = (idx + 1) % N_right
    merged_convexhull.append(right[idx])

    x, y = set_to_xy(merged_convexhull)
    mid = (np.average(x), np.average(y))
    merged_convexhull = sorted(merged_convexhull, key=angle)
    return merged_convexhull

def convexhull(P, depth):
    N = len(P)
    # print(f'[convexhull] N = {N}')
    # print(f'[convexhull] P = {P}')
    if N <= 5:
        return convexhull_bruteforce(P)
    
    leftP = P[:N // 2]
    rightP = P[N // 2:]

    left_convexhull = convexhull(leftP, depth + 1)
    right_convexhull = convexhull(rightP, depth + 1)
    # print(f'[convexhull] left_convexhull = {left_convexhull}')
    # print(f'[convexhull] right_convexhull = {right_convexhull}')
    # with open('convex-hull-points.txt', 'a') as file:
    #     # write left_convexhull
    #     file.write(f'{depth}, ')
    #     for pair in left_convexhull:
    #         file.write(f'{str(pair[0])}, {str(pair[1])}, ')
    #     file.write(f'{len(left_convexhull)}, ')
    #     file.write('\n')
    #     # write right_convexhull
    #     file.write(f'{depth}, ')
    #     for pair in right_convexhull:
    #         file.write(f'{str(pair[0])}, {str(pair[1])}, ')
    #     file.write(f'{len(right_convexhull)}, ')
    #     file.write('\n')

    return merge(left_convexhull, right_convexhull)

def draw_convexhull(P, color='r'):
    x, y = set_to_xy(P)
    N = len(x)
    for i in range(0, N):
        x1, y1 = x[i], y[i]
        x2, y2 = x[(i + 1) % N], y[(i + 1) % N]
        plt.plot([x1, x2], [y1, y2], '-' + color)
        # plt.text(x1, y1, f'P{i}({x1}, {y1})')

mid = (0, 0)

N = 100
x = [1, 1, 1]
y = [1, 1, 1]
while len(np.unique(x)) != N or len(np.unique(y)) != N:
    x = np.random.randint(-N*N, N*N, N)
    y = np.random.randint(-N*N, N*N, N)
    if len(x) % 50 == 0:
        print(len(np.unique(x)), len(np.unique(y)))
print(len(np.unique(x)) == N)
print(len(np.unique(y)) == N)
# x = np.random.randint(-100, 100, N)
# y = np.random.randint(-100, 100, N)

# with open('points.txt', 'w') as file:
#     for i in x:
#         file.write(str(i) + ', ')
#     file.write('\n')
#     for i in y:
#         file.write(str(i) + ', ')
#     file.write('\n')
# f = open('starting-points.txt', 'r').read().split('\n')
# x = [int(i) for i in f[0].split(', ')[:-1]]
# y = [int(i) for i in f[1].split(', ')[:-1]]

P = xy_to_set(x, y)
# print(f'P = {P}')
P = sorted(P, key=lambda x: x[0])
# print(f'P = {P}')

# with open('convex-hull-points.txt', 'w') as file:
#     pass
t1 = time.time()
S = convexhull_bruteforce(P)
t2 = time.time()
print(f'time taken: {(t2 - t1) * 100} ms')

depth = 0
t1 = time.time()
S = convexhull(P, depth + 1)
t2 = time.time()
print(f'time taken: {(t2 - t1) * 100} ms')
# with open('convex-hull-points.txt', 'a') as file:
#     file.write(f'{depth}, ')
#     for pair in S:
#         file.write(f'{str(pair[0])}, {str(pair[1])}, ')
#     file.write(f'{len(S)}, ')
#     file.write('\n')

# print(f'S = {S}')
# print(f'convex_hull = {convex_hull}')
# print(f'P = {len(P)}, S = {len(S)}')
xS, yS = set_to_xy(S)

draw_convexhull(S, 'r')
plt.plot(xS, yS, 'og')
plt.plot(x, y, '*r')
# plt.plot(*mid, 'ok')
plt.savefig(f'convex-hull-{N}.png', dpi=300)
plt.show()

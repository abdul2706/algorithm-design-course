import numpy as np
import matplotlib.pyplot as plt

def set_to_xy(s):
    x = [i[0] for i in s]
    y = [i[1] for i in s]
    return x, y

def xy_to_set(x, y):
    s = {(i, j) for i, j in zip(x, y)}
    return s

# def quadrant(p):
#     if p[0] >= 0 and p[1] >= 0:
#         return 1
#     elif p[0] < 0 and p[1] >= 0:
#         return 2
#     elif p[0] < 0 and p[1] < 0:
#         return 3
#     return 4

# def compare(p1, q1):
#     global mid
#     p2 = (p1[0] - mid[0], p1[1] - mid[1])
#     q2 = (q1[0] - mid[0], q1[1] - mid[1])
#     p2_quad = quadrant(p2)
#     q2_quad = quadrant(q2)
#     if (p2_quad != q2_quad):
#         return p2_quad < q2_quad
#     return p2[1] * q2[0] < p2[0] * q2[1]

def angle(p):
    global mid
    p2 = (p[0] - mid[0], p[1] - mid[1])
    angle_ = np.abs(np.arctan(p2[1] / p2[0])) * 180 / np.pi
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
    
    xS, yS = set_to_xy(S)
    mid = (np.average(xS), np.average(yS))
    # print(f'S = {S}')
    S = sorted(S, key=angle)
    # print(f'S = {S}')

    return S

mid = (0, 0)

N = 100
x = np.random.randint(0, 100, N)
y = np.random.randint(0, 100, N)
P = xy_to_set(x, y)
# print(f'P = {P}')
P = sorted(P, key=lambda x: x[0])
# print(f'P = {P}')

S = convexhull_bruteforce(P)
# print(f'S = {S}')
print(f'P = {len(P)}, S = {len(S)}')
xS, yS = set_to_xy(S)

Ns = len(xS)
for i in range(0, Ns):
    x1, y1 = xS[i], yS[i]
    x2, y2 = xS[(i + 1) % Ns], yS[(i + 1) % Ns]

    a = y1 - y2
    b = x2 - x1
    c = x1 * y2 - x2 * y1
    
    plt.plot([x1, x2], [y1, y2], '-k')
    plt.text(x1, y1, f'P{i}({x1}, {y1})')

plt.plot(xS, yS, 'og')
plt.plot(x, y, '*r')
# plt.plot(*mid, 'ok')

plt.show()

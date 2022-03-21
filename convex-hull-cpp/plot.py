import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

max_points = 10000000
step_size = 50000
df = pd.read_csv(f'convex-hull-{max_points}-{step_size}.csv')
df.columns = ['n', 'cpu_time']
df = df.drop(index=[0], axis='index')
print(df)

model = LinearRegression()
X, y = df['n'].values.reshape(-1, 1), df['cpu_time'].values.reshape(-1, 1)
print(X.shape, y.shape)
model.fit(X, y)
predicted_cpu_time = model.predict(X)

plt.figure(figsize=(12, 8))
plt.suptitle('CGAL Convex Hull Algorithm Benchmark')

c1 = 2.5e-14
plt.plot(df['n'], c1 * df['n'] * df['n'], label='O(n^2)')
c2 = 8e-8
plt.plot(df['n'], c2 * df['n'], label='O(n)')
c3 = 5e-3
plt.plot(df['n'], c3 * np.log(df['n']), label='O(log(n))')

c4 = 2.5e-8
plt.plot(df['n'], c4 * df['n'] * np.log(df['n']), '--k', label='O(n*log(n))')
c5 = 1.2e-8
plt.plot(df['n'], c5 * df['n'] * np.log(df['n']), '--k', label='Ω(n*log(n))')

plt.plot(df['n'], df['cpu_time'], 'or', markersize=2, label='CGAL')
plt.plot(df['n'], predicted_cpu_time, label='LinearRegression')

plt.xlabel('Points')
plt.ylabel('Time Taken')

plt.legend(fontsize=12)
plt.savefig(f'plot-{max_points}-{step_size}.jpg', dpi=300)
plt.show()

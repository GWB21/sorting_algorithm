import numpy as np
import matplotlib.pyplot as plt

# 데이터 설정
n = np.linspace(1, 10, 100)  # x 값 (1부터 10까지)
O_n = n                      # O(n)
O_2n = 2 * n                 # O(2n)

# 그래프 그리기
plt.figure(figsize=(10, 6))
plt.plot(n, O_n, label='O(n)', color='blue')
plt.plot(n, O_2n, label='O(2n)', color='orange', linestyle='--')
plt.title('Comparison of O(n) and O(2n)')
plt.xlabel('Input size (n)')
plt.ylabel('Time Complexity')
plt.axhline(0, color='black',linewidth=0.5, ls='--')
plt.axvline(0, color='black',linewidth=0.5, ls='--')
plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
plt.legend()
plt.xlim(0, 10**10)
plt.ylim(0, 22)
plt.show()

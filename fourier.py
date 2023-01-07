import numpy as np
import matplotlib.pyplot as plt
import time

%matplotlib inline

import functools
import matplotlib.pyplot as plt
import cmath
import random

import numpy as np
# データのパラメータ
N = 2**20           # サンプル数,ここを変更して実験する
dt = 0.01          # サンプリング間隔
f1, f2 = 10, 20    # 周波数
t = np.arange(0, N*dt, dt) # 時間軸
freq = np.linspace(0, 1.0/dt, N) # 周波数軸

# 信号を生成（周波数10の正弦波+周波数20の正弦波+ランダムノイズ）
f = np.sin(2*np.pi*f1*t) + np.sin(2*np.pi*f2*t) + 0.3 * np.random.randn(N)

# ここからFFTの実行をするため、その時間を測り始める
time_sta = time.time()
# 高速フーリエ変換
F = np.fft.fft(f)
time_end = time.time()
tim = time_end- time_sta
print(tim)
#FFT自体はここで終わりなので、止める

# DFTの定義
def dft(f):
    n = len(f)
    A = np.arange(n)
    M = cmath.e**(-1j * A.reshape(1, -1) * A.reshape(-1, 1) * 2 * cmath.pi / n)
    return np.sum(f * M, axis=1)
# DFTはここから始まるのでタイマーをセット
time_sta = time.time()
fy = dft(f)
time_end = time.time()
tim = time_end- time_sta
print(tim)
#DFTはここで終わりなので止める。

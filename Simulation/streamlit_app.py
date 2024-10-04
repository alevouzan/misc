import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import convolve2d
import streamlit as st

nx, ny = 600, 450
alpha, beta, gamma = 1, 1, 1

def update(p, arr):
    q = (p + 1) % 2
    s = np.zeros((3, ny, nx))
    m = np.ones((3, 3)) / 9
    for k in range(3):
        s[k] = convolve2d(arr[p, k], m, mode='same', boundary='wrap')
    arr[q, 0] = s[0] + s[0] * (alpha * s[1] - gamma * s[2])
    arr[q, 1] = s[1] + s[1] * (beta * s[2] - alpha * s[0])
    arr[q, 2] = s[2] + s[2] * (gamma * s[0] - beta * s[1])
    np.clip(arr[q], 0, 1, arr[q])
    return arr

arr = np.random.random(size=(2, 3, ny, nx))

st.title("Reaction-Diffusion Simulation")
frames = st.slider("Number of frames", min_value=1, max_value=500, value=100, step=10)

fig, ax = plt.subplots()
im = ax.imshow(arr[0, 0], cmap=plt.cm.winter)
ax.axis('off')

for i in range(frames):
    arr = update(i % 2, arr)
    im.set_array(arr[i % 2, 0])
    st.pyplot(fig)

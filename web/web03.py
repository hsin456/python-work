import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

x=np.linspace(-10,10,200)
y=np.sinc(x)
plt.plot(x,y)
st.pyplot()
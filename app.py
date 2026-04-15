import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

# Load data [cite: 535]
df = pd.read_csv('poll_data.csv')

st.title("📊 Poll Results Visualizer") [cite: 536]

# Sidebar for interactivity [cite: 537, 538]
st.sidebar.header("Filter Results")
tool_filter = st.sidebar.multiselect("Select Tool:", df['Preferred Tool'].unique(), default=df['Preferred Tool'].unique()) [cite: 539]
filtered_df = df[df['Preferred Tool'].isin(tool_filter)] [cite: 540]

# Metrics
st.subheader("Project Statistics")
st.write(f"Total Responses: {len(filtered_df)}")

# Bar Chart [cite: 544, 549]
st.subheader("Tool Preferences")
fig, ax = plt.subplots()
sns.countplot(data=filtered_df, x='Preferred Tool', palette='Set2', ax=ax)
st.pyplot(fig) [cite: 555]

# Word Cloud [cite: 563, 565]
st.subheader("Feedback Keywords")
text = ' '.join(filtered_df['Feedback'].astype(str))
if text.strip():
    wc = WordCloud(width=800, height=400, background_color='white').generate(text)
    fig_wc, ax_wc = plt.subplots()
    ax_wc.imshow(wc, interpolation='bilinear')
    ax_wc.axis('off')
    st.pyplot(fig_wc) [cite: 573]
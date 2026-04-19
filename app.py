import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

# Load data
df = pd.read_csv('poll_data.csv')
df['Timestamp'] = pd.to_datetime(df['Timestamp']) # [cite: 412]

st.title("📊 Poll Results Visualizer")

# Sidebar for interactivity
st.sidebar.header("Filter Results")
tool_filter = st.sidebar.multiselect("Select Tool:", df['Preferred Tool'].unique(), default=df['Preferred Tool'].unique())
filtered_df = df[df['Preferred Tool'].isin(tool_filter)]

# 1. Project Statistics [cite: 542]
st.subheader("Project Statistics")
st.write(f"Total Responses: {len(filtered_df)}")

# 2. Bar Chart - Tool Preference [cite: 546]
st.subheader("Tool Preferences")
fig1, ax1 = plt.subplots()
sns.countplot(data=filtered_df, x='Preferred Tool', hue='Preferred Tool', palette='Set2', ax=ax1, legend=False)
st.pyplot(fig1)

# 3. Line Plot - Submissions Over Time [cite: 558]
st.subheader("Responses Over Time")
daily = filtered_df.groupby(filtered_df['Timestamp'].dt.date).size()
st.line_chart(daily)

# 4. Histogram - Satisfaction Ratings [cite: 552]
st.subheader("Satisfaction Ratings")
fig2, ax2 = plt.subplots()
sns.histplot(filtered_df['Satisfaction (1-5)'], bins=5, kde=True, ax=ax2)
st.pyplot(fig2)

# 5. Word Cloud - Feedback Keywords [cite: 565]
st.subheader("Feedback Word Cloud")
text = ' '.join(filtered_df['Feedback'].dropna().astype(str))
if text.strip():
    wc = WordCloud(width=800, height=400, background_color='white').generate(text)
    fig_wc, ax_wc = plt.subplots()
    ax_wc.imshow(wc, interpolation='bilinear')
    ax_wc.axis('off')
    st.pyplot(fig_wc)
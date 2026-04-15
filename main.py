import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

# 1. Load Data [cite: 315]
df = pd.read_csv("poll_data.csv")

# 2. Cleaning [cite: 385]
df = df.drop_duplicates() # Remove duplicates [cite: 391]
df = df.dropna(subset=['Preferred Tool', 'Satisfaction (1-5)']) # Handle missing values [cite: 398]
df['Preferred Tool'] = df['Preferred Tool'].str.strip().str.title() # Standardize text [cite: 404]

# 3. Visualization - Tool Preference [cite: 449, 452]
plt.figure(figsize=(8,5))
sns.countplot(x='Preferred Tool', data=df, hue='Preferred Tool', palette='Set2', legend=False)
plt.title('Most Preferred Tools')
plt.savefig('outputs/tool_preference.png') # Save for GitHub proof [cite: 162]
plt.show()

# 4. Word Cloud for Feedback [cite: 484, 487]
text = ' '.join(df['Feedback'].astype(str).tolist())
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title("Common Words in Feedback")
plt.show()

# 5. Convert Timestamp and Plot Daily Trends [cite: 412, 473]
df['Timestamp'] = pd.to_datetime(df['Timestamp']) 
df['Date'] = df['Timestamp'].dt.date
daily_counts = df.groupby('Date').size()

plt.figure(figsize=(8,4))
daily_counts.plot(kind='line', marker='o', color='green')
plt.title('Daily Poll Submissions')
plt.xlabel('Date')
plt.ylabel('Number of Responses')
plt.grid(True)
plt.savefig('outputs/daily_trends.png') # Proof for GitHub [cite: 162]
plt.show()

# 6. Satisfaction Rating Distribution [cite: 463]
plt.figure(figsize=(6,4))
sns.histplot(df['Satisfaction (1-5)'], bins=5, kde=True, color='skyblue')
plt.title('Satisfaction Rating Distribution')
plt.xlabel('Rating (1-5)')
plt.ylabel('Frequency')
plt.savefig('outputs/satisfaction_distribution.png')
plt.show()

# 7. Save the Cleaned Dataset [cite: 420]
df.to_csv("data/cleaned_poll_data.csv", index=False)
print("Cleaned data saved to 'data/cleaned_poll_data.csv' [cite: 424]")
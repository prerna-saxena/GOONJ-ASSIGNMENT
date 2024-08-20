import matplotlib.pyplot as plt
import seaborn as sns

# Trend of Activities and Distributions
plt.figure(figsize=(12, 6))
sns.lineplot(data=monthly_summary, x='ActivityMonth', y='NumActivities', hue='ActivityYear', marker='o')
sns.lineplot(data=monthly_summary, x='ActivityMonth', y='NumDistributions', hue='ActivityYear', linestyle='--', marker='o')
plt.title('Monthly Trends of Activities and Distributions')
plt.xlabel('Month')
plt.ylabel('Count')
plt.legend(title='Year')
plt.grid(True)
plt.show()

# Activities by Type and SubType
plt.figure(figsize=(12, 6))
sns.barplot(data=activity_summary, x='ActivityType', y='NumActivities', hue='ActivitySubType')
plt.title('Activities by Type and SubType')
plt.xlabel('Activity Type')
plt.ylabel('Number of Activities')
plt.xticks(rotation=45)
plt.legend(title='Activity SubType')
plt.grid(True)
plt.show()

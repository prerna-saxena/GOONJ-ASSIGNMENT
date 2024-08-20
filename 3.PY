import pandas as pd

# Load the data
activities = pd.read_csv('Activities.csv')
activity_distribution = pd.read_csv('ActivityDistribution.csv')
distributions = pd.read_csv('Distribution.csv')

# Merge the data
merged = activity_distribution.merge(activities, on='ActivityID').merge(distributions, on='DistributionID')

# Aggregated data by Activity Type and SubType
activity_summary = merged.groupby(['ActivityType', 'ActivitySubType']).agg(
    NumDistributions=('DistributionID', 'count'),
    NumActivities=('ActivityID', 'count')
).reset_index()

activity_summary.to_csv('activity_summary.csv', index=False)

# Yearly and Monthly Aggregation
merged['ActivityYear'] = pd.to_datetime(merged['ActivityStartDate']).dt.year
merged['ActivityMonth'] = pd.to_datetime(merged['ActivityStartDate']).dt.month
merged['DistributionYear'] = pd.to_datetime(merged['DistributionDate']).dt.year
merged['DistributionMonth'] = pd.to_datetime(merged['DistributionDate']).dt.month

monthly_summary = merged.groupby(['ActivityYear', 'ActivityMonth']).agg(
    NumActivities=('ActivityID', 'count'),
    NumDistributions=('DistributionID', 'count')
).reset_index()

monthly_summary.to_csv('monthly_summary.csv', index=False)

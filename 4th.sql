-- a. Number of activities done in year 2023
SELECT COUNT(*) AS NumberOfActivities
FROM Activities
WHERE strftime('%Y', ActivityStartDate) = '2023';

-- b. Number of activities done in month of May
SELECT COUNT(*) AS NumberOfActivities
FROM Activities
WHERE strftime('%m', ActivityStartDate) = '05';

-- c. Number of activities with no distribution
SELECT COUNT(*) AS NumberOfActivitiesWithNoDistribution
FROM Activities
LEFT JOIN ActivityDistribution ON Activities.ActivityID = ActivityDistribution.ActivityID
WHERE ActivityDistribution.ActivityID IS NULL;

-- d. Number of distributions with no activities
SELECT COUNT(*) AS NumberOfDistributionsWithNoActivities
FROM Distribution
LEFT JOIN ActivityDistribution ON Distribution.DistributionID = ActivityDistribution.DistributionID
WHERE ActivityDistribution.DistributionID IS NULL;

-- e. List of states with number of distributions sorted in descending order
-- Assuming "Distribution" table has a 'State' column
SELECT State, COUNT(*) AS NumberOfDistributions
FROM Distribution
GROUP BY State
ORDER BY NumberOfDistributions DESC;

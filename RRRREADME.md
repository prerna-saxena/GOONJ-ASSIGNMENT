Merging and Creating CSV Files
Read the CSV Files: Use Python's pandas library to read the files.

Merge the Files:

Load Activities.csv, ActivityDistribution.csv, and Distribution.csv.
Merge them based on the IDs present in ActivityDistribution.csv.
Create the Desired CSV Files:

a. Aggregated Data by Activity Type and SubType

Activity Type, Activity SubType, NumDistributions, NumActivities
NumDistributions: Count of distributions for each activity type and subtype.
NumActivities: Count of activities for each activity type and subtype.
b. Yearly and Monthly Aggregation

Year, Month, Num Activities, Num Distributions
Year and Month: Derived from Activity Start Date and Distribution Date.
Num Activities: Count of activities per year and month.
Num Distributions: Count of distributions per year and month.

Visualization
1. Potential Data Insights and Visualization Options:

a. Information Derived:

Trend of Activities and Distributions Over Time: To observe how activity and distribution volumes change over the months and years.
Activity Types and Their Distributions: To understand which activity types have more distributions and activities.
b. Visualization Options:

Line Chart: Show trends of NumActivities and NumDistributions over time.
Bar Chart: Compare NumDistributions and NumActivities across different activity types and subtypes.


. Read Files and Enter Data into a Database
Database Choice: SQLite

Reason for Choosing SQLite:

Ease of Use: SQLite is lightweight and does not require server installation.
Local Storage: Ideal for handling local datasets and small to medium-sized projects.
Integrated: Many programming environments support SQLite natively.
Good for Prototyping: Suitable for quickly creating and managing databases for small projects.
Implementation Steps:

Read the Files: Use Python's pandas library to read the CSV files.

Create SQLite Database and Tables: Define the schema and create tables.

Insert Data: Validate and insert data into the tables. Record erroneous entries

Adjust column names and table structures according to the actual schema in your CSV files.
Use SQL commands in an SQLite client or through a Python script using sqlite3 to execute these queries.

import pandas as pd

# Load the Excel sheets into dataframes
before_df = pd.read_excel('C:/Test/Before_Prod/qTest_UserProfile_Permission_ProjectSpecific.xlsx')
after_df = pd.read_excel('C:/Test/After_Prod/qTest_UserProfile_Permission_ProjectSpecific.xlsx')

# Find differences in values for each column
diff_dict = {}
for column in before_df.columns:
    diff_values = set(before_df[column]) ^ set(after_df[column])
    if diff_values:
        diff_dict[column] = diff_values

# Display the differences
print("Differences between before and after:")
for column, diff_values in diff_dict.items():
    print(f"Column: {column}")
    print(f"Differences: {diff_values}")
    print()

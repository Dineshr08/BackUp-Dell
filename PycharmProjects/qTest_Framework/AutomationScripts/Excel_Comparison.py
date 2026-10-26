import pandas as pd

# Load the two Excel files into DataFrames
Before = pd.read_excel('C:/Test/Before_Stage/qTest_BearerToken.xlsx', engine='openpyxl')
After = pd.read_excel('C:/Test/After_Stage/qTest_BearerToken.xlsx', engine='openpyxl')


# Compare the DataFrames
are_equal = Before.equals(After)

if are_equal:
    print("The two DataFrames are equal.")
else:
    print("The two DataFrames are not equal.")

    # Find the differences
    diff_df = pd.concat([Before, After]).drop_duplicates(keep=False)
    print("Differences:")
    print(diff_df)
# diff.to_excel('differences.xlsx', index=False)

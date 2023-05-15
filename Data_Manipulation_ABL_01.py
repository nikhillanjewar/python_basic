import pandas as pd
df1 = 0;


# Filtering data
def filter_data(df, condition):
    filtered_df = df[condition]
    return filtered_df

# Sorting data
def sort_data(df, column, ascending=True):
    sorted_df = df.sort_values(by=column, ascending=ascending)
    return sorted_df

# Merging data
def merge_data(df1, df2, column):
    merged_df = pd.merge(df1, df2, on=column)
    return merged_df

# Example usage
# Assuming we have two dataframes: df1 and df2

# Filtering data
filtered_df1 = filter_data(df1, df1['column_name'] > 10)

# Sorting data
sorted_df2 = sort_data(df2, 'column_name', ascending=False)

# Merging data
merged_df = merge_data(df1, df2, 'common_column')

# Print the resulting dataframes
print("Filtered Data:")
print(filtered_df1)

print("\nSorted Data:")
print(sorted_df2)

print("\nMerged Data:")
print(merged_df)

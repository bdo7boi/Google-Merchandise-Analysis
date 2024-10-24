import pandas as pd

# Read the datasets
#Replace with path to each data set
events_df = pd.read_csv('C:\\Users\\Provectus Alpha\\Desktop\\Sample Datasets\\Google_Merchandise_datasets\\events1.csv')
users_df = pd.read_csv('C:\\Users\\Provectus Alpha\\Desktop\\Sample Datasets\\Google_Merchandise_datasets\\users.csv')
items_df = pd.read_csv('C:\\Users\\Provectus Alpha\\Desktop\\Sample Datasets\\Google_Merchandise_datasets\\items.csv')

# Convert date columns to datetime
events_df['date'] = pd.to_datetime(events_df['date'])
users_df['date'] = pd.to_datetime(users_df['date'])

# Merge events with items to get product details
events_items_df = pd.merge(events_df, items_df, left_on='item_id', right_on='id', how='inner')

# Merge the above result with users to get user details
merged_df = pd.merge(events_items_df, users_df, left_on='user_id', right_on='id', how='inner')

# Drop redundant columns
merged_df.drop(columns=['id_x', 'id_y'], inplace=True)

# Group products by theme
def assign_theme(product_name):
    if product_name.startswith('#IAmRemarkable'):
        return '#IAmRemarkable'
    elif product_name.startswith('Android'):
        return 'Android'
    elif product_name.startswith('Google'):
        return 'Google'
    elif product_name.startswith('Stan and Friends'):
        return 'Stan and Friends'
    elif product_name.startswith('Supernatural'):
        return 'Supernatural'
    elif product_name.startswith('YouTube'):
        return 'YouTube'
    else:
        return 'Other'

# Apply the function to create a new column in the merged DataFrame
merged_df['Product Theme'] = merged_df['name'].apply(assign_theme)

# Total sales by product theme
theme_sales = merged_df[merged_df['type'] == 'purchase'].groupby('Product Theme')['price_in_usd'].sum().reset_index()
theme_sales.columns = ['Product Theme', 'Total Sales (USD)']

# Number of purchases per product theme
theme_purchase_counts = merged_df[merged_df['type'] == 'purchase'].groupby('Product Theme').size().reset_index(name='Number of Purchases')

# Merge sales and purchase counts by theme for analysis
theme_performance = pd.merge(theme_sales, theme_purchase_counts, on='Product Theme')

# Save the grouped data to a CSV for Tableau
theme_performance.to_csv('product_theme_performance.csv', index=False)

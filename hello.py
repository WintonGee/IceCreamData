from preswald import text, plotly, connect, get_df, table
import pandas as pd
import plotly.express as px

text("# Welcome to Preswald!")
text("Data found on Kaggle for Ice Cream sales w/ Temperature. 🎉")

# Load the CSV
connect() # load in all sources, which by default is the sample_csv
df = get_df('sample_csv')

# Create a scatter plot
fig = px.scatter(df, x='Temperature_F', y='Ice_Cream_Sales_thousands',
                 title='Temperature vs Ice Cream Sales',
                 labels={'Temperature_F': 'Quantity', 'Ice_Cream_Sales_thousands': 'Value'})

# Add labels for each point
fig.update_traces(textposition='top center', marker=dict(size=12, color='lightblue'))

# Style the plot
fig.update_layout(template='plotly_white')

# Show the plot
plotly(fig)

# Show the data
table(df)

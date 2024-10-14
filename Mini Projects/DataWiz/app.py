import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import io
from PIL import Image

# Function to generate a download link for the plot
def generate_download_link(fig, filename="plot.png"):
    buf = io.BytesIO()
    fig.savefig(buf, format="png")
    buf.seek(0)
    return st.download_button(
        label="Download Plot",
        data=buf,
        file_name=filename,
        mime="image/png"
    )

# Title of the Streamlit app
st.set_page_config(
    page_title='Comprehensive CSV Data Visualization App',
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",

)

# File uploader for CSV files
uploaded_file = st.file_uploader('Upload your CSV file', type=['csv'])

if uploaded_file is not None:
    # Read the CSV file
    df = pd.read_csv(uploaded_file)
    st.write('Data Preview:')
    st.dataframe(df)

    # Initialize session state variables to hold datasets and the filter button state
    if "df_filtered" not in st.session_state:
        st.session_state.df_filtered = None
    if "null_values_filtered" not in st.session_state:
        st.session_state.null_values_filtered = False

    # Button to filter out null values
    if st.button('Filter out null values'):
        if df.isnull().values.any():
            st.session_state.df_filtered = df.dropna()
            st.session_state.null_values_filtered = True
            st.write('Null values removed. Updated Data:')
            st.dataframe(st.session_state.df_filtered)
        else:
            st.session_state.null_values_filtered = False
            st.write('No null values found in the dataset.')

    # Dropdown menu for choosing dataset to plot
    if st.session_state.null_values_filtered:
        dataset_choice = st.selectbox(
            'Choose the dataset to plot:',
            ('Original Dataset', 'Dataset without Null Values')
        )
    else:
        dataset_choice = st.selectbox(
            'Choose the dataset to plot:',
            ('Original Dataset',)
        )

    # Select the appropriate dataset based on user choice
    if dataset_choice == 'Original Dataset':
        data_to_plot = df
    elif dataset_choice == 'Dataset without Null Values':
        data_to_plot = st.session_state.df_filtered

    # Slider to select the number of data points to plot
    max_entries = len(data_to_plot)
    num_entries = st.slider('Select the number of data points to plot', min_value=1, max_value=max_entries, value=min(100, max_entries))

    # Subset the data according to the slider value
    df_subset = data_to_plot.head(num_entries)

    # Separate numeric and categorical columns
    numeric_columns = df_subset.select_dtypes(include=['float64', 'int64']).columns.tolist()
    categorical_columns = df_subset.select_dtypes(include=['object', 'category']).columns.tolist()

    # Dropdown menu for selecting the type of graph
    graph_type = st.selectbox(
        'Select the type of graph you want to plot',
        [
            'Scatter Plot', 'Bar Graph', 'Pie Chart', 
            'Line Chart', 'Histogram', 'Box Plot', 
            'Heat Map', 'Violin Plot', 'Pair Plot', 'Correlation Matrix', 'Animated Line Chart'
        ]
    )

    # Plotting the selected graph
    fig, ax = plt.subplots(figsize=(14, 8))  # Increased figure size for better readability

    if graph_type == 'Scatter Plot':
        st.subheader('Scatter Plot')
        x_axis = st.selectbox('Select X-axis:', numeric_columns)
        y_axis = st.selectbox('Select Y-axis:', numeric_columns)
        sns.scatterplot(x=df_subset[x_axis], y=df_subset[y_axis], ax=ax)

    elif graph_type == 'Bar Graph':
        st.subheader('Bar Graph')
        x_axis = st.selectbox('Select X-axis:', categorical_columns + numeric_columns)
        y_axis = st.selectbox('Select Y-axis:', numeric_columns)
        sns.barplot(x=df_subset[x_axis], y=df_subset[y_axis], ax=ax)

    elif graph_type == 'Pie Chart':
        st.subheader('Pie Chart')
        column = st.selectbox('Select the column for the pie chart:', categorical_columns + numeric_columns)
        data = df_subset[column].value_counts()
        plt.pie(data, labels=data.index, autopct='%1.1f%%')

    elif graph_type == 'Line Chart':
        st.subheader('Line Chart')
        x_axis = st.selectbox('Select X-axis:', numeric_columns)
        y_axis = st.selectbox('Select Y-axis:', numeric_columns)
        ax.plot(df_subset[x_axis], df_subset[y_axis])
        ax.set_xlabel(x_axis)
        ax.set_ylabel(y_axis)

    elif graph_type == 'Histogram':
        st.subheader('Histogram')
        column = st.selectbox('Select the column for the histogram:', numeric_columns)
        sns.histplot(df_subset[column], bins=30, ax=ax)

    elif graph_type == 'Box Plot':
        st.subheader('Box Plot')
        column = st.selectbox('Select the column for the box plot:', numeric_columns)
        sns.boxplot(y=df_subset[column], ax=ax)

    elif graph_type == 'Heat Map':
        st.subheader('Heat Map')
        corr = df_subset[numeric_columns].corr()
        sns.heatmap(corr, annot=True, cmap='coolwarm', linewidths=0.5, ax=ax)

    elif graph_type == 'Violin Plot':
        st.subheader('Violin Plot')
        x_axis = st.selectbox('Select X-axis:', categorical_columns + numeric_columns)
        y_axis = st.selectbox('Select Y-axis:', numeric_columns)
        sns.violinplot(x=df_subset[x_axis], y=df_subset[y_axis], ax=ax)

    elif graph_type == 'Pair Plot':
        st.subheader('Pair Plot')
        sns.pairplot(df_subset[numeric_columns])
        st.pyplot()

    elif graph_type == 'Correlation Matrix':
        st.subheader('Correlation Matrix')
        corr = df_subset[numeric_columns].corr()
        st.write(corr)
        sns.heatmap(corr, annot=True, cmap='coolwarm', linewidths=0.5, ax=ax)

    elif graph_type == 'Animated Line Chart':
        st.subheader('Animated Line Chart')
        x_axis = st.selectbox('Select X-axis:', numeric_columns)
        y_axis = st.selectbox('Select Y-axis:', numeric_columns)
        fig = px.line(df_subset, x=x_axis, y=y_axis, title='Animated Line Chart', animation_frame=x_axis, range_y=[df_subset[y_axis].min(), df_subset[y_axis].max()])
        st.plotly_chart(fig)

    # Show the plot
    if graph_type != 'Animated Line Chart':  # Plotly takes care of its own plotting
        # Rotate x-axis labels to avoid overlap
        plt.xticks(rotation=45, ha='right')  # Rotate the labels by 45 degrees for better readability
        # Limit the number of x-ticks (optional)
        ax.set_xticks(ax.get_xticks()[::10])  # This keeps every 10th tick on the x-axis, adjust as needed
        
        st.pyplot(fig)
        # Add a download button beside the plot
        generate_download_link(fig)

    # Show the DataFrame statistics in horizontal format
    st.subheader('Data Statistics')
    st.write(df_subset.describe().T)

# Add "Made by Aditya and Uditya" section with GitHub logo in a button-like element with hover effect
st.markdown(
    """
        <style>
    .button-like {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        padding: 4px 8px; /* Further reduced padding */
        font-size: 10px; /* Smaller font size */
        font-weight: bold;
        color: #ffffff;
        background-color: #141414;
        border: none;
        border-radius: 15px; /* Smaller rounded corners */
        text-decoration: none;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    }
    
    .button-like img {
        width: 12px; /* Smaller logo size */
        height: 12px;
        margin-right: 4px; /* Reduced margin */
        border-radius: 50%;
    }
    
    .button-like:hover {
        transform: translateY(-2px); /* Smaller lift effect */
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.3);
    }
    
    .footer {
        position: fixed;
        bottom: 10px;
        left: 10px;
        display: flex;
        gap: 8px; /* Smaller gap between buttons */
    }
    </style>
    <div class="footer">
        <a class="button-like" href="https://github.com/AdityaRoy999" target="_blank">
            <img src="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png" alt="GitHub"> Made by Aditya
        </a>
        <a class="button-like" href="https://github.com/udityamerit" target="_blank">
            <img src="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png" alt="GitHub"> Made by Uditya
        </a>
    </div>
    """,
    unsafe_allow_html=True
)

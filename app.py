import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Interactive Data Visualizer")

# File Uploader
uploaded_file = st.file_uploader("Upload your CSV file", type="csv")

# Have pandas read the csv and put it into a data frame
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write("Dataset Preview:")
    st.dataframe(df) # streamlit renders a table and references the data frame from pandas

    # Add filtering section
    st.header("Filter Data")
    
    # Allow user to select only one column to filter
    column_to_filter = st.selectbox("Select column to filter", options=df.columns)
    
    filtered_df = df.copy()
    
    # Determine column data type to show appropriate filter options
    col_type = df[column_to_filter].dtype
    
    # Different filter options based on data type
    if pd.api.types.is_numeric_dtype(col_type):
        # For numeric columns, provide range filters
        min_val = float(filtered_df[column_to_filter].min())
        max_val = float(filtered_df[column_to_filter].max())
        
        st.subheader(f"Filter {column_to_filter}")
        filter_type = st.selectbox(f"Filter type for {column_to_filter}", 
                                 ["Range", "Greater than", "Less than", "Equals"],
                                 key=f"filter_type_{column_to_filter}")
        
        if filter_type == "Range":
            values = st.slider(f"Select range for {column_to_filter}", 
                             min_value=min_val, 
                             max_value=max_val,
                             value=(min_val, max_val),
                             key=f"range_{column_to_filter}")
            filtered_df = filtered_df[filtered_df[column_to_filter].between(values[0], values[1])]
        elif filter_type == "Greater than":
            value = st.number_input(f"Greater than value for {column_to_filter}", 
                                  value=min_val,
                                  key=f"gt_{column_to_filter}")
            filtered_df = filtered_df[filtered_df[column_to_filter] > value]
        elif filter_type == "Less than":
            value = st.number_input(f"Less than value for {column_to_filter}", 
                                  value=max_val,
                                  key=f"lt_{column_to_filter}")
            filtered_df = filtered_df[filtered_df[column_to_filter] < value]
        elif filter_type == "Equals":
            value = st.number_input(f"Equal to value for {column_to_filter}", 
                                  value=min_val,
                                  key=f"eq_{column_to_filter}")
            filtered_df = filtered_df[filtered_df[column_to_filter] == value]
    else:
        # For non-numeric columns, provide a multi-select
        unique_values = filtered_df[column_to_filter].unique()
        selected_values = st.multiselect(f"Select values for {column_to_filter}", 
                                       options=unique_values,
                                       default=unique_values,
                                       key=f"multi_{column_to_filter}")
        filtered_df = filtered_df[filtered_df[column_to_filter].isin(selected_values)]
    
    # Display the filtered DataFrame
    st.subheader("Filtered Data:")
    st.dataframe(filtered_df)

    # Update visualization to use filtered DataFrame
    st.sidebar.header("Visualization Options")
    
    # Let user pick columns for visualization
    x_axis = st.sidebar.selectbox("Choose X-axis", filtered_df.columns)
    y_axis = st.sidebar.selectbox("Choose Y-axis", filtered_df.columns)
    chart_type = st.sidebar.selectbox("Choose Chart Type", ["Scatter", "Line", "Bar", "Pie"])
    
    # Import the chart creation function
    from charts import create_chart
    
    # Create the chart using the imported function
    try:
        fig = create_chart(chart_type, filtered_df, x_axis, y_axis)
        st.plotly_chart(fig)
    except Exception as e:
        st.error(f"Error creating chart: {str(e)}")
else:
    st.write("Please upload a CSV file to get started.")
   



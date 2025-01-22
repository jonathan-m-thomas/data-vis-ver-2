import plotly.express as px
import pandas as pd

def create_chart(chart_type, data, x_axis, y_axis):
    """
    Create a chart based on the specified type and data
    
    Parameters:
    chart_type (str): Type of chart to create ('Scatter', 'Line', 'Bar', 'Pie')
    data (pd.DataFrame): DataFrame containing the data
    x_axis (str): Column name for x-axis
    y_axis (str): Column name for y-axis (also used as values for pie chart)
    
    Returns:
    plotly.graph_objects.Figure: The created chart
    """
    if chart_type == "Scatter":
        return px.scatter(data, x=x_axis, y=y_axis, title="Scatter Plot")
    elif chart_type == "Line":
        return px.line(data, x=x_axis, y=y_axis, title="Line Chart")
    elif chart_type == "Bar":
        return px.bar(data, x=x_axis, y=y_axis, title="Bar Chart")
    elif chart_type == "Pie":
        # For pie charts, if y_axis is not numeric, count occurrences of x_axis values
        if not pd.api.types.is_numeric_dtype(data[y_axis]):
            pie_data = data[x_axis].value_counts().reset_index()
            pie_data.columns = ['category', 'count']
            return px.pie(pie_data, names='category', values='count', 
                         title=f"Distribution of {x_axis}")
        else:
            # If y_axis is numeric, use sum as before
            pie_data = data.groupby(x_axis, as_index=False).agg({y_axis: 'sum'})
            return px.pie(pie_data, names=x_axis, values=y_axis, 
                         title=f"Pie Chart of {y_axis} by {x_axis}")
    else:
        raise ValueError(f"Unsupported chart type: {chart_type}")

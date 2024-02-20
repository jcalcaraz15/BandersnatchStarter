import altair as alt
from altair import Chart, Tooltip
import pandas as pd

alt.data_transformers.enable('vegafusion')


def chart(df: pd.DataFrame, x: str, y:  str, target: str) -> alt.Chart:
    """ Create a chart function that takes a dataframe and a target column and returns a chart """

    graph = alt.Chart(df).mark_circle(size=100).encode(
        x=alt.X(x, axis=alt.Axis(labelColor='#AAAAAA', titleColor='#AAAAAA', gridColor="#333333")),  # Set label and title color to white for x-axis
        y=alt.Y(y, axis=alt.Axis(labelColor='#AAAAAA', titleColor='#AAAAAA', gridColor='#333333')), # Set label and title color to white for y-axis
        color=alt.Color(target, legend=alt.Legend(labelColor='#AAAAAA', titleColor='#AAAAAA')),  # Set legend label and title color to white
        tooltip=list(df.columns)  # You can directly pass the list of column names
    ).properties(
        title=alt.TitleParams(text=f"{y} by {x} for {target}", color='#AAAAAA', fontSize=23),
        width=450,
        height=500,
        padding={"left": 33, "right": 33, "top": 33, "bottom": 33},  # Adjust padding values as needed
        background="#232323"
    )
    return graph

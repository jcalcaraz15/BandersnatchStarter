""" MongoDB Collection visualization using Altair """
import altair as alt
import pandas as pd

alt.data_transformers.enable('vegafusion')


def chart(df: pd.DataFrame, x: str, y:  str, target: str) -> alt.Chart:
    """Create a scatter plot chart.

    Parameters:
    - df (pd.DataFrame): The dataframe containing the data.
    - x (str): The column name to be plotted on the x-axis.
    - y (str): The column name to be plotted on the y-axis.
    - target (str): The column name representing the color encoding.

    Returns:
    - alt.Chart: An Altair chart object representing the scatter plot.
    """

    properties = {"labelColor":'#AAAAAA',
                  "titleColor":'#AAAAAA',
                  "gridColor":"#333333",
                  "labelFontSize":12,
                  "titlePadding":20,
                  "titleFontSize":14,
                  "legendtitlePadding":15}

    graph = alt.Chart(df).mark_circle(size=100).encode(
        x=alt.X(x, axis=alt.Axis(labelColor=properties['labelColor'],
                                 labelFontSize=properties['labelFontSize'],
                                 titleColor=properties['titleColor'],
                                 titlePadding=properties['titlePadding'],
                                 titleFontSize=properties['titleFontSize'],
                                 gridColor=properties['gridColor'])),
        y=alt.Y(y, axis=alt.Axis(labelColor=properties['labelColor'],
                                 labelFontSize=properties['labelFontSize'],
                                 titleColor=properties['titleColor'],
                                 titlePadding=properties['titlePadding'],
                                 titleFontSize=properties['titleFontSize'],
                                 gridColor=properties['gridColor'])),
        color=alt.Color(target, legend=alt.Legend(labelColor=properties['labelColor'],
                                                  labelFontSize=properties['labelFontSize'],
                                                  titleColor=properties['titleColor'],
                                                  titleFontSize=properties['titleFontSize'],
                                                  titlePadding=properties['legendtitlePadding'])),
        tooltip=list(df.columns)
    ).properties(
        title=alt.TitleParams(text=f"{y} by {x} for {target}",
                              color='#AAAAAA',
                              fontSize=23),
        width=450,
        height=500,
        background="#232323",
        padding={
            "left": 42,
            "right": 42,
            "top": 42,
            "bottom": 42
            }
)

    return graph

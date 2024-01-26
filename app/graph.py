import altair as alt
from altair import Chart, Tooltip
import pandas as pd


def chart(df: pd.DataFrame, x: str, y:  str, target: str) -> alt.Chart:
    """ Create a chart function that takes a dataframe and a target column and returns a chart """
    graph = Chart(
        df,
        title=f"{y} by {x} for {target}").mark_circle(size=100).encode(
        x=x,
        y=y,
        color=target,
        tooltip=Tooltip(df.columns.to_list())
    )
    return graph

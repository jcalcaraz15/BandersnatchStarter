from altair import Chart, Tooltip
from pandas import DataFrame
from app.data import Database

def chart(df: DataFrame, x: str, y: str, target: str) -> Chart:
    graph = Chart(
        df,
        title=f"{x} by {y} for {target}"
    ).mark_circle(size=100).encode(
        x=x,
        y=y,
        color=target,
        tooltip=Tooltip(df.columns.to_list())
    )
    return graph

if __name__ == '__main__':
    collection_graph = Database("Collection")
    collection_graph.seed()

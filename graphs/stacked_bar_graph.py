import pandas as pd
from pathlib import Path

from bokeh.io import curdoc
from bokeh.layouts import column
from bokeh.plotting import figure
from bokeh.models.widgets import Select
from bokeh.models import ColumnDataSource, Legend, LegendItem

"""
    
"""

# Run bokeh serve --show graphs/stacked_bar_graph.py

def createLegend(renderers, labels):
    """ 
    This function creates a legend object for a plot. 
    It takes two parameters: 
        1. `renderers`, which is a list of renderers,
        2. `labels`, which is a list of labels corresponding to the renderers.
    """
    items = []

    for i, r in enumerate(renderers):
        items.append(LegendItem(label=labels[i], renderers=[r], index=0))

    return Legend(items=items)

# Define path
proj_path = Path.cwd()

# Import data from csv
df_IPI = pd.read_csv(f'{proj_path}/data/ipi.csv')


# Define variables
components = ["Efficiency", "Diversification", "Quality", "Internationalization", "Time"]
region_name = {"EC": "Ecuador", "BY": "Belarus", "TN": "Tunicia", "UY": "Uruguay", "VN": "Vietnam"}
colors_comp=['red', 'blue', 'green', 'orange', 'purple']
regions = list(region_name.values())
hover_alpha = 1.0
nonhover_alpha = 0.75

# Set source
source = ColumnDataSource(df_IPI[df_IPI['Year']==int(2023)][['Region']+components])

# Create Select widget to control graph year
select = Select(
        title=f'Year: ',
        options=[(str(y), str(y)) for y in range(2017, 2023 + 1)],
        value=2023
        )

# Create figure
p = figure(x_range=regions, height=350, title=f'IPI indicators for 2023',
            toolbar_location=None, tools='hover', tooltips='$name: @$name')

# Adjust figure values
p.y_range.start = 0
p.x_range.range_padding = 0.1

p.xgrid.grid_line_color = None
p.axis.minor_tick_line_color = None
p.outline_line_color = None

# Plot bar graph
r = p.vbar_stack(stackers=components, x='Region', width=0.9, color=colors_comp, source=source, alpha=nonhover_alpha, hover_alpha=hover_alpha)

# Create legend
legend = createLegend(r, components)
legend.click_policy = 'mute'
p.add_layout(legend, 'right')

# add a callback to a widget
def callback(attr, old, new):
    p.title.text = f'IPI indicators for {select.value}'
    source.data.update(df_IPI[df_IPI['Year']==int(select.value)][['Region']+components])

# Assign callback to Select widget
select.on_change('value', callback)

# Create a layout 
layout = column(select, p)

# Add the layout to curdoc
curdoc().add_root(layout)
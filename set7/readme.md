TODO: Reflect on what you learned this week and what is still unclear.
CATEGORICAL:
To count the amount of times a certain category is repeated in a dataset, use "df["colummn name"].value_counts()".
To produce a bar graph that gives a visual idea of these value counts, use "df["column name"].value_counts().plot(kind="bar") => change to "barh" if you want the bars horizontal

CONTINUOUS:
df["column name"].hist() produces a histogram with integer values as both the x- and y- axes to see how the numbers are distributed
data that is measured through a timeline can be plotted visually using "df["column name"].plot()

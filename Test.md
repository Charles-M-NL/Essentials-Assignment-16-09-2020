Essentials assignment Charles Meijer
================
Charles Meijer 5938244
16-09-2020

  - [Assignment](#assignment)
      - [Dataset](#dataset)
      - [Figures](#figures)

This is an [R Markdown](http://rmarkdown.rstudio.com) Notebook. When you
execute code within the notebook, the results appear beneath the code.

Try executing this chunk by clicking the *Run* button within the chunk
or by placing your cursor inside it and pressing *Ctrl+Shift+Enter*.

# Assignment

## Dataset

``` r
mcdonalds = read.csv("menu.csv")

head(mcdonalds[1:4], 5)
```

    ##    Category                             Item   Serving.Size Calories
    ## 1 Breakfast                     Egg McMuffin 4.8 oz (136 g)      300
    ## 2 Breakfast                Egg White Delight 4.8 oz (135 g)      250
    ## 3 Breakfast                 Sausage McMuffin 3.9 oz (111 g)      370
    ## 4 Breakfast        Sausage McMuffin with Egg 5.7 oz (161 g)      450
    ## 5 Breakfast Sausage McMuffin with Egg Whites 5.7 oz (161 g)      400

The data consists of a number of features of a variety of McDonalds
products. I got this data during the “Data science and biology” bachelor
course with the assignment: “Make a figure”. It was up to us what
feature we wanted to visualize and how our figures would look. I decided
on showing the amounts of sugar in different smoothies and shakes and I
thought it’d be funny if the color of the bar would correspond with the
color of the product. This took quite some googling for pictures of
smoothies and then deciding on the right hexadecimal color code.
Hopefully I’ll be able to include my figure in this notebook. I’ll try
to include both the python produced figure I made then, and a new
Tableau version.

## Figures

![Bar chart suikergehalte smoothies python](Figuur%20smoothies.png)
*Python figure of sugar in smoothies and shakes* ![Bar chart
tableau](Smoothies.png) *Tableau version*

It seems like tableau is way easier because picking the right parts of
the data is quite intuitive. However, I did have some issues with the
header, and I don’t think I can pick a color based on hexadecimal code,
as I could in python. This kinda limited the amount of colors to choose
from.

I tried to find how to add the image description underneath the image in
small letters

Add a new chunk by clicking the *Insert Chunk* button on the toolbar or
by pressing *Ctrl+Alt+I*.

When you save the notebook, an HTML file containing the code and output
will be saved alongside it (click the *Preview* button or press
*Ctrl+Shift+K* to preview the HTML file).

The preview shows you a rendered HTML copy of the contents of the
editor. Consequently, unlike *Knit*, *Preview* does not run any R code
chunks. Instead, the output of the chunk when it was last run in the
editor is displayed.
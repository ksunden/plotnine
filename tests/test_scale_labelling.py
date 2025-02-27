import pandas as pd

from plotnine import (
    aes,
    element_text,
    facet_grid,
    geom_point,
    ggplot,
    labs,
    theme,
)
from plotnine.data import mtcars

_theme = theme(subplots_adjust={"right": 0.80})
_theme_captions = theme(subplots_adjust={"bottom": 0.30})

c1 = "This is a sample caption"
c2 = """\
Lorem Ipsum is simply dummy text of the printing and typesetting industry.
Lorem Ipsum has been the industry's standard dummy text ever since the 1500s,
when an unknown printer took a galley of type and scrambled it to make
a type specimen book."""


df = pd.DataFrame({"x": [1, 2], "y": [3, 4], "cat": ["a", "b"]})


def test_labelling_with_colour():
    p = (
        ggplot(df, aes("x", "y", color="cat"))
        + geom_point()
        + labs(colour="Colour Title")
    )

    assert p + _theme == "labelling_with_colour"


def test_caption_simple():
    p = ggplot(mtcars, aes("wt", "mpg")) + geom_point() + labs(caption=c1)

    assert p == "caption_simple"


def test_caption_complex():
    p = (
        ggplot(mtcars, aes("wt", "mpg"))
        + geom_point()
        + labs(caption=c2)
        + facet_grid("am ~ vs")
        + theme(plot_caption=element_text(x=0.125, ha="left", size=12))
    )

    assert p == "caption_complex"

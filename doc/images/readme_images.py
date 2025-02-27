from plotnine import (
    aes,
    facet_wrap,
    geom_point,
    ggplot,
    stat_smooth,
    theme_tufte,
    theme_xkcd,
)
from plotnine.data import mtcars

kwargs = {"width": 6, "height": 4, "dpi": 300}

p1 = ggplot(mtcars, aes("wt", "mpg")) + geom_point()
p1.save("readme-image-1.png", **kwargs)

p2 = p1 + aes(color="factor(gear)")
p2.save("readme-image-2.png", **kwargs)

p3 = p2 + stat_smooth(method="lm")
p3.save("readme-image-3.png", **kwargs)

p4 = p3 + facet_wrap("~gear")
p4.save("readme-image-4.png", **kwargs)

p5 = p4 + theme_xkcd()
p5.save("readme-image-5.png", **kwargs)

p5alt = p4 + theme_tufte()
p5alt.save("readme-image-5alt.png", **kwargs)

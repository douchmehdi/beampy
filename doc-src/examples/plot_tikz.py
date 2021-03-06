"""
tikz
====

Add pgf/tikz drawing to the slide.

You could find great examples here http://www.texample.net/tikz/examples/

"""

from beampy import *

# Remove quiet=True to get beampy compilation outputs
doc = document(quiet=True)

latex_cmd = r"\newcounter{density}\setcounter{density}{10}"
tex_packages = ['ifthen']

with slide('A tikz figure'):
    tikz(r"""
    \def\couleur{SeaGreen}
    \path[coordinate] (0,0)  coordinate(A)
                ++( 60:12cm) coordinate(B)
                ++(-60:12cm) coordinate(C);
    \draw[fill=\couleur!\thedensity] (A) -- (B) -- (C) -- cycle;
    \foreach \x in {1,...,15}{%
        \pgfmathsetcounter{density}{\thedensity+10}
        \setcounter{density}{\thedensity}
        \path[coordinate] coordinate(X) at (A){};
        \path[coordinate] (A) -- (B) coordinate[pos=.15](A)
                            -- (C) coordinate[pos=.15](B)
                            -- (X) coordinate[pos=.15](C);
        \draw[fill=\couleur!\thedensity] (A)--(B)--(C)--cycle;
    }
    """, latex_pre_tikzpicture=latex_cmd,
         tex_packages=tex_packages,
         x='center', y='center')


display_matplotlib(gcs())

#########################################################################
#
#Module arguments
#================
#
#.. autoclass:: beampy.tikz
#   :noindex:
#


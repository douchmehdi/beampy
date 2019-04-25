

.. _sphx_glr_auto_examples_plot_tikz.py:


tikz
====

Add pgf/tikz drawing to the slide.

You could find great examples here http://www.texample.net/tikz/examples/




.. code-block:: python


    from beampy import *

    # Remove quiet=True to get beampy compilation outputs
    doc = document(quiet=True)

    tkz_options = r"scale=1.4, every node/.style={minimum size=1cm},on grid"

    with slide('A tikz figure'):
        tikz(r"""
    \begin{scope}[
               yshift=-83,every node/.append style={
               yslant=0.5,xslant=-1},yslant=0.5,xslant=-1
               ]
           \draw[step=4mm, black] (0,0) grid (5,5); 
           \draw[black,thick] (0,0) rectangle (5,5);%borders
           \fill[greenMW] (2.05,2.05) rectangle (2.35,2.35); % center pixel
           \fill[greenMW] (1.65,2.05) rectangle (1.95,2.35); %left
           \fill[greenMW] (2.45,2.05) rectangle (2.75,2.35); %right
           \fill[greenMW] (2.05,2.45) rectangle (2.35,2.75); %top
           \fill[greenMW] (2.05,1.95) rectangle (2.35,1.65); %bottom
    % 8 -pixel setting
           \fill[greenMW] (1.65,2.45) rectangle (1.95,2.75); %top-left
           \fill[greenMW] (2.45,2.45) rectangle (2.75,2.75); %top-right
           \fill[greenMW] (2.75,1.95) rectangle (2.45,1.65); %bottom-right
           \fill[greenMW] (1.65,1.95) rectangle (1.95,1.65); %bottom-left
    % 2. ring
           \fill[greenMW] (1.25,1.55) rectangle (1.55,1.25); %bottom-left
           \fill[greenMW] (0.85,1.55) rectangle (1.15,1.25); %bottom-left
           \fill[greenMW] (0.85,1.15) rectangle (1.15,0.85); %bottom-left
           \fill[greenMW] (1.25,0.75) rectangle (1.55,0.45); %bottom-left
       \end{scope}
    %
       \begin{scope}[
               yshift=0,every node/.append style={
               yslant=0.5,xslant=-1},yslant=0.5,xslant=-1
               ]
           \fill[white,fill opacity=0.9] (0,0) rectangle (5,5);
           \draw[step=4mm, black] (0,0) grid (5,5); %grid definition
           \draw[black,thick] (0,0) rectangle (5,5);%borders
           \fill[greenMW] (2.05,2.05) rectangle (2.35,2.35); % center pixel
           \fill[greenMW] (1.65,2.05) rectangle (1.95,2.35); %left
           \fill[greenMW] (2.45,2.05) rectangle (2.75,2.35); % right
           \fill[greenMW] (2.05,2.45) rectangle (2.35,2.75); % top
           \fill[greenMW] (2.05,1.95) rectangle (2.35,1.65); % bottom
    % 4 -pixel setting
           \fill[greenMW] (1.65,2.45) rectangle (1.95,2.75); %top-left
           \fill[greenMW] (2.45,2.45) rectangle (2.75,2.75); %top-right
           \fill[greenMW] (2.75,1.95) rectangle (2.45,1.65); %bottom-right
           \fill[greenMW] (1.65,1.95) rectangle (1.95,1.65); %bottom-left
    % 2. ring
           \fill[orange] (1.25,1.55) rectangle (1.55,1.25); 
           \fill[orange] (0.85,1.55) rectangle (1.15,1.25); 
           \fill[orange] (0.85,1.15) rectangle (1.15,0.85); 
           \fill[blue] (1.25,0.75) rectangle (1.55,0.45); 
       \end{scope}
    %
    % draw annotations
    %
       \draw[-latex,thick,orange](-3,5)node[left]{ }
           to[out=0,in=90] (-.4,1.4);
       \draw[-latex,thick,blue](-3,5)node[left]{ }
           to[out=0,in=90] (0.8,1.15);
       \draw[-latex,thick,greenMW](-3,5)node[left]{3 patches}
           to[out=0,in=90] (0,2.8);
    %
       \draw[-latex,thick,greenMW](-3,-2)node[left]{1 patch}
           to[out=0,in=200] (-1,-.9);
       \draw[thick,gray!70!black](6,4) node {4 neighbourhood rule};
       \draw[thick,gray!70!black](6,-2) node {8 neighbourhood rule};
    %
        """, figure_options=tkz_options,
             x='center', y='center')


    display_matplotlib(gcs())




.. code-block:: pytb

    Traceback (most recent call last):
      File "/home/hugo/developpement/python/beampy_git/doc-src/examples/plot_tikz.py", line 85, in <module>
        display_matplotlib(gcs())
      File "/home/hugo/developpement/python/libperso/beampy/exports.py", line 398, in display_matplotlib
        slide.newrender()
      File "/home/hugo/developpement/python/libperso/beampy/modules/core.py", line 321, in newrender
        elem.run_render()
      File "/home/hugo/developpement/python/libperso/beampy/modules/core.py", line 585, in run_render
        self.render()
      File "/home/hugo/developpement/python/libperso/beampy/modules/tikz.py", line 110, in render
        svgout = latex2svg(pretex, write_tmpsvg=False)
      File "/home/hugo/developpement/python/libperso/beampy/functions.py", line 338, in latex2svg
        outsvg = clean_ghostscript_warnings(outsvg)
    UnboundLocalError: local variable 'outsvg' referenced before assignment




Module arguments
================

.. autoclass:: beampy.tikz
   :noindex:





.. only :: html

 .. container:: sphx-glr-footer


  .. container:: sphx-glr-download

     :download:`Download Python source code: plot_tikz.py <plot_tikz.py>`



  .. container:: sphx-glr-download

     :download:`Download Jupyter notebook: plot_tikz.ipynb <plot_tikz.ipynb>`


.. only:: html

 .. rst-class:: sphx-glr-signature

    `Gallery generated by Sphinx-Gallery <https://sphinx-gallery.readthedocs.io>`_

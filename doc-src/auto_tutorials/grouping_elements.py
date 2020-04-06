"""
How to group Beampy modules
===========================

Beampy allows to group your module to move operate them as a group (a
bit like minipage in beamer). Group could be used to create margins,
columns layout for instance.

If you want to know all the option of the group module you can look at
the :ref:`sphx_glr_auto_examples_plot_group.py` module inside the
beampy modules section.

Let's play with group to see how it works.

Create a simple group
---------------------
"""

from beampy import *

doc = document(quiet=True)

with slide('Group tutorial'):
    with group() as g:
        rectangle(width='80%', height=100)
        text('This is a nice rectangle')

    #show the group contour
    g.add_border()

display_matplotlib(gcs())

#############################################################
#
# In this example you can see that a group is created around the two
# modules (the rectangle and the text). These two modules have been
# positioned "centered" horizontally and "distributed spacing"
# vertically taking the presentation height as available space.
#
# Now lets try to give a size to this group

with slide('Group tutorial'):
    with group(width=300, height=300) as g:
        rectangle(width='80%', height=100)
        text('This is a nice rectangle')

    #show the group contour
    g.add_border()

display_matplotlib(gcs())

#############################################################
#
# The rectangle width is now 80% of the with of the group. The
# vertical available space to compute the spacing of the two modules
# is now the height of the group.
#
# Group inside a group
# --------------------
#
# Lets increase the complexity a bit of our example to create a piece
# of art with 3 squares horizontally distributed in the group. To do
# so we need to group these 3 rectangles with a group inside the first
# group. The position of the rectangles should be set to x='auto' to
# make horizontal distribution and y to 0 or 'center'.
#

with slide('Group tutorial'):
    with group(width=300, height=300) as g:
        with group(width="100%", height="30%") as g2:
            for c in ['green', 'orange', 'crimson']:
                rectangle(width='30%', height="100%", x='auto', y=0, color=c)

        text('This is a nice rectangle')

    #show the group contour
    g.add_border()
    g2.add_border()
    
display_matplotlib(gcs())

############################################################
#
# You can see that the group and the text are now equally spaced
# vertically inside the first group. You can group as many group as
# you need to create your complex layout.
#
# Create a two columns layout
# ---------------------------
#
# To do so we create two group with a width of 44% (this will create 3
# blank spaces with a width 2% of the presentation width).

colw = '47%'
colh = '90%'

with slide('Group tutorial'):
    with group(width=colw, height=colh, y='center', x='auto') as g1:
        rectangle(width='90%', height=200, color='orange')
        text('This is a nice rectangle')

    with group(width=colw, height=colh, y=g1.top+0, x='auto') as g2:
        rectangle(width='90%', height=200, color='crimson')
        text('This is a second nice rectangle')
        
    #show the group contour
    g1.add_border()
    g2.add_border()
    
display_matplotlib(gcs())


#################################################
#
# Now that you know how to group beampy modules together, you can have
# a look to the next tutorial on how to fragment the apparition of you
# module on you slide
# :ref:`sphx_glr_auto_tutorials_animating_slide.py`. Or if you did
# not remain you how to place the beampy module on your slide go back
# to the previous tutorial
# :ref:`sphx_glr_auto_tutorials_positioning_system.py`.

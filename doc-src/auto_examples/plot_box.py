"""
box
===

Create a boxed group, that could have a title. 

"""

from beampy import *

# Remove quiet=True to get Beampy render outputs
doc = document(quiet=True)


with slide('Add nice boxes to group'):

    with box(x=20, y='center', width=300, height='60%', title='Very very very long box title') as b1:
        text('Box text')

    with box(x=b1.right+10, y=b1.top+0, width=450,
             title='Change color and drop-shadow', title_align='center',
             color='crimson', shadow=True) as b2:
        
        text('Box text, with a centered title, and a nice crimson color', width='90%')

    with box(x=b1.right+10, y=b2.bottom+50, width=b2.width, color='darkorange',
             rounded=70, background_color='lightgray', linewidth=4, auto_height_margin=30) as b3:
        
        text('''
            Without title for the box, more rounded angle, bigger
            linewidth, and a background color
            ''', align='center', width='90%')
            

display_matplotlib(gcs())

###################################################
#
#Module arguments
#================
#
#.. autoclass:: beampy.box
#   :noindex:

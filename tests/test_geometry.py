# coding: utf-8
"""
Python file to test geometry (placement of module and width/height)
"""

from beampy import *

doc = document(cache=False)

with slide('Width as percent'):

    a = rectangle(width='50%', height='10%')

    
with slide('Width opetation'):
    d = circle(r=10)
    rectangle(width=d.width*5, height=d.height*2)


with slide('Operation on None'):
    t = text('teset tootto tototo tututu', width=200, align='center')
    print(t.width, t.height)
    c = rectangle(width=t.width, height=t.height, color='yellow',
                  y=t.top+0, x=t.left+0, opacity=0.5)
    
with slide('size and position operation'):

    a = rectangle(width='50%', height='50%', y='center', x=5)
    for c in ['yellow', 'red', 'purple', 'pink','blue']:
        a = rectangle(width=a.width/2, height=a.height/2,
                      x=a.left + a.width, y=a.top+a.height/2,
                      color=c)
        

with slide('group size'):
    
    with group() as g1:
        for c in ['green', 'yellow', 'red']:
            rectangle(width=50, height=50, color=c)

        text("A text without height to see if it's rendered by the blue rectangle to get its height",
             width='50%')
        
    g1.add_border()

    rectangle(height=g1.height, width=g1.width/2,
              color='None', edgecolor='blue',
              x=g1.center+center(0), y=g1.top+0)


with slide('Font size and svg size'):

    t = text('Text of a length of 70px', width=70)
    rectangle(height=t.height, width=70)
    t.add_border()
    
    t = text('Text of a length of 3cm', width='3cm')
    rectangle(height=t.height, width='3cm')
    t.add_border()
    
save('./html_out/test_geometry.html')

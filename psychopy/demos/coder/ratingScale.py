""" demo for visual.ratingScale.py
"""

__author__ = 'Jeremy Gray'

from psychopy import visual, event
import random

myWin = visual.Window(fullscr=True, units='pix', monitor='testMonitor') 

instr = visual.TextStim(myWin,text="""This is a demo of visual.ratingScale(). The first example shows how simple it can be, and the second example illustrates how you can customize the display.

Example 1. On the next screen, you will see the default configuration, which will probably suffice for most ratings or be pretty close. It uses a 'triangle' marker style, color blue, range 1 to 7 (not at all to extremely).

By relying on the defaults, the entire next screen requires nothing more than this code in your script:

    visual.ratingScale(myWin, "How cool was that?")

To respond, use the mouse to indicate a rating by clicking somewhere on the line (on the next screen). Or select and drag the marker. Or type a number 1 to 7 to indicate your choice. In this example, responses are rounded to the nearest tick-mark.

Then either press enter, or click the button to accept it. 

Press any key to start example 1.""")
event.clearEvents()
while len(event.getKeys()) == 0:
    instr.draw()
    myWin.flip()

# this is line of code makes Example 1 happen, and saves the return values:
rating, ratingRT, scaleInfo = visual.ratingScale(myWin, "How cool was that?")
print rating, ratingRT, scaleInfo

instr = visual.TextStim(myWin,text="""Your rating was: %d on a scale of %d to %d. (These three numbers were all returned by the function. The question text is also returned.)

If you want a 1 to 5 scale instead, just add 'high=5' to the argument list:

visual.ratingScale(myWin, "How cool was that?", high=5)

---

Example 2. This example overrides some of the default options. First, lets use markerStyle='glow'. The default color for 'glow' is white, but we'll use markerColor='DarkRed' instead, and we'll accept quasi-continuous ratings (precision=100) but not reveal them to the subject (showValue=False). See the documentation for several other options.

visual.ratingScale(myWin, "How hot was that?", low=0, high=100, precision=100, markerStyle='glow', markerColor='DarkRed', markerExpansion=10, showValue=False)

In this example, the marker becomes larger as you place it furher to the right (markerExpansion=10).

Press any key to start Example 2.""" % (rating, scaleInfo[0],scaleInfo[1]))
event.clearEvents()
while len(event.getKeys()) == 0:
    instr.draw()
    myWin.flip()

# this line of code make Example 2 happen:
rating, ratingRT, scaleInfo = visual.ratingScale(myWin, "How hot was that?", low=0, high=100, precision=100,
        markerStyle='glow', markerColor='DarkRed', markerExpansion=10, showValue=False)
        
print rating, ratingRT, scaleInfo
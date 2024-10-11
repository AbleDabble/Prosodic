poem = """Lost debris of ice here meet in
strangely charming quiet orbit
'til momentum conquers gravity
'lone again in tranquil silence 
quiet comets travel nowhere destined."""

prose = """
As rivers meander and oceans swell, 
carried by echoes between turbulent waves, 
the kraken awakens to rapture's knell. 
In the still darkness of the abyss 
inbetween the decay of sunken ships, 
the stirring of an enormous beast 
turns gyres at the surface of the sea. 
About the peaks of misty mountains, 
in their caverns old, 
adown the lightless chasms 
where legends die untold, 
a shot aroused from slumber Dragons 
resting after their reign of terror
"""

gpt = """
Lost debris of ice in flight,
In a quiet orbit, alight.
Until momentum forceful might,
Tears the silence of the night.

Once again, they drift alone,
Quiet comets, paths unknown.
In the silence, softly thrown,
Destinations yet unshown
"""

import prosodic as p 
meter_name = 'iambic_pentameter'
meter = p.get_meter(meter_name)
text = p.Text(poem)
text.parse(meter=meter)
#text = p.Text(prose)
#text.parse()
#line = "Turns gyres at the surface of the sea"
#text = p.Text(line)
#text.parse()


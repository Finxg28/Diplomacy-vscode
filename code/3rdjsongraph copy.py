import pandas as pd

import matplotlib.pyplot as plot

 

# A python dictionary

data = {"lies":[1,0,0,2,0,12,3],

        "gamescore":[5, 4, 5, 9, 3, 8,6]

        };

index     = ["austria", "italy","russia","germany","england","Turkey","france"];

 

# Dictionary loaded into a DataFrame       

dataFrame = pd.DataFrame(data=data, index=index);

 

# Draw a vertical bar chart

dataFrame.plot.bar(rot=15, title="lies told vs game score")
plot.show(block=True);
lie_countdict= {"austria":0,"germany":0,"italy":0,"turkey":0,"russia":0,"england":0,"france":0}  

    
import pandas as pd

import matplotlib.pyplot as plot

 

# A python dictionary

data = {"lies":[1,0,],

        "gamescore":[5, 4,]

        };

index     = ["austria", "italy",];

 

# Dictionary loaded into a DataFrame       

dataFrame = pd.DataFrame(data=data, index=index);

 

# Draw a vertical bar chart

dataFrame.plot.bar(rot=15, title="lies told vs game score")
plot.show(block=True);
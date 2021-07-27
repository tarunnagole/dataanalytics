import matplotlib.pyplot as plt
import pandas as pd
df =  pd.read_csv('Match.csv')
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
class Pie():
    sizes=[]
    df=pd.read_csv('Match.csv')
    teams=np.unique(df.Team1)
    def wins(x,df):
        count=0
        for i in range(len(df)):
            if x == df.match_winner[i]:
                count=count+1
        return count
    for x in teams:
        ans=wins(x,df)
        sizes.append(ans)
    plt.pie(sizes,labels=teams,autopct='%1.2f%%',startangle=90)
    plt.show()







import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
class Bar:
    def __init__(self,team):
        def matcheswon(x,team,df):
            count=0
            for i in range(len(df)):
                if (x==df.Season_Year[i]) and team==df.match_winner[i] and team==df.Toss_Winner[i]:
                    count=count+1
            return count
        df=pd.read_csv('Match.csv')
        years=np.unique(df.Season_Year)
        x=[]
        for z in years:
            ans=matcheswon(z,team,df)
            x.append(ans)
        width=1/3
        plt.bar(years,x,width,color='green')
        plt.xlabel('year')
        plt.ylabel('no.of winnings')
        
        plt.title('Statistics of Mumbai Indians')
        plt.show()
Bar('Mumbai Indians')

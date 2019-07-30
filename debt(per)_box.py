import numpy as np
import matplotlib.pyplot as plt
import seaborn
from scipy import stats

x=[38510,36854,36250,34415,34144,32247,32065,31899,31734,31364,31289,31275,30931,30891,
30775,30651,30629,30439,29887,29859,29569,29561,29314,29214,28653,28466,28447,27885,27720,
27505,27210,27108,26824,26799,26675,26530,26526,25952,25750,25682,25252,25125,24041,23967,23936,
22785,22524,22064,21237,18838]
y=[.57,.67,.64,.74,.62,.61,.59,.50,.68,.56,.58,.74,.60,.58,.46,.60,.62,.58,.56,.63,.64,.57,
.56,.61,.57,.59,.64,.56,.59,.74,.48,.58,.55,.55,.61,.52,.57,.49,.54,.46,.56,.49,.50,.54,.52,.50,
.47,.49,.54,.38]

x = np.array(x)
y = np.array(y)

quartX= np.percentile(x,[25,50,75])
quartY= np.percentile(y,[25,50,75])
print(x.min()," ",quartX[0]," ",quartX[1]," ",quartX[2]," ",x.max())
print(y.min()," ",quartY[0]," ",quartY[1]," ",quartY[2]," ",y.max())

print(np.mean(x),np.std(x))
print(np.mean(y),np.std(y))
#plt.title("BoxPlot Average Debt per State")
#plt.boxplot(x,vert=False)


#plt.title("Percent of Students with Debt")
#plt.boxplot(y,vert=False)

plt.title("Residual Plot Percent Students in Debt(%) vs Average State Debt($)")
plt.xlabel("Average State Debt($)")
plt.ylabel("Difference from LSRL prediction")
seaborn.residplot(x,y)


slope, intercept,r_val,p_val,std_err = stats.linregress(x,y)

print(slope,intercept,r_val,p_val,std_err)

mn=np.min(x)-1000
mx=np.max(x)+1000
x1=np.linspace(mn,mx,500)
y1=slope*x1+intercept

#plt.scatter(x,y,color="Red")
#plt.plot(x1,y1,color="Green")
#plt.title("Percent Students in Debt(%) vs Average State Debt($)")
#plt.xlabel("Average State Debt($)")
#plt.ylabel("Percent Students in Debt(%)")
plt.show()
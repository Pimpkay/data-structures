import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data=pd.read_csv('Accident Data.csv')

print(data.head())
# Data.to_csv('Accident.Data.csv')

# fatality=np.array(Data['Fatality'])
# SevereInjury=np.array(Data['Severe injury'])
# MinorInjury=np.array(Data['Minor injury'])


data['PersonsAffected']=data['Fatality']+data['Severe injury']+data['Minor injury']

plt.figure(figsize=(10,10))
plt.subplot(2,1,1)
plt.plot(data['Year'],data['PersonsAffected'])
plt.xlabel('Year')
plt.ylabel('Persons Affected')
plt.title('A graph of Persons affected against year')
plt.subplot(2,1,2)
plt.plot(data['Year'],data['Fatality'])
plt.xlabel('Year')
plt.ylabel('Fatality')
plt.title('A graph of fatality against year')
plt.savefig('6932521.png')
plt.show()
#https://github.com/Godwinosei/Data-structure.git

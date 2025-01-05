import pandas as pd
data_series = pd.Series([10,20,30,40,50,6.7])
#print(data_series)
data_frame = pd.DataFrame({'dept':['HR','IT','Engineering'], 'emp_count':[10,22,45] })
#print(data_frame)

#data_frame.info()
#print(data_frame['dept name'])

#print(data_frame.iloc[1])

specific_dept = ['HR','Engineerings']

print(data_frame[data_frame['dept'].isin(specific_dept)])
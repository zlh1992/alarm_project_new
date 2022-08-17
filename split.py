import pandas as pd

df_train_Alarm = pd.read_csv("df_train_Alarm.csv")
l = df_train_Alarm.shape[0]


df_train_Alarm.iloc[:l//4].to_csv("Alarm_0.csv",index=False)
df_train_Alarm.iloc[l//4:l//4*2].to_csv("Alarm_1.csv",index=False)
df_train_Alarm.iloc[l//4*2:l//4*3].to_csv("Alarm_2.csv",index=False)
df_train_Alarm.iloc[l//4*3:].to_csv("Alarm_3.csv",index=False)


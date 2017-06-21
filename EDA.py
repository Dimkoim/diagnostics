from Data_grouping_and_merging import *
import matplotlib.pyplot as plt
import configuration as conf



my_object = files_to_df(conf.directory)
full_dataset = my_object.df()
df_four_resistances = full_dataset[4].dropna(thresh = 3)
df_eight_resistances = full_dataset[8].dropna(thresh = 3)

#Find if they are any missing or NAN values and where they are in the two dataframes
idxs_four = np.where(pd.isnull(df_four_resistances))
idxs_eight = np.where(pd.isnull(df_eight_resistances))


plt.figure()
plt.plot(df_four_resistances.iloc[:,3], df_four_resistances.iloc[:,4])
plt.show()

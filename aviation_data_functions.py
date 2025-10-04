import pandas as pd 


def data_inspect():
    aviation_data_df = pd.read_csv('Aviation_Data.csv',  low_memory=False)
    print("There are",aviation_data_df.shape[1],"columns and",aviation_data_df.shape[0],"rows")
    print()
    print(aviation_data_df.columns)
    print("Information")
    print(aviation_data_df.info())
    print()
    print(aviation_data_df.describe())
    print()
    print("The Nan values in each column are:")
    print(aviation_data_df .isnull().sum())
    print()
    print('There are',aviation_data_df .duplicated().sum(),"duplicates")
    return aviation_data_df 
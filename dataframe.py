import pandas as pd
def my_func():
    df = pd.read_csv(r"item spreadsheet.csv")
    df_cleaned = df.dropna()
    print(df.head())
    df_cleaned['total price'] = df_cleaned['quantity']*df_cleaned['sales price']
    print(' ++++++++working ++++++++++ ')
    return df_cleaned

my_func()
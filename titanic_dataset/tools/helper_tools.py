# Helper tools created to make data cleaning simpler & more abstract
# Created by: Jimmy Grzybek

# Receives df object and returns a list of columns with the number of null entries
def find_columns_with_null_vals(df):
    columns = [] 
    for feature, is_null in df.isnull().any().iteritems():
        if is_null:
            print feature + ' missing values: ' + str(df[feature].isnull().sum()) 
            columns.append({'column': feature, 'num_null_values' : df[feature].isnull().sum() })
    
    return columns

     

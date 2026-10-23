import pandas as pd
import numpy as np


def create_series():
    s = pd.Series([10,15,20],index = [1,2,3] )
    print(s)
    print(s[1])

def create_dataframe():
    df = pd.DataFrame({
        "name": ["alice","jack","bob"],
        "age": [18,19,20],
        "score":[90,80,100]
    },index = ['a','b','c'])

    print(df)
    print(f'df index is:\n{df.index}')
    print(f"df columns is:\n{df.columns}")
    print(f'df value is:\n{df.values}')
    print(f'df dtypes is:\n{df.dtypes}')
    print(f'df shape is:\n{df.shape}')


    df.info()
    print(df.describe())

def create_data_frame():
    # 字典创建
    data = {
        "name": ["alice","jack","bob"],
        "age": [18,19,20],
        "score": [90,80,100]
    }
    df1 = pd.DataFrame(data)
    print(df1)

    # numpy.array创建
    arr = np.arange(1,7).reshape((2,3))
    df2 = pd.DataFrame(arr,columns = ["c1","c2","c3"])
    print(df2)

    # 列表嵌套
    df3 = pd.DataFrame([[1,2],[3,4]],columns = ["c1","c2"])
    print(df3)

    # json风格列表（由字典组成）
    # 即使某些行少了字段或多了字段，Pandas 也会自动对齐列名，并用 NaN 补齐。
    data = [
        {'age': 18, 'score': 80, 'name': 'Alice'},
        {'age': 19, 'score': 90, 'name': 'Bob'},
        {'score': 100, 'name': 'Charlie'}
    ]
    df4 = pd.DataFrame(data)
    print(df4)

def loc():
    df = pd.read_csv('S')

    
if __name__ == "__main__":
    create_data_frame()
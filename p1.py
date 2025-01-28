Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import pandas as pd
>>> import numpy as np
>>> df = pd.read_csv ('E:\Fall 2021\DASC 5300 (Foundation of Computing)\Project 1\Census Adult Data - dasc-5300-p1-census-adult.csv')
>>> df1=df.replace({'United-States':'US'},regex=True)
>>> df2=df1.replace("?",np.NaN)
>>> df3=df2.dropna()
>>> df3
       Age         workclass  fnlwgt  ... hours-per-week  native-country gincome
0       39         State-gov   77516  ...             40              US   <=50K
1       50  Self-emp-not-inc   83311  ...             13              US   <=50K
2       38           Private  215646  ...             40              US   <=50K
3       53           Private  234721  ...             40              US   <=50K
4       28           Private  338409  ...             40            Cuba   <=50K
...    ...               ...     ...  ...            ...             ...     ...
32556   27           Private  257302  ...             38              US   <=50K
32557   40           Private  154374  ...             40              US    >50K
32558   58           Private  151910  ...             40              US   <=50K
32559   22           Private  201490  ...             20              US   <=50K
32560   52      Self-emp-inc  287927  ...             40              US    >50K

[30162 rows x 15 columns]
>>> df3.to_csv('cleandata.csv',index=False)
>>> df4=df3[df3.gincome=='<=50K']
>>> df4
       Age         workclass  fnlwgt  ... hours-per-week  native-country gincome
0       39         State-gov   77516  ...             40              US   <=50K
1       50  Self-emp-not-inc   83311  ...             13              US   <=50K
2       38           Private  215646  ...             40              US   <=50K
3       53           Private  234721  ...             40              US   <=50K
4       28           Private  338409  ...             40            Cuba   <=50K
...    ...               ...     ...  ...            ...             ...     ...
32553   32           Private  116138  ...             11          Taiwan   <=50K
32555   22           Private  310152  ...             40              US   <=50K
32556   27           Private  257302  ...             38              US   <=50K
32558   58           Private  151910  ...             40              US   <=50K
32559   22           Private  201490  ...             20              US   <=50K

[22654 rows x 15 columns]
>>> df4.to_csv('gincome_lessthanorequalto50K.csv',index=False)
>>> df5=df3[df3.gincome=='>50K']
>>> df5
       Age         workclass  fnlwgt  ... hours-per-week  native-country gincome
7       52  Self-emp-not-inc  209642  ...             45              US    >50K
8       31           Private   45781  ...             50              US    >50K
9       42           Private  159449  ...             40              US    >50K
10      37           Private  280464  ...             80              US    >50K
11      30         State-gov  141297  ...             40           India    >50K
...    ...               ...     ...  ...            ...             ...     ...
32538   38           Private  139180  ...             45              US    >50K
32545   39         Local-gov  111499  ...             20              US    >50K
32554   53           Private  321865  ...             40              US    >50K
32557   40           Private  154374  ...             40              US    >50K
32560   52      Self-emp-inc  287927  ...             40              US    >50K

[7508 rows x 15 columns]
>>> df5.to_csv('gincome_greaterthan50K.csv',index=False)
>>> df6 = df1[np.invert(df1.index.isin(df3.index))]
>>> df6
       Age workclass  fnlwgt  ... hours-per-week  native-country gincome
14      40   Private  121772  ...             40               ?    >50K
27      54         ?  180211  ...             60           South    >50K
38      31   Private   84154  ...             38               ?    >50K
51      18   Private  226956  ...             30               ?   <=50K
61      32         ?  293936  ...             40               ?   <=50K
...    ...       ...     ...  ...            ...             ...     ...
32530   35         ?  320084  ...             55              US    >50K
32531   30         ?   33811  ...             99              US   <=50K
32539   71         ?  287372  ...             10              US    >50K
32541   41         ?  202822  ...             32              US   <=50K
32542   72         ?  129912  ...             25              US   <=50K

[2399 rows x 15 columns]
>>> df6.to_csv('eleminatedlines.csv',index=False)
>>> 
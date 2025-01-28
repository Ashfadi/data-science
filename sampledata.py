Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> sample_data=dataframe.sample(175, random_state = 09201999)
SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
>>> import pandas as pd
>>> import numpy as np
>>> sample_data=dataframe.sample(175, random_state = 09201999)
SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
>>>  sample_data=dataframe.sample(175, random_state = 9201999)
 
SyntaxError: unexpected indent
>>> sample_data=dataframe.sample(175, random_state = 09201999)
SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
>>> sample_data=dataframe.sample(175, random_state = 9201999)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    sample_data=dataframe.sample(175, random_state = 9201999)
NameError: name 'dataframe' is not defined
>>> df = pd.read_csv ('E:\Fall 2021\DASC 5300 (Foundation of Computing)\Project 1\cleandata.csv')
>>> sample_data=df.sample(175, random_state = 9201999)
>>> sample_data
       Age  workclass  fnlwgt  ... hours-per-week  native-country gincome
23527   27    Private   78529  ...             15              US   <=50K
24071   31    Private  169589  ...             30              US   <=50K
9558    36    Private  135289  ...             48              US    >50K
28403   56    Private  170070  ...             40              US    >50K
9341    24    Private   32311  ...             40              US   <=50K
...    ...        ...     ...  ...            ...             ...     ...
3374    27    Private  150025  ...             40       Guatemala   <=50K
8790    39  Local-gov  222572  ...             43              US   <=50K
21384   47    Private   39530  ...              4              US   <=50K
18394   39    Private  236391  ...             50              US    >50K
23325   19    Private   43003  ...             20              US   <=50K

[175 rows x 15 columns]
>>> sample_data.to_csv('sampledata.csv',index=False)
>>> import os
>>> os.cgwd()
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    os.cgwd()
AttributeError: module 'os' has no attribute 'cgwd'
>>> 
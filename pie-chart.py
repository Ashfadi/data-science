Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import pandas as pd
>>> import numpy as np
>>> import matplotlib.pyplot as plt
>>> df=pd.read_csv('E:\Fall 2021\DASC 5300 (Foundation of Computing)\Project 1\sampledata.csv')
>>> df['Age'].value_counts(bins=[0,20,40,60,100])
(20.0, 40.0]      98
(40.0, 60.0]      58
(60.0, 100.0]     12
(-0.001, 20.0]     7
Name: Age, dtype: int64
>>> df.groupby['Age']('workclass').value_counts(bins=[0,20,40,60,100])
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    df.groupby['Age']('workclass').value_counts(bins=[0,20,40,60,100])
TypeError: 'method' object is not subscriptable
>>> df.groupby['Age']('workclass').value_counts()
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    df.groupby['Age']('workclass').value_counts()
TypeError: 'method' object is not subscriptable
>>> df.groupby('workclass')['Age'].value_counts()
workclass    Age
Federal-gov  27     1
             39     1
             42     1
             51     1
             53     1
                   ..
State-gov    35     1
             37     1
             47     1
             58     1
             59     1
Name: Age, Length: 85, dtype: int64
>>> df.groupby('workclass')['Age'].value_counts(bins=[0,20,40,60,100])
workclass         Age           
Federal-gov       (40.0, 60.0]       3
                  (20.0, 40.0]       2
                  (-0.001, 20.0]     0
                  (60.0, 100.0]      0
Local-gov         (20.0, 40.0]      12
                  (40.0, 60.0]       5
                  (-0.001, 20.0]     0
                  (60.0, 100.0]      0
Private           (20.0, 40.0]      75
                  (40.0, 60.0]      38
                  (-0.001, 20.0]     7
                  (60.0, 100.0]      5
Self-emp-inc      (40.0, 60.0]       5
                  (20.0, 40.0]       1
                  (60.0, 100.0]      1
                  (-0.001, 20.0]     0
Self-emp-not-inc  (60.0, 100.0]      6
                  (40.0, 60.0]       4
                  (20.0, 40.0]       3
                  (-0.001, 20.0]     0
State-gov         (20.0, 40.0]       5
                  (40.0, 60.0]       3
                  (-0.001, 20.0]     0
                  (60.0, 100.0]      0
Name: Age, dtype: int64
>>> plt.pie(df.groupby('workclass')['Age'].value_counts(bins=[0,20,40,60,100]))
([<matplotlib.patches.Wedge object at 0x0000025C8F8CD130>, <matplotlib.patches.Wedge object at 0x0000025C8F8CD5B0>, <matplotlib.patches.Wedge object at 0x0000025C8F8CDA90>, <matplotlib.patches.Wedge object at 0x0000025C8F8CDF70>, <matplotlib.patches.Wedge object at 0x0000025C92422490>, <matplotlib.patches.Wedge object at 0x0000025C92422970>, <matplotlib.patches.Wedge object at 0x0000025C92422E50>, <matplotlib.patches.Wedge object at 0x0000025C92430370>, <matplotlib.patches.Wedge object at 0x0000025C92430850>, <matplotlib.patches.Wedge object at 0x0000025C92430D30>, <matplotlib.patches.Wedge object at 0x0000025C8F82FCD0>, <matplotlib.patches.Wedge object at 0x0000025C9243E700>, <matplotlib.patches.Wedge object at 0x0000025C9243EBE0>, <matplotlib.patches.Wedge object at 0x0000025C9244B100>, <matplotlib.patches.Wedge object at 0x0000025C9244B5E0>, <matplotlib.patches.Wedge object at 0x0000025C9244BAC0>, <matplotlib.patches.Wedge object at 0x0000025C9244BFA0>, <matplotlib.patches.Wedge object at 0x0000025C924594C0>, <matplotlib.patches.Wedge object at 0x0000025C924599A0>, <matplotlib.patches.Wedge object at 0x0000025C92459E80>, <matplotlib.patches.Wedge object at 0x0000025C924643A0>, <matplotlib.patches.Wedge object at 0x0000025C92464880>, <matplotlib.patches.Wedge object at 0x0000025C92464D60>, <matplotlib.patches.Wedge object at 0x0000025C92471280>], [Text(1.098405135318831, 0.05921282551289575, ''), Text(1.0886754827943856, 0.15743472667239497, ''), Text(1.0823225484108048, 0.19641257903082862, ''), Text(1.0823225484108048, 0.19641257903082862, ''), Text(1.0153203197720881, 0.42323119953272, ''), Text(0.8412368682764212, 0.7087457452799836, ''), Text(0.7743188167773495, 0.7813004351621249, ''), Text(0.7743188167773495, 0.7813004351621249, ''), Text(-0.5894094681725242, 0.9287607220530929, ''), Text(-0.5726423382327758, -0.9391915419462099, ''), Text(0.2831110651859813, -1.0629431427735254, ''), Text(0.5037831748527211, -0.9778560797659914, ''), Text(0.6702901180136627, -0.8721875702469226, ''), Text(0.7601688812182518, -0.7950743814432657, ''), Text(0.7882191211580297, -0.7672747989090111, ''), Text(0.8018654587905542, -0.7530018499304064, ''), Text(0.8781688067079911, -0.6624345604850814, ''), Text(0.9823385284319058, -0.49498587409969375, ''), Text(1.0366306748609564, -0.36796310132582355, ''), Text(1.0549350832820816, -0.31162793530206445, ''), Text(1.078622337646405, -0.2158097605072689, ''), Text(1.0984051318538888, -0.05921288978796486, ''), Text(1.0999999999999983, -6.436839559439856e-08, ''), Text(1.0999999999999983, -6.436839559439856e-08, '')])
>>> plt.show()
>>> df.groupby('Age')['workclass'].value_counts(bins=[0,20,40,60,100])
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    df.groupby('Age')['workclass'].value_counts(bins=[0,20,40,60,100])
  File "C:\Users\alish\AppData\Local\Programs\Python\Python39\lib\site-packages\pandas\core\groupby\generic.py", line 725, in value_counts
    lab = cut(Series(val), bins, include_lowest=True)
  File "C:\Users\alish\AppData\Local\Programs\Python\Python39\lib\site-packages\pandas\core\reshape\tile.py", line 287, in cut
    fac, bins = _bins_to_cuts(
  File "C:\Users\alish\AppData\Local\Programs\Python\Python39\lib\site-packages\pandas\core\reshape\tile.py", line 421, in _bins_to_cuts
    ids = ensure_platform_int(bins.searchsorted(x, side=side))
TypeError: '<' not supported between instances of 'int' and 'str'
>>> df.groupby('Age')['workclass'].value_counts(bins=[Private,Federal-gov,Local-gov,Self-emp-inc,Self-emp-not-inc,State-gov])
SyntaxError: invalid syntax
>>> df.groupby('Age')['workclass'].value_counts(bins=[Private,self-employed,government,without-pay])
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    df.groupby('Age')['workclass'].value_counts(bins=[Private,self-employed,government,without-pay])
NameError: name 'Private' is not defined
>>> df.groupby('Age')['workclass'].value_counts()
Age  workclass       
17   Private             1
18   Private             2
19   Private             3
20   Private             1
21   Private             3
                        ..
68   Self-emp-not-inc    1
69   Private             1
70   Self-emp-not-inc    1
71   Private             1
73   Self-emp-not-inc    1
Name: workclass, Length: 85, dtype: int64
>>> df['age_bins']=pd.cut(df['Age'],bins=[0,20,40,60,100],labels=('<21','21-40','41-60','>60'))
>>> df
     Age  workclass  fnlwgt  ... native-country  gincome age_bins
0     27    Private   78529  ...             US    <=50K    21-40
1     31    Private  169589  ...             US    <=50K    21-40
2     36    Private  135289  ...             US     >50K    21-40
3     56    Private  170070  ...             US     >50K    41-60
4     24    Private   32311  ...             US    <=50K    21-40
..   ...        ...     ...  ...            ...      ...      ...
170   27    Private  150025  ...      Guatemala    <=50K    21-40
171   39  Local-gov  222572  ...             US    <=50K    21-40
172   47    Private   39530  ...             US    <=50K    41-60
173   39    Private  236391  ...             US     >50K    21-40
174   19    Private   43003  ...             US    <=50K      <21

[175 rows x 16 columns]
>>> df.groupby('workclass')['Age'].value_counts()
workclass    Age
Federal-gov  27     1
             39     1
             42     1
             51     1
             53     1
                   ..
State-gov    35     1
             37     1
             47     1
             58     1
             59     1
Name: Age, Length: 85, dtype: int64
>>> df.groupby('workclass')['age_bins'].value_counts()
workclass              
Federal-gov       41-60     3
                  21-40     2
                  <21       0
                  >60       0
Local-gov         21-40    12
                  41-60     5
                  <21       0
                  >60       0
Private           21-40    75
                  41-60    38
                  <21       7
                  >60       5
Self-emp-inc      41-60     5
                  21-40     1
                  >60       1
                  <21       0
Self-emp-not-inc  >60       6
                  41-60     4
                  21-40     3
                  <21       0
State-gov         21-40     5
                  41-60     3
                  <21       0
                  >60       0
Name: age_bins, dtype: int64
>>> df.groupby('age_bins')['workclass'].value_counts()
age_bins  workclass       
<21       Private              7
21-40     Private             75
          Local-gov           12
          State-gov            5
          Self-emp-not-inc     3
          Federal-gov          2
          Self-emp-inc         1
41-60     Private             38
          Local-gov            5
          Self-emp-inc         5
          Self-emp-not-inc     4
          Federal-gov          3
          State-gov            3
>60       Self-emp-not-inc     6
          Private              5
          Self-emp-inc         1
Name: workclass, dtype: int64
>>> plt.pie(df.groupby('age_bins')['workclass'].value_counts())
([<matplotlib.patches.Wedge object at 0x0000025C8FB76C70>, <matplotlib.patches.Wedge object at 0x0000025C8FB851F0>, <matplotlib.patches.Wedge object at 0x0000025C8FB856D0>, <matplotlib.patches.Wedge object at 0x0000025C8FB85BB0>, <matplotlib.patches.Wedge object at 0x0000025C8FB910D0>, <matplotlib.patches.Wedge object at 0x0000025C8FB915B0>, <matplotlib.patches.Wedge object at 0x0000025C8FB91A90>, <matplotlib.patches.Wedge object at 0x0000025C8FB91F70>, <matplotlib.patches.Wedge object at 0x0000025C8FBA0490>, <matplotlib.patches.Wedge object at 0x0000025C8FBA0970>, <matplotlib.patches.Wedge object at 0x0000025C8FA12790>, <matplotlib.patches.Wedge object at 0x0000025C8FBAC340>, <matplotlib.patches.Wedge object at 0x0000025C8FBAC820>, <matplotlib.patches.Wedge object at 0x0000025C8FBACD00>, <matplotlib.patches.Wedge object at 0x0000025C8FBB9220>, <matplotlib.patches.Wedge object at 0x0000025C8FBB9700>], [Text(1.0913261718331657, 0.13786655385541477, ''), Text(-0.02961715966054547, 1.0996012112823639, ''), Text(-1.0998227544657784, -0.019746107447000123, ''), Text(-1.0430689605588643, -0.34929520969897426, ''), Text(-0.982338551603866, -0.4949858281131075, ''), Text(-0.9340137592575304, -0.5810493073032755, ''), Text(-0.9013817612405436, -0.6304846711085812, ''), Text(-0.28311113049592845, -1.062943125378455, ''), Text(0.5385598181255471, -0.9591419719210383, ''), Text(0.7011663533115138, -0.8475645963487585, ''), Text(0.8283785821721403, -0.7237326333657165, ''), Text(0.9125543190775844, -0.6142024216273054, ''), Text(0.9732947546826942, -0.512540067221241, ''), Text(1.0430689431851936, -0.349295261580405, ''), Text(1.0913261633622895, -0.13786662090928792, ''), Text(1.099822753570282, -0.019746157324469132, '')])
>>> plt.show()
>>> df.groupby('age_bins')['workclass'].value_counts(bins=1)
Traceback (most recent call last):
  File "C:\Users\alish\AppData\Local\Programs\Python\Python39\lib\site-packages\pandas\core\algorithms.py", line 835, in value_counts
    ii = cut(values, bins, include_lowest=True)
  File "C:\Users\alish\AppData\Local\Programs\Python\Python39\lib\site-packages\pandas\core\reshape\tile.py", line 253, in cut
    mn, mx = (mi + 0.0 for mi in rng)
  File "C:\Users\alish\AppData\Local\Programs\Python\Python39\lib\site-packages\pandas\core\reshape\tile.py", line 253, in <genexpr>
    mn, mx = (mi + 0.0 for mi in rng)
TypeError: can only concatenate str (not "float") to str

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "C:\Users\alish\AppData\Local\Programs\Python\Python39\lib\site-packages\pandas\core\groupby\groupby.py", line 1272, in apply
    result = self._python_apply_general(f, self._selected_obj)
  File "C:\Users\alish\AppData\Local\Programs\Python\Python39\lib\site-packages\pandas\core\groupby\groupby.py", line 1306, in _python_apply_general
    keys, values, mutated = self.grouper.apply(f, data, self.axis)
  File "C:\Users\alish\AppData\Local\Programs\Python\Python39\lib\site-packages\pandas\core\groupby\ops.py", line 820, in apply
    res = f(group)
  File "C:\Users\alish\AppData\Local\Programs\Python\Python39\lib\site-packages\pandas\core\groupby\groupby.py", line 1256, in f
    return func(g, *args, **kwargs)
  File "C:\Users\alish\AppData\Local\Programs\Python\Python39\lib\site-packages\pandas\core\base.py", line 960, in value_counts
    return value_counts(
  File "C:\Users\alish\AppData\Local\Programs\Python\Python39\lib\site-packages\pandas\core\algorithms.py", line 837, in value_counts
    raise TypeError("bins argument only works with numeric data.") from err
TypeError: bins argument only works with numeric data.

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Users\alish\AppData\Local\Programs\Python\Python39\lib\site-packages\pandas\core\algorithms.py", line 835, in value_counts
    ii = cut(values, bins, include_lowest=True)
  File "C:\Users\alish\AppData\Local\Programs\Python\Python39\lib\site-packages\pandas\core\reshape\tile.py", line 253, in cut
    mn, mx = (mi + 0.0 for mi in rng)
  File "C:\Users\alish\AppData\Local\Programs\Python\Python39\lib\site-packages\pandas\core\reshape\tile.py", line 253, in <genexpr>
    mn, mx = (mi + 0.0 for mi in rng)
TypeError: can only concatenate str (not "float") to str

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    df.groupby('age_bins')['workclass'].value_counts(bins=1)
  File "C:\Users\alish\AppData\Local\Programs\Python\Python39\lib\site-packages\pandas\core\groupby\generic.py", line 710, in value_counts
    return apply_series_value_counts()
  File "C:\Users\alish\AppData\Local\Programs\Python\Python39\lib\site-packages\pandas\core\groupby\generic.py", line 698, in apply_series_value_counts
    return self.apply(
  File "C:\Users\alish\AppData\Local\Programs\Python\Python39\lib\site-packages\pandas\core\groupby\generic.py", line 223, in apply
    return super().apply(func, *args, **kwargs)
  File "C:\Users\alish\AppData\Local\Programs\Python\Python39\lib\site-packages\pandas\core\groupby\groupby.py", line 1283, in apply
    return self._python_apply_general(f, self._selected_obj)
  File "C:\Users\alish\AppData\Local\Programs\Python\Python39\lib\site-packages\pandas\core\groupby\groupby.py", line 1306, in _python_apply_general
    keys, values, mutated = self.grouper.apply(f, data, self.axis)
  File "C:\Users\alish\AppData\Local\Programs\Python\Python39\lib\site-packages\pandas\core\groupby\ops.py", line 820, in apply
    res = f(group)
  File "C:\Users\alish\AppData\Local\Programs\Python\Python39\lib\site-packages\pandas\core\groupby\groupby.py", line 1256, in f
    return func(g, *args, **kwargs)
  File "C:\Users\alish\AppData\Local\Programs\Python\Python39\lib\site-packages\pandas\core\base.py", line 960, in value_counts
    return value_counts(
  File "C:\Users\alish\AppData\Local\Programs\Python\Python39\lib\site-packages\pandas\core\algorithms.py", line 837, in value_counts
    raise TypeError("bins argument only works with numeric data.") from err
TypeError: bins argument only works with numeric data.
>>> df.groupby('workclass')['age_bins'].value_counts(bins=1)
Traceback (most recent call last):
  File "C:\Users\alish\AppData\Local\Programs\Python\Python39\lib\site-packages\pandas\core\algorithms.py", line 835, in value_counts
    ii = cut(values, bins, include_lowest=True)
  File "C:\Users\alish\AppData\Local\Programs\Python\Python39\lib\site-packages\pandas\core\reshape\tile.py", line 252, in cut
    rng = (nanops.nanmin(x), nanops.nanmax(x))
  File "C:\Users\alish\AppData\Local\Programs\Python\Python39\lib\site-packages\pandas\core\nanops.py", line 155, in f
    result = alt(values, axis=axis, skipna=skipna, **kwds)
  File "C:\Users\alish\AppData\Local\Programs\Python\Python39\lib\site-packages\pandas\core\nanops.py", line 410, in new_func
    result = func(values, axis=axis, skipna=skipna, mask=mask, **kwargs)
  File "C:\Users\alish\AppData\Local\Programs\Python\Python39\lib\site-packages\pandas\core\nanops.py", line 1017, in reduction
    result = getattr(values, meth)(axis)
  File "C:\Users\alish\AppData\Local\Programs\Python\Python39\lib\site-packages\pandas\util\_decorators.py", line 207, in wrapper
    return func(*args, **kwargs)
TypeError: min() takes 1 positional argument but 2 were given

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "C:\Users\alish\AppData\Local\Programs\Python\Python39\lib\site-packages\pandas\core\groupby\groupby.py", line 1272, in apply
    result = self._python_apply_general(f, self._selected_obj)
  File "C:\Users\alish\AppData\Local\Programs\Python\Python39\lib\site-packages\pandas\core\groupby\groupby.py", line 1306, in _python_apply_general
    keys, values, mutated = self.grouper.apply(f, data, self.axis)
  File "C:\Users\alish\AppData\Local\Programs\Python\Python39\lib\site-packages\pandas\core\groupby\ops.py", line 820, in apply
    res = f(group)
  File "C:\Users\alish\AppData\Local\Programs\Python\Python39\lib\site-packages\pandas\core\groupby\groupby.py", line 1256, in f
    return func(g, *args, **kwargs)
  File "C:\Users\alish\AppData\Local\Programs\Python\Python39\lib\site-packages\pandas\core\base.py", line 960, in value_counts
    return value_counts(
  File "C:\Users\alish\AppData\Local\Programs\Python\Python39\lib\site-packages\pandas\core\algorithms.py", line 837, in value_counts
    raise TypeError("bins argument only works with numeric data.") from err
TypeError: bins argument only works with numeric data.

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Users\alish\AppData\Local\Programs\Python\Python39\lib\site-packages\pandas\core\algorithms.py", line 835, in value_counts
    ii = cut(values, bins, include_lowest=True)
  File "C:\Users\alish\AppData\Local\Programs\Python\Python39\lib\site-packages\pandas\core\reshape\tile.py", line 252, in cut
    rng = (nanops.nanmin(x), nanops.nanmax(x))
  File "C:\Users\alish\AppData\Local\Programs\Python\Python39\lib\site-packages\pandas\core\nanops.py", line 155, in f
    result = alt(values, axis=axis, skipna=skipna, **kwds)
  File "C:\Users\alish\AppData\Local\Programs\Python\Python39\lib\site-packages\pandas\core\nanops.py", line 410, in new_func
    result = func(values, axis=axis, skipna=skipna, mask=mask, **kwargs)
  File "C:\Users\alish\AppData\Local\Programs\Python\Python39\lib\site-packages\pandas\core\nanops.py", line 1017, in reduction
    result = getattr(values, meth)(axis)
  File "C:\Users\alish\AppData\Local\Programs\Python\Python39\lib\site-packages\pandas\util\_decorators.py", line 207, in wrapper
    return func(*args, **kwargs)
TypeError: min() takes 1 positional argument but 2 were given

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    df.groupby('workclass')['age_bins'].value_counts(bins=1)
  File "C:\Users\alish\AppData\Local\Programs\Python\Python39\lib\site-packages\pandas\core\groupby\generic.py", line 710, in value_counts
    return apply_series_value_counts()
  File "C:\Users\alish\AppData\Local\Programs\Python\Python39\lib\site-packages\pandas\core\groupby\generic.py", line 698, in apply_series_value_counts
    return self.apply(
  File "C:\Users\alish\AppData\Local\Programs\Python\Python39\lib\site-packages\pandas\core\groupby\generic.py", line 223, in apply
    return super().apply(func, *args, **kwargs)
  File "C:\Users\alish\AppData\Local\Programs\Python\Python39\lib\site-packages\pandas\core\groupby\groupby.py", line 1283, in apply
    return self._python_apply_general(f, self._selected_obj)
  File "C:\Users\alish\AppData\Local\Programs\Python\Python39\lib\site-packages\pandas\core\groupby\groupby.py", line 1306, in _python_apply_general
    keys, values, mutated = self.grouper.apply(f, data, self.axis)
  File "C:\Users\alish\AppData\Local\Programs\Python\Python39\lib\site-packages\pandas\core\groupby\ops.py", line 820, in apply
    res = f(group)
  File "C:\Users\alish\AppData\Local\Programs\Python\Python39\lib\site-packages\pandas\core\groupby\groupby.py", line 1256, in f
    return func(g, *args, **kwargs)
  File "C:\Users\alish\AppData\Local\Programs\Python\Python39\lib\site-packages\pandas\core\base.py", line 960, in value_counts
    return value_counts(
  File "C:\Users\alish\AppData\Local\Programs\Python\Python39\lib\site-packages\pandas\core\algorithms.py", line 837, in value_counts
    raise TypeError("bins argument only works with numeric data.") from err
TypeError: bins argument only works with numeric data.
>>> df1=df.replace({'Federal-gov','Local-gov','State-gov':'Government'},regex=True)
SyntaxError: invalid syntax
>>> df1=df.replace({'Federal-gov':'Government'},regex=True)
>>> df2=df1.replace({'Local-gov':'Government'},regex=True)
>>> df3=df2.replace({'State-gov':'Government'},regex=True)
>>> df4=df3.replace({'Self-emp-inc':'self-employed'},regex=True)
>>> df5=df4.replace({'Self-emp-not-inc':'self-employed'},regex=True)
>>> df5
     Age   workclass  fnlwgt  ... native-country  gincome age_bins
0     27     Private   78529  ...             US    <=50K    21-40
1     31     Private  169589  ...             US    <=50K    21-40
2     36     Private  135289  ...             US     >50K    21-40
3     56     Private  170070  ...             US     >50K    41-60
4     24     Private   32311  ...             US    <=50K    21-40
..   ...         ...     ...  ...            ...      ...      ...
170   27     Private  150025  ...      Guatemala    <=50K    21-40
171   39  Government  222572  ...             US    <=50K    21-40
172   47     Private   39530  ...             US    <=50K    41-60
173   39     Private  236391  ...             US     >50K    21-40
174   19     Private   43003  ...             US    <=50K      <21

[175 rows x 16 columns]
>>> df5.to_csv('workclass.csv',index=False)
>>> df5.groupby('age_bins')['workclass'].value_counts()
age_bins  workclass    
<21       Private           7
21-40     Private          75
          Government       19
          self-employed     4
41-60     Private          38
          Government       11
          self-employed     9
>60       self-employed     7
          Private           5
Name: workclass, dtype: int64
>>> tasks=[7,0,0,0]
>>> labels='Private','Government','self-employed','without-pay'
>>> plot=plt.pie(tasks,labels=labels,autopct='%1.1f%%')
>>> plt.show()
>>> plot=plt.pie(tasks,labels=labels)
>>> plt.show()
>>> tasks=[75,19,4,0]
>>> labels='Private','Government','self-employed','without-pay'
>>> plt.pie(tasks,labels=labels)
([<matplotlib.patches.Wedge object at 0x0000025C9015C5E0>, <matplotlib.patches.Wedge object at 0x0000025C9015CB80>, <matplotlib.patches.Wedge object at 0x0000025C9014E640>, <matplotlib.patches.Wedge object at 0x0000025C9016B460>], [Text(-0.8143057798261399, 0.7395309979586673, 'Private'), Text(0.713051188426204, -0.8375905937174667, 'Government'), Text(1.0909690056976373, -0.14066495159459172, 'self-employed'), Text(1.0999999999999974, -7.724207505019229e-08, 'without-pay')])
>>> plt.show()
>>> plt.pie(tasks,labels=labels,autopct='%1.1f%%')
([<matplotlib.patches.Wedge object at 0x0000025C9496F700>, <matplotlib.patches.Wedge object at 0x0000025C9496FEE0>, <matplotlib.patches.Wedge object at 0x0000025C9497A520>, <matplotlib.patches.Wedge object at 0x0000025C9497AC40>], [Text(-0.8143057798261399, 0.7395309979586673, 'Private'), Text(0.713051188426204, -0.8375905937174667, 'Government'), Text(1.0909690056976373, -0.14066495159459172, 'self-employed'), Text(1.0999999999999974, -7.724207505019229e-08, 'without-pay')], [Text(-0.44416678899607626, 0.4033805443410912, '76.5%'), Text(0.3889370118688385, -0.4568675965731636, '19.4%'), Text(0.5950740031078021, -0.07672633723341366, '4.1%'), Text(0.5999999999999985, -4.213204093646852e-08, '0.0%')])
>>> plt.show()
>>> 
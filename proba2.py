import pandas as pd

stamps = pd.date_range('2012-10-08 18:15:05', periods=4, freq='D')
print(stamps)

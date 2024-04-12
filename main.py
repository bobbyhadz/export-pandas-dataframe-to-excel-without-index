# Export a Pandas DataFrame to Excel without the Index

import pandas as pd

df = pd.DataFrame({
    'name': ['Alice', 'Bobby', 'Carl', 'Dan', 'Ethan'],
    'experience': [1, 1, 5, 7, 7],
    'salary': [175.1, 180.2, 190.3, 205.4, 210.5],
})

df.to_excel('output.xlsx', sheet_name='Sheet1', index=False)
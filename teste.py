import sys
import pandas as pd

arg = {'arquivo': sys.argv[1]}
df_object = {'coluna 1': sys.argv}

print(arg['arquivo'])
print(f'df_obj {df_object}')

nome_saida = sys.argv[2]

pd.DataFrame(df_object).to_excel(nome_saida)

f = open(arg['arquivo'])

for i in f:
  print(i)

f.close()


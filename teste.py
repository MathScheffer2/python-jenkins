import sys
import pandas as pd

arg ={'arquivo': sys.argv[1]}


print(arg['arquivo'])

pd.DataFrame(arg).to_excel('teste.xlsx')

f = open(arg['arquivo'])

for i in f:
  print(i)

f.close()


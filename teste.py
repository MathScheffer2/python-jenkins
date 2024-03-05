import sys
import pandas as pd

arg ={'teste': sys.argv}
"""  {"arg": sys.argv[1]} """

print(arg)

pd.DataFrame(arg).to_excel('teste.xlsx')


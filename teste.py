import sys
import pandas as pd

arg ={'teste': sys.argv}
"""  {"arg": sys.argv[1]} """


pd.DataFrame(arg).to_excel('teste.xlsx')


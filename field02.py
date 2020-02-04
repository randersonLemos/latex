import pandas as pd
from os import sys, path; sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
from config.scripts import settings as sett
from dictionary.scripts.sector_keys import Sector_Keys
from latex.scripts.fielddf import FieldDf


FieldDf.csvName = 'Field.csv'
FieldDf.csvRoot = sett.CSV_ROOT
FieldDf.simsFolder = sett.SIMS_FOLDER
FieldDf.dfIndex = Sector_Keys.date()
FieldDf.dfColsSelect.append(Sector_Keys.cum_oil_sc())
FieldDf.dfColsSelect.append(Sector_Keys.cum_gas_sc())
FieldDf.dfColsSelect.append(Sector_Keys.cum_wat_sc())
FieldDf.dfColsRename[Sector_Keys.cum_oil_sc()] = 'Oil'
FieldDf.dfColsRename[Sector_Keys.cum_gas_sc()] = 'Gas'
FieldDf.dfColsRename[Sector_Keys.cum_wat_sc()] = 'Water'


fDf1 = FieldDf('OWIPS', 'REFERENCE_OTM', 'sim_001')


fDfs = []
fDfs.append(FieldDf('BOIPS'   , 'SIM_ICV_01_STG'    , 'sim_006'))
fDfs.append(FieldDf('BSM2MIPS', 'SIM_ICV_02_STG_SMT', 'sim_007'))
fDfs.append(FieldDf('BNO2MIPS', 'SIM_ICV_02_STG'    , 'sim_007'))
fDfs.append(FieldDf('BSH2MIPS', 'SIM_ICV_02_STG_HRD', 'sim_007'))


df = pd.DataFrame()
for fDf in fDfs:
    fDf3 = fDf.div(fDf1)
    df[fDf3.name] = fDf3.df.iloc[-1,:]*100

ax = df.plot(kind='bar',rot=0)
ax.set_ylabel('%')
ax.set_title('Relative performance w/ respect to OWIPS')
ax.legend(loc='upper right')


#import matplotlib.pyplot as plt; plt.show()
import tikzplotlib; tikzplotlib.save('./latex/field/tikz/bar_graph02.tikz')

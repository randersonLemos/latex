from os import sys, path; sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
from config.scripts import settings as sett
from dictionary.scripts.sector_keys import Sector_Keys
from latex2.scripts.fielddf import FieldDf


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
fDf2 = FieldDf('BOIPS', 'SIM_ICV_01_STG','sim_006')
fDf3 = fDf2.div(fDf1)


srs = (fDf3.df.iloc[-1,:]*100)
srs.name = fDf3.name
ax = srs.plot(kind='bar',rot=0)
ax.set_title('Relative performance w/ respect to OWIPS')
ax.set_ylabel('%')


#import matplotlib.pyplot as plt; plt.show()
import tikzplotlib; tikzplotlib.save('./latex/field/tikz/bar_graph01.tikz')

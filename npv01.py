def filter_xtikcs(code, xticks):
    xticks = list(map(str, xticks))
    xticks_str = 'xtick={{{}}}'.format(','.join(xticks))
    bgn = code.find('xtick={')
    end = code.find('}',bgn)
    code = code.replace(code[bgn:end+1],xticks_str)
    return code



import matplotlib.pyplot as plt

from os import sys, path; sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
from config import settings as sett
from dictionary.scripts.sector_keys import Sector_Keys
from latex.scripts.npvdf import NpvDf
import tikzplotlib

NpvDf.csvSep = ','
NpvDf.csvName = 'Sims.npv'
NpvDf.csvRoot = sett.CSV_ROOT
NpvDf.simsFolder = sett.SIMS_FOLDER

nDf1 = NpvDf('OWIPS', 'REFERENCE_OTM')
nDf2 = NpvDf('OIPS', 'SIM_ICV_01_STG_EXT')

fig, ax = plt.subplots()


x = nDf2.df['Close Condition']
y = nDf2.df['Npv']/1000000
ax.plot(x, y, 'mo')
#ax.set_xticks(range(0,100,5))

ax.tick_params(axis="x", labelrotation=90)
ax.set_title('Net present value')
ax.set_xlabel('(GOR [$sm^3/sm^3$]; WCUT [$sm^3/sm^3$])')
ax.set_ylabel('Millions of dollars')
#plt.show()

code = tikzplotlib.get_tikz_code()
code = filter_xtikcs(code, range(0,100,5))
with open('./latex/npvf/tikz/graph01.tikz', 'w') as fh:
    fh.write(code)



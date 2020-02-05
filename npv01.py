TO_TIKZ = True


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
ax.plot(x, y, 'C0o', markersize=4)
#ax.set_xticks(range(0,100,5))

ax.tick_params(axis="x", labelrotation=90)
#ax.set_title('Net present value\\\\Production strategies w/ ON/OFF ICV\'s')
ax.set_xlabel('(GOR [$sm^3/sm^3$]; WCUT [$sm^3/sm^3$])')
ax.set_ylabel('Millions of dollars')
ax.set_xlim(-2,102)

if TO_TIKZ:
    settings = {}
    settings['textsize'] = 6
    settings['figurewidth'] = '0.90\\textwidth'
    settings['figureheight'] = '0.60\\textheight'
    eap = []
    eap.append('title={Net present value\\\\\\scriptsize{Production strategies w/ ON/OFF ICV\'s}}')
    eap.append('title style={align=left, font=\\normalsize}')
    eap.append('tick label style={font=\\scriptsize}')
    eap.append('label style={font=\\scriptsize}')
    eap.append('legend pos=north east')
    settings['extra_axis_parameters'] = eap
    settings['extra_tikzpicture_parameters'] = None
    code = tikzplotlib.get_tikz_code(**settings)
    code = filter_xtikcs(code, range(0,100,3))
    with open('./latex/npvf/tikz/graph01.tikz', 'w') as fh: fh.write(code)
else:
    plt.show()



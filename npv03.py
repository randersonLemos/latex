from os import sys, path; sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
import matplotlib.pyplot as plt
from config import settings as sett
from dictionary.scripts.sector_keys import Sector_Keys
from latex.scripts.npvdf import NpvDf
import tikzplotlib


NpvDf.csvSep = ','
NpvDf.csvName = 'Sims.npv'
NpvDf.csvRoot = sett.CSV_ROOT
NpvDf.simsFolder = sett.SIMS_FOLDER
NpvDf.dfColsScale['Npv'] = 0.000001

nDfs = []
nDfs.append(NpvDf('2MIPS', 'SIM_ICV_02_STG_SMT'))
nDfs.append(NpvDf('2MIPS', 'SIM_ICV_02_STG'))
nDfs.append(NpvDf('2MIPS', 'SIM_ICV_02_STG_HRD'))

fig, ax = plt.subplots()
for nDf in nDfs:
    ax.plot(nDf.df['Close Condition'], nDf.df['Npv'], '-o', markersize=4)
ax.tick_params(axis="x", labelrotation=90)
ax.set_xlabel('GOR [$sm^3/sm^3$]')
ax.set_ylabel('Millions of dollars')
ax.legend(['Smooth', 'Normal', 'Sharp'])
ax.set_xlim(1000,3500)
ax.set_ylim(2200,2400)

settings = {}
settings['textsize'] = 6
settings['figurewidth'] = '0.70\\textwidth'
settings['figureheight'] = '0.60\\textheight'
eap = []
eap.append('title={Net present value\\\\\\scriptsize{Production strategies w/ 2 stages multi-position ICV\'s}}')
eap.append('title style={align=left, font=\\normalsize}')
eap.append('tick label style={font=\\scriptsize}')
eap.append('label style={font=\\scriptsize}')
eap.append('legend style={font=\\tiny}')
eap.append('legend pos=north east')
eap.append('xtick={250,500,...,5000}')
settings['extra_axis_parameters'] = eap
settings['extra_tikzpicture_parameters'] = None
code = tikzplotlib.get_tikz_code(**settings)
#code = filter_xtikcs(code, 3)
with open('./latex/npvf/tikz/graph03.tikz', 'w') as fh: fh.write(code)

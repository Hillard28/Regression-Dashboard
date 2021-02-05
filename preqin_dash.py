# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 10:50:26 2020

@author: Ryan Gilland
"""

# =============================================================================
# Compiling Performance Dataset
# =============================================================================
# Import modules
import numpy as np
import pandas as pd
import glob

# Initialize filepaths
filePath = 'OneDrive - McKinsey & Company/Documents/scripts/preqin/'
path = 'OneDrive - McKinsey & Company/Documents/scripts/preqin/performance/'
all_files = glob.glob(path + '/*.xlsx')

# Merge all Preqin datasets to form raw master file
df_perf = pd.concat((pd.read_excel(f) for f in all_files))

# Convert all columns to string (Replace once astype(skipna) fixed)
df_perf = df_perf.where(df_perf.isna(), df_perf.astype(str))

# Convert numeric variables to int/float
df_perf[[
    'FUND ID',
    'FIRM ID',
    'VINTAGE / INCEPTION YEAR',
    'CALLED (%)',
    'DPI (%)',
    'RVPI (%)',
    'NET IRR (%)',
    'NET MULTIPLE (X)',
    'QUARTILE',
    'FUND SIZE (USD MN)',
    'FUND NUMBER (OVERALL)',
    'FUND NUMBER (SERIES)',
    'LIFESPAN (YEARS)',
    'TARGET IRR - NET MIN',
    'TARGET IRR - NET MAX',
    'TARGET IRR - GROSS MIN',
    'TARGET IRR - GROSS MAX',
    'TARGET SIZE (CURR. MN)',
    'TARGET SIZE (USD MN)',
    'TARGET SIZE (EUR MN)',
    'INITIAL TARGET (CURR. MN)',
    'INITIAL TARGET (USD MN)',
    'INITIAL TARGET (EUR MN)',
    'HARD CAP (CURR. MN)',
    'HARD CAP (USD MN)',
    'HARD CAP (EUR MN)',
    'LATEST INTERIM CLOSE SIZE (CURR. MN)',
    'LATEST INTERIM CLOSE SIZE (USD MN)',
    'LATEST INTERIM CLOSE SIZE (EUR MN)',
    'FINAL CLOSE SIZE (CURR. MN)',
    'FINAL CLOSE SIZE (USD MN)',
    'FINAL CLOSE SIZE (EUR MN)',
    'CO-INVESTMENT CAPITAL AMOUNT (CURR. MN)',
    'CO-INVESTMENT CAPITAL AMOUNT (USD MN)',
    'CO-INVESTMENT CAPITAL AMOUNT (EUR MN)',
    'MONTHS TO FIRST CLOSE',
    'MONTHS IN MARKET',
    'PE: BUYOUT FUND LEVERAGE (%)',
    'PE: BUYOUT FUND SIZE',
    'PE: INVESTMENT SIZE PER PORTFOLIO COMPANY (MIN)',
    'PE: INVESTMENT SIZE PER PORTFOLIO COMPANY (MAX)',
    'RE: TARGET LEVERAGE (UPPER RANGE)',
    'RE: TARGET LEVERAGE (LOWER RANGE)',
    'RE: MAXIMUM LEVERAGE',
    'PD: LEVERAGE USED (X) MIN',
    'PD: LEVERAGE USED (X) MAX',
    'MGMT FEE RATE (%) DURING INV PERIOD',
    'INVESTMENT PERIOD (YRS)',
    'MGMT FEE RATE (%) - POST-INVESTMENT PERIOD',
    'CARRIED INTEREST (%)',
    'GP CATCH UP RATE (%)',
    'HURDLE RATE (%)',
    'SHARE OF TRANSACTION FEES REBATED TO LP (%)',
    'LP MAJORITY REQUIRED (%)',
    'FUND FORMATION COSTS (MN)',
    'GP COMMITMENTS TO FUND (% OF TOTAL)',
    'NUMBER OF LPS (MIN)',
    'NUMBER OF LPS (MAX)',
    'PERCENTAGE OF RETURNING LPS',
    'MEDIAN BENCHMARK NET IRR (%)',
    'MEDIAN BENCHMARK CALLED (%)',
    'MEDIAN BENCHMARK DISTRIBUTED (%) DPI',
    'MEDIAN BENCHMARK NET MULTIPLE (X)',
    'MEDIAN BENCHMARK RVPI (%)',
    'AVERAGE BENCHMARK NET IRR (%)',
    'AVERAGE BENCHMARK CALLED (%)',
    'AVERAGE BENCHMARK DISTRIBUTED (%) DPI',
    'AVERAGE BENCHMARK NET MULTIPLE (X)',
    'AVERAGE BENCHMARK RVPI (%)',
    'WEIGHTED BENCHMARK NET IRR (%)',
    'WEIGHTED BENCHMARK CALLED (%)',
    'WEIGHTED BENCHMARK DISTRIBUTED (%) DPI',
    'WEIGHTED BENCHMARK NET MULTIPLE (X)',
    'WEIGHTED BENCHMARK RVPI (%)',
    'POOLED BENCHMARK NET IRR (%)',
    'S&P 500 LN-PME',
    'S&P 500 KS-PME',
    'S&P 500 PME+',
    'RUSSELL 2000 LN-PME',
    'RUSSELL 2000 KS-PME',
    'RUSSELL 2000 PME+',
    'RUSSELL 3000 LN-PME',
    'RUSSELL 3000 KS-PME',
    'RUSSELL 3000 PME+',
    'MSCI EMERGING MARKETS LN-PME',
    'MSCI EMERGING MARKETS KS-PME',
    'MSCI EMERGING MARKETS PME+',
    'MSCI EUROPE STANDARD LN-PME',
    'MSCI EUROPE STANDARD KS-PME',
    'MSCI EUROPE STANDARD PME+',
    'MSCI US REIT LN-PME',
    'MSCI US REIT KS-PME',
    'MSCI US REIT PME+',
    'MSCI WORLD LN-PME',
    'MSCI WORLD KS-PME',
    'MSCI WORLD PME+',
    'ESTIMATED LAUNCH',
    'AUM (CURR. MN)',
    'AUM (USD MN)',
    'AUM (EUR MN)',
    'DRY POWDER (CURR. MN)',
    'DRY POWDER (USD MN)',
    'DRY POWDER (EUR MN)',
    'UNREALIZED VALUE (CURR. MN)',
    'UNREALIZED VALUE (USD MN)',
    'UNREALIZED VALUE (EUR MN)',
    'S&P 500 - DIRECT ALPHA',
    'RUSSELL 2000 - DIRECT ALPHA',
    'RUSSELL 3000 - DIRECT ALPHA',
    'MSCI EMERGING MARKETS - DIRECT ALPHA',
    'MSCI EUROPE STANDARD - DIRECT ALPHA',
    'MSCI US REIT - DIRECT ALPHA',
    'MSCI WORLD - DIRECT ALPHA'
     ]] = df_perf[[
         'FUND ID',
         'FIRM ID',
         'VINTAGE / INCEPTION YEAR',
         'CALLED (%)',
         'DPI (%)',
         'RVPI (%)',
         'NET IRR (%)',
         'NET MULTIPLE (X)',
         'QUARTILE',
         'FUND SIZE (USD MN)',
         'FUND NUMBER (OVERALL)',
         'FUND NUMBER (SERIES)',
         'LIFESPAN (YEARS)',
         'TARGET IRR - NET MIN',
         'TARGET IRR - NET MAX',
         'TARGET IRR - GROSS MIN',
         'TARGET IRR - GROSS MAX',
         'TARGET SIZE (CURR. MN)',
         'TARGET SIZE (USD MN)',
         'TARGET SIZE (EUR MN)',
         'INITIAL TARGET (CURR. MN)',
         'INITIAL TARGET (USD MN)',
         'INITIAL TARGET (EUR MN)',
         'HARD CAP (CURR. MN)',
         'HARD CAP (USD MN)',
         'HARD CAP (EUR MN)',
         'LATEST INTERIM CLOSE SIZE (CURR. MN)',
         'LATEST INTERIM CLOSE SIZE (USD MN)',
         'LATEST INTERIM CLOSE SIZE (EUR MN)',
         'FINAL CLOSE SIZE (CURR. MN)',
         'FINAL CLOSE SIZE (USD MN)',
         'FINAL CLOSE SIZE (EUR MN)',
         'CO-INVESTMENT CAPITAL AMOUNT (CURR. MN)',
         'CO-INVESTMENT CAPITAL AMOUNT (USD MN)',
         'CO-INVESTMENT CAPITAL AMOUNT (EUR MN)',
         'MONTHS TO FIRST CLOSE',
         'MONTHS IN MARKET',
         'PE: BUYOUT FUND LEVERAGE (%)',
         'PE: BUYOUT FUND SIZE',
         'PE: INVESTMENT SIZE PER PORTFOLIO COMPANY (MIN)',
         'PE: INVESTMENT SIZE PER PORTFOLIO COMPANY (MAX)',
         'RE: TARGET LEVERAGE (UPPER RANGE)',
         'RE: TARGET LEVERAGE (LOWER RANGE)',
         'RE: MAXIMUM LEVERAGE',
         'PD: LEVERAGE USED (X) MIN',
         'PD: LEVERAGE USED (X) MAX',
         'MGMT FEE RATE (%) DURING INV PERIOD',
         'INVESTMENT PERIOD (YRS)',
         'MGMT FEE RATE (%) - POST-INVESTMENT PERIOD',
         'CARRIED INTEREST (%)',
         'GP CATCH UP RATE (%)',
         'HURDLE RATE (%)',
         'SHARE OF TRANSACTION FEES REBATED TO LP (%)',
         'LP MAJORITY REQUIRED (%)',
         'FUND FORMATION COSTS (MN)',
         'GP COMMITMENTS TO FUND (% OF TOTAL)',
         'NUMBER OF LPS (MIN)',
         'NUMBER OF LPS (MAX)',
         'PERCENTAGE OF RETURNING LPS',
         'MEDIAN BENCHMARK NET IRR (%)',
         'MEDIAN BENCHMARK CALLED (%)',
         'MEDIAN BENCHMARK DISTRIBUTED (%) DPI',
         'MEDIAN BENCHMARK NET MULTIPLE (X)',
         'MEDIAN BENCHMARK RVPI (%)',
         'AVERAGE BENCHMARK NET IRR (%)',
         'AVERAGE BENCHMARK CALLED (%)',
         'AVERAGE BENCHMARK DISTRIBUTED (%) DPI',
         'AVERAGE BENCHMARK NET MULTIPLE (X)',
         'AVERAGE BENCHMARK RVPI (%)',
         'WEIGHTED BENCHMARK NET IRR (%)',
         'WEIGHTED BENCHMARK CALLED (%)',
         'WEIGHTED BENCHMARK DISTRIBUTED (%) DPI',
         'WEIGHTED BENCHMARK NET MULTIPLE (X)',
         'WEIGHTED BENCHMARK RVPI (%)',
         'POOLED BENCHMARK NET IRR (%)',
         'S&P 500 LN-PME',
         'S&P 500 KS-PME',
         'S&P 500 PME+',
         'RUSSELL 2000 LN-PME',
         'RUSSELL 2000 KS-PME',
         'RUSSELL 2000 PME+',
         'RUSSELL 3000 LN-PME',
         'RUSSELL 3000 KS-PME',
         'RUSSELL 3000 PME+',
         'MSCI EMERGING MARKETS LN-PME',
         'MSCI EMERGING MARKETS KS-PME',
         'MSCI EMERGING MARKETS PME+',
         'MSCI EUROPE STANDARD LN-PME',
         'MSCI EUROPE STANDARD KS-PME',
         'MSCI EUROPE STANDARD PME+',
         'MSCI US REIT LN-PME',
         'MSCI US REIT KS-PME',
         'MSCI US REIT PME+',
         'MSCI WORLD LN-PME',
         'MSCI WORLD KS-PME',
         'MSCI WORLD PME+',
         'ESTIMATED LAUNCH',
         'AUM (CURR. MN)',
         'AUM (USD MN)',
         'AUM (EUR MN)',
         'DRY POWDER (CURR. MN)',
         'DRY POWDER (USD MN)',
         'DRY POWDER (EUR MN)',
         'UNREALIZED VALUE (CURR. MN)',
         'UNREALIZED VALUE (USD MN)',
         'UNREALIZED VALUE (EUR MN)',
         'S&P 500 - DIRECT ALPHA',
         'RUSSELL 2000 - DIRECT ALPHA',
         'RUSSELL 3000 - DIRECT ALPHA',
         'MSCI EMERGING MARKETS - DIRECT ALPHA',
         'MSCI EUROPE STANDARD - DIRECT ALPHA',
         'MSCI US REIT - DIRECT ALPHA',
         'MSCI WORLD - DIRECT ALPHA'
         ]].apply(pd.to_numeric, errors = 'coerce')

# Convert dates to datetime format
df_perf[[
    'DATE REPORTED',
    'FUND RAISING LAUNCH DATE',
    'LATEST INTERIM CLOSE DATE',
    'FINAL CLOSE DATE'
    ]] = df_perf[[
        'DATE REPORTED',
        'FUND RAISING LAUNCH DATE',
        'LATEST INTERIM CLOSE DATE',
        'FINAL CLOSE DATE'
        ]].apply(pd.to_datetime, errors = 'coerce')

# Convert categories to categorical format
df_perf[[
    'STRATEGY',
    'ASSET CLASS',
    'PRIMARY REGION FOCUS',
    'STATUS',
    'FUND STRUCTURE',
    'DOMICILE',
    'FUND LEGAL STRUCTURE',
    'SINGLE DEAL FUND',
    'SOLELY FINANCED BY',
    'FUND CURRENCY',
    'OFFER CO-INVESTMENT OPPORTUNITIES TO LPS?',
    'RE: PRIMARY STRATEGY',
    'RE: MAIN PROPERTY TYPE',
    'INF: PRIMARY STRATEGY',
    'INF: PRIMARY SECTOR',
    'PD: PRIMARY DIRECT LENDING STRATEGY',
    'CHARGE FREQUENCY',
    'SPECIAL PROVISION FOR LARGER LPS',
    'CARRIED INTEREST BASIS',
    'KEY MAN CLAUSE',
    'NO-FAULT DIVORCE CLAUSE?',
    'ADVISORY BOARD LP REPRESENTATION',
    'REGION',
    'CITY',
    'STATE/COUNTY',
    'COUNTRY',
    ]] = df_perf[[
        'STRATEGY',
        'ASSET CLASS',
        'PRIMARY REGION FOCUS',
        'STATUS',
        'FUND STRUCTURE',
        'DOMICILE',
        'FUND LEGAL STRUCTURE',
        'SINGLE DEAL FUND',
        'SOLELY FINANCED BY',
        'FUND CURRENCY',
        'OFFER CO-INVESTMENT OPPORTUNITIES TO LPS?',
        'RE: PRIMARY STRATEGY',
        'RE: MAIN PROPERTY TYPE',
        'INF: PRIMARY STRATEGY',
        'INF: PRIMARY SECTOR',
        'PD: PRIMARY DIRECT LENDING STRATEGY',
        'CHARGE FREQUENCY',
        'SPECIAL PROVISION FOR LARGER LPS',
        'CARRIED INTEREST BASIS',
        'KEY MAN CLAUSE',
        'NO-FAULT DIVORCE CLAUSE?',
        'ADVISORY BOARD LP REPRESENTATION',
        'REGION',
        'CITY',
        'STATE/COUNTY',
        'COUNTRY',
        ]].astype('category')

df_perf.sort_values(by = ['FUND ID', 'DATE REPORTED'],
                    inplace = True,
                    ignore_index = True)

# Calculate difference between reporting time and start of vintage year
df_perf['INITIAL VINTAGE DATE'] = pd.to_datetime(
    # Converts vintage year to conform with months (i.e. 2010 -> 2009-12-31)
    (df_perf['VINTAGE / INCEPTION YEAR'] - 1).astype(str) + '-12-31',
    errors = 'coerce')
df_perf['MONTHS SINCE VINTAGE'] = (
    (df_perf['DATE REPORTED'].dt.year - df_perf['INITIAL VINTAGE DATE'].dt.year) * 12
    + (df_perf['DATE REPORTED'].dt.month - df_perf['INITIAL VINTAGE DATE'].dt.month)
    )
df_perf['QUARTERS SINCE VINTAGE'] = df_perf['MONTHS SINCE VINTAGE'] / 3

# Add alternate benchmarks
df_perf.loc[df_perf['ASSET CLASS'] == 'Private Equity',
            'ALT BENCHMARK NAME'] = 'Private Equity - All'
df_perf.loc[df_perf['ASSET CLASS'] == 'Venture Capital',
            'ALT BENCHMARK NAME'] = 'Venture - All'
df_perf.loc[df_perf['ASSET CLASS'] == 'Real Estate',
            'ALT BENCHMARK NAME'] = 'Real Estate - All'
df_perf.loc[df_perf['ASSET CLASS'] == 'Private Debt',
            'ALT BENCHMARK NAME'] = 'Private Debt - All'
df_perf.loc[df_perf['ASSET CLASS'] == 'Infrastructure',
            'ALT BENCHMARK NAME'] = 'Infrastructure - All'
df_perf.loc[df_perf['ASSET CLASS'] == 'Natural Resources',
            'ALT BENCHMARK NAME'] = 'Natural Resources - All'
df_perf.loc[df_perf['ASSET CLASS'] == 'Multi',
            'ALT BENCHMARK NAME'] = 'Private Capital - All'
df_perf.loc[df_perf['ASSET CLASS'] == np.nan,
            'ALT BENCHMARK NAME'] = 'Private Capital - All'

# Replace column names with more friendly naming structure
df_perf.columns = df_perf.columns.str.lower()
df_perf.columns = df_perf.columns.str.replace(' - ', '_')
df_perf.columns = df_perf.columns.str.replace(' / ', '_')
df_perf.columns = df_perf.columns.str.replace(' ', '_')
df_perf.columns = df_perf.columns.str.replace(':', '')
df_perf.columns = df_perf.columns.str.replace('.', '')
df_perf.columns = df_perf.columns.str.replace('(%)', 'pct', regex = False)
df_perf.columns = df_perf.columns.str.replace('(x)', 'x', regex = False)
df_perf.columns = df_perf.columns.str.replace(')', '', regex = False)
df_perf.columns = df_perf.columns.str.replace('(', '', regex = False)

# Save core data as efficient gzip
df_perf.to_parquet(
    filePath + '20210110_preqin_performance_2000_2020Q3.gzip',
    compression = 'gzip'
    )

# =============================================================================
# Compiling Fund Dataset
# =============================================================================
# Import modules
import numpy as np
import pandas as pd
# Initialize filepaths
filePath = 'OneDrive - McKinsey & Company/Documents/scripts/preqin/'

# Load raw master file
df_fund = pd.read_excel(filePath + '20210128_preqin_funds.xlsx')

# Convert all columns to string (Replace once astype(skipna) fixed)
df_fund = df_fund.where(df_fund.isna(), df_fund.astype(str))

# Convert numeric variables to int/float
df_fund[['FUND ID',
         'FIRM ID',
         'VINTAGE / INCEPTION YEAR',
         'FUND SIZE (USD MN)',
         'FUND NUMBER (OVERALL)',
         'FUND NUMBER (SERIES)',
         'LIFESPAN (YEARS)',
         'TARGET IRR - NET MIN',
         'TARGET IRR - NET MAX',
         'TARGET IRR - GROSS MIN',
         'TARGET IRR - GROSS MAX',
         'TARGET SIZE (CURR. MN)',
         'TARGET SIZE (USD MN)',
         'TARGET SIZE (EUR MN)',
         'INITIAL TARGET (CURR. MN)',
         'INITIAL TARGET (USD MN)',
         'INITIAL TARGET (EUR MN)',
         'HARD CAP (CURR. MN)',
         'HARD CAP (USD MN)',
         'HARD CAP (EUR MN)',
         'LATEST INTERIM CLOSE SIZE (CURR. MN)',
         'LATEST INTERIM CLOSE SIZE (USD MN)',
         'LATEST INTERIM CLOSE SIZE (EUR MN)',
         'FINAL CLOSE SIZE (CURR. MN)',
         'FINAL CLOSE SIZE (USD MN)',
         'FINAL CLOSE SIZE (EUR MN)',
         'CO-INVESTMENT CAPITAL AMOUNT (CURR. MN)',
         'CO-INVESTMENT CAPITAL AMOUNT (USD MN)',
         'CO-INVESTMENT CAPITAL AMOUNT (EUR MN)',
         'MONTHS TO FIRST CLOSE',
         'MONTHS IN MARKET',
         'PE: BUYOUT FUND LEVERAGE (%)',
         'PE: BUYOUT FUND SIZE',
         'PE: INVESTMENT SIZE PER PORTFOLIO COMPANY (MIN)',
         'PE: INVESTMENT SIZE PER PORTFOLIO COMPANY (MAX)',
         'RE: TARGET LEVERAGE (UPPER RANGE)',
         'RE: TARGET LEVERAGE (LOWER RANGE)',
         'RE: MAXIMUM LEVERAGE',
         'PD: LEVERAGE USED (X) MIN',
         'PD: LEVERAGE USED (X) MAX',
         'MGMT FEE RATE (%) DURING INV PERIOD',
         'INVESTMENT PERIOD (YRS)',
         'MGMT FEE RATE (%) - POST-INVESTMENT PERIOD',
         'CARRIED INTEREST (%)',
         'GP CATCH UP RATE (%)',
         'HURDLE RATE (%)',
         'SHARE OF TRANSACTION FEES REBATED TO LP (%)',
         'LP MAJORITY REQUIRED (%)',
         'FUND FORMATION COSTS (MN)',
         'GP COMMITMENTS TO FUND (% OF TOTAL)',
         'NUMBER OF LPS (MIN)',
         'NUMBER OF LPS (MAX)',
         'PERCENTAGE OF RETURNING LPS',
         'ESTIMATED LAUNCH'
     ]] = df_fund[['FUND ID',
                   'FIRM ID',
                   'VINTAGE / INCEPTION YEAR',
                   'FUND SIZE (USD MN)',
                   'FUND NUMBER (OVERALL)',
                   'FUND NUMBER (SERIES)',
                   'LIFESPAN (YEARS)',
                   'TARGET IRR - NET MIN',
                   'TARGET IRR - NET MAX',
                   'TARGET IRR - GROSS MIN',
                   'TARGET IRR - GROSS MAX',
                   'TARGET SIZE (CURR. MN)',
                   'TARGET SIZE (USD MN)',
                   'TARGET SIZE (EUR MN)',
                   'INITIAL TARGET (CURR. MN)',
                   'INITIAL TARGET (USD MN)',
                   'INITIAL TARGET (EUR MN)',
                   'HARD CAP (CURR. MN)',
                   'HARD CAP (USD MN)',
                   'HARD CAP (EUR MN)',
                   'LATEST INTERIM CLOSE SIZE (CURR. MN)',
                   'LATEST INTERIM CLOSE SIZE (USD MN)',
                   'LATEST INTERIM CLOSE SIZE (EUR MN)',
                   'FINAL CLOSE SIZE (CURR. MN)',
                   'FINAL CLOSE SIZE (USD MN)',
                   'FINAL CLOSE SIZE (EUR MN)',
                   'CO-INVESTMENT CAPITAL AMOUNT (CURR. MN)',
                   'CO-INVESTMENT CAPITAL AMOUNT (USD MN)',
                   'CO-INVESTMENT CAPITAL AMOUNT (EUR MN)',
                   'MONTHS TO FIRST CLOSE',
                   'MONTHS IN MARKET',
                   'PE: BUYOUT FUND LEVERAGE (%)',
                   'PE: BUYOUT FUND SIZE',
                   'PE: INVESTMENT SIZE PER PORTFOLIO COMPANY (MIN)',
                   'PE: INVESTMENT SIZE PER PORTFOLIO COMPANY (MAX)',
                   'RE: TARGET LEVERAGE (UPPER RANGE)',
                   'RE: TARGET LEVERAGE (LOWER RANGE)',
                   'RE: MAXIMUM LEVERAGE',
                   'PD: LEVERAGE USED (X) MIN',
                   'PD: LEVERAGE USED (X) MAX',
                   'MGMT FEE RATE (%) DURING INV PERIOD',
                   'INVESTMENT PERIOD (YRS)',
                   'MGMT FEE RATE (%) - POST-INVESTMENT PERIOD',
                   'CARRIED INTEREST (%)',
                   'GP CATCH UP RATE (%)',
                   'HURDLE RATE (%)',
                   'SHARE OF TRANSACTION FEES REBATED TO LP (%)',
                   'LP MAJORITY REQUIRED (%)',
                   'FUND FORMATION COSTS (MN)',
                   'GP COMMITMENTS TO FUND (% OF TOTAL)',
                   'NUMBER OF LPS (MIN)',
                   'NUMBER OF LPS (MAX)',
                   'PERCENTAGE OF RETURNING LPS',
                   'ESTIMATED LAUNCH'
         ]].apply(pd.to_numeric, errors = 'coerce')

# Convert dates to datetime format
df_fund[['DATE ADDED',
         'FUND RAISING LAUNCH DATE',
         'LATEST CLOSE DATE',
         'LATEST INTERIM CLOSE DATE',
         'FINAL CLOSE DATE'
         ]] = df_fund[['DATE ADDED',
                       'FUND RAISING LAUNCH DATE',
                       'LATEST INTERIM CLOSE DATE',
                       'LATEST CLOSE DATE',
                       'FINAL CLOSE DATE'
                       ]].apply(pd.to_datetime, errors = 'coerce')

# Convert categories to categorical format
df_fund[['STRATEGY',
         'ASSET CLASS',
         'PRIMARY REGION FOCUS',
         'STATUS',
         'FUND STRUCTURE',
         'DOMICILE',
         'FUND LEGAL STRUCTURE',
         'SINGLE DEAL FUND',
         'SOLELY FINANCED BY',
         'FUND CURRENCY',
         'OFFER CO-INVESTMENT OPPORTUNITIES TO LPS?',
         'RE: PRIMARY STRATEGY',
         'RE: MAIN PROPERTY TYPE',
         'INF: PRIMARY STRATEGY',
         'INF: PRIMARY SECTOR',
         'PD: PRIMARY DIRECT LENDING STRATEGY',
         'CHARGE FREQUENCY',
         'SPECIAL PROVISION FOR LARGER LPS',
         'CARRIED INTEREST BASIS',
         'KEY MAN CLAUSE',
         'NO-FAULT DIVORCE CLAUSE?',
         'ADVISORY BOARD LP REPRESENTATION',
         'REGION',
         'CITY',
         'STATE',
         'COUNTRY',
         ]] = df_fund[['STRATEGY',
                       'ASSET CLASS',
                       'PRIMARY REGION FOCUS',
                       'STATUS',
                       'FUND STRUCTURE',
                       'DOMICILE',
                       'FUND LEGAL STRUCTURE',
                       'SINGLE DEAL FUND',
                       'SOLELY FINANCED BY',
                       'FUND CURRENCY',
                       'OFFER CO-INVESTMENT OPPORTUNITIES TO LPS?',
                       'RE: PRIMARY STRATEGY',
                       'RE: MAIN PROPERTY TYPE',
                       'INF: PRIMARY STRATEGY',
                       'INF: PRIMARY SECTOR',
                       'PD: PRIMARY DIRECT LENDING STRATEGY',
                       'CHARGE FREQUENCY',
                       'SPECIAL PROVISION FOR LARGER LPS',
                       'CARRIED INTEREST BASIS',
                       'KEY MAN CLAUSE',
                       'NO-FAULT DIVORCE CLAUSE?',
                       'ADVISORY BOARD LP REPRESENTATION',
                       'REGION',
                       'CITY',
                       'STATE',
                       'COUNTRY',
                       ]].astype('category')

df_fund.sort_values(by = ['FUND ID'],
                    inplace = True,
                    ignore_index = True)

# Replace column names with more friendly naming structure
df_fund.columns = df_fund.columns.str.lower()
df_fund.columns = df_fund.columns.str.replace(' - ', '_')
df_fund.columns = df_fund.columns.str.replace(' / ', '_')
df_fund.columns = df_fund.columns.str.replace(' ', '_')
df_fund.columns = df_fund.columns.str.replace(':', '')
df_fund.columns = df_fund.columns.str.replace('.', '')
df_fund.columns = df_fund.columns.str.replace('(%)', 'pct', regex = False)
df_fund.columns = df_fund.columns.str.replace('(x)', 'x', regex = False)
df_fund.columns = df_fund.columns.str.replace(')', '', regex = False)
df_fund.columns = df_fund.columns.str.replace('(', '', regex = False)

# Save core data as efficient gzip
df_fund.to_parquet(
    filePath + '20210128_preqin_funds.gzip',
    compression = 'gzip'
    )

# =============================================================================
# Compiling Benchmark Dataset
# =============================================================================
# Import modules
import numpy as np
import pandas as pd

# Initialize filepaths
filePath = 'OneDrive - McKinsey & Company/Documents/scripts/preqin/'

# Load raw master file
df_bmrk = pd.read_excel(filePath + '20210128_preqin_benchmarks_2000_2020Q3.xlsx')

# Convert all columns to string (Replace once astype(skipna) fixed)
df_bmrk = df_bmrk.where(df_bmrk.isna(), df_bmrk.astype(str))

# Convert numeric variables to int/float
df_bmrk[['BENCHMARK VINTAGE',
         'CONSTITUENT NO. OF FUNDS',
         'CONSTITUENT SIZE (USD BN)',
         'CALLED (%) MAX',
         'CALLED (%) TOP QUARTILE BOUNDARY (Q1)',
         'CALLED (%) MEDIAN',
         'CALLED (%) BOTTOM QUARTILE BOUNDARY (Q3)',
         'CALLED (%) MIN',
         'CALLED (%) MEAN',
         'CALLED (%) WEIGHTED',
         'CALLED (%) STANDARD DEVIATION',
         'DPI (%) MAX',
         'DPI (%) TOP QUARTILE BOUNDARY (Q1)',
         'DPI (%) MEDIAN',
         'DPI (%) BOTTOM QUARTILE BOUNDARY (Q3)',
         'DPI (%) MIN',
         'DPI (%) MEAN',
         'DPI (%) WEIGHTED',
         'DPI (%) STANDARD DEVIATION',
         'RVPI (%) MAX',
         'RVPI (%) TOP QUARTILE BOUNDARY (Q1)',
         'RVPI (%) MEDIAN',
         'RVPI (%) BOTTOM QUARTILE BOUNDARY (Q3)',
         'RVPI (%) MIN',
         'RVPI (%) MEAN',
         'RVPI (%) WEIGHTED',
         'RVPI (%) STANDARD DEVIATION',
         'NET MULTIPLE (X) MAX',
         'NET MULTIPLE (X) TOP QUARTILE BOUNDARY (Q1)',
         'NET MULTIPLE (X) MEDIAN',
         'NET MULTIPLE (X) BOTTOM QUARTILE BOUNDARY (Q3)',
         'NET MULTIPLE (X) MIN',
         'NET MULTIPLE (X) MEAN',
         'NET MULTIPLE (X) WEIGHTED',
         'NET MULTIPLE (X) STANDARD DEVIATION',
         'NET IRR (%) MAX',
         'NET IRR (%) TOP QUARTILE BOUNDARY (Q1)',
         'NET IRR (%) MEDIAN',
         'NET IRR (%) BOTTOM QUARTILE BOUNDARY (Q3)',
         'NET IRR (%) MIN',
         'NET IRR (%) MEAN',
         'NET IRR (%) WEIGHTED',
         'NET IRR (%) STANDARD DEVIATION',
         'POOLED IRR NO. FUNDS',
         'POOLED IRR POOLED IRR',
         'S&P 500 - DIRECT ALPHA (%)',
         'S&P 500 LN-PME (%)',
         'S&P 500 KS-PME',
         'S&P 500 PME+ (%)',
         'RUSSELL 2000 - DIRECT ALPHA (%)',
         'RUSSELL 2000 LN-PME (%)',
         'RUSSELL 2000 KS-PME',
         'RUSSELL 2000 PME+ (%)',
         'RUSSELL 3000 - DIRECT ALPHA (%)',
         'RUSSELL 3000 LN-PME (%)',
         'RUSSELL 3000 KS-PME',
         'RUSSELL 3000 PME+ (%)',
         'MSCI EMERGING MARKETS - DIRECT ALPHA (%)',
         'MSCI EMERGING MARKETS LN-PME (%)',
         'MSCI EMERGING MARKETS KS-PME',
         'MSCI EMERGING MARKETS PME+ (%)',
         'MSCI EUROPE STANDARD - DIRECT ALPHA (%)',
         'MSCI EUROPE STANDARD LN-PME (%)',
         'MSCI EUROPE STANDARD KS-PME',
         'MSCI EUROPE STANDARD PME+ (%)',
         'MSCI US REIT - DIRECT ALPHA (%)',
         'MSCI US REIT LN-PME (%)',
         'MSCI US REIT KS-PME',
         'MSCI US REIT PME+ (%)',
         'MSCI WORLD - DIRECT ALPHA (%)',
         'MSCI WORLD LN-PME (%)',
         'MSCI WORLD KS-PME',
         'MSCI WORLD PME+ (%)'
     ]] = df_bmrk[['BENCHMARK VINTAGE',
                   'CONSTITUENT NO. OF FUNDS',
                   'CONSTITUENT SIZE (USD BN)',
                   'CALLED (%) MAX',
                   'CALLED (%) TOP QUARTILE BOUNDARY (Q1)',
                   'CALLED (%) MEDIAN',
                   'CALLED (%) BOTTOM QUARTILE BOUNDARY (Q3)',
                   'CALLED (%) MIN',
                   'CALLED (%) MEAN',
                   'CALLED (%) WEIGHTED',
                   'CALLED (%) STANDARD DEVIATION',
                   'DPI (%) MAX',
                   'DPI (%) TOP QUARTILE BOUNDARY (Q1)',
                   'DPI (%) MEDIAN',
                   'DPI (%) BOTTOM QUARTILE BOUNDARY (Q3)',
                   'DPI (%) MIN',
                   'DPI (%) MEAN',
                   'DPI (%) WEIGHTED',
                   'DPI (%) STANDARD DEVIATION',
                   'RVPI (%) MAX',
                   'RVPI (%) TOP QUARTILE BOUNDARY (Q1)',
                   'RVPI (%) MEDIAN',
                   'RVPI (%) BOTTOM QUARTILE BOUNDARY (Q3)',
                   'RVPI (%) MIN',
                   'RVPI (%) MEAN',
                   'RVPI (%) WEIGHTED',
                   'RVPI (%) STANDARD DEVIATION',
                   'NET MULTIPLE (X) MAX',
                   'NET MULTIPLE (X) TOP QUARTILE BOUNDARY (Q1)',
                   'NET MULTIPLE (X) MEDIAN',
                   'NET MULTIPLE (X) BOTTOM QUARTILE BOUNDARY (Q3)',
                   'NET MULTIPLE (X) MIN',
                   'NET MULTIPLE (X) MEAN',
                   'NET MULTIPLE (X) WEIGHTED',
                   'NET MULTIPLE (X) STANDARD DEVIATION',
                   'NET IRR (%) MAX',
                   'NET IRR (%) TOP QUARTILE BOUNDARY (Q1)',
                   'NET IRR (%) MEDIAN',
                   'NET IRR (%) BOTTOM QUARTILE BOUNDARY (Q3)',
                   'NET IRR (%) MIN',
                   'NET IRR (%) MEAN',
                   'NET IRR (%) WEIGHTED',
                   'NET IRR (%) STANDARD DEVIATION',
                   'POOLED IRR NO. FUNDS',
                   'POOLED IRR POOLED IRR',
                   'S&P 500 - DIRECT ALPHA (%)',
                   'S&P 500 LN-PME (%)',
                   'S&P 500 KS-PME',
                   'S&P 500 PME+ (%)',
                   'RUSSELL 2000 - DIRECT ALPHA (%)',
                   'RUSSELL 2000 LN-PME (%)',
                   'RUSSELL 2000 KS-PME',
                   'RUSSELL 2000 PME+ (%)',
                   'RUSSELL 3000 - DIRECT ALPHA (%)',
                   'RUSSELL 3000 LN-PME (%)',
                   'RUSSELL 3000 KS-PME',
                   'RUSSELL 3000 PME+ (%)',
                   'MSCI EMERGING MARKETS - DIRECT ALPHA (%)',
                   'MSCI EMERGING MARKETS LN-PME (%)',
                   'MSCI EMERGING MARKETS KS-PME',
                   'MSCI EMERGING MARKETS PME+ (%)',
                   'MSCI EUROPE STANDARD - DIRECT ALPHA (%)',
                   'MSCI EUROPE STANDARD LN-PME (%)',
                   'MSCI EUROPE STANDARD KS-PME',
                   'MSCI EUROPE STANDARD PME+ (%)',
                   'MSCI US REIT - DIRECT ALPHA (%)',
                   'MSCI US REIT LN-PME (%)',
                   'MSCI US REIT KS-PME',
                   'MSCI US REIT PME+ (%)',
                   'MSCI WORLD - DIRECT ALPHA (%)',
                   'MSCI WORLD LN-PME (%)',
                   'MSCI WORLD KS-PME',
                   'MSCI WORLD PME+ (%)'
                   ]].apply(pd.to_numeric, errors = 'coerce')

# Convert dates to datetime format
df_bmrk['CONSTITUENT AS AT'
        ] = df_bmrk['CONSTITUENT AS AT'
                    ].apply(pd.to_datetime)

df_bmrk.sort_values(by = ['BENCHMARK ID'],
                    inplace = True,
                    ignore_index = True)

# Calculate difference between reporting time and start of vintage year
df_bmrk['INITIAL VINTAGE DATE'] = pd.to_datetime(
    # Converts vintage year to conform with months (i.e. 2010 -> 2009-12-31)
    (df_bmrk['BENCHMARK VINTAGE'] - 1).astype(str) + '-12-31',
    errors = 'coerce')
df_bmrk['MONTHS SINCE VINTAGE'] = (
    (df_bmrk['CONSTITUENT AS AT'].dt.year
     - df_bmrk['INITIAL VINTAGE DATE'].dt.year) * 12
    + (df_bmrk['CONSTITUENT AS AT'].dt.month
       - df_bmrk['INITIAL VINTAGE DATE'].dt.month)
    )
df_bmrk['QUARTERS SINCE VINTAGE'] = df_bmrk['MONTHS SINCE VINTAGE'] / 3

# Replace column names with more friendly naming structure
df_bmrk.columns = df_bmrk.columns.str.lower()
df_bmrk.columns = df_bmrk.columns.str.replace(' - ', '_')
df_bmrk.columns = df_bmrk.columns.str.replace(' / ', '_')
df_bmrk.columns = df_bmrk.columns.str.replace(' ', '_')
df_bmrk.columns = df_bmrk.columns.str.replace(':', '')
df_bmrk.columns = df_bmrk.columns.str.replace('.', '')
df_bmrk.columns = df_bmrk.columns.str.replace('(%)', 'pct', regex = False)
df_bmrk.columns = df_bmrk.columns.str.replace('(x)', 'x', regex = False)
df_bmrk.columns = df_bmrk.columns.str.replace(')', '', regex = False)
df_bmrk.columns = df_bmrk.columns.str.replace('(', '', regex = False)

# Save core data as efficient gzip
df_bmrk.to_parquet(
    filePath + '20210110_preqin_benchmarks_2000_2020Q3.gzip',
    compression = 'gzip'
    )

# =============================================================================
# Create Master Dataset
# =============================================================================
# Import modules
import numpy as np
import pandas as pd

# Initialize filepaths
filePath = 'OneDrive - McKinsey & Company/Documents/scripts/preqin/'

# Load datasets
df_perf = pd.read_parquet(
    filePath + '20210110_preqin_performance_2000_2020Q3.gzip')
df_fund = pd.read_parquet(
    filePath + '20210128_preqin_funds.gzip')
df_bmrk = pd.read_parquet(
    filePath + '20210110_preqin_benchmarks_2000_2020Q3.gzip')


df_perf.loc[df_perf['benchmark_name'].str.contains('Buyout&North America'),
            'benchmark_name'] = 'Buyout - North America'
df_perf.loc[df_perf['benchmark_name'].str.contains('Buyout&Europe'),
            'benchmark_name'] = 'Buyout - Europe'
df_perf.loc[df_perf['benchmark_name'].str.contains('Buyout&Asia-Pacific'),
            'benchmark_name'] = 'Buyout - Asia-Pacific'
df_perf.loc[df_perf['benchmark_name'].str.contains('Buyout&Asia'),
            'benchmark_name'] = 'Buyout - Asia'
df_perf.loc[df_perf['benchmark_name'].str.contains('Buyout&All'),
            'benchmark_name'] = 'Buyout - All'

# Create benchmark for merge
df_bmrk_merge = df_perf[['vintage_inception_year',
                         'asset_class',
                         'strategy',
                         'primary_region_focus',
                         'benchmark_name']].drop_duplicates().copy()

df_bmrk_use = df_bmrk.loc[~(df_bmrk['benchmark_name'].contains()

# =============================================================================
# Create SQL Database
# =============================================================================
# # Import modules
# from sqlalchemy import create_engine

# # Initialize filepaths
# dbfilePath = 'OneDrive - McKinsey & Company/Documents/sqlite/db/'

# engine = create_engine('sqlite:///' + dbfilePath + 'preqin_database.db')
# df_perf.to_sql('performance', con = engine)
# df_fund.to_sql('funds', con = engine)

# with engine.connect() as con:
#     rs = con.execute('SELECT firm_id, fund_id, asset_class, final_close_size_usd_mn FROM funds')
#     test = pd.DataFrame(rs.fetchall())
#     test.columns = rs.keys()

# =============================================================================
# Create dashboard
# =============================================================================
# For loading data if you want to skip all the previous inputs
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import linear_model, tree, neighbors
from sklearn.preprocessing import PolynomialFeatures
import plotly.express as px
import plotly.graph_objects as go
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

def format_coefs(coefs):
    coef_string = "yhat = "

    for order, coef in enumerate(coefs):
        if coef >= 0:
            sign = ' + '
        else:
            sign = ' - '
        if order == 0:
            coef_string += f'{coef}'
        elif order == 1:
            coef_string += sign + f'{abs(coef):.3f}*x'
        else:
            coef_string += sign + f'{abs(coef):.3f}*x^{order}'

    return coef_string

# Set filepath
filepath = 'preqin/'

# Load dataset
df_perf = pd.read_parquet(
    filepath + '20210110_preqin_performance_2000_2020Q3.gzip')
df_fund = pd.read_parquet(
    filepath + '20210128_preqin_funds.gzip')
df_bmrk = pd.read_parquet(
    filepath + '20210110_preqin_benchmarks_2000_2020Q3.gzip')

df = df_perf[[
    'fund_id',
    'vintage_inception_year',
    'asset_class',
    'strategy',
    'quarters_since_vintage',
    'called_pct',
    'rvpi_pct',
    'dpi_pct',
    'net_multiple_x'
]].copy().dropna()

# Create array of available variables
available_indicators = np.array([
    'quarters_since_vintage',
    'called_pct',
    'rvpi_pct',
    'dpi_pct',
    'net_multiple_x'],
    dtype = object
)

# Create array of available models
models = {
    'Regression': linear_model.LinearRegression,
    'Lasso': linear_model.Lasso,
    'Decision Tree': tree.DecisionTreeRegressor,
    'k-NN': neighbors.KNeighborsRegressor
}

df_fig = df.copy()
# df_fig = df.loc[(df['vintage_inception_year'] >= 2000) & (df['vintage_inception_year'] <= 2010)]

# df_fig['asset_class'] = df_fig['asset_class'].astype(str).str.replace('nan', 'Unknown')
# df_fig['strategy'] = df_fig['strategy'].astype(str).str.replace('nan', 'Unknown')

available_asset_classes = df_fig['asset_class'].unique()
available_vintages = df_fig['vintage_inception_year'].sort_values().unique()

# Create graph object
app = dash.Dash(__name__)

# Set parameters for graph
app.layout = html.Div([
    html.Div([
        html.Div([
            # Creates dropdown to select x variable
            dcc.Dropdown(
                id='xaxis-column',
                options=[{'label': i, 'value': i} for i in available_indicators],
                value='quarters_since_vintage',
                searchable = False
            ),
            # Creates dropdown to select y variable
            dcc.Dropdown(
                id='yaxis-column',
                options=[{'label': i, 'value': i} for i in available_indicators],
                value='called_pct',
                searchable = False
            ),
            # Select asset class
            dcc.Dropdown(
                id='sector-name',
                options=[{'label': i, 'value': i} for i in available_asset_classes],
                value='Private Equity',
                searchable = False
            ),
            # Select vintage year
            dcc.Dropdown(
                id='vintage-year',
                options=[{'label': i, 'value': i} for i in available_vintages],
                value=2015,
                searchable = False
            ),
            # Select model type
            dcc.Dropdown(
                id='model-name',
                options=[{'label': x, 'value': x} 
                         for x in models],
                value='Regression',
                searchable=False
            ),
            # Select polynomial degree
            dcc.Slider(
                id='polynomial-degree-slider',
                min=1,
                max=10,
                step=1,
                value=1,
                marks = {i: str(i) for i in range(1,11)}
            ),
            # Set alpha for lasso regression
            dcc.Slider(
                id='alpha-slider',
                min=-4,
                max=3,
                value=0,
                marks = {i: '{}'.format(10**i) for i in range(-4,4)}
            )
        ])
    ]),
    # Create graph object
    dcc.Graph(id='graph')
])

# Set inputs and outputs
@app.callback(
    Output('graph', 'figure'),
    Input('xaxis-column', 'value'),
    Input('yaxis-column', 'value'),
    Input('sector-name', 'value'),
    Input('vintage-year', 'value'),
    Input('model-name', 'value'),
    Input('polynomial-degree-slider', 'value'),
    Input('alpha-slider', 'value')
)

# Generate dash plot
def update_graph(xaxis_column_name,
                 yaxis_column_name,
                 sector,
                 vintage,
                 name,
                 degree,
                 alpha
                 ):
    # Load x and y datasets
    x = df_fig.loc[(df_fig['asset_class'] == sector)
                   & (df_fig['vintage_inception_year'] == vintage),
                   xaxis_column_name].to_numpy().reshape(-1,1)
    y = df_fig.loc[(df_fig['asset_class'] == sector)
                   & (df_fig['vintage_inception_year'] == vintage),
                   yaxis_column_name]
    # Show empty plot if dataset empty or too small
    if len(x) < 2 or len(y) < 2:
        fig = go.Figure()
    else:
        # Generate training dataset
        x_train, x_test, y_train, y_test = train_test_split(
            x,
            y,
            random_state = 30
        )
        # Set range for predicting y
        x_range = np.linspace(x.min(), x.max(), 300)
        
        # Generate poly dataset (only relevant if poly > 1)
        poly = PolynomialFeatures(degree = degree)
        x_train_poly = poly.fit_transform(x_train)
        x_test_poly = poly.fit_transform(x_test)
        x_range_poly = poly.fit_transform(x_range.reshape(-1,1))
        
        # Sets parameters for linear regressions
        if name == 'Regression':
            model = models[name](normalize = True)
        elif name == 'Lasso':
            model = models[name](alpha = 10**alpha, normalize = True)
        else:
            model = models[name]()
        
        # Fit model
        model.fit(x_train_poly, y_train)
        
        # Predict y using model
        y_range = model.predict(x_range_poly)
        
        # Generate scatter of training and testing data
        trace0 = go.Scatter(x=x_train.squeeze(), y=y_train, 
                       name='train', mode='markers')
        trace1 = go.Scatter(x=x_test.squeeze(), y=y_test, 
                       name='test', mode='markers')
        
        # Add coefficients on hover if linear regression is used
        if name == 'Regression' or name == 'Lasso':
            trace2 = go.Scatter(x=x_range, y=y_range, 
                                name='prediction', mode = 'lines',
                                hovertext = format_coefs(model.coef_))
        else:
            trace2 = go.Scatter(x=x_range, y=y_range, 
                                name='prediction', mode = 'lines')
        # Combine traces
        data = [trace0, trace1, trace2]
        
        # Add score in title
        layout = go.Layout(title = f'Score: {model.score(x_test_poly, y_test):.5f}',
                           hovermode = 'closest')

    return go.Figure(data = data, layout = layout)

# Run debug server
if __name__ == '__main__':
    app.run_server(debug = True, use_reloader = False)













import pandas

# Hardcode paths to csv input files
hardcodedPlansCSV = './plans.csv'
hardcodedSlcspCSV = './slcsp.csv'
hardcodedZipsCSV = './zips.csv'

# Define helper function to get and format the second-lowest item in a list of dollar amount rates
def getSecondLowest(inputList):
    uniqueOrderedList = list(set(inputList))
    uniqueOrderedList.sort()
    if len(uniqueOrderedList) > 1:
        return str('{:.2f}'.format(round(uniqueOrderedList[1],2)))
    else:
        return ''

# Define main function to calculate second lowest cost silver plan per zip code
def main(plansCSV,slcspCSV,zipsCSV):
    # 1. Read csv files into pandas dataframes
    plans = pandas.read_csv(plansCSV)
    slcsp = pandas.read_csv(slcspCSV,dtype={'zipcode': 'str'})
    zips = pandas.read_csv(zipsCSV,dtype={'zipcode': 'str'})

    # 2. Create dataframe of zips with their state+rate_area, where unambiguous
    
    # a. Consolidate unique combinations of zip+state+rate_area (just take the first occurrence)
    zipsByRateArea = zips[['zipcode','state','rate_area']].drop_duplicates(['zipcode','state','rate_area'],keep='first')

    # b. Remove *all* occurrences of duplicate zip codes (these duplicates are ambiguous by rate area, so their slcsp can't be calculated)
    unambiguousZips = zipsByRateArea.drop_duplicates(['zipcode'],keep=False)

    # 3. Gather silver plan rates by state+rate_area and use helper function to create a new dataframe with second-lowest-cost-per-area rates, where they exist
    slcspRates = plans[plans['metal_level'] == 'Silver'].groupby(['state','rate_area'])['rate'].apply(list).apply(getSecondLowest).reset_index()

    # 4. Merge slcsp, unambiguousZips, and slcspRates dataframes to find rate per zip code
    outputData = slcsp.drop('rate', axis='columns').merge(unambiguousZips,how='left',on='zipcode').merge(slcspRates,how='left',on=['state','rate_area']).fillna('')

    # 5. Return zipcode & rate colums from outputData dataframe
    print(outputData[['zipcode','rate']].to_csv(index=False))

if __name__ == '__main__':
    main(hardcodedPlansCSV,hardcodedSlcspCSV,hardcodedZipsCSV)

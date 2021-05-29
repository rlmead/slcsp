import pandas

# Read the necessary data from csv files into dataframes
plans = pandas.read_csv('./plans.csv')
slcsp = pandas.read_csv('./slcsp.csv')
zips = pandas.read_csv('./zips.csv')

def getSecondItem(list):
    if len(list) > 1:
        return list[1]
    else:
        return ''

# Define function to calculate second lowest cost silver plan
def main():
    # 1. Get list of zips with their state+rate_area, where unambiguous
    
    # a. consolidate unique combinations of zip+state+rate_area into just the first occurrence of each combination
    zipsByRateArea = zips[['zipcode','state','rate_area']].drop_duplicates(['zipcode','state','rate_area'],keep='first')

    # b. remove *all* occurrences of duplicate zip codes (now, duplicates indicate ambiguity by rate area)
    unambiguousZips = zipsByRateArea.drop_duplicates(['zipcode'],keep=False)

    # 2. Gather silver plan rates by state+rate_area and create a new dataframe that 
    slcSilverPlans = plans[plans['metal_level'] == 'Silver'].sort_values('rate').groupby(['state','rate_area'])['rate'].apply(list).apply(getSecondItem).reset_index()

    # 3. Query across first two tables to find SLCSP per zip code
    mergeSlcspZip = slcsp.merge(unambiguousZips,how='left',on='zipcode')
    outputData = mergeSlcspZip.merge(slcSilverPlans,how='left',on=['state','rate_area'])
    outputData.fillna('')

    # 4. Return the necessary info 
    print("zipcode,rate")

if __name__ == "__main__":
    main()

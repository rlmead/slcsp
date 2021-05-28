import pandas

# Read the necessary data from csv files into dataframes
plans = pandas.read_csv('./plans.csv')
slcsp = pandas.read_csv('./slcsp.csv')
zips = pandas.read_csv('./zips.csv')

# Define function to calculate second lowest cost silver plan
def main():
    # 1. Get list of zips with their state+rate_area, where unambiguous
    
    # a. consolidate unique combinations of zip+state+rate_area into just the first occurrence of each combination
    zipsByRateArea = zips[['zipcode','state','rate_area']].drop_duplicates(['zipcode','state','rate_area'],keep='first')

    # b. remove *all* occurrences of duplicate zip codes (now, duplicates indicate ambiguity by rate area)
    unambiguousZips = zipsByRateArea.drop_duplicates(['zipcode'],keep=False)

    # 2. Consolidate silver plans by state+rate_area into sorted rate list
    silverPlans = plans[plans['metal_level'] == 'Silver'].sort_values('rate').groupby(['state','rate_area'])['rate'].apply(list).reset_index()

    # 3. Query across first two tables to find SLCSP per zip code
    mergeSlcspZip = slcsp.merge(unambiguousZips,how='left',on='zipcode')
    outputData = mergeSlcspZip.merge(silverPlans,how='left',on=['state','rate_area'])

    # 4. Return the necessary info 
    print("zipcode,rate")

if __name__ == "__main__":
    main()

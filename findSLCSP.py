import pandas

# Read the necessary data from csv files into dataframes
plans = pandas.read_csv('./plans.csv')
slcsp = pandas.read_csv('./slcsp.csv')
zips = pandas.read_csv('./zips.csv')

# Define function to calculate second lowest cost silver plan
def main():
    # 1. Get list of zips with their state+rate_area, where unambiguous

    # 2. Consolidate silver plans by state+rate_area

    # 3. Query across first two tables to find SLCSP per zip code

    # 4. Return the necessary info 
    print("zipcode,rate")

if __name__ == "__main__":
    main()

# MVP: Calculate the second lowest cost silver plan

## Must have
- data ingestion
- mapping between rate area and zip code
- data analysis with numpy & pandas to determine slcsp per zip code via rate area
- handling for edge cases:
    - zip codes with only one silver plan should be left blank
    - zip codes with unknown counties *may* still have an slcsp
    - zip codes in more than one county will be ambiguous and should be left blank
- properly-formatted and properly-ordered output

## Should have
- instructions for installing pandas and running with python3

## Won't have
- any extra data analysis
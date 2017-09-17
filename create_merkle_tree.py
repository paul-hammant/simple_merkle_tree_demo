import csv
import json
import os

# from sh import wget
# wget("https://raw.githubusercontent.com/tonmcg/County_Level_Election_Results_12-16/master/2016_US_County_Level_Presidential_Results.csv")

ix = 0
votes_dem = 1
votes_gop = 2
total_votes = 3
per_dem = 4
per_gop = 5
diff = 6
per_point_diff = 7
state_abbr = 8
county_name = 9
combined_fips = 10

with open('2016_US_County_Level_Presidential_Results.csv', 'rb') as csvfile:
    countyreader = csv.reader(csvfile, delimiter=',')
    for county in countyreader:
        if county[combined_fips] == "combined_fips":
            continue

        state_char_0 = county[state_abbr][0:1]
        county_char_0 = county[county_name][0:1]
        dir =  "data/" + state_char_0 + "/" + county[state_abbr] + "/" \
               +  county_char_0 + "/" + county[county_name].replace(" ", "_")
        if not os.path.exists(dir):
            os.makedirs(dir)

        path = dir + "/" + county[combined_fips]

        vd = int(float(county[votes_dem]))
        vg = int(float(county[votes_gop]))
        tv = int(float(county[total_votes]))
        pd = float(county[per_dem])
        pg = float(county[per_gop])
        d = int(county[diff].replace(",",""))
        ppd = float(county[per_point_diff].replace("%", ""))
        data = {"votes": {"dem": vd,
                          "gop": vg,
                          "tot": tv,
                          "diff": d},
                "pct": {"dem": float(format(pd * 100, '.2f')),
                        "gop": float(format(pg * 100, '.2f')),
                        "per_point_diff": ppd}
                ,
                "for": county[state_abbr] + "/" + county[county_name] + "/" + county[combined_fips]
                }
        f = open(path + ".json", 'w')
        f.write(json.dumps(data, indent=4))
        f.close()


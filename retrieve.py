import sfx
import json
import os
import sys

if (len(sys.argv) < 2):
    print("You must provide the dashboard ID to retrieve.")
    exit()

dashboard_id = sys.argv[1]

# Grab the requested dashboard
dashboard_str = sfx.get_dashboard(dashboard_id)
dashboard = json.loads(dashboard_str)

# Write it locally for later editing
path = dashboard['name'] + "/"
os.mkdir(path)
f = open(path + "dashboard.json", "w")
f.write(dashboard_str)
f.close()

# Grab all associated charts and write them locally
chartpath = path + "charts/"
os.mkdir(chartpath)

for chart in dashboard['charts']:
    chart_str = sfx.get_chart(chart["chartId"])
    f = open(chartpath + str(chart["chartId"]) + ".json", "w")
    f.write(chart_str)
    f.close()

print("Dashboard and charts written to '" + chartpath + "'.")
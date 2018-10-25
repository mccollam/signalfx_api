import sfx
import json
import os
import sys

if (len(sys.argv) < 2):
    print("You must provide the dashboard to upload.")
    exit()

name = sys.argv[1]

# Fields to remove before uploading
remove = "creator", "created", "lastUpdated", "lastUpdatedBy", "id"

path = name + "/"
chartpath = path + "charts/"

# Create each chart sequentially, noting the resulting IDs
newcharts = {}
donecharts = []  # track which charts we've already added or removed

for filename in os.listdir(chartpath):
    if filename.endswith(".json"):
        f = open(chartpath + filename, "r")        
        chart = json.loads(f.read())
        f.close()

        oldid = chart["id"]
        # We're creating a new chart, so get rid of the old data
        for i in remove:
            if i in chart:
                del chart[i]
        
        newchart = json.loads(sfx.post_chart(chart))
        newcharts[oldid] = newchart["id"]
        print("Created chart: " + newchart["id"])

# Load the dashboard...
f = open(path + "dashboard.json")
dashboard = json.loads(f.read())
f.close()

# ... and replace the old chart IDs with the newly generated ones
for chart in dashboard["charts"]:
    donecharts.append(chart["chartId"])
    chart["chartId"] = newcharts[chart["chartId"]]

for oldchart, newchart in newcharts.items():
    #if newchart not in dashboard["charts"] and newchart not in donecharts:
    if oldchart not in donecharts:
        dashboard["charts"].append({"chartId": newchart, "row": 1, "column": 1, "width": 6, "height": 1})
        print("New chart found: " + newchart)

# Get rid of the old data
for i in remove:
    if i in dashboard:
        del dashboard[i]

# Create the new dashboard

print(json.dumps(dashboard))

newdashboard = json.loads(sfx.post_dashboard(dashboard))
print("\n\nNew dashboard created!  ID: " + str(newdashboard["id"]))

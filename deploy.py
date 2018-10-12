import sfx
import json
import os

# Set this to the name of the local dashboard structure
name = "Dashboard Name"

path = name + "/"
chartpath = path + "charts/"

# Create each chart sequentially, noting the resulting IDs
newcharts = {}
for filename in os.listdir(chartpath):
    if filename.endswith(".json"):
        f = open(chartpath + filename, "r")        
        chart = json.loads(f.read())
        f.close()

        oldid = chart["id"]
        # We're creating a new chart, so get rid of the old data
        del chart["id"]
        del chart["creator"]
        del chart["created"]
        del chart["lastUpdated"]
        del chart["lastUpdatedBy"]
        
        newchart = json.loads(sfx.post_chart(chart))
        newcharts[oldid] = newchart["id"]

# Load the dashboard...
f = open(path + "dashboard.json")
dashboard = json.loads(f.read())
f.close()

# ... and replace the old chart IDs with the newly generated ones
for chart in dashboard["charts"]:
    chart["chartId"] = newcharts[chart["chartId"]]

# Get rid of the old data
del dashboard["created"]
del dashboard["creator"]
del dashboard["id"]
del dashboard["lastUpdated"]
del dashboard["lastUpdatedBy"]

# Create the new dashboard
newdashboard = json.loads(sfx.post_dashboard(dashboard))
print("New dashboard created!  ID: " + str(newdashboard["id"]))
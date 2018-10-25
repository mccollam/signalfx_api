# Create a sample chart via code

import sfx
import json

chart = {
  "customProperties" : { },
  "description" : "Chart as code example",
  "name" : "Chart As Code",
  "options" : {
    "areaChartOptions" : {
      "showDataMarkers" : False
    },
    "axes" : [ {
      "highWatermark" : None,
      "highWatermarkLabel" : None,
      "label" : "",
      "lowWatermark" : None,
      "lowWatermarkLabel" : None,
      "max" : None,
      "min" : None
    }, {
      "highWatermark" : None,
      "highWatermarkLabel" : None,
      "label" : "",
      "lowWatermark" : None,
      "lowWatermarkLabel" : None,
      "max" : None,
      "min" : None
    } ],
    "axisPrecision" : None,
    "colorBy" : "Dimension",
    "defaultPlotType" : "LineChart",
    "eventPublishLabelOptions" : [ ],
    "histogramChartOptions" : {
      "colorThemeIndex" : 16
    },
    "includeZero" : False,
    "legendOptions" : {
      "fields" : None
    },
    "lineChartOptions" : {
      "showDataMarkers" : False
    },
    "onChartLegendOptions" : {
      "dimensionInLegend" : None,
      "showLegend" : False
    },
    "programOptions" : {
      "disableSampling" : False,
      "maxDelay" : None,
      "minimumResolution" : 0
    },
    "publishLabelOptions" : [ {
      "displayName" : "memory.free - Sum",
      "label" : "A",
      "paletteIndex" : None,
      "plotType" : None,
      "valuePrefix" : None,
      "valueSuffix" : None,
      "valueUnit" : None,
      "yAxis" : 0
    }, {
      "displayName" : "cpu.utilization - Sum",
      "label" : "B",
      "paletteIndex" : None,
      "plotType" : None,
      "valuePrefix" : None,
      "valueSuffix" : None,
      "valueUnit" : None,
      "yAxis" : 1
    } ],
    "showEventLines" : False,
    "stacked" : False,
    "time" : {
      "range" : 900000,
      "type" : "relative"
    },
    "type" : "TimeSeriesChart",
    "unitPrefix" : "Metric"
  },
  "packageSpecifications" : "",
  "programText" : "A = data('memory.free').sum().publish(label='A')\nB = data('cpu.utilization').sum().publish(label='B')",
  "relatedDetectorIds" : [ ],
  "tags" : None
}

result = json.loads(sfx.post_chart(chart))
print("New chart: " + result["id"])
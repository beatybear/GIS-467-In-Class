# -*- coding: utf-8 -*-
"""
in class work 4.4.22
"""
import arcpy

input_coordinates = arcpy.GetParatemerAsText(0)
incident_type = arcpy.GetParatemerAsText(1)
comment = arcpy.GetParatemerAsText(2)

arcpy.addMessage("Collected information")
input_fc = r"" #path to feature class

long, lat = input_coordinates.split(",")
coords = (float(long), float(lat))
arcpy.addMessage("converted coordinate information")
with arcpy.da.InsertCursor(input_fc, ["SHAPE@XY", "Type", "Comments"]) as cursor: #make sure to check casing in ArcGIS tool as cursor
    #content manager approach to make sure cursor is closed by the end
    newRow = [coords, incident_type, comment]
    cursor.insertRow(newRow)
    arcpy.addMessage("New row inserted")
arcpy.addMessage("All done")
# -*- coding: utf-8 -*-
"""
in class work 3.31.22
"""

import arcpy

"""
Develop a script tool that finds parcels within a certain distance from streams
Three input parameters:
Input parcels
Input Streams
Distance (specify both units and value)
One output
Parcels within specified distance
"""
#Input Variables
input_parcels = arcpy.GetParameterAsText(0)
input_streams = arcpy.GetParameterAsText(1)
distance = arcpy.GetParameterAsText(2)
#Output Variableget
output_feature_class = arcpy.GetParameterAsText(3)

arcpy.MakeFeatureLayer_management(input_parcels, "input_parcels")
arcpy.SelectLayerByLocation_management("input_parcels", "WITHIN_A_DISTANCE", input_streams, distance)
arcpy.AddMessage("Selected features within {} of streams".format)
arcpy.CopyFeatures_management("input_parcels", output_feature_class)

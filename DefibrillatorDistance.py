# -*- coding: utf-8 -*-
"""
in class work 3.28.22
"""
import arcpy

arcpy.env.overwriteOutput = True #automatically overwrite any output

#make a feature class of the buildings that are 150 feet away from defibrillators
#adding a \ escapes a \ (for things like \t in a String)
buildings = r"C:\Users\student\OneDrive - University of Redlands\GIS 467_667 SP 22\GIS 467 Assignment 7\campus.gdb\buildings" #full path to file in geodatabase (can be found in properties)
defibrillators = r"C:\Users\student\OneDrive - University of Redlands\GIS 467_667 SP 22\GIS 467 Assignment 7\campus.gdb\defibrillators" #another path
output_location = r"C:\Users\student\OneDrive - University of Redlands\GIS 467_667 SP 22\GIS 467 Assignment 7\GIS 467 Assignment 7.gdb"
output_fc_name = "underservedBuildingsScript"

arcpy.MakeFeatureLayer_management(buildings, "buildings")
arcpy.management.SelectLayerByLocation("buildings", "WITHIN_A_DISTANCE", defibrillators, "150 Feet", "NEW_SELECTION", "INVERT")
arcpy.conversion.FeatureClassToFeatureClass("buildings",
                                            output_location,
                                            output_fc_name)
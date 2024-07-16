######################################################################################################################################
#
#	SCRIPT CODE: CHE-2
#       
#	SCRIPT TITLE: Average Dose Rate
#
#	VERSION: 1.0
#
#	ORIGINAL SCRIPT WRITTEN BY: O. Steel  
#
#	DESCRIPTION & VERSION HISTORY:
#       v1.0 (OS): Determines the average dose rate (MU/min) for a VMAT beam set. It assumes equal spacing of the control points.
#               
#                   _____________________________________________________________________________
#                           
#                           SCRIPT VALIDATION DATE IN RAYSTATION SHOULD MATCH FILE DATE
#                   _____________________________________________________________________________
#
######################################################################################################################################

from connect import *
import sys
clr.AddReference("System.Windows.Forms")
clr.AddReference("System.Drawing")
from System.Windows.Forms import Application, Form, Label, ComboBox,CheckBox, TextBox, Button, MessageBox, RadioButton, BorderStyle, FormBorderStyle
from System.Drawing import Point, Size,Font,FontStyle, Color

try:
    beam_set = get_current("BeamSet")

# Integrity check if there is no patient/plan open
except:
    MessageBox.Show("Ensure a patient/plan is open")
    sys.exit()

patient = get_current("Patient")
case = get_current("Case")
exam = get_current("Examination")
plan = get_current("Plan")
case_name = case.CaseName
plan_name = plan.Name
exam_name = exam.Name
beam_set_name = beam_set.DicomPlanLabel

beams = patient.Cases[case_name].TreatmentPlans[plan_name].BeamSets[beam_set_name].Beams

msg = "Plan: " + plan_name + "\nBeam set: " + beam_set_name

beam_av_doserates = []
beam_num = 0

for beam in beams:
    doserates = []
    beam_name = beams[beam_num].Name
    seg_num = 0
    for seg in beams[beam_num].Segments:
        doserates.append(beams[beam_num].Segments[seg_num].DoseRate)
        seg_num +=1
    beam_num +=1
    average = sum(doserates)/len(doserates)
    beam_av_doserates.append(average)

av_doserate = round(sum(beam_av_doserates)/len(beam_av_doserates),0)

msg = msg + "\n\nAverage dose rate = " + str(av_doserate) + " MU/min\n\n***Note that this assumes equal spacing of\ncontrol points throughout the beam set***"

MessageBox.Show(msg, "Average Dose Rate")
sys.exit()


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
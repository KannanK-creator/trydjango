from django import forms
from CaptData_DB.models import CaptData_Tbl

class DataCapt_Form(forms.ModelForm):
	class Meta:
		model = CaptData_Tbl
		fields = ['Capt_ID','Capt_Data'] 
	
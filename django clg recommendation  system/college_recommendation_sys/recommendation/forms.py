from django import forms

class StudentPreferencesForm(forms.Form):
    degree = forms.CharField(max_length=100, label='Enter  Degree (e.g., FSC(eng),FSC(med),ICS(Statistics),ICS(Phyics),ICS(Ecnomics),ICOM)')
    min_score = forms.FloatField(label='Enter Marks ')
    Degree_level = forms.CharField(max_length=100)
    college_choice = forms.ChoiceField(choices=[('boys', 'Boys College'), ('girls', 'Girls College')], label='Select criteria')
    Select_shift = forms.ChoiceField(choices=[('morning', 'morning shift'), ('evening', 'evening shift')], label='Select shift')

from django import forms

class ClientConsoleForm(forms.Form):
    text_to_convert = forms.CharField(label="Enter Text to Convert",widget=forms.Textarea(attrs={'class':'input'}))
    src_langauge    = forms.ChoiceField(
                                    label="Select Source Language",
                                    choices=[('SELECT', 'select'),('en', 'English'), ('hi', 'Hindi'), ('ja', 'Japanese'), ('ko', 'Korean')],
                                    widget=forms.Select(attrs={'class': 'input'}))
    dest_langauge   = forms.ChoiceField(
                                    label="Select Destination Language",
                                    choices=[('SELECT', 'select'),('en', 'English'),('hi', 'Hindi'), ('ja', 'Japanese'),('ko', 'Korean')],
                                    widget=forms.Select(attrs={'class':'input'}))




    ''' 
    1.Readonly Field:
    converted_text=forms.CharField(label="Translated Text",
                                   required=False,
                                   widget=forms.TextInput(attrs={'class':'input','readonly':'true'}))
    '''







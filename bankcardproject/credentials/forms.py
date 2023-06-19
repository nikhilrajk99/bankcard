from django import forms

class ApplicationForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100)
    dob = forms.DateField(label='Date of Birth')
    age = forms.IntegerField(label='Age')
    gender = forms.ChoiceField(label='Gender', choices=[('male', 'Male'), ('female', 'Female')])
    phone = forms.CharField(label='Phone Number', max_length=10)
    email = forms.EmailField(label='Email')
    address = forms.CharField(label='Address', widget=forms.Textarea)
    district = forms.ChoiceField(label='District', choices=[('district1', 'District 1'), ('district2', 'District 2')])
    branch = forms.ChoiceField(label='Branch')
    account_type = forms.ChoiceField(label='Account Type', choices=[('savings', 'Savings Account'), ('current', 'Current Account')])
    materials = forms.MultipleChoiceField(label='Materials Provide', choices=[('debit-card', 'Debit Card'), ('credit-card', 'Credit Card'), ('cheque-book', 'Cheque Book')], widget=forms.CheckboxSelectMultiple)

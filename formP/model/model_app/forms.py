from django import forms
choices =['1980','1991','1910']
colors=[('B','Black'),('G','Green'),('R','Red')]
# widgets = field to html input 
class contactForm(forms.Form):
    # name = forms.CharField(label="Full Name : ",help_text = "Total length must be within 20 chars",required= False,widget = forms.Textarea(attrs = {'id' : 'text_area','placeholder':'enter your name'}))
    # # file = forms.FileField()
    # email = forms.EmailField(label='useremail')
    # age = forms.IntegerField()
    # weight = forms.FloatField()
    # balance = forms.DecimalField()
    # check = forms.BooleanField()
    # birthday = forms.DateField(widget=forms.DateInput(attrs ={'type' : 'date'}))
    # appointment = forms.DateTimeField(widget=forms.DateTimeInput(attrs ={'type' : 'datetime-local'})) 
    # CHOICES = [('S','small'),('M','medium'),('L','large')] 
    # size = forms.ChoiceField(choices = CHOICES ,widget = forms.RadioSelect)
    # MEAL = [('P','Pepperoni'),('M','Mashroom'),('B','Beef')]
    # pizza = forms.MultipleChoiceField(choices = MEAL,widget=forms.CheckboxSelectMultiple)
    name = forms.CharField(label="Enter your name :")
    email = forms.EmailField(initial="google@gmail.com")
    birth_date = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    birth_date = forms.DateField(widget=forms.SelectDateWidget(years=choices),required=False)
    about_you = forms.CharField(widget=forms.Textarea(attrs={'rows':3}))
    Favourite_Color =forms.ChoiceField(choices=colors)
    Second_third = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=colors)
    Agree_the_terms = forms.BooleanField()



# class StudentData(forms.Form):
#     name = forms.CharField(widget=forms.TextInput)
#     email = forms.CharField(widget=forms.EmailInput)
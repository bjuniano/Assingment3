from django import forms
from .models import Note, Games, Sponsor
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Hidden, Button, HTML, Div, Field, Row, Fieldset

class NoteForm(forms.ModelForm):
    class Meta: 
        model = Note
        fields = ('title','content','join_date','Achievements','Games', 'Sponsor')
        
    
    def __init__(self, *args, **kwargs):
        super(NoteForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_id = "noteform"
        tag = Div('tag',css_class = "col-xs-12", style="padding:0px;")
        self.helper.layout.insert(5,Fieldset("Select Sponsor",Sponsor, Button("createSponsormodal", value="Add a Sponsor", css_class="btn btn-primary btn-sm col-xs-12 ", data_toggle="modal", data_target="#myModal")))
        self.helper.layout.insert(4, Fieldset("Select Games",Games, Button("createGamesmodal", value="Add a Game", css_class="btn btn-primary btn-sm col-xs-12", data_toggle="modal", data_target="#myModal")))
        self.helper.layout.append(Button('btn_createnote', 'Add Player', css_class='createnote', style="margin-top:15px;"))
        self.helper.layout.append(Hidden(name='btn_createnote', value="btn_createnote"))
        
        
        # self.helper.layout.pop(9)
        #self.helper.layout.append(Hidden(name="user", value="4"))
        #self.helper.add_input(Submit('submit', 'Create Note'))
        
    def full_clean(self):#http://stackoverflow.com/questions/4340287/override-data-validation-on-one-django-form-element
        super(NoteForm, self).full_clean()
        if 'Games' in self._errors:
            self.cleaned_data['Games'] = []
            print("remove Games errors")
            del self._errors['Games']
            
class NoteFormUpdate(forms.ModelForm):
    class Meta: 
        model = Note
        #fields = '__all__'
        exclude = ['user']
        
    def __init__(self, *args, **kwargs):
        super(NoteFormUpdate, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_id = "noteformupdate"
        
        self.helper.add_input(Submit('submit', 'Update'))

        
class SponsorForm(forms.ModelForm):
    class Meta:
        model = Sponsor
        fields = '__all__'
        
    def __init__(self, *args, **kwargs):
        super(SponsorForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_id = "Sponsorform"
        self.helper.layout.append(Hidden(name='btn_createSponsor', value="btn_createSponsor"))
        self.helper.layout.append(Button('btn_createSponsor', 'Add a Sponsor', css_class='createSponsor', data_dismiss="modal"))
        

class GamesForm(forms.ModelForm):
    class Meta:
        model = Games
        fields = '__all__'
        
    def __init__(self, *args, **kwargs):
        super(GamesForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_id = "Gamesform"
        self.helper.layout.append(Hidden(name='btn_createGames', value="btn_createGames"))
        self.helper.layout.append(Button('btn_createGames', 'Add a Game', css_class='createGames', data_dismiss="modal"))
        
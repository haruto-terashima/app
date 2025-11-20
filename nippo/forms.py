from django import forms

class NippoFormClass(forms.Form):
    title = forms.CharField(label="タイトル",widget=forms.TextInput(attrs={'placeholder':'内容...'}))
    content = forms.CharField(label="内容",widget=forms.Textarea(attrs={'placeholder':'タイトル...'}))
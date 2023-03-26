
# from django import forms
# from task2.tasks import send_review_email_task

# class ReviewForm(forms.Form):
  
#     email=forms.EmailField(min_length=200,widget=forms.TextInput(
#         attrs={'class':'form-control mb-3','placeholder':'firstName','id':'form-email'}
#     ))
#     review=forms.CharField(label="Review",min_length=4,max_length=50,widget=forms.TextInput(
#         attrs={'class':'form-control mb-3','placeholder':'firstName','id':'form-firstname'}
#     ))


#     def send_email(self):
#         self.send_review_email_task.delay(
#             self.cleaned_data['email'],self.cleaned_data['review']
#         )
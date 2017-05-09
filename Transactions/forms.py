from django import forms

class TransactionForm(forms.ModelForm):
	price 				=	forms.FloatField()
	start_date			=	forms.DateTimeField()
	end_date			=	forms.DateTimeField()

	class Meta:
		model 	=	Transaction
		fields	=	("price", "start_date", "end_date")
		
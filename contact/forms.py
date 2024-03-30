from django import forms


class ContactForm(forms.Form):
    nama_lengkap = forms.CharField(
        label='Nama Lengkap',
        max_length=50,
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Masukan nama lengkap'
            }
        )
        )

    tanggal_lahir = forms.DateField(

        widget=forms.SelectDateWidget(
            attrs={
                    'class':'form-control ',
                    'class':'col-sm-2'
                },
            
            
            years=range(1960, 2025)
        )
    )

    alamat = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class':'form-control',
                'placeholder':'masukan alamat lengkap anda',
            }
            ),
        label='alamat',
        max_length=255,
        required=False
    )
    email = forms.EmailField(
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'masukan Email anda',
            }
        )
    )

    jenis_kelamin = forms.ChoiceField(
        widget=forms.RadioSelect(
            attrs={
                'class':'form-check-input',
            }
            ),
        choices=[
            ('P', 'Pria'),
            ('W', 'Wanita')
        ]
    )
    
    agree =forms.BooleanField(
        widget=forms.CheckboxInput(
            attrs={
                'class':'form-check-input'
            }
        )
    )

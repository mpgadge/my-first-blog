from django.shortcuts import render
from .forms import ClientConsoleForm
from googletrans import Translator

def home(request):
    form = ClientConsoleForm()
    context = {
        'form': form
    }
    if request.method == 'POST':
        form = ClientConsoleForm(request.POST)

        if form.is_valid():
            text_to_convert = form.cleaned_data['text_to_convert']
            src_langauge = form.cleaned_data['src_langauge']
            dest_langauge = form.cleaned_data['dest_langauge']

            if src_langauge=='SELECT' or dest_langauge=='SELECT':
                pass
            translator = Translator()
            try:
                translator = Translator()
                translated_obj = translator.translate(text_to_convert, dest=dest_langauge, src=src_langauge)
                form.cleaned_data['converted_text'] = translated_obj.text
                context.update({'translated_obj': translated_obj})
            except Exception as ex:
                context.update({'Exception':ex})
                print(ex)
                return render(request,'client_console/home.html',context)
    return render(request, 'client_console/home.html', context)

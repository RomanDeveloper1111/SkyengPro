from djchoices import DjangoChoices, ChoiceItem


class FileStatusChoices(DjangoChoices):
    uploaded = ChoiceItem('uploaded', 'Uploaded')
    checking = ChoiceItem('checking', 'Checking')
    success = ChoiceItem('success', 'Success')

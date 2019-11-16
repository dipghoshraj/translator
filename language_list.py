import json
from ibm_watson import LanguageTranslatorV3

language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    iam_apikey='0QKCoygPFvBXklx16XK0P2mPSp5eJrFEllWh7xoBpwLb',
    url='https://gateway-lon.watsonplatform.net/language-translator/api')

languages = language_translator.list_identifiable_languages().get_result()
print(json.dumps(languages, indent=2))

import json
from ibm_watson import LanguageTranslatorV3

language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    iam_apikey='0QKCoygPFvBXklx16XK0P2mPSp5eJrFEllWh7xoBpwLb',
    url='https://gateway-lon.watsonplatform.net/language-translator/api')

translation = language_translator.translate(
    text="तुम कौन हो",  # तुम कौन हो तुम कौन हो
    model_id='hi-en').get_result()
print(json.dumps(translation, indent=2, ensure_ascii=False))


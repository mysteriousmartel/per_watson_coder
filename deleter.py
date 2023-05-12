import json
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator('')#Insert API key
natural_language_understanding = NaturalLanguageUnderstandingV1(
    version='2021-03-25',
    authenticator=authenticator)

natural_language_understanding.set_service_url('')#Insert URL

model = natural_language_understanding.delete_classifications_model(
  model_id='',#Insert model_id
).get_result()


print(json.dumps(model, indent=2))
import pandas as pd

mayo_diseases = pd.read_csv("data/Mayo/diseases.csv")
mayo_diseases['type'] = 'disease'
mayo_diseases['website'] = 'Mayo Clinic'

mayo_drugs = pd.read_csv("data/Mayo/drugs.csv")
mayo_drugs['type'] = 'drug'
mayo_drugs['website'] = 'Mayo Clinic'

mayo_supplements = pd.read_csv("data/Mayo/supplements.csv")
mayo_supplements['type'] = 'supplement'
mayo_supplements['website'] = 'Mayo Clinic'

mayo_symptoms = pd.read_csv("data/Mayo/symptoms.csv")
mayo_symptoms['type'] = 'symptom'
mayo_symptoms['website'] = 'Mayo Clinic'


webmd_drugs = pd.read_csv("data/Webmd/drugs.csv")
webmd_drugs['type'] = 'drug'
webmd_drugs['website'] = 'Webmd'

webmd_supplements = pd.read_csv("data/Webmd/supplements.csv")
webmd_supplements['type'] = 'supplement'
webmd_supplements['website'] = 'Webmd'

frames = [mayo_diseases, mayo_symptoms, mayo_drugs, \
          mayo_supplements, webmd_drugs, webmd_supplements]
result = pd.concat(frames)

result.to_csv("full_data.csv", index = False)
# print(result.head())
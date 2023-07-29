# Import relevant libraries
import streamlit as st
from helper_functions import Helper_Functions 

# Intiating the app
st.header("Med Router ")
hf = Helper_Functions()

# Side Bar
with st.sidebar:
    # Init
    st.header("Customize Your Options")
    # Website Checkbox
    st.write("Website")
    mayo = st.checkbox('Mayo Clinic', value = True)
    webmd = st.checkbox("Webmd", value = True)

    # Type Checkbox
    st.write("Type")
    disease = st.checkbox('Diseases', value = True)
    drug = st.checkbox('Drugs', value = True)
    supplement = st.checkbox('Supplements', value = True)
    symptom = st.checkbox('Symptoms', value = True)

    # Number of ouputs
    number = st.number_input('No Of Results', step = 1, min_value= 5, max_value= 50)

    # Button
    submit_state = st.button("Submit")
    if submit_state:
        hf.customize_refresh()

        hf.customize_mayo(mayo)
        hf.customize_webmd(webmd)

        hf.customize_disease(disease)
        hf.customize_drugs(drug)
        hf.customize_supplements(supplement)
        hf.customize_symptoms(symptom)

        hf.customize_number(number)

# Main Content - Input
var = st.text_input("Input Your Query Here", placeholder="Abdominal aortic aneurysm")
state, results = hf.cosine_similarity_check(var)

# Main Content - Output
if state:
    for ind in results.index:
        name = results['name'][ind]
        url = results['url'][ind]
        type = results['type'][ind]
        website = results['website'][ind]
        score = results['Cosine Similarity'][ind]
        with st.expander(name, expanded=False):
            col1, col2 = st.columns([1, 3])
            with col1:
                st.write("**Website :**", website)
                st.write("**Score :**", round(score,3))
            with col2:
                st.write("**Type :**", type.capitalize())
                st.write("**URL :**", url)
else:
    with st.expander("No Matches", expanded=False):
        st.write("There are no results found. This could be because of the input or the options. Please try something else! ")
            
            
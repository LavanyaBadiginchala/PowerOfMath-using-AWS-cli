import streamlit as st
import requests

st.title('To the Power of Math!')

base = st.number_input('Base number', min_value=0, value=2)
exponent = st.number_input('...to the power of', min_value=0, value=3)

if st.button('Calculate'):
    api_gateway_url = "https://c2ocj3j0fe.execute-api.us-east-2.amazonaws.com/prod/calculate"
    response = requests.post(api_gateway_url, json={"base": base, "exponent": exponent})
    
    if response.status_code == 200:
        try:
            st.write("Success")
            response_json = response.json()
            st.write(response_json)
        except ValueError:
            st.error('Failed to parse JSON response')
    else:
        st.error(f'Error: {response.status_code}')

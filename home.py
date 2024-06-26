import utils
import streamlit as st
import streamlit.components.v1 as comps
import time

def main():
    st.title('Website Builder')
    user_text = st.text_input("Enter text:", "")

    
    if user_text:
            st.write("You entered:", user_text)
            code = utils.generate_code(user_text)
            utils.write_to_file(code)
            time.sleep(2)
            utils.git_commit_push(r"https://github.com/amoghubhalkar19/deepsoft", "changing index.html for current input") 
            with st.spinner('Deploying website...'):
                website_url = utils.deploy_render_api()
                time.sleep(150)
            # Show website URL and iframe once deployment is complete
            st.write(f'Website Link: {website_url}')
            st.write("Here's your website:")
            comps.iframe(website_url, height=500, scrolling=True)

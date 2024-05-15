import utils
import streamlit as st
import streamlit.components.v1 as comps
import time

def main():
    st.title('Modify your Website')
    modified_text = st.text_input("Enter text:", "")

    
    if modified_text:
            with open("public/index.html", "r") as file:
                html_content = file.read()
            st.write("You entered:", modified_text)
            code = utils.perform_modifications(modified_text, html_content)
            utils.write_to_file(code)
            time.sleep(2)
            utils.git_commit_push(r"D:\deepsoft", "changing index.html for current input") 
            with st.spinner('Deploying website...'):
                website_url = utils.deploy_render_api()
                time.sleep(150)
            # Show website URL and iframe once deployment is complete
            st.write(f'Website Link: {website_url}')
            st.write("Here's your website:")
            comps.iframe(website_url, height=500, scrolling=True)
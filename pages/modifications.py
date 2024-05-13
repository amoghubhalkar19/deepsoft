# import streamlit as st
# import utils
# import streamlit.components.v1 as comps
# import time

# st.title('Modifications Page')
# st.write("Perform modifications here...")
# # Add modification functionalities here
# modified_text = st.text_input("Modify your website:", "")
# # You can add more prompts for other modifications
# html_content = ""
# with open("public/index.html", "r") as file:
#     html_content = file.read()
# # Generate and deploy modified website
# if st.button("Deploy Modified Website"):
#     code = utils.perform_modifications(modified_text, html_content)
#     utils.write_to_file(code)
#     utils.git_commit_push(r"D:\deepsoft", "changing index.html for modified input")
#     with st.spinner('Deploying modified website...'):
#         modified_website_url = utils.deploy_render_api()
#         time.sleep(90)
#     st.write(f'Modified Website Link: {modified_website_url}')
#     st.write("Here's your modified website:")
#     comps.iframe(modified_website_url, height=500, scrolling=True)

#     # Update session state to navigate back to the home page
#     st.session_state.page = 'home'

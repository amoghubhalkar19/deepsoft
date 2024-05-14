import utils
import streamlit as st
import streamlit.components.v1 as comps
import time

def main():
    st.title('Website Builder')
    user_text = st.text_input("Enter text:", "")
    
    # # Initialize session state to manage page navigation
    # if 'page' not in st.session_state:
    #     st.session_state.page = 'home'

    # if st.session_state.page == 'home':
    if user_text:
            st.write("You entered:", user_text)
            code = utils.generate_code(user_text)
            utils.write_to_file(code)
            utils.git_commit_push(r"D:\deepsoft", "changing index.html for current input") 
            with st.spinner('Deploying website...'):
                website_url = utils.deploy_render_api()
                time.sleep(90)
            # Show website URL and iframe once deployment is complete
            st.write(f'Website Link: {website_url}')
            st.write("Here's your website:")
            comps.iframe(website_url, height=500, scrolling=True)

            modifications_text=st.text_input("Enter modifications:", "")
            if modifications_text:
                code_modified=utils.perform_modifications(modifications_text, code)
                utils.write_to_file(code_modified)
                utils.git_commit_push(r"D:\deepsoft", "changing index.html for current input")
                with st.spinner('Deploying website...'):
                    website_url = utils.deploy_render_api()
                    time.sleep(90)
            # Show website URL and iframe once deployment is complete
                st.write(f'Website Link: {website_url}')
                st.write("Here's your website:")
                comps.iframe(website_url, height=500, scrolling=True)



if __name__ == "__main__":
    main()

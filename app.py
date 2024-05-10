import utils
import streamlit as st
import streamlit.components.v1 as comps


def main():
    st.title('Website Builder')
    user_text = st.text_input("Enter text:", "")
    
    if user_text:
        st.write("You entered:", user_text)
        code=utils.generate_code(user_text)
        utils.write_to_file(code)
        utils.git_commit_push(r"D:\deepsoft", "changing index.html for current input")
        website_url=utils.deploy_render_api()
        
        comps.iframe(website_url, height=500, scrolling=True)
        st.text(f'Hosted Link: {website_url}')

if __name__ == "__main__":
    main()

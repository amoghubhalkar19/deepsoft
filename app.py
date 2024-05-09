import streamlit as st
import streamlit.components.v1 as comps

def main():
    st.title('Website Preview')
    website_url = "http://barc.iitkgp.ac.in/index.html"
    comps.iframe(website_url, height=600)

if __name__ == "__main__":
    main()

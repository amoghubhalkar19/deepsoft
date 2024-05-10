import langchain
from langchain import PromptTemplate, HuggingFaceHub, LLMChain
import streamlit as st
import streamlit.components.v1 as comps
import requests
import os
import subprocess

def git_commit_push(repo_path, commit_message):
            try:
        # Change directory to the repository path
                # subprocess.run(["cd", repo_path], check=True)

        # Stage all changes
                subprocess.run(["git", "add", "-A"], check=True)

        # Commit changes with the provided commit message
                subprocess.run(["git", "commit", "-m", commit_message], check=True)

        # Push changes to the remote repository
                subprocess.run(["git", "push"], check=True)

                print("Changes committed and pushed successfully.")

            except subprocess.CalledProcessError as e:
                print("Failed to commit and push changes.")
                print(f"Error: {e}")


def main():
    st.title('Website Builder')
    user_text = st.text_input("Enter text:", "")
    
    if user_text:
        st.write("You entered:", user_text)

        # Define the prompt template
        prompt =PromptTemplate(
            input_variables=["text"],
            template='''Task: {text}

            Objective:
            Design and implement a product website showcasing a fictional product using HTML, CSS, and JavaScript in a single file. The website should have the following sections:

            Header Section: Create a header section with a navigation menu and any relevant branding elements.
            Hero Section: Design a hero section that prominently displays the product with a compelling headline and call-to-action button.
            Features Section: Develop a section that highlights key features of the product using vibrant colors and fonts.
            Pricing Section: Implement a pricing section that displays different pricing plans or options for the product.
            Banner: Incorporate a banner section to grab attention and convey important messages or promotions.
            FAQ Section: Include a frequently asked questions (FAQ) section where users can find answers to common queries about the product.
            Footer: Create a footer section with links to important pages, social media icons, and any other relevant information.
            
            Instructions:

            HTML Structure:
            Use semantic HTML elements for better accessibility and SEO.
            Structure the page with appropriate sections and divs for each component.

            CSS Styling:
            Apply inline CSS to style each section.
            Use vibrant colors and modern fonts to enhance visual appeal.
            Ensure responsive design to optimize for various screen sizes.

            JavaScript Interactivity:
            Use JavaScript to add interactivity to the website, such as smooth scrolling, form validation, or interactive elements.

            Third-Party Libraries/Frameworks:
            Utilize open-source third-party libraries or frameworks to enhance creativity and functionality if desired. Examples include Bootstrap, jQuery, or Font Awesome.

            Modern Coding Techniques:
            Implement modern coding techniques, such as flexbox or grid layout for responsiveness and CSS variables for easier customization.
            Optimize code for performance and efficiency to ensure fast loading times.

            Deliverables:
            Submit a single HTML file containing the complete code for the product website including CSS and JavaScript. The website should be visually appealing, user-friendly, and fully functional.'''
        )

        chain=LLMChain(llm=HuggingFaceHub(repo_id='mistralai/Mistral-7B-Instruct-v0.2', model_kwargs={'temperature':0.1, 'max_new_tokens':8000}, huggingfacehub_api_token="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"), prompt=prompt)        
        code=chain.invoke(user_text)

        print("generated response from llm")

        doctype_index = code['text'].find("<!DOCTYPE html>")
        doctype_index_last=code['text'].find("</html>")
        final_code=code['text'][doctype_index:doctype_index_last+7]

        print("extracted the relevant code")

        file_path = os.path.join("public", "index.html")
        with open(file_path, "w") as file:
            file.write(final_code)

        print("Edited the index.html file")
        #commiting and publishing on github

        repo_path = r'D:\deepsoft'
        commit_message = "changing index.html"
        git_commit_push(repo_path, commit_message)

        #Deploying using render.com API

        API_KEY = 'rnd_8xSMgp0rGoZ9Ic1YT4XZDq4BQNAq'
        headers = {'Authorization': f'Bearer {API_KEY}'}

        url='https://api.render.com/v1/owners'
        response_owner=requests.get(url, headers=headers)
        owner_id=response_owner.json()[0]['owner']['id']


        # deploy_key="ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQDGGeSNaQ/25WtzvdtAQIOQkEYnR4kjNa22NT92zmYEBjW9UTu0tZiU+UFm2rQs/PfQwakzLNl0HcsUdchCJIk2g+EXj0BZaG+a96I7Tk436rT40qyROZ5tJghz/EDtZvQriL8fp3aOUuGn5vvaGvC1rOo7066mMcO5io/M67wbk0xHMdYR0Xr4JUaWdihoqoRaBr+C0M877qVCowVLMZrH5c9neEjoLfp6nfEYgiuW7THXHRc8NJ6Me009MquEHzpUNeaZ3Lw3ji2AsTqicPm+MotjQBGoYvwQ/RluaPij0PoT6II2lNy1roFlsam5tTlWr0JCRcGot5cLMEdk63g8IjXCdYaMGkl8xJD8xP960tn+yVR2RDl0Dl8X8Sb82ZZnToUbz3HOIrHVdYy64MT6zEqi97xizxtKo5S4y7J24MOulit8OoSufmoNbeU1j1m632pReEUw4O8prq3JuheDVBuqIjRL+BoGiDwwnZ0DH13Tbekv4/DAJKQkSn7Z6xboRZmamK65JGnyPHafrSL0tdE4z2hrUoxEHa6336VifALQV5aYXGI0g/vuwkm6uiqNiKMEABVla7ZhqZxWJHeDSuMRnJ2ZQtFCxhMNlGvuywgIzjcaodm0IE3cMXrku7evtfbXWwzHrV6e1ghPqlOm4jJcAj7kvxoQq1jdPIJ1oQ== ubhalkar.amogh@kgpian.iitkgp.ac.in"
        service_config = {
            "name": "product",
            "type": "static_site",
            "plan": "starter",
            "ownerId": owner_id,
            "repo": {
                "repoName": "amoghubhalkar19/deepsoft",
                # "deployKeyID": deploy_key
            },
            "buildCommand": "echo 'Build complete'",
            "publishDir": "./"
        }

        create_response = requests.post('https://api.render.com/v1/services', headers=headers, json=service_config)
        create_get=requests.get('https://api.render.com/v1/services', headers=headers)
        service_id=create_get.json()[0]['service']['id']
        # print(create_response.json())

        deploy_response = requests.post(f'https://api.render.com/v1/services/{service_id}/deploys', headers=headers)
        deploy_id = deploy_response.json()['id']
        # print(deploy_id)

        service_info_url = f'https://api.render.com/v1/services/{service_id}'
        service_info_response = requests.get(service_info_url, headers=headers)
        web_url=service_info_response.json()['serviceDetails']['url']
        print(web_url)
        print("deployed successfully")


        # URL for website preview
        website_url = web_url
        
        comps.iframe(website_url, height=500, scrolling=True)
        st.text(f'Hosted Link: {website_url}')

if __name__ == "__main__":
    main()

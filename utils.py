import os

# function to deploy website on render.com and generating hosted link

import requests

def deploy_render_api(): #params when integrating as a whole: repo name, api key
    API_KEY = 'rnd_7GmEswXRdw0yPXandA0thflgPpgk'
    headers = {'Authorization': f'Bearer {API_KEY}'}

    url='https://api.render.com/v1/owners'
    response_owner=requests.get(url, headers=headers)
    owner_id=response_owner.json()[0]['owner']['id']

    # deploy_key="ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQDGGeSNaQ/25WtzvdtAQIOQkEYnR4kjNa22NT92zmYEBjW9UTu0tZiU+UFm2rQs/PfQwakzLNl0HcsUdchCJIk2g+EXj0BZaG+a96I7Tk436rT40qyROZ5tJghz/EDtZvQriL8fp3aOUuGn5vvaGvC1rOo7066mMcO5io/M67wbk0xHMdYR0Xr4JUaWdihoqoRaBr+C0M877qVCowVLMZrH5c9neEjoLfp6nfEYgiuW7THXHRc8NJ6Me009MquEHzpUNeaZ3Lw3ji2AsTqicPm+MotjQBGoYvwQ/RluaPij0PoT6II2lNy1roFlsam5tTlWr0JCRcGot5cLMEdk63g8IjXCdYaMGkl8xJD8xP960tn+yVR2RDl0Dl8X8Sb82ZZnToUbz3HOIrHVdYy64MT6zEqi97xizxtKo5S4y7J24MOulit8OoSufmoNbeU1j1m632pReEUw4O8prq3JuheDVBuqIjRL+BoGiDwwnZ0DH13Tbekv4/DAJKQkSn7Z6xboRZmamK65JGnyPHafrSL0tdE4z2hrUoxEHa6336VifALQV5aYXGI0g/vuwkm6uiqNiKMEABVla7ZhqZxWJHeDSuMRnJ2ZQtFCxhMNlGvuywgIzjcaodm0IE3cMXrku7evtfbXWwzHrV6e1ghPqlOm4jJcAj7kvxoQq1jdPIJ1oQ== ubhalkar.amogh@kgpian.iitkgp.ac.in"
    service_config = {
        "name": "deepsoft",
        "type": "static_site",
        "plan": "starter",
        "ownerId": owner_id,
        "repo": {
        "repoName": "amoghubhalkar19/deepsoft",
            # "deployKeyID": deploy_key
        },
        "buildCommand": "echo 'Build complete'",
        "publishDir": "./public"
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

    return web_url


#function for commiting changes on git hub

import subprocess

def git_commit_push(repo_path, commit_message):
    try:
        subprocess.run(["git", "-C", repo_path, "add", "-A"], check=True)
        subprocess.run(["git", "-C", repo_path, "commit", "-m", commit_message], check=True)
        subprocess.run(["git", "-C", repo_path, "push"], check=True)
        print("Changes committed and pushed successfully.")

    except subprocess.CalledProcessError as e:
        print("Failed to commit and push changes.")
        print(f"Error: {e}")
    
    return git_commit_push


#function for generating respsonse from llm and getting the code

from langchain import PromptTemplate, HuggingFaceHub, LLMChain

def generate_code(input_text):

    prompt=PromptTemplate(
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
            Submit a single HTML file containing the complete code for the product website including css and javascript. The website should be visually appealing, user-friendly, and fully functional.
        '''
    )

    chain=LLMChain(llm=HuggingFaceHub(repo_id='mistralai/Mistral-7B-Instruct-v0.2', model_kwargs={'temperature':0.1, 'max_new_tokens':8000}, huggingfacehub_api_token="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"), prompt=prompt)
    code=chain.invoke(input_text)
    doctype_index = code['text'].find("<!DOCTYPE html>")
    doctype_index_last=code['text'].find("</html>")
    final_code=code['text'][doctype_index:doctype_index_last+7]

    return final_code


#function to write code in the html file 

import os

def write_to_file(code):
    file_path = os.path.join("public", "index.html")
    with open(file_path, "w") as file:
        file.write(code)

#funciton to perform modifications:

def perform_modifications(input_text, code):

    prompt=PromptTemplate(
        input_variables=["input_text", "code"],
        template='''Task: {input_text}
                    code: {code}

           Task: Modify the existing product website code to incorporate specific changes based on user input.
            Objective:
            You are tasked with making modifications to an existing product website to enhance its design and functionality. The website showcases a fictional product and currently consists of several sections including Header, Hero, Features, Pricing, Banner, FAQ, and Footer. Your goal is to update the website according to the provided input text while adhering to modern design principles and coding techniques.

            Instructions:
            1. Read the existing website code and understand its structure and content.
            2. Review the provided input text carefully, which outlines the desired changes to be made to the website.
            3. Implement modifications to each section of the website as specified in the input text.
            4. Ensure that the modified website remains visually appealing, user-friendly, and fully functional.
            5. Use semantic HTML elements, inline CSS styling, and JavaScript interactivity to enhance the website's design and functionality.
            6. Utilize modern coding techniques such as flexbox or grid layout, CSS variables, and third-party libraries/frameworks (if necessary) to optimize the website's performance and responsiveness.
            7. Verify the correctness of the modifications and ensure that the website meets the specified requirements.

            Deliverables:
            Submit the modified HTML, css and javascript code for the product website in a single page, incorporating the requested changes based on the provided input text. The modified website should reflect the desired improvements and adhere to the best practices of web development.

        '''
    )

    chain=LLMChain(llm=HuggingFaceHub(repo_id='mistralai/Mistral-7B-Instruct-v0.2', model_kwargs={'temperature':0.1, 'max_new_tokens':8000}, huggingfacehub_api_token="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"), prompt=prompt)
    modified_code=chain.invoke({'input_text':input_text, 'code':code})
    doctype_index = modified_code['text'].find("<!DOCTYPE html>")
    doctype_index_last=modified_code['text'].find("</html>")
    final_code=modified_code['text'][doctype_index:doctype_index_last+7]

    return final_code


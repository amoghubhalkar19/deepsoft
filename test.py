import utils
with open("public/index.html", "r") as file:
            html_content = file.read()

final_code=utils.perform_modifications("make the navbar and hero page more creative and colourful", html_content)

print(final_code)
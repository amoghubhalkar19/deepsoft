import requests

API_KEY = 'rnd_8xSMgp0rGoZ9Ic1YT4XZDq4BQNAq'
headers = {'Authorization': f'Bearer {API_KEY}'}

url='https://api.render.com/v1/owners'
response_owner=requests.get(url, headers=headers)
owner_id=response_owner.json()[0]['owner']['id']


# files = {'file': open('index.html', 'r')} 
deploy_key="ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQDGGeSNaQ/25WtzvdtAQIOQkEYnR4kjNa22NT92zmYEBjW9UTu0tZiU+UFm2rQs/PfQwakzLNl0HcsUdchCJIk2g+EXj0BZaG+a96I7Tk436rT40qyROZ5tJghz/EDtZvQriL8fp3aOUuGn5vvaGvC1rOo7066mMcO5io/M67wbk0xHMdYR0Xr4JUaWdihoqoRaBr+C0M877qVCowVLMZrH5c9neEjoLfp6nfEYgiuW7THXHRc8NJ6Me009MquEHzpUNeaZ3Lw3ji2AsTqicPm+MotjQBGoYvwQ/RluaPij0PoT6II2lNy1roFlsam5tTlWr0JCRcGot5cLMEdk63g8IjXCdYaMGkl8xJD8xP960tn+yVR2RDl0Dl8X8Sb82ZZnToUbz3HOIrHVdYy64MT6zEqi97xizxtKo5S4y7J24MOulit8OoSufmoNbeU1j1m632pReEUw4O8prq3JuheDVBuqIjRL+BoGiDwwnZ0DH13Tbekv4/DAJKQkSn7Z6xboRZmamK65JGnyPHafrSL0tdE4z2hrUoxEHa6336VifALQV5aYXGI0g/vuwkm6uiqNiKMEABVla7ZhqZxWJHeDSuMRnJ2ZQtFCxhMNlGvuywgIzjcaodm0IE3cMXrku7evtfbXWwzHrV6e1ghPqlOm4jJcAj7kvxoQq1jdPIJ1oQ== ubhalkar.amogh@kgpian.iitkgp.ac.in"
service_config = {
    "name": "product",
    "type": "static_site",
    "plan": "starter",
    "ownerId": owner_id,
    "repo": {
        "repoName": "amoghubhalkar19/deepsoft_test",
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


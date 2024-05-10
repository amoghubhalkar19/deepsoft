import requests

API_KEY = 'rnd_7GmEswXRdw0yPXandA0thflgPpgk'
headers = {'Authorization': f'Bearer {API_KEY}'}
url = 'https://api.render.com/v1/owners'

# Get owner ID
response_owner = requests.get(url, headers=headers)
owner_id = response_owner.json()[0]['owner']['id']
print(owner_id)

# Create service configuration
deploy_key="ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQCygItAYX9MWOe/2C4DkgJAXfkDS3Gzdw5edswSk4dXXHA0/ZJeH3Kj/Z+IiHCXVh12F7OkWcX9MK4P2xH/fVteNYVpAAQBBZiowuyvsJYJtf7P/jhdBjXyy9aPx0q8Q8JqgDCc2cFdhjkThrepAoBfeGhgAprJWZ0u3wx31Bo0zA0G5Bx49OtEVgQ6RJL+r0HfDBJfvOr1H/2wRjI1jiKIfYlqz3UGf3R7E+fKB75qpq7FxahRmcXWUt6QByWKzFcU4Zm9QTSSeyTDrP2ifXSCYm1HZ8kVpY/cYQxizTBZc9sERk6ZJqM9XS0Z9bp/AKLrOUPrgNyWNodtXHE7G/7qgOM4Qa4pw2sqnWr7LQgE/UMEshd0Dg4WACJej9eb1wL+WoHymiyFB8n1jvDkLYvzIQVqriobH3OEuZ9EZV4DhgKnGKgV+xIyvBv/20b1iPnNazP1SqB4u85/rpsYPuLzpTlKdzcvmnIzWcci3SU/yLpVuCsqN/xoV/IDeg3AnnoMVqcxerEBm3VkcRhE0hXVsWk1CQXE3bFeTXRknze0uqngCwHyIDdWYQAURxVwXaafXA0hGjMY6zP7FU6usHs0Umk1xxPm4bE+RcXaOEIFfmzXxbt7TUB2pcZV6flkZ2csTLUkwzKnDqfypH14KFtRlcyiGBbYwqtIWCREGckVrw== ubhalkar.amogh@kgpian.iitkgp.ac.in"
service_config = {
    "name": "deepsoft",
    "type": "static_site",
    "plan": "starter",
    "ownerId": owner_id,
    "repo": {
        "repoName": "amoghubhalkar19/deepsoft",
        "deployKeyID": deploy_key
    },
    "buildCommand": "echo 'Build complete'",
    "publishDir": "./"
}

create_get=requests.get('https://api.render.com/v1/services', headers=headers)
service_id=create_get.json()[0]['service']['id']
    # print(create_response.json())

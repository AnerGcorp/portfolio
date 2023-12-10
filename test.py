import yaml

with open('info.yml', 'r') as user:
    user_info = yaml.full_load(user)

print(user_info['awards_and_certificates'])
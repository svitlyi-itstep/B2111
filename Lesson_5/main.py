import requests

url = "https://meowfacts.herokuapp.com/"

'''
    Запитувати у користувача мову, якою мають бути надані факти (ukr, eng) та кількість фактів.
'''

lang = input("Оберіть мову (ukr, eng, ita): ")
count = int(input("Скільки фактів вивести:"))

response = requests.get(url=url, params= {
    'lang': lang,
    'count': count
})

if response.ok:
    as_json = response.json()
    facts = as_json['data']

    print(f'Random facts:')
    for fact in facts:
        print(f' — {fact}')

    character = as_json['data']
else:
    print(f"Status code: {response.status_code}")
#Add Info with POST Request
import requests
import json

url = "https://student-info-api.netlify.app/.netlify/functions/submit_student_info"

body = {
    "UCID": "mkm",
    "first_name": "Michael",
    "last_name": "McGillycuddy",
    "github_username": "mikemcg33",
    "discord_username": "mikemcg33",
    "favorite_cartoon": "SpongeBob SquarePants",
    "favorite_language": "Java",
    "movie_or_game_or_book": "Interstellar",
    "section": "103"
}

headers = {
    "Content-Type": "application/json"
}

try:
    json.dumps(body)
except(TypeError, ValueError):
    print("Incorrect Data Format")
    exit(100)

response = requests.post(url, json=body, headers=headers)

if response.status_code == 200:
    print("Success")
    print("Status: ", response.status_code)
    print("Body: ", response.text)
else:
    print("Failure")
    print("Status: ", response.status_code)
    print("Body: ", response.text)
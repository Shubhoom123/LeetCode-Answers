import requests
import json

LEETCODE_USERNAME = "ShubhamKhalkho"

query = '''
query getUserProfile($username: String!) {
  matchedUser(username: $username) {
    submitStats {
      acSubmissionNum {git
        difficulty
        count
      }
    }
  }
}
'''

variables = {
    "username": LEETCODE_USERNAME
}

response = requests.post('https://leetcode.com/graphql', json={'query': query, 'variables': variables})

# Print the response for debugging
print(f"Response status code: {response.status_code}")
print(f"Response JSON: {response.text}")

data = json.loads(response.text)

if data.get('data') and data['data'].get('matchedUser') and data['data']['matchedUser'].get('submitStats'):
    easy_count = data['data']['matchedUser']['submitStats']['acSubmissionNum'][1]['count']
    medium_count = data['data']['matchedUser']['submitStats']['acSubmissionNum'][2]['count']
    hard_count = data['data']['matchedUser']['submitStats']['acSubmissionNum'][3]['count']
    total_count = easy_count + medium_count + hard_count

    # Update README file
    readme_content = f"""
    # LeetCode Solutions

    Welcome to my LeetCode solutions repository! Here, I post my solutions to various LeetCode problems.

    ## Session Progress

    ![All](https://img.shields.io/badge/All-{total_count}%2F3247-lightgrey)  
    ![Easy](https://img.shields.io/badge/Easy-{easy_count}%2F817-brightgreen)  
    ![Medium](https://img.shields.io/badge/Medium-{medium_count}%2F1704-yellow)  
    ![Hard](https://img.shields.io/badge/Hard-{hard_count}%2F726-red)

    ## About
    This repository is a collection of my LeetCode problem solutions. I aim to solve problems across all difficulty levels: Easy, Medium, and Hard. 

    Feel free to browse through the solutions and see my approaches to different challenges.
    """

    with open("README.md", "w") as readme_file:
        readme_file.write(readme_content)
else:
    print("Error: Unable to retrieve user stats. Please check the username or try again later.")
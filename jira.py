import requests

# Jira credentials
JIRA_USERNAME = 'naphtalid@legitsecurity.com'
JIRA_API_TOKEN = 'ATATT3xFfGF0ipa_xRQgri6d5rSlQcs0_MSnex__PGawj3B2MYvlI6liMyZhkkC1cFlwpW4EIIjqWZJTsLo1wKo2kc65T3dVTc4HR0_STbxDAfqZU8I6L7sLKxQ3sueulUMZ_wRrnasKiX2M-bgna3_Rk1GBC0lVZXprwQU9hyJEyg19egSnScY=2D46D876'
JIRA_URL = 'https://your_company.atlassian.net/rest/api/3/'

# Fetch issues from a project
def fetch_issues(project_key):
    url = f"{JIRA_URL}search"
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }
    params = {
        "jql": f"project={project_key}",
        "maxResults": 10
    }
    response = requests.get(url, params=params, auth=(JIRA_USERNAME, JIRA_API_TOKEN), headers=headers)
    if response.status_code == 200:
        data = response.json()
        issues = data.get('issues', [])
        for issue in issues:
            key = issue.get('key')
            summary = issue.get('fields', {}).get('summary')
            print(f"Issue Key: {key}, Summary: {summary}")
    else:
        print(f"Failed to fetch issues. Status code: {response.status_code}")

# Example usage
fetch_issues("PROJ")

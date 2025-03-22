import requests

url = "https://api.github.com/search/repositories"
url += "?q=language:python+sort:stars+stars:>10000"
headers = {"Accept": "application/vnd.github.v3+json"}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

response_dict = r.json()

print(f"Total repositories: {response_dict['total_count']}")
print(f"Complete results: {not response_dict['incomplete_results']}")
# Explore information about the repositories.
repo_dicts = response_dict['items']
print(f"Repositories returned: {len(repo_dicts)}")

print("\nSelected information about each repository:")

stars = []
names = []
descs = []
for repo_dict in repo_dicts:
    stars.append(repo_dict['stargazers_count'])
    names.append(repo_dict['name'])
    
    description = f"{repo_dict['name']}</br>{repo_dict['description']}</br>Description: {repo_dict['description']} "
    descs.append(description)
    print(f"\nName: {repo_dict['name']}")
    print(f"Owner: {repo_dict['owner']['login']}")
    print(f"Stars: {repo_dict['stargazers_count']}")
    print(f"Repository: {repo_dict['html_url']}")
    print(f"Description: {repo_dict['description']}")


import plotly.express as px

plotAnnotes = []

plotAnnotes.append(dict(x="jee",
                        y="fff",
                        text="""<a href="https://plot.ly/">{}</a>""".format("Text"),
                        showarrow=False,
                        xanchor='center',
                        yanchor='center',
                        ))
fig = px.bar(x = names, y = stars,
             
    hover_name=descs   ,
# labels={
#                      "x": "name",
#                      "y": "stars"
#                  }
labels=plotAnnotes
    )

fig.show()
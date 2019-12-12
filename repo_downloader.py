from github import Github
import subprocess
import time

g = Github('a3572ad361f28478ba5bfe28a066c0753e209efa')

repositories = set()

content_files = g.search_repositories(query='org:adafruit')
for content in content_files:
    if 'circuitpython' in content.full_name.lower():
        repositories.add(content.full_name)
    rate_limit = g.get_rate_limit()
    if rate_limit.search.remaining == 0:
        print('WARNING: Rate limit on searching was reached. Results are incomplete')
        break
    time.sleep(1)

with open('repo_names', 'w') as f:
    for i in repositories:
        f.write(i + '\n')

for repo in sorted(repositories):
    url = 'https://github.com/'+repo
    bashCommand = 'git clone {} repositories1/'.format(url) + repo.split('/')[1]
    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
    time.sleep(1)

rate_limit = g.get_rate_limit()
print('Search rate limit:')
print(rate_limit.search)

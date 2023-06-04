import neededModules as ws 
import getLinks as gl

#These are snippets of code that test out the custom modules we made
query = str(input("Google Search:"))
results = gl.google_search(query)

urls = []
titles = []
for result in results:
    titles.append(result["title"])
    urls.append(result["link"])

text = ws.getArticleText(urls[1])
output = ws.summarize(text)

with open('output.txt', 'w') as f:
    f.write(urls[0])
    f.write(output)
from flask import Flask, render_template, request, redirect, url_for
import neededModules as ws
import getLinks as gl

app = Flask(__name__)
app.secret_key = "mjgiudsygifbdngs8dngnmsnadiuqwmnsdnb"

@app.route("/")
@app.route("/home/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        query = request.form["search"]
        return redirect(url_for("viewWebsites", query=query))
    else:
        return render_template("home.html")
    
@app.route("/home/?search=<query>", methods=["GET", "POST"])
def viewWebsites(query):
    if request.method == "POST":
        newQuery = request.form["search"]
        return redirect(url_for("viewWebsites", query=newQuery))
    else:
        results = gl.google_search(query)
        urls = []
        titles = []
        for result in results:
            titles.append(result["title"])
            urls.append(result["link"])

        if len(urls) > 0:
            links = [urls, titles]
            summaries = []
            for i in range(len(urls)):
                text = ws.getArticleText(urls[i])
                output = ws.summarize(text)
                summaries.append(output)
            links.append(summaries)
            return render_template("viewWebsites.html", links=links, length=len(urls))
        else:
            return render_template("viewWebsites.html", links=None)


if __name__ == "__main__":
    app.run(debug=True)
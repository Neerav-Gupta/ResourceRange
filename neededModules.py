from newspaper import Article

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

from youtube_transcript_api import YouTubeTranscriptApi

def getArticleText(url):
    # Getting the text out of an article
    article = Article(url)
    article.download()
    article.parse()
    return article.text

def summarize(text):
    try:
        # Tokenizing the text
        stopWords = set(stopwords.words("english"))
        words = word_tokenize(text)
        
        # Creating a frequency table to keep the 
        # score of each word
        
        freqTable = dict()
        for word in words:
            word = word.lower()
            if word in stopWords:
                continue
            if word in freqTable:
                freqTable[word] += 1
            else:
                freqTable[word] = 1
        
        # Creating a dictionary to keep the score
        # of each sentence
        sentences = sent_tokenize(text)
        sentenceValue = dict()
        
        for sentence in sentences:
            for word, freq in freqTable.items():
                if word in sentence.lower():
                    if sentence in sentenceValue:
                        sentenceValue[sentence] += freq
                    else:
                        sentenceValue[sentence] = freq
        
        
        
        sumValues = 0
        for sentence in sentenceValue:
            sumValues += sentenceValue[sentence]
        
        # Average value of a sentence from the original text
        
        average = int(sumValues / len(sentenceValue))
        
        # Storing sentences into our summary.
        summary = ''
        for sentence in sentences:
            if (sentence in sentenceValue) and (sentenceValue[sentence] > (1.2 * average)):
                summary += " " + sentence

        return summary
    
    except ZeroDivisionError:
        return "There is no summary available for this website!"

def videoTranscriptSummary(url):
    # We were able to create this code, but we were never able to use it due to time constraints
    vid_id = url.replace("https://www.youtube.com/watch?v=", "")

    summary = YouTubeTranscriptApi.get_transcript(vid_id)

    transcript = ""

    for i in summary:
        transcript += i['text'] + " "

    transcript = summarize(transcript)

    return transcript
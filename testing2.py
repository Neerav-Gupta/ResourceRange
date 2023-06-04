import neededModules as ws 
#These are snippets of code that test out the custom modules we made

output = ws.videoTranscriptSummary("https://www.youtube.com/watch?v=8_KWmzLObQ4")

with open('output.txt', 'w') as f:
    f.write(output)
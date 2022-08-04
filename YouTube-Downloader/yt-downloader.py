from pytube import YouTube
from pytube.cli import on_progress 

print('YT-Downloader')
print('')
print('---------------------------------------------------------------------------------')
print('You can Download every YT-Video what you want in the highest resoultion!')
print('Paste the YouTube Link with STRG + V in this window and you download will starts.')
print('You can see how much time is left with the progress bar')
print('---------------------------------------------------------------------------------')
print('')

items = list(range(0, 57))
l = len(items)


#link question
linkquestion = input("Enter the link:  ")
print('')
yt = YouTube(linkquestion, on_progress_callback=on_progress)

# A list with all items
items = list(range(0, 57))
l = len(items)

#details
print('---------------------------------------------------------------------------------')
print("Title: ",yt.title)
print("Creator: ",yt.author)
print("Views: ",yt.views)
print('---------------------------------------------------------------------------------')

#Getting highest res.
ys = yt.streams.get_highest_resolution()

#download video
ys.download()
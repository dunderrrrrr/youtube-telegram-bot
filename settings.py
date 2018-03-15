#fhbot.py settings

#youtube playlist id (uploads playlist)
#generate from https://www.googleapis.com/youtube/v3/channels?id={CHANNEL ID}&key={API KEY}&part=contentDetails
#copy from items > 0 > contentDetails > relatedPlaylists > uploads (example: "UUboMX_UNgaPBsUOIgasn3-Q")
pid = "" #playlist id

#youtube api key
#generate from https://developers.google.com/youtube/v3/getting-started (step #2)
apikey = ""

#telegram settings
#create token by messaging BotFather (https://telegram.me/BotFather)
t_token = ""
t_url = "https://api.telegram.org/bot"
#telegram group id
t_group = ""

maxvids = 5 #at least 1 - 5 is default (used in apiurl below)

#urls (dont touch)
apiurl = "https://www.googleapis.com/youtube/v3/playlistItems?playlistId={}&key={}&part=snippet&maxResults={}".format(pid, apikey, maxvids)
watchurl = "https://www.youtube.com/watch?v="

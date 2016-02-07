import sys
import time
import telepot
import httplib
import urllib
import json

def handle(msg):
	content_type, chat_type, chat_id = telepot.glance(msg)
	print content_type, chat_type, chat_id

	query_args = {'q':msg['text']}

	MURFIE_API_CONNECTION = httplib.HTTPSConnection('api.murfie.com')
	MURFIE_API_CONNECTION.request('GET', '/albums?%s' % urllib.urlencode(query_args))
	murfie_api_response = MURFIE_API_CONNECTION.getresponse()
	raw_murfie_api_response = murfie_api_response.read()
	try:
		albums = json.loads(raw_murfie_api_response)
		bot.sendMessage(chat_id, 'https://www.murfie.com/albums/%s' % albums['albums'][0]['album']['slug'])
	except:
		bot.sendMessage(chat_id, 'Hmm... I couldn\'t find any albums like that, want to try something else?')

	MURFIE_API_CONNECTION.close()
		

TOKEN = sys.argv[1]

bot = telepot.Bot(TOKEN)
bot.notifyOnMessage(handle)
print 'Listening...'

while 1:
	time.sleep(10)

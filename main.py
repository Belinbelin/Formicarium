BOT_TOKEN = "xoxb-2678547454819-2678572414083-MIbxmHHme6N3MxSuAZt4RMGT"
import sys
import hdc1080
import slack
import time
import logging
import csv



def main():
	while 1:
		#client.chat_postMessage(channel='#fourmillière', text="Hello")
		t = time.localtime()
		current_time = time.strftime("%H:%M:%S", t)
		f.write(current_time + ",data\n")

		time.sleep(3)


if __name__=='__main__':
	client = slack.WebClient(token=BOT_TOKEN)
	f = open('./logger.txt', 'a')
	sys.exit(main())

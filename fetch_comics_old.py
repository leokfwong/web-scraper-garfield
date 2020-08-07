import requests
import time
import random
import datetime
import os 
import sys
import getopt

def fetchComics(start_date, end_date):

	for i in range((start_date - end_date).days):

		date = (start_date - datetime.timedelta(i)).strftime("%Y-%m-%d")

		image = requests.get(f"https://d1ejxu6vysztl5.cloudfront.net/comics/garfield/{date[:4]}/{date}.gif?v=1.1")

		with open("comics/" + date + ".png", "wb") as f:
			f.write(image.content)

		# Generate random pause
		pause = random.randint(5, 13)
		print(f"Saved comic {date}, sleeping for {pause} seconds.")
		time.sleep(pause)

	print("Done.")

if __name__ == "__main__":

	# Get values
	today_date = datetime.datetime.now().date()
	most_recent_date = datetime.datetime.strptime(sorted([x.decode(encoding="UTF-8") for x in os.listdir(os.fsencode("comics"))])[-1][:-4], "%Y-%m-%d").date()

	# Set defaults
	start_date = today_date
	end_date = most_recent_date

	# Fetch command line arguements
	args_list = sys.argv[1:]

	if (len(args_list) > 0):
		options = "s:e:"
		long_options = ["start", "end"]

		try:
			opts, args = getopt.getopt(args_list, options, long_options)
		except getopt.error as err:
			print (str(err))
			sys.exit(2)

	    # evaluate given options
		for opt, arg in opts:
			if opt in ("-s", "--start"):
				print ("Start date: ", arg)
				start_date = datetime.datetime.strptime(arg, "%Y-%m-%d").date()
				if (start_date > today_date):
					print("Start date cannot be in the future.")
					sys.exit()
			elif opt in ("-e", "--end"):
				print ("End date: ", arg)
				end_date = datetime.datetime.strptime(arg, "%Y-%m-%d").date()
			else:
				print("Invalid argument.")

	fetchComics(start_date, end_date)
import requests
import time
import random
import datetime

start_date = datetime.date(2020, 4, 1)

for i in range(22):

	date = (start_date - datetime.timedelta(i)).strftime("%Y-%m-%d")

	image = requests.get(f"https://d1ejxu6vysztl5.cloudfront.net/comics/garfield/{date[:4]}/{date}.gif?v=1.1")

	with open("comics/" + date + ".png", "wb") as f:
		f.write(image.content)

	# Generate random pause
	pause = random.randint(5, 13)
	print(f"Saved comic {date}, sleeping for {pause} seconds.")
	time.sleep(pause)

print("Done.")
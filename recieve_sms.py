import os
import sys
import chatbotAI
from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse

#from xlutils.copy import copy    
#from xlrd import open_workbook

app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])

def sms_reply():
	body = request.values.get('Body', None)
	resp = MessagingResponse()
	print (body)
	bodyArr = body.split(" ")

	if(bodyArr[0] == "app"):
		##add app
		if(len(bodyArr) == 6):
			fname = bodyArr[1]
			lnam = bodyArr[2]
			date = bodyArr[3]
			time = bodyArr[4]
			don = bodyArr[5]
			fullName = fname
			fullName += " "
			fullName += lnam

			#book_ro = open_workbook("C:\Users\Darko\Jupyter Projects\AiChatbot\appointments.xls")
			#book = copy(book_ro)  # creates a writeable copy
			#sheet1 = book.get_sheet(0)  # get a first sheet

		    #sheet1.write(rowx,colx, url)
		    #sheet1.write(rowx,colx+1, count)

			#book.save("C:\Users\Darko\Jupyter Projects\AiChatbot\appointments.xls")


			msg = f"You're appointment has been set {fname}! See you on {date} at {time} {don}!"
			resp.message(msg)

			return str(resp)
		else:
			msg = "Oops! You have entered the wrong format. Please try again."
			resp.message(msg)

			return str(resp)

	if(bodyArr[0] == "info"):
		##add app
		pain = bodyArr[1]
		msg = f"Here's the info for {pain} pain: "

		if(bodyArr[1] == "back"):
			msg += "https://www.whyiexercise.com/back-stretching-exercises.html"
		elif(bodyArr[1] == "knees" or bodyArr[1] == "knee"):
			msg += "https://www.whyiexercise.com/knee-strengthening-exercises.html"
		elif(bodyArr[1] == "shoulder" or bodyArr[1] == "shoulders"):
			msg += "https://www.whyiexercise.com/shoulder-exercises.html"
		elif(bodyArr[1] == "legs" or bodyArr[1] == "leg"):
			msg += "https://teamselecthh.com/home-physical-therapy-exercises-leg-strength/"
		elif(bodyArr[1] == "neck"):
			msg += "https://mayfieldclinic.com/pe-neckex.htm"
		elif (bodyArr[1] == "chest"):
			msg += "https://www.livestrong.com/article/122961-exercises-strengthen-chest-muscles-alleviate/"
		else:
			msg = "Sorry I couldn't find an excersise for that. Maybe try phrasing it a diffirent way."

		resp.message(msg)

		return str(resp)



	msg = chatbotAI.chat(str(body))
	resp.message(msg)

	return str(resp)


if __name__ == '__main__':
	app.run()
# Using flask to make an api 
# import necessary libraries and functions 
from flask import Flask, jsonify, request 
from pytube import YouTube
# creating a Flask app 
app = Flask(__name__) 

# on the terminal type: curl http://127.0.0.1:5000/ 
# returns hello world when we use GET. 
# returns the data that we send when we use POST. 
@app.route('/', methods = ['GET', 'POST']) 
def home(): 
    if(request.method == 'GET'): 

        data = "nothing here"
        return jsonify({'data': data}) 


# A simple function to calculate the square of a number 
# the number to be squared is sent in the URL when we use GET 
# on the terminal type: curl http://127.0.0.1:5000 / home / 10 
# this returns 100 (square of 10) 
@app.route('/audio', methods = ['GET']) 
def disp(): 
  
  link = request.args.get('link')
  yt = YouTube(link)
  audio_stream = yt.streams.filter(only_audio=True).first()
  if audio_stream:
    return jsonify({'link': audio_stream.url})  
  else:
    return "No audio stream found for this video."
    


# driver function 
if __name__ == '__main__': 

    app.run(debug = True) 

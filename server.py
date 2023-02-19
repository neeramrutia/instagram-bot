from flask import Flask, request, render_template
from insta import InstaFollower
from sheet import createsheet
app = Flask(__name__,template_folder='/home/neer/Desktop/testing/templates/',static_folder='/home/neer/Desktop/testing/static/')
chrome_driver_path = '/usr/bin/chromedriver'
# username=''

# email=''
@app.route('/')
def index():
  return render_template('index.html')

@app.route('/my-link/' , methods=["GET", "POST"])
def my_link():
  if request.method=='GET':
      email=request.form.get('email')
      username=request.form.get("user",default='tester2053')
      print(username)
      password=request.form.get("pass",default='testingaccount')
      print(password)
      
      bot = InstaFollower(chrome_driver_path,username,password)
      bot.login()
      bot.find_followers()
      bot.follow()    
      bot.unfollow()
  return render_template('index.html')  

  
@app.route('/my-link1/' , methods=["GET","POST"]) 
def my_link1():   
  if request.method=='GET':  
      email=request.form.get("email")
      username=request.form.get("username" , default='tester2053')
      password=request.form.get("password" , default='testingaccount')
      bot = InstaFollower(chrome_driver_path,username,password)
      bot.login()
      bot.sendmessage()
      # return render_template('index.html')
  return render_template('index.html')      

@app.route('/my-link2/',methods=["GET" , "POST"])
def my_link2():
  if request.method=='GET':
      email=request.form.get("email" ,default='neer.amrutia@gmail.com')
      username=request.form.get("username" , default='tester2053')
      password=request.form.get("password" , default='testingaccount')
      bot = InstaFollower(chrome_driver_path,username,password)
      bot.login()
      bot.followerlist()
      bot.followinglist()
      bot.createcsv()
      cs=createsheet()
      cs.sheets(email)
      bot.erasecsvdata()
  return render_template('index.html')

if __name__ == '__main__':
  app.run(debug=True)

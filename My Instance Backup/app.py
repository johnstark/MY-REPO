import os
from passlib.hash  import sha256_crypt
from flask import *
from functools import wraps
from flask.ext.mysqldb import MySQL
from werkzeug import secure_filename
import boto
from boto.s3.key import Key
import os

mysql = MySQL()

app = Flask(__name__)

#cnx = mysql.connector.connect(MYSQL_HOST='localhost',MYSQL_USER='root',MYSQL_PASSWORD='root',MYSQL_DB='demo')

app.config['MYSQL_HOST'] = 'vasanth-test-dbinstance.ckdqzljpe2py.us-east-1.rds.amazonaws.com'
app.config['MYSQL_USER'] = 'vasanthakumar'
app.config['MYSQL_PASSWORD'] = 'vasanthakumar'
app.config['MYSQL_DB'] = 'REDVISION'

mysql.init_app(app)



app.secret_key = "myflaskapp"

#app.database = "login.db"

vid_dir = 'static/videos/'

app.config['UPLOAD_FOLDER'] = 'static/videos/'

app.config['ALLOWED_EXTENSIONS'] = set(['mp4'])

def login_required(f):
	@wraps(f)
	def wrap(*args,**kwargs):
		if 'Logged_in' in session:
			return f(*args,**kwargs)
		else:
			flash('Session expired.You need to login first.')
			return render_template('welcome.html')
	return wrap




@app.route('/')
def home():
	return render_template('welcome.html')




@app.route('/check',methods=['GET','POST'])
def check():
	if request.method == 'POST':
		entered_passw = request.form['passw']
		entered_name = request.form['uname']
		#g.db = connect_db()
		#cur = g.db.execute('select * from logs')
		cur = mysql.connection.cursor()
		cur.execute("select * from datas where username = '" +entered_name+ "'")
		data = cur.fetchall()
		for row in data:
			if row[0] == entered_name and (sha256_crypt.verify(entered_passw,row[1])):
				return render_template('upload.html')
			else:
				errors='Invalid Credentials.Please try again'
				return render_template('welcome.html',errors=errors)

		
		



@app.route('/upload_page')
def upload_page():
	return render_template('upload.html')


@app.route('/contact_us')
def contact_us():
	return render_template('contact_us.html')



@app.route('/register',methods=['GET','POST'])
def register():
	if request.method == 'POST':
		entered_passw = request.form['passw']
		entered_name = request.form['uname']
		hash_obj = sha256_crypt.encrypt(entered_passw)
		print hash_obj
		#g.db = connect_db()
		#cur = g.db.execute('select * from logs')
		cur = mysql.connection.cursor()
		cur.execute("select username from datas where username = '" +entered_name+ "'")
		data = cur.fetchone()
		print data
		if data == None:
			cur.execute("insert into datas values(%s,%s)",(entered_name,hash_obj))
			mysql.connection.commit()
			return render_template('index.html')
		else:
			u_errors = 'Username already exits.Please choose a different one.'
			return render_template('welcome.html',u_errors=u_errors)	
		#if row[0] == entered_name:
		#		u_errors = 'Username already exits.Please choose a different one.'
		#		return render_template('welcome.html',u_errors=u_errors)	
		#	else:
		#		cur.execute("insert into logs values(%s,%s)",(entered_name,hash_obj))
		#		mysql.connection.commit()
		#		return redirect(url_for('video'))

		#g.db.close()






@app.route('/video',methods=['GET','POST'])
def video():
	
	files = [f for f in os.listdir(vid_dir) if f.endswith('mp4')]
	files_len  = len(files)
	files1 = [f for f in os.listdir(vid_dir1) if f.endswith('mp4')]
	files_len1  = len(files1)
	files2 = [f for f in os.listdir(vid_dir2) if f.endswith('mp4')]
	files_len2  = len(files2)
	files3 = [f for f in os.listdir(vid_dir3) if f.endswith('mp4')]
	files_len3  = len(files3)
	files4 = [f for f in os.listdir(vid_dir4) if f.endswith('mp4')]
	files_len4  = len(files4)
	files5 = [f for f in os.listdir(vid_dir5) if f.endswith('mp4')]
	files_len5  = len(files5)
	
	return render_template('index.html',files=files,files_len=files_len,files1=files1,files_len1=files_len1,files2=files2,files_len2=files_len2,files3=files3,files_len3=files_len3,files4=files4,files_len4=files_len4,files5=files5,files_len5=files_len5)




@app.route('/selected_files',methods=['GET','POST'])
def selected_files():
	if request.form == 'POST':
		return render_template('welcome.html')




def allowed_file(filename):
	return '.' in filename and \
		   filename.rsplit('.',1)[1] in app.config['ALLOWED_EXTENSIONS']





@app.route('/upload_file',methods=['POST'])
def upload_file():
		file = request.files['file']
		if file and allowed_file(file.filename):
			filename = secure_filename(file.filename)
			file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
			message = 'Your video has been uploaded successfully'
			files = [f for f in os.listdir(vid_dir) if f.endswith('mp4')]
			files_len  = len(files)
			return render_template('index.html',message=message,files=files,files_len=files_len,files1=files1,files_len1=files_len1,files2=files2,files_len2=files_len2,files3=files3,files_len3=files_len3,files4=files4,files_len4=files_len4,files5=files5,files_len5=files_len5)


@app.route('/upload_file_s3',methods=['GET','POST'])
def upload_file_s3():
	if request.method == 'POST':
		file = request.files['file']
		c = boto.connect_s3()
		b = c.get_bucket('vasanths3-project')
		k = Key(b)
		k.key = file.filename
		k.set_contents_from_file(file)
		return "uploaded"
	return "method out"

@app.route('/index')
def index():
	files=[]
	AWS_KEY = 'AKIAJTV4LXLCT2EJADXA'
    AWS_SECRET = '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'
    aws_connection = s3connection(AWS_KEY,AWS_SECRET)
    bucket = aws_connection.get_bucket('vasanths3-project')
    for f in bucket.list():
    	res = str(f.key)
    	files.append(res)
    	file_len = len(files)
    	return render_template('index.html',files=files,files_len=files_len)
    	


@app.route('/login_again')
def login_again():
	return render_template('logout.html')


@app.route('/services')
def services():
	return render_template('services.html')

@app.route('/login')
def login():
	return render_template('login.html')

#def connect_db():
#	return sqlite3.connect(app.database)




if __name__ == ('__main__'):
	app.run(debug=True)
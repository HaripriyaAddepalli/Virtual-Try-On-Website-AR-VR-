from flask import Flask, render_template, request, redirect, url_for, flash, session, send_from_directory
import sqlite3
import os
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a secure secret key
UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Database setup
def init_db():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        );
    ''')
    conn.commit()
    conn.close()

# Initialize the database
init_db()

# Helper function to check allowed file extensions
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Route for the home page
@app.route('/')
def home():
    return render_template('home.html')

# Route for the signup page
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        name = request.form['name']

        hashed_password = generate_password_hash(password)  # Properly hash the password

        try:
            with sqlite3.connect('users.db') as conn:
                cursor = conn.cursor()
                cursor.execute('INSERT INTO users (name, email, username, password) VALUES (?, ?, ?, ?)',
                               (name, email, username, hashed_password))
                conn.commit()
                flash('Registration successful! Please log in.', 'success')
                return redirect(url_for('login'))
        except sqlite3.IntegrityError:
            flash('Username or email already exists. Please choose a different one.', 'danger')

    return render_template('signup.html')

# Route for the login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        try:
            with sqlite3.connect('users.db') as conn:
                cursor = conn.cursor()
                cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
                user = cursor.fetchone()
                if user and (user[4]== password):  # Properly check the password hash
                    print("hiiiiiiiiiiiii")     
                    session['username'] = user[2]
                    flash('Login successful!', 'success')
                    return redirect(url_for('dashboard'))
                else:
                    flash('Invalid username or password. Please try again.', 'danger')
        except sqlite3.IntegrityError:
            flash('Error occurred. Please try again later.', 'danger')

    return render_template('login.html')

# Route for the dashboard page
@app.route('/dashboard')
def dashboard():
    if 'username' in session:
        return render_template("dashboard.html")
    else:
        flash('You are not logged in. Please log in first.', 'danger')
        return redirect(url_for('login'))

# Route to log out
@app.route('/logout')
def logout():
    session.pop('username', None)
    flash('You have been logged out.', 'info')
    return redirect(url_for('login'))

# Route for the tryon page
@app.route('/tryon', methods=['GET', 'POST'])
def tryon():
    # if 'username' in session:
        # filename = request.args.get('filename')
        # category = request.args.get('category')
        # products = []

        # if request.method == 'POST':
        #     # Handle image upload
        #     if 'image' in request.files:
        #         image = request.files['image']
        #         if image and allowed_file(image.filename):
        #             filename = secure_filename(image.filename)
        #             image.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        #             flash('Image uploaded successfully.', 'success')
        #             return redirect(url_for('tryon', filename=filename))

        #     # Handle category selection
        #     elif 'category' in request.form:
        #         category = request.form['category']
        #         return redirect(url_for('tryon', filename=filename, category=category))

        # # Load products based on the selected category
        # product_data = {
        #     'men': [
        #         {'name': "Men's T-Shirt 1", 'image': 'references/men/shirt1.png'},
        #         {'name': "Men's T-Shirt 2", 'image': 'references/men/shirt2.png'},
        #         {'name': "Men's T-Shirt 3", 'image': 'references/men/shirt3.png'},
        #     ],
        #     'women': [
        #         {'name': "Women's Dress 1", 'image': 'references/women/dress1.png'},
        #         {'name': "Women's Dress 2", 'image': 'references/women/dress2.png'},
        #     ],
        #     'kids': [
        #         {'name': "Kid's T-Shirt 1", 'image': 'references/kids/shirt1.png'},
        #         {'name': "Kid's T-Shirt 2", 'image': 'references/kids/shirt2.png'},
        #     ],
        # }
        # products = product_data.get(category, [])

        # return render_template('tryon.html', filename=filename, category=category, products=products)
    # else:
    #     flash('You are not logged in. Please log in first.', 'danger')
        # return redirect(url_for('login'))
    return redirect("https://huggingface.co/spaces/Kwai-Kolors/Kolors-Virtual-Try-On")
# Route to process product selection via AJAX
@app.route('/tryon/process_product', methods=['POST'])
def process_product():
    if 'username' in session:
        data = request.json
        product_image = data.get('product')
        uploaded_image_path = data.get('uploadedImagePath')
        print(product_image, uploaded_image_path)
        if product_image and uploaded_image_path:
            # Handle the selected product image and uploaded image path
            print("Product Image Path:", product_image)
            print("Uploaded Image Path:", uploaded_image_path)
            return {'message': 'Product selected successfully!'}, 200
        else:
            return {'message': 'Incomplete data.'}, 400
    else:
        return {'message': 'You are not logged in.'}, 403


# Serve uploaded files
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    app.run(debug=True)

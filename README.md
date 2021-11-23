# Final project Python
 ### Installation 
Download server.py file from src/ to your project folder
###  Usage
First of all you need to change the following row based on your postgresql settings
``` python

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://<username>:<password>@localhost:<port>/<db_name>"

```
Then you need to run local server by running server.py from your IDE or from command line using the following command(do not forget to install required packages in your virtual environment):
``` python

python server.py

```
Now you can open your browser to create a login, password and send requests:
- route /login

After you create or log in to your account. A page with text input and a button will appear. Just enter the correct name of the coin, and then wait a little (or more) while the analyzer looks through the articles and summarizes the results. The next time you enter the same coin, you don't have to wait because it takes the saved articles from the database.

### Examples
Enter the name of the coin
![Screenshot 2021-11-07 183802](https://user-images.githubusercontent.com/74852501/140645619-678e2d61-a3ef-4ae5-9339-fcd9b72641e0.png)

Then wait a little
![Screenshot 2021-11-07 185134](https://user-images.githubusercontent.com/74852501/140645673-b957c38f-a674-4275-a5b5-300d210a4ba3.png)


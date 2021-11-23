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
Now you can open your browser to create an account or you already have then log in and send requests:
- route /login

After you create or log in to your account. A page with text input and a button will appear. Just enter the correct name of the coin, and then wait a little (or more) while the analyzer looks through the articles and summarizes the results. The next time you enter the same coin, you don't have to wait because it takes the saved articles from the database.

### Examples
Login
![login](https://user-images.githubusercontent.com/74852501/143067880-7f2b1d95-7cf0-45f2-a16b-b687f3562a85.png)

If you don't have an account register
![sign_up](https://user-images.githubusercontent.com/74852501/143067939-bdfb9f7d-0494-4965-9bb4-09fa3a1421ca.png)

Enter the name of the coin
![coin_name](https://user-images.githubusercontent.com/74852501/143068080-2b329834-f004-46fd-bd8f-7ad7066e8362.png)

Then wait a little(or more)
![search](https://user-images.githubusercontent.com/74852501/143068203-4f1cc8b9-d5a8-4e9e-b574-c157504693ca.png)

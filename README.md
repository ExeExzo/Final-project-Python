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
Now you can open your browser or requests making program and make requests:
- route /coin

A page with text input and a button will show up. Just type coin name correctly and then wait for a little while the parser is looking through articles. The next time you input the same coin, you do not need to wait, because it takes saved articles from the database.

### Examples
Enter the name of the coin
![Screenshot 2021-11-07 183802](https://user-images.githubusercontent.com/74852501/140645619-678e2d61-a3ef-4ae5-9339-fcd9b72641e0.png)

Then wait a little
![Screenshot 2021-11-07 185134](https://user-images.githubusercontent.com/74852501/140645673-b957c38f-a674-4275-a5b5-300d210a4ba3.png)


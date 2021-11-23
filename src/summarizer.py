from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from transformers import pipeline
from bs4 import BeautifulSoup
import requests

class Summarizer:
    def __init__(self):
        self.summarizer = pipeline("summarization") 
        options = webdriver.ChromeOptions()
        options.add_argument("--window-size=1920,1080")
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--incognito')
        options.add_argument('--headless')
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)
        
    def summarize(self, URL):
    # summarizer = pipeline("summarization")
    # URL = "https://towardsdatascience.com/a-bayesian-take-on-model-regularization-9356116b6457"
    # URL = "https://hackernoon.com/will-the-game-stop-with-gamestop-or-is-this-just-the-beginning-2j1x32aa"

        #r = requests.get(URL)
        self.driver.get(URL)

        soup = BeautifulSoup(self.driver.page_source, 'html.parser')
        results = soup.find_all(['h1', 'p'])
        text = [result.text for result in results]
        ARTICLE = ' '.join(text)

        max_chunk = 500

        ARTICLE = ARTICLE.replace('.', '.<eos>')
        ARTICLE = ARTICLE.replace('?', '?<eos>')
        ARTICLE = ARTICLE.replace('!', '!<eos>')

        sentences = ARTICLE.split('<eos>')
        current_chunk = 0 
        chunks = []
        for sentence in sentences:
            if len(chunks) == current_chunk + 1: 
                if len(chunks[current_chunk]) + len(sentence.split(' ')) <= max_chunk:
                    chunks[current_chunk].extend(sentence.split(' '))
                else:
                    current_chunk += 1
                    chunks.append(sentence.split(' '))
            else:
                chunks.append(sentence.split(' '))

        for chunk_id in range(len(chunks)):
            chunks[chunk_id] = ' '.join(chunks[chunk_id])

        res = self.summarizer(chunks, max_length=120, min_length=30, do_sample=False)

        text = ' '.join([summ['summary_text'] for summ in res])
        return text



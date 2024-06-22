import os
import requests
from bs4 import BeautifulSoup as bs

data_dir = os.path.join(os.path.dirname(__file__), '..', 'Data')
url = "https://iuhoosiers.com/sports/2015/6/26/MBB_Season_Stats"
debugged_url = 'https://s3.us-east-2.amazonaws.com/sidearm.nextgen.sites/iuhoosiers.com'
os.makedirs(data_dir, exist_ok=True)

def extract_data():
    response = requests.get(url)
    soup = bs(response.text, 'html.parser')
    links = soup.find_all('a')

    i = 0
    for link in links:
        if '.pdf' in link.get('href', []):
            pdf_url = debugged_url + link.get('href')
            response = requests.get(pdf_url)
            
            if str(response) != '<Response [200]>':  response = requests.get(link.get('href'))
            pdf_path = os.path.join(data_dir, f'PDF{i}.pdf')
            
            with open(pdf_path, 'wb') as pdf:
                pdf.write(response.content)
            
            # For debugging request state, uncomment below line
            # print(f"File {pdf_path} downloaded")
            i += 1


if __name__ == '__main__':
    extract_data()

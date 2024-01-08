
import requests
from bs4 import BeautifulSoup

def get_google_scholar_results(query, num_results=5):
    base_url = "https://scholar.google.com/scholar"
    params = {
        "q": query,
        "num": num_results
    }

    response = requests.get(base_url, params=params)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        results = soup.find_all('h3', class_='gs_rt')
        sites = []
        for idx, result in enumerate(results[:num_results]):
            title = result.a.text
            link = result.a['href']
            
            sites.append(link)
        return sites
            
      

    else:
        print(f"Error: Unable to retrieve results. Status code: {response.status_code}")
        #return None

# Example usage

def scrapesites(query, name):
    sitelist = get_google_scholar_results(query, num_results=5)

    with open(name + ".txt", "w", encoding="utf-8") as outfile:
        for url in sitelist:
            response = requests.get(url)

            if response.status_code == 200:
                print("found: " + url)
                # Parse the HTML content using BeautifulSoup
                soup = BeautifulSoup(response.text, 'html.parser')

                # Extract and write the text from paragraphs to the file
                paragraphs = soup.find_all('p')
                for paragraph in paragraphs:
                    outfile.write( paragraph.text + "\n")

            else:
                print(f"Error: Unable to fetch the content from {url}. Status code: {response.status_code}")




    
    
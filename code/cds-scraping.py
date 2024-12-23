import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

universities = {
    "Princeton": "https://ir.princeton.edu/other-university-data/common-data-set",
    "Harvard": "https://oira.harvard.edu/common-data-set/",
    "Stanford": "https://ucomm.stanford.edu/cds/",
    "Yale": "https://oir.yale.edu/common-data-set",
    "Caltech": "https://finance.caltech.edu/Resources/cds",
    "Duke": "https://provost.duke.edu/administrative-resources/institutional-research/",
    "Johns Hopkins": "https://oira.jhu.edu/",
    "Northwestern": "https://enrollment.northwestern.edu/data/common-data-set.html",
    "UPenn": "https://ira.upenn.edu/penn-numbers/common-data-set",
    "Cornell": "https://irp.dpb.cornell.edu/common-data-set",
    "Chicago": "https://data.uchicago.edu/common-data-set/",
    "Brown": "https://oir.brown.edu/institutional-data/common-data-set",
    "Columbia": "https://opir.columbia.edu/cds",
    "Dartmouth": "https://www.dartmouth.edu/oir/data-reporting/cds/index.html",
    "UCLA": "https://apb.ucla.edu/campus-statistics/common-data-set",
    "Berkeley": "https://opa.berkeley.edu/campus-data/common-data-set",
    "Rice": "https://oie.rice.edu/common-data-set",
    "Notre Dame": "https://iris.nd.edu/institutional-research/common-data-set-cds/",
    "Carnegie Mellon": "https://www.cmu.edu/ira/CDS/index.html",
    "Michigan": "https://obp.umich.edu/campus-statistics/common-data-set/",
}

years = ["2021", "2022", "2023", "2024"]

save_path = "../data/cds/"

os.makedirs(save_path, exist_ok = True)

def download_pdf(url, file_name):
    try:
        response = requests.get(url)
        response.raise_for_status()
        with open(file_name, "wb") as f:
            f.write(response.content)
        print(f"Downloaded: {file_name}")
    except requests.exceptions.RequestException as e:
        print(f"Failed to download {url}: {e}")

for university, url in universities.items():
    print(f"Processing {university}...")

    try:
        # Fetch the university page
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")

        # Find all links to PDFs on the page
        pdf_links = [a['href'] for a in soup.find_all('a', href=True) if a['href'].endswith('.pdf')]

        # Filter links by year and download the relevant files
        for year in years:
            for pdf_link in pdf_links:
                if year in pdf_link:
                    pdf_url = urljoin(url, pdf_link)
                    file_name = os.path.join(save_path, f"{university}_{year}_CDS.pdf")
                    download_pdf(pdf_url, file_name)

    except requests.exceptions.RequestException as e:
        print(f"Failed to access {url} for {university}: {e}")
        
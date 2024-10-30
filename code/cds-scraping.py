import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

universities = {
    "Princeton University": "https://ir.princeton.edu/other-university-data/common-data-set",
    "Harvard University": "https://oira.harvard.edu/common-data-set/",
    "Stanford University": "https://ucomm.stanford.edu/cds/",
    "Yale University": "https://oir.yale.edu/common-data-set",
    "California Institute of Technology": "https://finance.caltech.edu/Resources/cds",
    "Duke University": "https://provost.duke.edu/administrative-resources/institutional-research/",
    "Johns Hopkins University": "https://oira.jhu.edu/",
    "Northwestern University": "https://enrollment.northwestern.edu/data/common-data-set.html",
    "University of Pennsylvania": "https://ira.upenn.edu/penn-numbers/common-data-set",
    "Cornell University": "https://irp.dpb.cornell.edu/common-data-set",
    "University of Chicago": "https://data.uchicago.edu/common-data-set/",
    "Brown University": "https://oir.brown.edu/institutional-data/common-data-set",
    "Columbia University": "https://opir.columbia.edu/cds",
    "Dartmouth College": "https://www.dartmouth.edu/oir/data-reporting/cds/index.html",
    "University of California, Los Angeles": "https://apb.ucla.edu/campus-statistics/common-data-set",
    "University of California, Berkeley": "https://opa.berkeley.edu/campus-data/common-data-set",
    "Rice University": "https://oie.rice.edu/common-data-set",
    "University of Notre Dame": "https://iris.nd.edu/institutional-research/common-data-set-cds/",
    "Carnegie Mellon University": "https://www.cmu.edu/ira/CDS/index.html",
    "University of Michigan": "https://obp.umich.edu/campus-statistics/common-data-set/",
}


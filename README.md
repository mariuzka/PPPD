# PPPD

The purpose of this project is mainly to scrape press releases from [Presseportal-Blaulicht](https://www.presseportal.de/blaulicht/), extract the relevant data and save it as datasets.



## Installation
1. Clone this repository using git.
2. Install the conda environment from the file "env.yaml".

## Usage

The simplest way of scraping press releases from [Presseportal-Blaulicht](https://www.presseportal.de/blaulicht/) is to use the function **get_blaulicht_data()** from the module **ppRunner**. This function downloads and processes every press release from every newsroom for given federal states and years of interest.



```python
from src import ppRunner as ppr

ppr.get_blaulicht_data(
    states="baden-württemberg",                         
    years=2020,                                         
    dept_type="police",
    output_folder_name="ppp_bw_crime_and_elections",
)
```

```python
from src import ppRunner as ppr

ppr.get_blaulicht_data(
    states=["baden-württemberg", "hessen", "niedersachesen"],                         
    years=[2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021],                                         
    dept_type="police",
    output_folder_name="ppp_bw_crime_and_elections",
)
```

# PPPD

The purpose of this project is mainly to scrape press releases from [Presseportal-Blaulicht](https://www.presseportal.de/blaulicht/), extract the relevant data and save it as datasets.



## Installation
1. Clone this repository using git.
2. Install the conda environment from the file "env.yaml".

## Usage

The simplest way of scraping press releases from [Presseportal-Blaulicht](https://www.presseportal.de/blaulicht/) is to use the function **get_blaulicht_data()** from the module **ppRunner**. This function downloads and processes every press release from every newsroom in the given federal states and years of interest.

In the following example, the function is used to download all press releases from 2020 (years=2020) posted by police departments (dept_type="police") in Baden-Württemberg (states="baden-württemberg"). A folder named "ppp_bw_crime_and_elections" (output_folder_name="ppp_bw_crime_and_elections") will be created within the project folder and all data will be stored in it.

```python
from src import ppRunner as ppr

ppr.get_blaulicht_data(
    states="baden-württemberg",                         
    years=2020,                                         
    dept_type="police",
    output_folder_name="ppp_bw",
)
```

The arguments *states* and *years* can both be either a single value or a list of values. In the following example multiple federal states and multiple years are given. Caution: the execution of the code below may take a few days.

```python
from src import ppRunner as ppr

ppr.get_blaulicht_data(
    states=["baden-württemberg", "hessen", "niedersachesen"],                         
    years=[2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021],                                         
    dept_type="police",
    output_folder_name="example_project",
)
```


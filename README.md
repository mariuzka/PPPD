# PPPD

The purpose of **PPPD** (**P**rojekt-**P**olizei-**P**resse-**D**aten) is mainly to scrape press releases from [Presseportal-Blaulicht](https://www.presseportal.de/blaulicht/) and extract the relevant data to use it in research projects.


## Installation
1. Clone/download this repository.
2. Populate `config.ini` (see [`config.ini[EXAMPLE]`](config.ini[EXAMPLE]), use `DEVEL_MODE=True` to toggle the webscraping to a small subset as proof of concept).
3. Install the conda environment from the file "env.yaml".



## Usage

The simplest way of scraping press releases from [Presseportal-Blaulicht](https://www.presseportal.de/blaulicht/) is to use the function `get_blaulicht_data()` from the module `ppRunner`. This function downloads and processes every press release from every newsroom in the given federal states and years of interest.

In the following example, the function is used to download all press releases from 2020 (years=2020) posted by police departments (dept_type="police") in Baden-Württemberg (states="baden-württemberg"). A folder named "ppp_bw" (output_folder_name="ppp_bw") will be created within the project folder and all data will be stored in it.

```python
from src import ppRunner as ppr

ppr.get_blaulicht_data(
    states="baden-württemberg",                         
    years=2020,                                         
    dept_type="police",
    output_folder_name="ppp_bw",
)
```


**Multiple states and years at once**

The arguments *states* and *years* can both be either a single value or a list of values. In the following example, multiple federal states and multiple years are specified. Caution: The execution of the code below may take a few days.

```python
from src import ppRunner as ppr

ppr.get_blaulicht_data(
    states=["baden-württemberg", "hessen", "niedersachsen"],                         
    years=[2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021],                                         
    dept_type="police",
    output_folder_name="example_project",
)
```


**Update an existing output folder**

... 

## Database usage (work in progress)

If you want to use PostgreSQL as database, fire up a docker environment e.g. as provided in the `docker-compose.yml`: 

```sh 
sudo docker-compose -f docker-compose.yml --env-file config.ini up -d
```  

Don't forget to provide the credentials within the `config.ini`.

To import legacy data (from csv and txt files from the initial webscraping) rund script `01-load_basic_data.py` from the folder `scripts/init_db`. It creates the database and fills the tables (takes ~5-10 minutes).

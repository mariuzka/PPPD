# PPPD

The purpose of this project is mainly to scrape press releases from presseportal.de/blaulicht, extract the relevant data and save it as datasets.



## Installation
1. Clone this repository using git.
2. Install the conda environment from the file "env.yaml".

## Usage

```python
from src import ppRunnerFunctions as ppr

ppr.get_blaulicht_data(
    states="baden-württemberg",
    years=2020,
    dept_type="police",
    output_folder_name="ppp_bw_crime_and_elections",
)
```

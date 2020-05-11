To save lives from the plague, one must have the capacity to foresee and to forestall. Yet tracking the current situation has been notoriously difficult.
Based on our experience in studying China outbreak, there are several basic data sets required to fit the macro puzzle together, which are

- Number of patients (tested ill, recover, death) to deduce the constant in the basic epidemic model.
- Detailed patient travel information to reproduce the transmission process.
- The network of social connections to address the likelihood of transmission. (e.g. in a global level, an economic dependence index could be used to address the connection between countries)
- Time and quality of social-distancing control.
- The available number of testing and the nature of testing.
- Availability of hospital resources.
- All variables that can address the demography or level of public governance.

Those datasets are not available for all localities, and many of them don't have quality control or have a vague definition thus make it impossible to make a cross-border comparison.

We already have transparancy in some regions of the world. The African union (AU) and the European union (EU) publish the pandemic data for every countries everyday. Many European countries publish the detailed data of state/city level. However, it takes hours coding to merge them together. see [repo](https://github.com/covid19-eu-zh/covid19-eu-data) here. it's worth noticing that even between OECD countries, the level of information disclosure between countries varies. Not to mention other countries that has more diverged economic or social nature.

However, some crowd-sourcing/self-organizing research groups has managed to form some of the datasets in several places. Including the famous [covid-tracking project](https://covidtracking.com/) and [JHU dashboard](http://gisanddata.maps.arcgis.com/apps/opsdashboard/index.html) in the US.

Here we present some datasets available for research. Though many of them are not our best recommendation but are the best in the public space.
We hope to work under the licence that anyone working with the facilitate of this project agrees to make his/her own data public the time his/her work get published. Also, feel free to open issues for adding/make adjustment to data resources.

## Data Resources by Regions
**For each country, we usually have two levels of data. The data of province/state level is more abundant**

### World
- Number of Patients: [JHU Data](https://github.com/CSSEGISandData/COVID-19)
- Detailed Patient Data: Not applicable
- Transmission: Not applicable. Paid data resource: IATA
- Social-distancing control: [COVID19-Intervention](https://covid19-interventions.com/) [Oxford Project](http://epidemicforecasting.org/containment), [Google Mobility](https://www.google.com/covid19/mobility/), [School Closure UNESCO](https://data.humdata.org/dataset/global-school-closures-covid19), [Travel Restriction IATA](https://data.humdata.org/dataset/travel-restiction-monitoring-iata-covid-19-iom-dtm)
- Number of testing: [Our World in Data](https://data.humdata.org/dataset/total-covid-19-tests-performed-by-country)
- Availability of hospital resources: WHO
- Demography/Public governance: UN, [World Bank](https://data.humdata.org/dataset/world-bank-indicators-of-interest-to-the-covid-19-outbreak)

### China
Two Levels: Province, City
- Number of Patients: [Daily](https://github.com/Glacier-Ice/COVID-19-2019-nCoV-Infection-Data-cleaning-), [Hourly](https://github.com/BlankerL/DXY-COVID-19-Data/blob/master/README.en.md)
- Detailed Patient Data [Paper](https://www.nature.com/articles/s41597-020-0448-0) [Data](https://github.com/beoutbreakprepared/nCoV2019/tree/master/latest_data)
- Transmission: Baidu Migration Index archieved by [Harvard](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/FAEZIO)
- Social-distancing control: Not applicable
- Number of testing: Not applicable
- Availability of hospital resources: City Level available, Hospital Level [Paid Data](https://db.yaozh.com/hmap?p=4&pageSize=20)
- Demography & Public governance: City level available
- Others: [News](https://github.com/chinatimeline/chinatimeline.github.io)

### The United States
Two Levels: State, County
- Number of Patients: [JHU](https://github.com/CSSEGISandData/COVID-19), [NY Times](https://github.com/nytimes/covid-19-data): worth noticing that looks like JHU does not verify data by themselves.
- Detailed Patient Data: [Paper](https://www.nature.com/articles/s41597-020-0448-0) [Data](https://github.com/beoutbreakprepared/nCoV2019/tree/master/latest_data)
- Transmission: Not applicable
- Social-distancing control: [School Closure](https://www.kaggle.com/jaimeblasco/coronavirus-and-school-closures)
- Number of testing: [covid-tracking project](https://covidtracking.com/)
- Availability of hospital resources: [ICU Beds from KNN](https://khn.org/news/as-coronavirus-spreads-widely-millions-of-older-americans-live-in-counties-with-no-icu-beds/#lookup), [Beds on AWS](https://aws.amazon.com/marketplace/pp/prodview-yivxd2owkloha?qid=1585241268884&sr=0-8&ref_=srh_res_product_title#overview)
- Demography & Public governance: [COVID-19_US_County-level_Summaries Project by UCB & Kaggle](https://github.com/JieYingWu/COVID-19_US_County-level_Summaries)
- Others: [News Media](https://github.com/narcisoyu/Institutional-and-news-media-tweet-dataset-for-COVID-19-social-science-research), [Twitter](https://github.com/thepanacealab/covid19_twitter)

### Europe
Two Levels: Country, Province
- Number of Patients: [Covid-19-eu](https://github.com/covid19-eu-zh/covid19-eu-data/tree/master/dataset) 
- Detailed Patient Data: Not applicable
- Transmission: Not applicable
- Social-distancing control: Not applicable
- Number of testing: Not applicable
- Availability of hospital resources: Not applicable
- Demography/Public governance: Not applicable
- Others: Not applicable

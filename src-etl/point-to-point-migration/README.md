# Point to point migration data

## Programmatic Usage
```
python integration.py # get baidu data
mv db-config.json.example db-config.json # modify the db config
export CONFIG_PATH=$(cat db-config.json) 
python main.py # put the data into db
```

The `get_p2p_overall_dataframe` in [integration.py](integration.py) receives a list of dates in the format `%Y%M%d`, e.g. `20200215`, and returns a pandas DataFrame of the point to point migration data.

Due to the TTL of the data source, only data within one month is available.

Example usage can be found at the `if __name__=="__main__"` part in [integration.py](integration.py), the output of which is

```text
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 7756 entries, 0 to 7755
Data columns (total 6 columns):
 #   Column           Non-Null Count  Dtype
---  ------           --------------  -----
 0   date             7756 non-null   object
 1   from             7756 non-null   object
 2   to               7756 non-null   object
 3   to_province      7756 non-null   object
 4   percentage       7756 non-null   float64
 5   migration_index  7756 non-null   float64
dtypes: float64(2), object(4)
memory usage: 363.7+ KB
       date from   to to_province  percentage  migration_index
0  20200215  北京市   廊坊         河北省       15.73         1.539648
1  20200215  北京市   保定         河北省        6.95         1.539648
2  20200215  北京市  张家口         河北省        4.28         1.539648
3  20200215  北京市   天津         天津市        4.26         1.539648
4  20200215  北京市   邯郸         河北省        3.19         1.539648
5  20200215  北京市  石家庄         河北省        2.30         1.539648
6  20200215  北京市   邢台         河北省        1.70         1.539648
7  20200215  北京市   承德         河北省        1.39         1.539648
8  20200215  北京市   衡水         河北省        1.36         1.539648
9  20200215  北京市   临汾         山西省        1.34         1.539648
```

## Date utilities

The [`dateutils` module](dateutils.py) provides useful date utilities.

```python
from dateutils import today, yesterday, all_dates_since_last_month
```

In the data backtracking, all data in the last month is wanted. You can call

```python
get_p2p_overall_dataframe(
    all_dates_since_last_month(today())
)
```

After that, in daily update, you can call

```python
get_p2p_overall_dataframe([yesterday()])

# or
get_p2p_overall_dataframe() # as [yesterday()] is set as default
```

## Running as a Daily Cronjob Script

`cd` to `src-etl/point-to-point-migration`, and run

```bash
$ python main.py
```

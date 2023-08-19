import os
import sys
from pathlib import Path

p = Path(__file__).resolve().parents[5]
sys.path.insert(1, str(p))

from scrapers_library.data_portals.opendata.opendata_scraper_2 import opendata_scraper2

# Change to what you need (remove what you don't)
save_url = [
    ["annual_crime/2015/", "https://data.austintexas.gov/resource/spbg-9v94.csv"],
    ["annual_crime/2016/", "https://data.austintexas.gov/resource/8iue-zpf6.csv"],
    [
        "racial_profiling/2015/citations/",
        "https://data.austintexas.gov/resource/sc6h-qr9f.csv",
    ],
    ["r2r/2015/", "https://data.austintexas.gov/resource/iydp-s2cf.csv"],
    ["hate_crimes/2017/", "https://data.austintexas.gov/resource/79qh-wdpx.csv"],
    ["arrests/guide/", "https://data.austintexas.gov/resource/cpxf-2jga.csv"],
    ["hate_crimes/2018/", "https://data.austintexas.gov/resource/idj2-d9th.csv"],
    ["r2r/2016/", "https://data.austintexas.gov/resource/h8jq-pcz3.csv"],
    [
        "racial_profiling/2017/citations/",
        "https://data.austintexas.gov/resource/7guv-wkre.csv",
    ],
    [
        "officer_involved_shooting/guide/",
        "https://data.austintexas.gov/resource/eqwy-k8kh.csv",
    ],
    [
        "racial_profiling/2018/guide/",
        "https://data.austintexas.gov/resource/mipf-8at9.csv",
    ],
    [
        "racial_profiling/2018/arrests/",
        "https://data.austintexas.gov/resource/xfke-9bsj.csv",
    ],
    ["annual_crime/2017/", "https://data.austintexas.gov/resource/3t4q-mqs5.csv"],
    ["hate_crimes/2018/", "https://data.austintexas.gov/resource/idj2-d9th.csv"],
    [
        "racial_profiling/2014/citations/",
        "https://data.austintexas.gov/resource/mw6q-k5gy.csv",
    ],
    [
        "racial_profiling/2017/arrests/",
        "https://data.austintexas.gov/resource/x4p3-hj3y.csv",
    ],
    [
        "racial_profiling/2018/guide/",
        "https://data.austintexas.gov/resource/mipf-8at9.csv",
    ],
    ["annual_crime/2018/", "https://data.austintexas.gov/resource/pgvh-cpyq.csv"],
    [
        "officer_involved_shooting/2008-2017/",
        "https://data.austintexas.gov/resource/uzqv-9uza.csv",
    ],
    [
        "officer_involved_shooting/2008-2017/subjects/",
        "https://data.austintexas.gov/resource/u2k2-n8ez.csv",
    ],
    ["r2r/2010/", "https://data.austintexas.gov/resource/q5ym-htjz.csv"],
    ["hate_crimes/2020/", "https://data.austintexas.gov/resource/mi2a-twn5.csv"],
    ["arrests/2016/", "https://data.austintexas.gov/resource/bmz9-cdnt.csv"],
    ["r2r/2017/", "https://data.austintexas.gov/resource/5evd-3tba.csv"],
    ["r2r/2017/subjects/", "https://data.austintexas.gov/resource/5w6q-adh8.csv"],
    [
        "racial_profiling/2016/citations",
        "https://data.austintexas.gov/resource/urfd-wng9.csv",
    ],
    ["r2r/2011/", "https://data.austintexas.gov/resource/jipa-v8m5.csv"],
    [
        "racial_profiling/2014/arrests/",
        "https://data.austintexas.gov/resource/fk9e-2udt.csv",
    ],
    ["r2r/2012/", "https://data.austintexas.gov/resource/bx9w-y5sd.csv"],
    [
        "racial_profiling/2018/citations/",
        "https://data.austintexas.gov/resource/b9rk-dixy.csv",
    ],
    [
        "racial_profiling/2017/warnings_field_obs/",
        "https://data.austintexas.gov/resource/5asp-dw2k.csv",
    ],
    ["crime_reports/2015/", "https://data.austintexas.gov/resource/g3bw-w7hh.csv"],
    [
        "discarge_firearm_at_dog/2019/",
        "https://data.austintexas.gov/resource/9qgn-zgva.csv",
    ],
    [
        "racial_profiling/2017/guide/",
        "https://data.austintexas.gov/resource/tud4-5x9v.csv",
    ],
    ["hate_crimes/2019/", "https://data.austintexas.gov/resource/e3qf-htd9.csv"],
    [
        "racial_profiling/2018/warnings_field_obs/",
        "https://data.austintexas.gov/resource/vchc-c622.csv",
    ],
    ["r2r/2017/subjects/", "https://data.austintexas.gov/resource/bmeh-xaea.csv"],
    [
        "racial_profiling/2014/warnings_field_obs/",
        "https://data.austintexas.gov/resource/tqet-vty2.csv",
    ],
    [
        "racial_profiling/2019/citations/",
        "https://data.austintexas.gov/resource/uzta-a386.csv",
    ],
    ["r2r/2018/", "https://data.austintexas.gov/resource/rus9-w6q5.csv"],
    ["r2r/2019/", "https://data.austintexas.gov/resource/3bfz-mri4.csv"],
    [
        "racial_profiling/2015/warnings_field_obs/",
        "https://data.austintexas.gov/resource/v6rq-ainw.csv",
    ],
    [
        "racial_profiling/2019/warnings_field_obs/",
        "https://data.austintexas.gov/resource/djcn-eje6.csv",
    ],
    ["r2r/2019/subjects/", "https://data.austintexas.gov/resource/dwrk-z7q9.csv"],
    ["r2r/2018/subjects/", "https://data.austintexas.gov/resource/c7is-tz8m.csv"],
    [
        "racial_profiling/2019/guide/",
        "https://data.austintexas.gov/resource/f59a-wt7w.csv",
    ],
]

save_folder = "./data/"

# Optional argument `save_subfolder` allows saving in a subfolder

# Crawl-delay is 1, so no need to set it.
opendata_scraper2(save_url, save_folder, save_subfolder=True)

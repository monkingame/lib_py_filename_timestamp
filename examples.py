# -*- coding: utf-8 -*-

from datetime import datetime
import filename_timestamp as ndt

now=ndt.get_now_date(date=datetime(2011, 5, 17, 10, 30, 0))
print(now)

now=ndt.get_now_time()
print(now)

now=ndt.get_now_datetime()
print(now)

now=ndt.get_now_datetime(date_time=datetime(2011, 3, 21, 10, 30, 1))
print(now)

now=ndt.get_now_datetime(with_millison=True)
print(now)

now=ndt.get_now_datetime(with_millison=True,hyphen_join='')
print(now)


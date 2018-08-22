# coding=utf-8
# fish_date.py 单元测试
# 2018.6.11 create by Hu Jun

import pytest
import sys
import time
sys.path.append('../fishbase')
from fishbase.fish_date import *
import datetime


# 2018.6.11 v1.0.14 #37 create by Hu Jun
class TestFishDate(object):
    # test get_years() tc
    def test_get_years_01(self):
        this_month = datetime.date(day=1, month=6, year=2018)
        
        assert get_years(7, this_month) == '201901'
        assert get_years(-5, this_month) == '201801'
        assert get_years(-6, this_month) == '201712'

        this_month1 = datetime.datetime.now()
        
        y = this_month1.year
        m = this_month1.month + 1
        if m == 12:
            y += 1
            m = 1
        
        assert get_years(1) == ''.join(['%04d' % y, '%02d' % m])
        
        with pytest.raises(TypeError):
            get_years(-5, 8)

    def test_get_date_range_01(self):
        this_month = datetime.date(day=1, month=2, year=2018)
    
        assert get_date_range(this_month) == ('2018-02-1', '2018-02-28')
        assert get_date_range('201802', separator='/') == ('2018/02/1', '2018/02/28')
        
        with pytest.raises(ValueError):
            get_date_range('2016798')
        
        with pytest.raises(TypeError):
            get_date_range('asdafsd')

    # 测试 GetRandomTime()  tc
    def test_date_time_this_month_01(self):
        this_month = GetRandomTime.date_time_this_month()
        now = datetime.datetime.now()
        this_month_days = calendar.monthrange(now.year, now.month)
        assert now.year == this_month.year
        assert now.month == this_month.month
        assert now.day <= this_month_days[1]

    # 测试 GetRandomTime()  tc
    def test_date_time_this_year_01(self):
        this_month = GetRandomTime.date_time_this_year()
        now = datetime.datetime.now()
        this_year_days = sum(calendar.mdays)
        assert now.year == this_month.year
        assert now.day <= this_year_days

    #  测试 get_time_interval()  tc
    def test_get_time_interval_01(self):
        start = int(time.time())
        end = start - 98908
    
        interval_dict = get_time_interval(end, start)
    
        assert interval_dict['days'] == 98908 // (60 * 60 * 24)
        remain = 98908 % (60 * 60 * 24)
        assert interval_dict['hours'] == remain // (60 * 60)

    #  测试 get_time_interval()  tc
    def test_get_time_interval_02(self):
        start = int(time.time())
        end = str(start - 98908)
    
        with pytest.raises(TypeError):
            get_time_interval(end, start)

    #  测试 transform_unix_to_datetime()  tc
    def test_transform_unix_to_datetime_01(self):
        timestamp = 1534938627
        data_type = transform_unix_to_datetime(timestamp)
    
        assert isinstance(data_type, datetime)
        assert data_type.year == 2018

    #  测试 transform_unix_to_datetime()  tc
    def test_transform_unix_to_datetime_02(self):
        timestamp = '1534938627'
    
        with pytest.raises(TypeError):
            transform_unix_to_datetime(timestamp)

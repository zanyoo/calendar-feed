import uuid
from datetime import date, datetime, timedelta

import pytz
from icalendar import Calendar, Event
from holidays import holiday_list

STRFT_DATE = "%Y%m%d"
TZ_BEIJING = pytz.timezone("Asia/Shanghai")
META_LIMIT_DURATION_DAYS = 90
META_INIT_DATE = date(2024, 4, 1)
META_INIT_LIMIT_INFO = {
    0: "限行 5和0",  # 星期一
    1: "限行 1和6",  # 星期二
    2: "限行 2和7",  # 星期三
    3: "限行 3和8",  # 星期四
    4: "限行 4和9",  # 星期五
}
META_NOLIMIT_INFO = "不限行"


def build_calendar():
    cal = Calendar()
    cal["VERSION"] = "2.0"  # 强制为 2.0
    cal["PRODID"] = "zanyoo/beijing-xianxing"
    cal["CALSCALE"] = "GREGORIAN"  # 公历
    cal["METHOD"] = "PUBLISH"  # 发布日历
    # 苹果私有属性
    cal["X-APPLE-LANGUAGE"] = "zh"
    cal["X-APPLE-REGION"] = "CN"
    # 多方私有属性
    cal["X-WR-CALNAME"] = "北京工作日尾号限行"
    cal["X-WR-CALDESC"] = "北京市实施[工作日高峰时段区域限行]交通管理措施"
    cal["X-WR-TIMEZONE"] = "Asia/Shanghai"
    return cal


def build_event(dt_start: date, summary: str):
    event = Event()
    event.add("DTSTAMP", datetime.now(pytz.UTC))
    event.add("UID", uuid.uuid1())
    event.add("DTSTART", dt_start)
    event.add("CLASS", "PUBLIC")  # 公开
    event.add("SUMMARY", summary)
    event.add("TRANSP", "TRANSPARENT")  # 透明的，不会影响日程安排
    return event


def build_calendar_info(start_date, end_date, num=-1):
    if end_date < start_date:
        raise Exception("结束时间必须晚于开始时间")

    cal = build_calendar()

    days = (end_date - start_date).days + 1
    for i in range(days):
        d = start_date + timedelta(days=i)
        limit_info = get_limit_info(d, num)
        if d in holiday_list:
            continue
        if limit_info == META_NOLIMIT_INFO:
            continue
        if limit_info is None:
            continue
        cal.add_component(build_event(d, limit_info))
    # 虽然 iCalendar 官方要求的 CRLF，但大部分现在日历应用可以解析 LF
    return cal.to_ical().decode('utf-8').replace("\r\n", "\n")


def get_limit_info(d: datetime.date, num: int) -> str:
    if d < META_INIT_DATE:
        raise Exception("只支持2024/04/01之后的日期")
    if d.weekday() == 5 or d.weekday() == 6:
        return META_NOLIMIT_INFO
    days = (d - META_INIT_DATE).days
    cycle_offset = (days // 91) * 4
    day_offset = d.weekday()

    offset = (cycle_offset + day_offset) % 5
    if num == -1 or offset == num:
        return META_INIT_LIMIT_INFO[offset]
    return META_NOLIMIT_INFO


if __name__ == '__main__':
    result_file = "../limit_4_9.ics"

    ics = build_calendar_info(date(2025, 1, 1), date(2026, 1, 1), 4)
    # 可以使用https://icalendar.org/validator.html进行校验
    # 1. iCalendar要求文件内容用 CRLF 来换行，但 apple 不要求
    with open(result_file, 'w', encoding='utf-8') as f:
        f.write(ics)  # 读取所有内容

from datetime import datetime

holiday_list = []
# 元旦：1月1日（周三）放假1天，不调休。
holiday_list.append(datetime(2025, 1, 1).date())
# 春节：1月28日（农历除夕、周二）至2月4日（农历正月初七、周二）放假调休，共8天。1月26日（周日）、2月8日（周六）上班。
holiday_list.append(datetime(2025, 1, 28).date())
holiday_list.append(datetime(2025, 1, 29).date())
holiday_list.append(datetime(2025, 1, 30).date())
holiday_list.append(datetime(2025, 1, 31).date())
holiday_list.append(datetime(2025, 2, 1).date())
holiday_list.append(datetime(2025, 2, 2).date())
holiday_list.append(datetime(2025, 2, 3).date())
holiday_list.append(datetime(2025, 2, 4).date())
# 清明节：4月4日（周五）至6日（周日）放假，共3天。
holiday_list.append(datetime(2025, 4, 4).date())
holiday_list.append(datetime(2025, 4, 5).date())
holiday_list.append(datetime(2025, 4, 6).date())
# 劳动节：5月1日（周四）至5日（周一）放假调休，共5天。4月27日（周日）上班。
holiday_list.append(datetime(2025, 5, 1).date())
holiday_list.append(datetime(2025, 5, 2).date())
holiday_list.append(datetime(2025, 5, 3).date())
holiday_list.append(datetime(2025, 5, 4).date())
holiday_list.append(datetime(2025, 5, 5).date())
# 端午节：5月31日（周六）至6月2日（周一）放假，共3天。
holiday_list.append(datetime(2025, 5, 31).date())
holiday_list.append(datetime(2025, 6, 1).date())
holiday_list.append(datetime(2025, 6, 2).date())
# 国庆节、中秋节：10月1日（周三）至8日（周三）放假调休，共8天。9月28日（周日）、10月11日（周六）上班。
holiday_list.append(datetime(2025, 10, 1).date())
holiday_list.append(datetime(2025, 10, 2).date())
holiday_list.append(datetime(2025, 10, 3).date())
holiday_list.append(datetime(2025, 10, 4).date())
holiday_list.append(datetime(2025, 10, 5).date())
holiday_list.append(datetime(2025, 10, 6).date())
holiday_list.append(datetime(2025, 10, 7).date())
holiday_list.append(datetime(2025, 10, 8).date())
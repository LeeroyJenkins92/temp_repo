from datetime import datetime
dist_diff = 12 * 5


def current_total_month_getter():
    now = datetime.now()
    current_year = int(str(now.year)[-2:]) * 12
    current_month = int(str(now.month))
    current_total_month = current_year + current_month
    return current_total_month


def release_total_month_getter():
    with open("/etc/lsb-release", "r", encoding='utf-8') as file:
        release_lst = [line for line in file if "DISTRIB_RELEASE" in line]
        release_year = int(release_lst[0][:-4][-2:]) * 12
        release_month = int(release_lst[0][:-1][-2:])
        release_total_month = release_year + release_month
        return release_total_month


def date_comparer():
    if current_total_month_getter() - release_total_month_getter() >= dist_diff:
        print("Support period is over")
    else:
        print("Support period just fine :)")


date_comparer()

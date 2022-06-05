# temp_repo

ОС Linux. В файле /etc/lsb-release содержится информация об ОС в следующем виде:

DISTRIB_ID=Ubuntu

DISTRIB_RELEASE=20.04

DISTRIB_CODENAME=focal

DISTRIB_DESCRIPTION="Ubuntu 20.04.1 LTS"

При этом номер версии DISTRIB_RELEASE указывает на дату релиза, например 20.04 - апрель 2020 года (для простоты будем считать, что 1-го числа, т.е. 1 апреля 2020 года).

Напишите bash-скрипт, который сверяет дату релиза с текущей и выдает сообщение "Support period is over", если с момента релиза прошло более 5 лет.

###get current year###
current_year=$((date +"%Y") | cut -c3-)
current_month=$(date +"%m")

total_current_month=$(($current_year*12+$current_month))


###get release year###
release_year=$(sudo cat /etc/lsb-release | grep DISTRIB_RELEASE | sed s/"DISTRIB_RELEASE="// | cut -d '.' -f1)
release_month=$(sudo cat /etc/lsb-release | grep DISTRIB_RELEASE | sed s/"DISTRIB_RELEASE="// | cut -d '.' -f2)

total_release_month=$(($release_year*12+$release_month))


###compare dates###
dates_diff=$(($total_current_month-$total_release_month))

if [ $dates_diff -ge 60 ]
then
	echo "Support period is over"
else
	echo "Support period just fine :)"
fi

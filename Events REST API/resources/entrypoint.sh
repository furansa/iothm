#!/usr/bin/env bash
# Leave if any command fails
set -e

# Used for debugging if no foreground application is being called
while true; do
    date
    sleep 5
done

# Call the application in foreground, in test mode, just run the unit tests,
# generate test and coverage reports and exit
if [ ${APP_TEST_MODE} = "True" ]; then
    /usr/bin/env python3 manage.py test -v2
else
    /usr/bin/env python3 manage.py runserver ${APP_HOST}:${APP_PORT}
fi

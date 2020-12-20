#!/usr/bin/env bash
# Leave if any command fails
set -e

# Used for debugging if no foreground application is being called
#while true; do
#    date
#    sleep 5
#done

# Call the application in foreground, in test mode, just run the unit tests,
# generate test and coverage reports and exit
if [ ${TEST_MODE} = "True" ]; then
    TEST_DIR="./tests"
    TEST_REPORTS="${TEST_DIR}/reports"

    echo "Starting the tests."
    /usr/bin/env pytest -q --cov=api --cov-report html:${TEST_REPORTS}/coverage --html=${TEST_REPORTS}/$(date +%Y-%m-%d_%H%M%S).html ${TEST_DIR}

    echo "All done, goodbye."
else
    if [ ${DEBUG} = "True" ]; then
        /usr/bin/env python3 manage.py runserver ${HOST}:${PORT} DEBUG=True
    else
        /usr/bin/env python3 manage.py runserver ${HOST}:${PORT}
    fi
fi

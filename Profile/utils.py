from datetime import datetime


def timestamp_convertion():
    # time formatting
    unformatted_time = datetime.now()
    formarted_time = unformatted_time.strftime("%Y%m%d%H%M%S")
    return formarted_time
    
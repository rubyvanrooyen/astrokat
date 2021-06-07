"""Utility script to calculate solar body equatorial coordinates for MKAT
   and indicate of target moves slow enough to be observed over obs duration
"""

from astropy.coordinates import solar_system_ephemeris
from astropy.coordinates import SkyCoord
from astropy import units as u

from astrokat import (Observatory,
                      datetime2timestamp,
                      targets)

import argparse
from datetime import datetime, timedelta
import sys

solar_bodies = [body.encode('ascii') for body in solar_system_ephemeris.bodies]
datetime_format = "%Y-%m-%d %H:%M"


def cli(prog):
    usage = "{} [options]".format(prog)
    description = 'Planning solar body observations with MeerKAT telescope'
    parser = argparse.ArgumentParser(
        usage=usage,
        description=description,
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        "--body",
        type=str,
        choices=solar_bodies,
        required=True,
        help="name of solar body to be observed",
    )
    parser.add_argument(
        "-t", "--datetime",
        default=datetime.utcnow().strftime(datetime_format),
        help="observation date and time string in UTC timezone, "
             "'YYYY-MM-DD HH:MM'",
    )
    parser.add_argument(
        "-d", "--duration",
        type=float,
        default=60.,
        help="target observation duration in seconds"
    )
    parser.add_argument(
        "-s", "--separation",
        type=float,
        default=60.,
        help="separation angle limit in arcseconds",
    )

    return parser.parse_args()


def main():
    pass


if __name__ == "__main__":

    args = cli(sys.argv[0])

    body = args.body
    date_time = datetime. strptime(args.datetime, datetime_format)
    observer = Observatory().get_location().observer
    location = targets.mkat_locale(observer)


    start_ts = datetime2timestamp(date_time)
    ra, dec = targets.solar2eq(body,
                               location,
                               timestamp=start_ts)
    print(ra, dec)
    c0 = SkyCoord(ra*u.deg, dec*u.deg, frame='icrs')
    print(c0)

    end_ts = datetime2timestamp(date_time + timedelta(seconds=args.duration))
    ra, dec = targets.solar2eq(body,
                               location,
                               timestamp=end_ts)
    print(ra, dec)
    c1 = SkyCoord(ra*u.deg, dec*u.deg, frame='icrs')
    print(c1)

    sep = c0.separation(c1)
    print(sep.arcsecond)

    print(args.separation)
    print(sep.arcsecond/args.separation)
    factor = sep.arcsecond/args.separation

    print(args.duration, factor)
    dt = args.duration/factor
    print("{:0>8}".format(str(timedelta(seconds=dt))))

    dtt = timedelta(seconds=dt)
    print(dtt, dtt.days, dtt.seconds, dtt.microseconds)


# -fin-

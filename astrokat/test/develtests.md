# Quick CAM unit test scripts

## Use python unit tests
```
pip install mock
pip install tox
```

Running individual test
```
python -m unittest astrokat.test.test_offline_observe.TestAstrokatYAML.test_targets_sim
python -m unittest astrokat.test.test_offline_observe.TestAstrokatYAML.test_two_calib_sim
python -m unittest astrokat.test.test_offline_observe.TestAstrokatYAML.test_image_single_sim
python -m unittest astrokat.test.test_offline_observe.TestAstrokatYAML.test_image_sim
python -m unittest astrokat.test.test_offline_observe.TestAstrokatYAML.test_below_horizon
```
Using tox
```
LC_ALL=C test_flags=astrokat tox -e py27
```

Or for convenience some tests are grouped into bash scripts for manual testing
* `./check_nd_units.sh`
* `./check_offline_observe_units.sh`
* `./check_scans_units.sh`

-fin-

import numpy as np

num_scans = 3
scan_extent = 10.
scan_spacing = 0.5
scan_in_azimuth = True
# Create start and end positions of each scan, based on scan parameters
scan_levels = np.arange(-(num_scans // 2), num_scans // 2 + 1)
print scan_levels
scanning_coord = (scan_extent / 2.0) * (-1.0) ** scan_levels
print scanning_coord
stepping_coord = scan_spacing * scan_levels
print stepping_coord
# Flip sign of elevation offsets to ensure that the first scan always
# starts at the top left of target
scan_starts = (zip(scanning_coord, -stepping_coord)
               if scan_in_azimuth else
               zip(stepping_coord, -scanning_coord))
print scan_starts
scan_ends = (zip(-scanning_coord, -stepping_coord)
             if scan_in_azimuth else
             zip(stepping_coord, scanning_coord))
print scan_ends
# Perform multiple scans across the target
target = (55.26731, 43.70517)
for scan_index, (start, end) in enumerate(zip(scan_starts, scan_ends)):
    print scan_index, target, start, end
    print np.asarray(target)+np.asarray(start)
    print np.asarray(target)+np.asarray(end)

# -fin-

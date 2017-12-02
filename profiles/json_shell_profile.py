# Value of the source=* tag, if added.
source = 'Shell'
# A boolean value, False by default. If True the script won't store identifiers in objects, relying on geometric matching every time the matching process is done.
no_dataset_id = True
# Tags for querying with overpass api
query = [('amenity', 'fuel')]
# A set of authoritative tags to replace on matched objects
master_tags = ('brand', 'opening_hours', 'phone', 'website')
# Empty dict so we don't add a fixme tag to unmatched objects
tag_unmatched = {}
# How close OSM point should be to register a match, in meters. Default is 100
max_distance = 100


# No dataset function is required in this profile as I load the data in from a JSON file (conflate -i shell_input.json -v -o result.osm -c preview.json json_shell_profile.py)


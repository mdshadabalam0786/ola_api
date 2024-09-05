from requests import Session
from json import loads
session=Session()
session.headers.update({"content-type":"application/json"})
response=session.post("https://api.olamaps.io/routing/v1/directions?origin=12.84305,77.63897&destination=12.93857,77.60377&api_key=dxMKc5TGUmXq4qSHB6ySwPaNkD1ivRMM0BFR73kQ")
assert response.status_code==200,f"{response.status_code}"
l=loads(response.text)
# print(l)

li_of_routes=[]
for i in l['routes'][0]['legs'][0]['steps']:
    li_of_routes.append(i['instructions'])
assert any('you have arrived at your destination' in step.lower() for step in li_of_routes), "The word 'destination' is not in the list."

# Validate all entries have valid distances and durations
for step in l['routes'][0]['legs'][0]['steps']:
    assert step['distance'] >= 0, f"Invalid distance in step: {step['instructions']}"
    assert step['duration'] >= 0, f"Invalid duration in step: {step['instructions']}"
    assert 'instructions' in step, f"Missing instructions in step: {step}"
    assert 'maneuver' in step, f"Missing maneuver in step: {step}"

# Check if all start and end locations have lat and lng
for step in l['routes'][0]['legs'][0]['steps']:
    assert 'lat' in step['start_location'] and 'lng' in step['start_location'], f"Missing start location lat/lng in step: {step['instructions']}"
    assert 'lat' in step['end_location'] and 'lng' in step['end_location'], f"Missing end location lat/lng in step: {step['instructions']}"

print("All validations passed successfully.")

# {'status': 'SUCCESS',
# 'geocoded_waypoints': [{'geocoder_status': 'OK', 'place_id': 'tdr1ndnbp', 'types': []},
# {'geocoder_status': 'OK', 'place_id': 'tdr1tgmkd', 'types': []}],
# 'routes': [{'summary': '',
# 'legs': [{'steps': [
# {'instructions': 'Head north', 'distance': 19, 'readable_distance': '0 km 19 metres', 'maneuver': 'depart', 'duration': 4, 'readable_duration': '0 hours 1 minutes', 'start_location': {'lat': 12.84305, 'lng': 77.63897}, 'end_location': {'lat': 12.84322, 'lng': 77.639}, 'bearing_before': 0, 'bearing_after': 10},
# {'instructions': 'Turn right onto Neeladri Road', 'distance': 593, 'readable_distance': '0 km 593 metres', 'maneuver': 'turn-right', 'duration': 106, 'readable_duration': '0 hours 2 minutes', 'start_location': {'lat': 12.84322, 'lng': 77.639}, 'end_location': {'lat': 12.843580000000001, 'lng': 77.64425000000001}, 'bearing_before': 9, 'bearing_after': 101},
# {'instructions': 'Turn left', 'distance': 649, 'readable_distance': '0 km 649 metres', 'maneuver': 'turn-left', 'duration': 93, 'readable_duration': '0 hours 2 minutes', 'start_location': {'lat': 12.84358, 'lng': 77.64425}, 'end_location': {'lat': 12.849389999999998, 'lng': 77.64359999999998}, 'bearing_before': 70, 'bearing_after': 355},
# {'instructions': 'Continue onto Neeladri Road', 'distance': 1775, 'readable_distance': '1 km 775 metres', 'maneuver': 'continue', 'duration': 281, 'readable_duration': '0 hours 5 minutes', 'start_location': {'lat': 12.84939, 'lng': 77.6436}, 'end_location': {'lat': 12.862550000000006, 'lng': 77.6485800000001}, 'bearing_before': 345, 'bearing_after': 341},
# {'instructions': 'Continue onto Basapura Road', 'distance': 964, 'readable_distance': '0 km 964 metres', 'maneuver': 'continue', 'duration': 198, 'readable_duration': '0 hours 4 minutes', 'start_location': {'lat': 12.86255, 'lng': 77.64858}, 'end_location': {'lat': 12.86961, 'lng': 77.65338000000003}, 'bearing_before': 15, 'bearing_after': 9},
# {'instructions': 'Turn left', 'distance': 318, 'readable_distance': '0 km 318 metres', 'maneuver': 'turn-left', 'duration': 59, 'readable_duration': '0 hours 1 minutes', 'start_location': {'lat': 12.86961, 'lng': 77.65338}, 'end_location': {'lat': 12.87188, 'lng': 77.65156999999999}, 'bearing_before': 35, 'bearing_after': 320},
# {'instructions': 'Turn right onto Hosur Road (NH44)', 'distance': 6428, 'readable_distance': '6 km 428 metres', 'maneuver': 'turn-right', 'duration': 1190, 'readable_duration': '0 hours 20 minutes', 'start_location': {'lat': 12.87188, 'lng': 77.65157}, 'end_location': {'lat': 12.921009999999999, 'lng': 77.62025}, 'bearing_before': 320, 'bearing_after': 59},
# {'instructions': 'Continue onto Hosur road', 'distance': 438, 'readable_distance': '0 km 438 metres', 'maneuver': 'continue', 'duration': 94, 'readable_duration': '0 hours 2 minutes', 'start_location': {'lat': 12.92101, 'lng': 77.62025}, 'end_location': {'lat': 12.924410000000002, 'lng': 77.61817000000003}, 'bearing_before': 329, 'bearing_after': 333},
# {'instructions': 'Continue onto Hosur Road', 'distance': 916, 'readable_distance': '0 km 916 metres', 'maneuver': 'continue', 'duration': 228, 'readable_duration': '0 hours 4 minutes', 'start_location': {'lat': 12.92441, 'lng': 77.61817}, 'end_location': {'lat': 12.93152, 'lng': 77.61384}, 'bearing_before': 329, 'bearing_after': 329},
# {'instructions': 'Make a slight left onto Dr. M H Marigowda Road', 'distance': 1156, 'readable_distance': '1 km 156 metres', 'maneuver': 'turn-slight-left', 'duration': 253, 'readable_duration': '0 hours 5 minutes', 'start_location': {'lat': 12.93152, 'lng': 77.61384}, 'end_location': {'lat': 12.936639999999995, 'lng': 77.60479000000001}, 'bearing_before': 331, 'bearing_after': 305},
# {'instructions': 'Keep left onto Bannerghatta-Marigowda Turn Road', 'distance': 325, 'readable_distance': '0 km 325 metres', 'maneuver': 'turn-slight-left', 'duration': 75, 'readable_duration': '0 hours 2 minutes', 'start_location': {'lat': 12.93664, 'lng': 77.60479}, 'end_location': {'lat': 12.93699, 'lng': 77.60181}, 'bearing_before': 274, 'bearing_after': 275},
# {'instructions': 'Turn right onto Bannerghatta Road', 'distance': 53, 'readable_distance': '0 km 53 metres', 'maneuver': 'turn-right', 'duration': 7, 'readable_duration': '0 hours 1 minutes', 'start_location': {'lat': 12.93699, 'lng': 77.60181}, 'end_location': {'lat': 12.93725, 'lng': 77.60161000000001}, 'bearing_before': 277, 'bearing_after': 278},
# {'instructions': 'Turn right onto Marigowda Road', 'distance': 178, 'readable_distance': '0 km 178 metres', 'maneuver': 'turn-right', 'duration': 23, 'readable_duration': '0 hours 1 minutes', 'start_location': {'lat': 12.93725, 'lng': 77.60161}, 'end_location': {'lat': 12.937030000000002, 'lng': 77.60323999999999}, 'bearing_before': 12, 'bearing_after': 97},
# {'instructions': 'Turn left', 'distance': 155, 'readable_distance': '0 km 155 metres', 'maneuver': 'turn-left', 'duration': 30, 'readable_duration': '0 hours 1 minutes', 'start_location': {'lat': 12.93703, 'lng': 77.60324}, 'end_location': {'lat': 12.93833, 'lng': 77.60357}, 'bearing_before': 97, 'bearing_after': 9},
# {'instructions': 'Turn left', 'distance': 29, 'readable_distance': '0 km 29 metres', 'maneuver': 'turn-left', 'duration': 5, 'readable_duration': '0 hours 1 minutes', 'start_location': {'lat': 12.93833, 'lng': 77.60357}, 'end_location': {'lat': 12.938600000000001, 'lng': 77.60362}, 'bearing_before': 80, 'bearing_after': 9},
# {'instructions': 'You have arrived at your destination, on the right', 'distance': 0, 'readable_distance': '0 km 0 metres', 'maneuver': 'arrive', 'duration': 0, 'readable_duration': '0 hours 0 minutes', 'start_location': {'lat': 12.9386, 'lng': 77.60362}, 'end_location': {'lat': 12.9386, 'lng': 77.60362}, 'bearing_before': 10, 'bearing_after': 0}],
# 'distance': 14002, 'readable_distance': '14.00', 'duration': 2648, 'readable_duration': '0 hours 45 minutes',
# 'start_location': {'lat': 12.843051, 'lng': 77.638965}, 'end_location': {'lat': 12.938596, 'lng': 77.603619},
# 'start_address': '12.843051,77.638965', 'end_address': '12.938596,77.603619'}],
# 'overview_polyline': 'alkmAqzzxMa@EFg@LeA?AXwBPqA`@}CB[@SKg@gAsE]{A_AyDu@@iDHaABiA@uCDiA@oDBUDcFx@wAT{@LmCn@OFODUDO@I@OASAUAYCe@EoBUwBY{AUe@E_COYAsHc@{@GQCIAGAIAIA{A_@MCGCGCKEo@a@IGIGIGIIEGCGCEAI?IAo@AeB?G?GAI?EEECCECEAEAuC]WEu@Ks@EkBI]EE?EAKCECECAE?W?U@]NcD?IAGGEiAWUGYI{Ag@]KOC[EuBU]CKASGoAWoAWSCOCGCICECECGEGIEGO[KUKQEKKOo@u@sBgCk@s@a@i@IKKIKI[WGGGEwC}A}@i@cAo@GEMG_@UMGIESGOGQGy@SmCs@eAYWGgAYo@Q{@Uc@MUQa@Z}HzFkAz@YTGKKHyB~AyAhAwAhAcGhF]\\EBqAfA{DdDoA~@cAl@]Tc@Vmm@n[gMtGi@XiCtAsE~BEDKDQJMFkIpE_IbEqFpC_Bx@MHuDnBeHrDoPvIiIjEiHvDiO`ImIlEYNMFwH`EqBfAULs@TkAn@cHpDyH~DoBdAmCxAaBr@w@^uEtBaEnBQHsAr@gEzBeAr@qA|@{@n@aAf@wDlBOHC@YLKDID}@b@{BdAiAj@s@^wBpAIDm@^kCtA{@b@{DtBaAh@]PmDdBkDfB_ClA}C|AQH]R_CtAiCvAq@XGBcAb@EB]h@_@d@g@p@KLMR{FbIa@h@A@QVg@t@eAvAqAhBINmCxE}A`Da@`AIVQn@[jAETCFCRCTE^?DAJGbAALALSfCCh@Q~CK~BEl@MfBC`@OzBGr@k@KDs@L}ABS@_@JuADi@u@Km@GcDa@BKu@I',
# 'travel_advisory': '', 'bounds': {}, 'copyrights': 'OLA Map data ©2024', 'warnings': []}],
# 'source_from': 'Ola Maps'}

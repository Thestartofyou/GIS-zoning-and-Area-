import csv

def find_land_without_building(csv_file_path):
    try:
        # Dictionary to store land and building information
        land_building_dict = {}

        with open(csv_file_path, 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)

            # Populate the dictionary with land and building information
            for row in csv_reader:
                land_id = row.get("Land ID")
                building_id = row.get("Building ID")
                parcel_area = float(row.get("Parcel Area", 0))  # Assuming "Parcel Area" is a numeric field
                zoning = row.get("Zoning")

                if land_id not in land_building_dict:
                    land_building_dict[land_id] = {"building_ids": set(), "parcel_area": parcel_area, "zoning": zoning}

                if building_id:
                    land_building_dict[land_id]["building_ids"].add(building_id)

        # Print land IDs without buildings based on parcel area and zoning
        for land_id, data in land_building_dict.items():
            if not data["building_ids"] and data["parcel_area"] > 0 and data["zoning"] == "Residential":
                print(f"Land ID {land_id} has no building, parcel area: {data['parcel_area']}, zoning: {data['zoning']}.")

    except FileNotFoundError:
        print(f"File not found: {csv_file_path}")
    except Exception as e:
        print(f"Error processing CSV file: {e}")

# Example usage
csv_file_path = 'path/to/your/file.csv'
find_land_without_building(csv_file_path)


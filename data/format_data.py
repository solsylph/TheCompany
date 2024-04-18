
import json

# Formats original data into a chat-completion effective format for gpt-3.5-turbo
# Original data was contained within 1 dictionary key and obstructed with HTML tags
# New format:
#   {
#     "messages": [
#       {"role": "system", "content": "Here is an example of an optimized product title and description for better SEO and customer engagement."}
#       , {"role": "assistant", "content": "Title: {title}\nDescription: {description}{bullet_points}{color}"}
#     ]
#   }

def read_jsonl_file(file_path):
    try:
        with open(file_path, 'r') as file:
            data = [json.loads(line) for line in file]
        return data
    except FileNotFoundError:
        print(f"Error: The file {file_path} does not exist.")
        return []
    except json.JSONDecodeError:
        print("Error: Failed to decode JSON. Check file for formatting errors.")
        return []

def process_data(data):
    new_data = []
    for item in data:
        try:
            title = item['prompt'].split("<title>")[1].split("</title>")[0]
            description = item['prompt'].split("<text>")[1].split("</text>")[0]
            bullet_points = item['prompt'].split("<bullet_points>")[1].split("</bullet_points>")[0]
            color = ""
            if "<color>" in item['prompt']:
                color = item['prompt'].split("<color>")[1].split("</color>")[0]
                color = f" Color: {color}" if color else ""

            full_description = f"Title: {title}\nDescription: {description}{bullet_points}{color}"
            system_message = "Here is an example of an optimized product title and description for better SEO and customer engagement."
            new_entry = {
                "messages": [
                    {"role": "system", "content": system_message}
                    , {"role": "assistant", "content": full_description}
                ]
            }
            new_data.append(json.dumps(new_entry))
        except (IndexError, KeyError) as e:
            print(f"Error processing item: {item}. Error: {e}")
    return new_data

def write_jsonl_file(file_path, new_data):
    try:
        with open(file_path, 'w') as outfile:
            for entry in new_data:
                outfile.write(f"{entry}\n")
        print(f"Data successfully written to {file_path}")
    except IOError:
        print(f"Error: Could not write to file {file_path}.")

# Paths for the input and output files
input_file_path = './data/stats_final.jsonl'
output_file_path = './data/formatted_for_gpt35_stats.jsonl'

# Processing the data
raw_data = read_jsonl_file(input_file_path)
if raw_data:
    formatted_data = process_data(raw_data)
    write_jsonl_file(output_file_path, formatted_data)
else:
    print("No data processed due to earlier errors.")


import random

# Reduces the number of lines in a JSONL file by randomly keeping a fraction of them 

def reduce_dataset(input_file, output_file, keep_fraction=0.5):
    print(f"Fraction: {keep_fraction}")
    print("Starting reduction...")
    
    try:
        with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
            for line in infile:
                # Randomly decide whether to keep this line
                if random.random() < keep_fraction:
                    outfile.write(line)
    except FileNotFoundError:
        print(f"Error: The file {input_file} does not exist.")
    except IOError:
        print(f"Error: An I/O error occurred while handling the files.")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")

    print("Reduction complete")

input_path = './data/formatted_for_gpt35_stats.jsonl'
output_path = './data/formatted_for_gpt35_stats_onefour.jsonl'
reduce_dataset(input_path, output_path, 0.25)
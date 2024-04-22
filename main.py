import subprocess
import os
import pandas as pd
from json import dumps, loads

def extract_action_units(video_filename, is_bluff):
    # Path where the OpenFace executable is located
    openface_exec_path = "C:\\Users\\Wiktor\\Desktop\\OpenFace_2.2.0_win_x64\\FeatureExtraction"

    # Directory where the video files are stored
    video_directory = ".\\Data\\Videos"
    
    # Directory to save the output files
    output_directory = ".\\Data\\Output"
    
    # Construct the full path to the video file
    video_path = os.path.join(video_directory, video_filename)
    if not os.path.exists(video_path):
        print(f"Video file not found: {video_path}")
        return False
    
    # Build the command as a list
    command = [
        openface_exec_path,
        "-f", video_path,
        "-out_dir", output_directory,
        "-aus"
    ]
    
    # Run the command
    try:
        # Execute the command
        subprocess.run(command, check=True)
        print("Feature extraction completed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while running OpenFace: {e}")
        return False
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return False
    
    output_path = ".\\Data\\Output\\" + video_filename.strip(".mp4") + ".csv"
    
    output_dataframe = pd.read_csv(output_path)
    
    if is_bluff:
        output_dataframe["is_bluff"] = 1
    else:
        output_dataframe["is_bluff"] = 0
        
    output_dataframe.set_index("frame", inplace=True)
    
    output_dataframe.to_json(".\\Data\\Output\\" + video_filename.strip(".mp4") + ".json", orient="records")
    result_json = output_dataframe.to_json(orient="index")  #* converting the orient and set_index can change the data structure of the json file
    
    send_data(loads(result_json))
    
    return True
    

#* Example usage:
extract_action_units("1.mp4", True)
extract_action_units("2.mp4", False)

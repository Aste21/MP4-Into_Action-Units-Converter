import subprocess
import os

def extract_action_units(video_filename):
    # Path where the OpenFace executable is located
    openface_exec_path = "C:\\Users\\Wiktor\\Desktop\\poker_demo\\OpenFace_2.2.0_win_x64\\FeatureExtraction"

    # Directory where the video files are stored
    video_directory = "C:\\Users\\Wiktor\\Desktop\\poker_demo\\data"
    
    # Directory to save the output files
    output_directory = "C:\\Users\\Wiktor\\Desktop\\poker_demo\\output_directory"
    
    # Construct the full path to the video file
    video_path = os.path.join(video_directory, video_filename)
    
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
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

#* Example usage:
extract_action_units("video.mp4")

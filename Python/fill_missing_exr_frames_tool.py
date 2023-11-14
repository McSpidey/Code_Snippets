from pathlib import Path
import shutil

def fill_missing_frames(directory, sequence_prefix, frame_digits=4):
    """
    Fills in missing frames in an EXR sequence by duplicating the previous frame, using pathlib for file operations.
    Allows setting the number of digits in the frame sequence.

    :param directory: The directory containing the EXR sequences.
    :param sequence_prefix: The prefix of the sequence to process.
    :param frame_digits: The number of digits in the frame sequence (default is 4).
    """
    # Create a Path object for the directory
    dir_path = Path(directory)

    # Frame number format based on the number of digits
    frame_format = f"{{:0{frame_digits}d}}"

    # Filter out relevant sequence files
    sequence_files = sorted(dir_path.glob(f"{sequence_prefix}*.[eE][xX][rR]"))

    last_frame_number = None
    for file_path in sequence_files:
        # Extract frame number from the filename
        frame_number = int(file_path.stem[len(sequence_prefix):])

        # Check if there is a gap in the sequence
        if last_frame_number is not None and frame_number != last_frame_number + 1:
            for missing_frame in range(last_frame_number + 1, frame_number):
                # Construct the source and target file paths
                source_file = dir_path / f"{sequence_prefix}{frame_format.format(last_frame_number)}.exr"
                target_file = dir_path / f"{sequence_prefix}{frame_format.format(missing_frame)}.exr"

                # Check if the target file already exists
                if not target_file.exists():
                    print(f"Duplicating {source_file.name} to {target_file.name}")
                    shutil.copy(source_file, target_file)

        last_frame_number = frame_number

# Example usage
if __name__ == "__main__":
    #Example where input is a sequence of files [sequence0000.exr, sequence0002.exr, sequence0004.exr etc]
    target_folder = "."
    target_sequence = "sequence"
    fill_missing_frames(target_folder, target_sequence)

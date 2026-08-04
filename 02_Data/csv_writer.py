# ==========================================
# Purpose:
# Save generated data to CSV files.
# ==========================================

from pathlib import Path


def save_to_csv(dataframe, file_name):
    """
    Saves a pandas DataFrame to the project's
    03_Raw_Data folder.

    Parameters
    ----------
    dataframe : pandas.DataFrame
        Data to save.

    file_name : str
        Name of the CSV file.
    """

    # Get project root
    project_root = Path(__file__).resolve().parents[1]

    # Build output folder path
    output_folder = project_root / "03_Raw_Data"

    # Create folder if it doesn't exist
    output_folder.mkdir(exist_ok=True)

    # Save CSV
    output_file = output_folder / file_name

    dataframe.to_csv(
        output_file,
        index=False
    )

    print(f"CSV saved successfully: {output_file}")
# Spotify Playlist Downloader

This is a simple Python script that downloads a Spotify playlist using the spotdl library. It prompts the user to input the Spotify playlist link and the output path where the downloaded songs will be saved.


## Prerequisites

- Python 3.6 or above
- A Spotify account
- A Spotify Developer account (to obtain the client ID and client secret)


## Installation

1. Clone or download this repository to your local machine.
2. Create a virtual environment for the project using `venv` or `conda`.
3. Install the required packages listed in requirements.txt by running `pip install -r requirements.txt`
1. Create a `.env` file in the root directory of the project and add your Spotify client ID and client secret in the following format:

```
CLIENT_ID=<your-client-id>
CLIENT_SECRET=<your-client-secret>
```

## Usage

1. Run the script by running python `main.py`.
2. When prompted, enter the Spotify playlist link and output path.
3. If the playlist details are correct, confirm the download by entering `y`.
4. The script will search for the songs in the playlist and download them to the specified output path.
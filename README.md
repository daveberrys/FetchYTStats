# FetchYTStats
Fetch your youtube stats with;
- Video IDs
- Video Thumbnail URL
- Views count
- Likes count
- Comment counts

## How does this work?
Using the GitHub Workflow that runs 12 hours per day and a python script, it'll write a json file named `yt-data.json`, commit, and push it!

## How do I set it up?

### 1. Get a Google API key
- **1.1** Open [Google Cloud Console](https://console.cloud.google.com/) and select a project, or create a new project.
- **1.2** Click on the hamburger menu on the top right, and find "APIs and services". Then, click on "Library"
  - **1.2.1** Once in the Library tab, in the search bar of the Library, search "Youtube", and then press enter.
  - **1.2.2** Middle click (or open a new tab) for "YouTube Data API v3" and "YouTube Analytics API" and click enable on both of them.
- **1.3** Repeat step 1.2, but go to "Credentials".
- **1.4** Click on "Create Credentials" on the top, and then select "API Key"
  - **1.4.1** Put in a name, and in "Select API restrctions", select "YouTube Data API v3" and "YouTube Analytics API", then click "OK", and then click on "Create" at the bottom.
  - **1.4.2** Click on the copy icon, and then click "Close". Save that API Key somewhere.

### 2. Get your Channel ID.
- **2.1** Open your youtube channel, and click on "... more" in your about.
  - **2.1.1** Click on share channel, and then click "Copy Channel ID"
- **2.2** On your Channel ID, replace `UCxx_` to `UUxx_`.

### 3. Fork the GitHub repository, and add variables.
- **3.1** Fork the GitHub repository.
- **3.2** Once forked, click at the top "Settings".
  - **3.2.1** In the sidebar, scroll down until you see "Secrets and variables", and click on "Actions"
  - **3.2.2** Switch to "Variables" tab, and click "New Repository variable". You might need to middle click for this one since you need three.
  - **3.2.3** Once you're in the "New Variable" screen, put the variable name as `GOOGLE_API_KEY` and put in your Google API Key, and then "Add Variable".
    - **3.2.3.1** Do this two more times but for `YOUTUBE_CHANNEL_PLAYLIST` and `LIMIT`. I'd reccomend putting `LIMIT` set to 50.

### Congrats! You're done!
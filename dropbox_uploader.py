import sys
import dropbox
from dropbox.files import WriteMode
from dropbox.exceptions import ApiError, AuthError
from datetime import datetime
from logger import create_logger

dbx = dropbox.Dropbox('TOKEN HERE')
currentTime = datetime.now().strftime('%Y-%m-%d')



class backuper:
    def __init__(self):
        self.logger = create_logger("dropbox_uploader")
        self.logger.info(f"===== dropbox_uploader started =====")
        self.LOCALFILE = 'titles.txt'
        self.BACKUPPATH = '/TitlesDatabase/titles_' + currentTime + '.txt'
    # Uploads contents of LOCALFILE to Dropbox
    def backup(self):
        try:
            currentTime = datetime.now().strftime('%Y-%m-%d')
            with open(self.LOCALFILE, 'rb') as f:
                # We use WriteMode=overwrite to make sure that the settings in the file
                # are changed on upload
                print("Uploading " + self.LOCALFILE + " to Dropbox as " + self.BACKUPPATH + "...")
                self.logger.info(f"Uploading {self.LOCALFILE} to Dropbox as {self.BACKUPPATH}...")
                try:
                    dbx.files_upload(f.read(), self.BACKUPPATH, mode=WriteMode('overwrite'))
                except ApiError as err:
                    # This checks for the specific error where a user doesn't have
                    # enough Dropbox space quota to upload this file
                    if (err.error.is_path() and
                            err.error.get_path().reason.is_insufficient_space()):
                        self.logger.error(f"ERROR: Cannot back up; insufficient space.")
                        sys.exit("ERROR: Cannot back up; insufficient space.")
                    elif err.user_message_text:
                        print(err.user_message_text)
                        self.logger.error(f"ERROR: {err.user_message_text}")
                        sys.exit()
                    else:
                        print(err)
                        sys.exit()
        except:
            self.logger.error(f"Upload to Dropbox error.")
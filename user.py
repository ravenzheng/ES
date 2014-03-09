import time

from evernote.api.client import EvernoteClient
from evernote.edam.notestore import NoteStore


user_token = 'S=s1:U=605e6:E=147f355b468:C=1409ba4886b:P=1cd:A=en-devtoken:V=2:H=f7257342230a55dd4b86e914182a9fbe'

client = EvernoteClient(token=user_token, sandbox=True)
userStore = client.get_user_store()
user = userStore.getUser()

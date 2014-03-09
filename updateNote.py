import time

from evernote.api.client import EvernoteClient
from evernote.edam.notestore import NoteStore
import evernote.edam.userstore as UserStore
import evernote.edam.type.ttypes as Types


user_token = 'S=s1:U=605e6:E=147f355b468:C=1409ba4886b:P=1cd:A=en-devtoken:V=2:H=f7257342230a55dd4b86e914182a9fbe'
client = EvernoteClient(token=user_token, sandbox=True)
noteStore = client.get_note_store()
noteBooks = noteStore.listNotebooks(user_token)

oldStr=' style="background-color:#FF0000; word-wrap: break-word; -webkit-nbsp-mode: space; -webkit-line-break: after-white-space;"'
newStr=''

for noteBook in noteBooks:
	filter = NoteStore.NoteFilter()
	filter.noteBookGuid = noteBook.guid
	noteList = noteStore.findNotes(user_token,filter,0,1024)
	for note in noteList.notes:
		print note.title
		content = noteStore.getNoteContent(user_token,note.guid)
		note.content = content.replace(oldStr,newStr)
		noteStore.updateNote(user_token,note)
		content = noteStore.getNoteContent(user_token,note.guid)
		print content
		
	
import time

from evernote.api.client import EvernoteClient
from evernote.edam.notestore import NoteStore


user_token = 'S=s1:U=605e6:E=147f355b468:C=1409ba4886b:P=1cd:A=en-devtoken:V=2:H=f7257342230a55dd4b86e914182a9fbe'

client = EvernoteClient(token=user_token, sandbox=True)

note_store = client.get_note_store()

notebooks = note_store.listNotebooks()

print 'notebooks length is ' + str(len(notebooks))

for notebook in notebooks:	
	print notebook.name
	print notebook.guid

	filter = NoteStore.NoteFilter()
	filter.notebookGuid = notebook.guid
	notelist = note_store.findNotes(user_token, filter, 0, 10)
	for note in notelist.notes:
		print 'title	' + note.title
		print note.guid
		content = note_store.getNoteContent(user_token,note.guid)
		print content




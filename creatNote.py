import time

from evernote.api.client import EvernoteClient
import evernote.edam.notestore as NoteStore
import evernote.edam.userstore as UserStore
import evernote.edam.type.ttypes as Types


user_token = 'S=s1:U=605e6:E=147f355b468:C=1409ba4886b:P=1cd:A=en-devtoken:V=2:H=f7257342230a55dd4b86e914182a9fbe'
client = EvernoteClient(token=user_token, sandbox=True)

noteStore = client.get_note_store()
note = Types.Note()
note.title = "I'm a test note6!"
note.content = '<?xml version="1.0" encoding="UTF-8"?>'
note.content +='<!DOCTYPE en-note SYSTEM "http://xml.evernote.com/pub/enml2.dtd">'
note.content += '<en-note style="background-color: #FF0000; word-wrap: break-word; -webkit-nbsp-mode: space; -webkit-line-break: after-white-space;">change background color</en-note>'
note = noteStore.createNote(note)
print note.guid
content = noteStore.getNoteContent(user_token,note.guid)
print content
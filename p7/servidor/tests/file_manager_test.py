import os
from chat import Chat
from chat import FileManager

def test_saves_chat():
    id = "1"
    chat = Chat(id, set(), [])
    FileManager.save(chat)
    dir = os.path.dirname(__file__)
    path = os.path.join(dir, "..", "chats", id)
    assert os.path.exists(path)
    if os.path.exists(path):
        os.remove(path)

def test_saves_chat_content():
    id = "1"
    chat = Chat(id, set(), [])
    FileManager.save(chat)

    dir = os.path.dirname(__file__)
    path = os.path.join(dir, "..", "chats", id)
    file = open(path, "r")
    content = file.read()
    assert content == chat.to_json() 

    if os.path.exists(path):
        os.remove(path)

def test_load_all_returns_list_of_saved_chats():
    chats = [Chat("1", set(), []), Chat("2", set(), [])]
    verify_load_all(chats)

def test_load_all_returns_list_of_saved_chats():
    chats = [Chat("3", set(), []), Chat("4", set(), [])]
    verify_load_all(chats)

def verify_load_all(chats):
    for chat in chats:
        FileManager.save(chat)

    loaded_chats = FileManager.load_chats()
    assert loaded_chats == chats 

    current_dir = os.path.dirname(__file__)
    chats_path = os.path.join(current_dir, "..", "chats")
    for filename in os.listdir(chats_path):
        os.remove(os.path.join(chats_path, filename))

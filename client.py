#test client for the server
# requires socketio-client
from socketIO_client import SocketIO, BaseNamespace


class ChatNamespace(BaseNamespace):
    """
    The server broadcasts 'nicknames', 'announcement' and 'msg_to_room'
    """
    def on_announcement(self, *args):
        print 'announcement: %r' % args

    def on_nicknames(self, *args):
        print 'nicknames: %r' % args

    def on_msg_to_room(self, nickname, message):
        print 'msg_to_room: %s says %s' % (nickname, message)

    def on_connect(self, socketIO):
        """standard event"""
        print '[Connected]'

    def on_disconnect(self):
        """standard event"""
        print '[Disconnected]'

    def on_error(self, name, message):
        """standard event"""
        print '[Error] %s: %s' % (name, message)

    def on_message(self, id, message):
        """standard event"""
        print '[Message] %s: %s' % (id, message)


class TestNamespace(BaseNamespace):
    def on_connect(self, socketIO):
        """standard event"""
        print '[Connected]'

    def on_disconnect(self):
        """standard event"""
        print '[Disconnected]'

    def on_error(self, name, message):
        """standard event"""
        print '[Error] %s: %s' % (name, message)

    def on_message(self, id, message):
        """standard event"""
        print '[Message] %s: %s' % (id, message)


class MainNamespace(BaseNamespace):
    pass


socketIO = SocketIO('localhost', 8000, MainNamespace)
chatSocket = socketIO.connect('/chat', ChatNamespace)
testSocket = socketIO.connect('/test', TestNamespace)

testSocket.emit('nickname', 'compusdfsdtah')
testSocket.emit('user message', 'I\'m really alive!')
chatSocket.emit('nickname', 'computah')
chatSocket.emit('user message', 'I\'m alive!')

# socketIO.on('announcement', on_announcement)
# socketIO.on('nicknames', on_nicknames)
# socketIO.on('msg_to_room', on_msg_to_room)
socketIO.wait()

#socketIO.wait(seconds=1)

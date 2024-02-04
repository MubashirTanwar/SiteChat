css = '''
<style>
.chat-message {
    padding: 1.5rem; border-radius: 0.5rem; margin-bottom: 1rem; display: flex
}
.chat-message.user {
    background-color: #e6e3dc
}
.chat-message.user  .message{
    color: #484848
}
.chat-message.bot {
    background-color: #7951A8
}
.chat-message .avatar {
  width: 20%;
}

.chat-message .avatar img {
  max-width: 78px;
  max-height: 78px;
  border-radius: 50%;
  object-fit: cover;
}
.chat-message .message {
  width: 80%;
  padding: 0 1.5rem;
  color: #fff;
}
'''

bot = '''
<div class="chat-message bot">
    <div class="avatar">
        <img src="https://i.imgur.com/nJ5EuMJ.png" style="max-height: 78px; max-width: 78px; border-radius: 50%; object-fit: cover;">
    </div>
    <div class="message">{{temp}}</div>
</div>
'''

user = '''
<div class="chat-message user">
    <div class="avatar">
        <img src="https://i.imgur.com/QzM36fH.png">
    </div>    
    <div class="message">{{temp}}</div>
</div>
'''

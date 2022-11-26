import json
from django.http import JsonResponse
from chats.models import Message, Chat
from users.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.http import require_http_methods


def parse_request(request):
    try:
        data = json.loads(request.body)
    except json.decoder.JSONDecodeError:
        return {
            'ok': False,
            'result': 'wrong json format'
        }
    return {
        'ok': True,
        'data': data
    }
#{'chat_id':1,'members':['Andrey','Matvey'], 'is_group_chat': false, 'create_date': '29.06.2022', 'mes_amount':300} http://127.0.0.1:8000/chats/update_chat/
@require_http_methods(['PUT'])
def update_chat(request):
    """Обновляет данные о чате"""
    parse_result = parse_request(request)
    if parse_result['ok'] is False:
        return JsonResponse(parse_result)
    data = parse_result['data']
    chat_id = data['chat_id']
    try:
        chat = Chat.object.get(id=chat_id)
    except (ObjectDoesNotExist, ValueError):
        return JsonResponse({
            'ok': False,
            'code': 404,
            'result': f'chat with id={chat_id} does not exists'
        })

    members = data['members']
    is_group_chat = data['is_group_chat']
    create_date = data['create_date']
    mes_amount = data['mes_amount']

    if members is not None:
        try:
            for member in members:
                _user = User.object.get(username=member)
        except (ObjectDoesNotExist, ValueError):
            return JsonResponse({
                'ok': False,
                'code': 404,
                'result': f'user with id={_user} does not exist'
            })
        chat.members = members

    if is_group_chat is not None:
        chat.is_group_chat = is_group_chat
    if create_date is not None:
        chat.create_date = create_date
    if mes_amount is not None:
        chat.mes_amount = mes_amount

    chat.save()
    return JsonResponse({
        'ok': True,
        'code': 200,
    })


#{'message_id':1, 'chat_id':2, 'sent_from':'Matvey', 'sent_to': 'Andrey', 'text': 'Hello, bro', 'sent_time': '18.12.2011', 'is_delivered': true, 'is_read':true,}
#http://127.0.0.1:8000/chats/update_message/
@require_http_methods(['PUT'])
def update_message(request):
    """Обновляет сообщение"""
    parse_result = parse_request(request)
    if parse_result['ok'] is False:
        return JsonResponse(parse_result)
    data = parse_result['data']

    message_id = data['message_id']
    try:
        message = Message.objects.get(id=message_id)
    except (ObjectDoesNotExist, ValueError):
        return JsonResponse({
            'ok': False,
            'code': 404,
            'result': f'message with id={message_id} does not exists'
        })

    chat_id = data['chat_id']
    try:
        chat = Chat.object.get(id=chat_id)
    except (ObjectDoesNotExist, ValueError):
        return JsonResponse({
            'ok': False,
            'code': 404,
            'result': f'message with chat_id={chat_id} does not exists'
        })
    message.chat_id = chat_id

    sent_from = data['sent_from']
    try:
        user = User.object.get(username=sent_from)
    except (ObjectDoesNotExist, ValueError):
        return JsonResponse({
            'ok': False,
            'code': 404,
            'result': f'message with sent_from={sent_from} does not exists'
        })
    message.sent_from = sent_from

    sent_to = data['sent_to']
    try:
        user = User.object.get(username=sent_to)
    except (ObjectDoesNotExist, ValueError):
        return JsonResponse({
            'ok': False,
            'code': 404,
            'result': f'message with sent_to={sent_to} does not exists'
        })
    message.sent_to = sent_to

    text = data['text']
    if text is not None:
        message.text = text

    sent_time = data['sent_time']
    if sent_time is not None:
        message.sent_time = sent_time

    is_delivered = data['is_delivered']
    if sent_time is not None:
        message.is_delivered = is_delivered

    is_read = data['is_read']
    if is_read is not None:
        message.is_read = is_read

    message.save()

    return JsonResponse({
        'ok': True,
        'code': 200,
    })


#{"chat_id": 1}
#http://127.0.0.1:8000/chats/get_all_messages/
@require_http_methods(['GET'])
def get_all_messages(request):
    parse_result = parse_request(request)
    if parse_result['ok'] is False:
        return JsonResponse(parse_result)
    data = parse_result['data']

    chat_id = data['chat_id']
    try:
        chat = Chat.objects.get(id=chat_id)
    except (ObjectDoesNotExist, ValueError):
        return JsonResponse({
            'ok': False,
            'code': 404,
            'result': f'chat with id={chat_id} does not exists'
        })
    try:
        messages = Message.objects.filter(chat_id=chat)
    except (ObjectDoesNotExist, ValueError):
        return JsonResponse({
            'ok': False,
            'code': 404,
            'result': f'no messages in chat id={chat.id}'
        })
    response = {}
    for message in messages:
        response[message.id] = {
            'first_user': message.sent_from,
            'second_user': message.sent_to,
            'text': message.text,
            'sent_time': message.sent_time,
            'is_delivered': message.is_delivered,
            'is_read': message.is_read,
        }

    return JsonResponse({
        'ok': True,
        'code': 200,
        'result': response
    })

#{"user_id": 1}
@require_http_methods(['GET'])
def get_all_chats(request):
    parse_result = parse_request(request)
    if parse_result['ok'] is False:
        return JsonResponse(parse_result)
    data = parse_result['data']

    user_id = data['user_id']
    try:
        user = User.objects.get(id=user_id)
    except (ObjectDoesNotExist, ValueError):
        return JsonResponse({
            'ok': False,
            'code': 404,
            'result': f'user with id={user_id} does not exists'
        })
    try:
        chats = Chat.objects.filter(members=user)
    except (ObjectDoesNotExist, ValueError):
        return JsonResponse({
            'ok': False,
            'code': 404,
            'result': f'no chats where the user {user.username} is'
        })
    response = {}
    for chat in chats:
        response[chat.id] = {
            'first_user': chat.first_user,
            'second_user': chat.second_user,
            'is_group_chat': chat.is_group_chat,
            'create_date': chat.create_date,
            'mes_amount': chat.mes_amount,
        }

    return JsonResponse({
        'ok': True,
        'code': 200,
        'result': response
    })


#{"chat_id": 1}
@require_http_methods(['GET'])
def get_chat(request):
    parse_result = parse_request(request)
    if parse_result['ok'] is False:
        return JsonResponse(parse_result)
    data = parse_result['data']

    chat_id = data['chat_id']
    try:
        chat = Chat.objects.get(id=chat_id)
    except (ObjectDoesNotExist, ValueError):
        return JsonResponse({
            'ok': False,
            'code': 404,
            'result': f'chat with id={chat_id} does not exists'
        })

    members = User.objects.filter(chats=chat_id).values()
    if chat.is_group_chat:
        return JsonResponse({
            'ok': True,
            'code': 200,
            'result': {
                'chat_id': chat.id,
                'create_date': chat.create_date,
                'message_amount': chat.mes_amount,
                'members': list(members),
            }
        })
    else:
        return JsonResponse({
            'ok': True,
            'code': 200,
            'result': {
                'chat_id': chat.id,
                'first_user': chat.first_user,
                'second_user': chat.second_user,
                'create_date': chat.create_date,
                'message_amount': chat.mes_amount,
            }
        })


#{"message_id": 1}
@require_http_methods(['GET'])
def get_message(request):
    parse_result = parse_request(request)
    if parse_result['ok'] is False:
        return JsonResponse(parse_result)
    data = parse_result['data']

    message_id = data['message_id']
    try:
        message = Message.objects.get(id=message_id)
    except (ObjectDoesNotExist, ValueError):
        return JsonResponse({
            'ok': False,
            'code': 404,
            'result': f'message with id={message_id} does not exists'
        })

    return JsonResponse({
        'ok': True,
        'code': 200,
        'result': {
            'id': message.id,
            'sent_from': message.sent_from,
            'sent_to': message.sent_to,
            'text': message.text,
            'sent_time': message.sent_time,
            'is_delivered': message.is_delivered,
            'is_read': message.is_read,
        }
    })


#{'first_user':'Matvey', 'second_user':'Andrey', 'is_group_chat': true}
@require_http_methods(['POST'])
def create_chat(request):
    parse_result = parse_request(request)
    if parse_result['ok'] is False:
        return JsonResponse(parse_result)
    data = parse_result['data']

    first_user = data['first_user']
    second_user = data['second_user']
    is_group_chat = data['is_group_chat']
    try:
         user1 = User.objects.get(id=first_user)
    except (ObjectDoesNotExist, ValueError):
        return JsonResponse({
            'ok': False,
            'code': 404,
            'result': f'user with id={first_user} does not exists'
        })

    try:
         user2 = User.objects.get(id=second_user)
    except (ObjectDoesNotExist, ValueError):
        return JsonResponse({
            'ok': False,
            'code': 404,
            'result': f'user with id={second_user} does not exists'
        })

    Chat.objects.create(first_user=first_user, second_user=second_user, is_group_chat=is_group_chat, mes_amount=0)

    return JsonResponse({
        'ok': True,
        'code': 200,
    })


#{"chat_id": 2}
@require_http_methods(['DELETE'])
def delete_chat(request):
    parse_result = parse_request(request)
    if parse_result['ok'] is False:
        return JsonResponse(parse_result)
    data = parse_result['data']

    chat_id = data['chat_id']
    try:
        Chat.objects.get(id=chat_id).delete()
    except (ObjectDoesNotExist, ValueError):
        return JsonResponse({
            'ok': False,
            'code': 404,
            'result': f'chat with id={chat_id} does not exists'
        })

    return JsonResponse({
        'ok': True,
        'code': 200,
    })


#{'chat_id':2, 'sent_from':'Matvey', 'sent_to': 'Andrey', 'text': 'Hello, bro',}
@require_http_methods(['POST'])
def create_message(request):
    parse_result = parse_request(request)
    if parse_result['ok'] is False:
        return JsonResponse(parse_result)
    data = parse_result['data']

    user1 = data['sent_from']
    try:
        author1 = User.objects.get(username=user1)
    except (ObjectDoesNotExist, ValueError):
        return JsonResponse({
            'ok': False,
            'code': 404,
            'result': f'user {user1} does not exists'
        })
    user2 = data['sent_to']
    try:
        author2 = User.objects.get(username=user2)
    except (ObjectDoesNotExist, ValueError):
        return JsonResponse({
            'ok': False,
            'code': 404,
            'result': f'user {user2} does not exists'
        })
    chat_id = data['chat_id']
    try:
        chat = Chat.objects.get(id=chat_id)
    except (ObjectDoesNotExist, ValueError):
        return JsonResponse({
            'ok': False,
            'code': 404,
            'result': f'chat with id={chat_id} does not exists'
        })

    text = data['text']
    Message.objects.create(chat_id=chat_id, sent_from=user1, sent_to=user2, text=text,)

    return JsonResponse({
        'ok': True,
        'code': 200,
    })


#{"message_id": 1}
@require_http_methods(['POST'])
def delete_message(request):
    parse_result = parse_request(request)
    if parse_result['ok'] is False:
        return JsonResponse(parse_result)
    data = parse_result['data']

    message_id = data.get('message_id')
    try:
        Message.objects.get(id=message_id).delete()
    except (ObjectDoesNotExist, ValueError):
        return JsonResponse({
            'ok': False,
            'code': 404,
            'result': f'message with id={message_id} does not exists'
        })

    return JsonResponse({
        'ok': True,
        'code': 200,
    })


#{"chat_id": 1, "user_id": 1}
@require_http_methods(['POST'])
def add_member(request):
    parse_result = parse_request(request)
    if parse_result['ok'] is False:
        return JsonResponse(parse_result)
    data = parse_result['data']

    chat_id = data['chat_id']
    try:
        chat = Chat.objects.get(id=chat_id)
    except (ObjectDoesNotExist, ValueError):
        return JsonResponse({
            'ok': False,
            'code': 404,
            'result': f'chat with id={chat_id} does not exists'
        })

    if not chat.is_group_chat:
        return JsonResponse({
            'ok': False,
            'code': 404,
            'result': f'you can\'t add new member in chat with id={chat_id}'
        })
    else:

        user_id = data['user_id']
        try:
            user = User.objects.get(id=user_id)
        except (ObjectDoesNotExist, ValueError):
            return JsonResponse({
                'ok': False,
                'code': 404,
                'result': f'user with id={user_id} does not exists'
            })

        user_already_member = User.objects.filter(chats__id=chat_id).first()
        if user_already_member is not None:
            return JsonResponse({
                'ok': False,
                'code': 404,
                'result': f'user with id={user_id} already member of the chat with id={chat_id}'
            })

        user.chats.add(chat)
        user.save()

        return JsonResponse({
            'ok': True,
            'code': 200,
        })


#{"chat_id": 1, "user_id": 1}
@require_http_methods(['POST'])
def delete_member(request):
    parse_result = parse_request(request)
    if parse_result['ok'] is False:
        return JsonResponse(parse_result)
    data = parse_result['data']

    chat_id = data['chat_id']
    try:
        chat = Chat.objects.get(id=chat_id)
    except (ObjectDoesNotExist, ValueError):
        return JsonResponse({
            'ok': False,
            'code': 404,
            'result': f'chat with id={chat_id} does not exists'
        })

    user_id = data['user_id']
    try:
        user = User.objects.get(id=user_id)
    except (ObjectDoesNotExist, ValueError):
        return JsonResponse({
            'ok': False,
            'code': 404,
            'result': f'user with id={user_id} does not exists'
        })

    user.chats.remove(chat)
    user.save()

    return JsonResponse({
        'ok': True,
        'code': 200,
    })


#{"message_id": 1}
@require_http_methods(['POST'])
def read_message(request):
    parse_result = parse_request(request)
    if parse_result['ok'] is False:
        return JsonResponse(parse_result)
    data = parse_result['data']

    message_id = data['message_id']
    try:
        message = Message.objects.get(id=message_id)
    except (ObjectDoesNotExist, ValueError):
        return JsonResponse({
            'ok': False,
            'code': 404,
            'result': f'message with id={message_id} does not exists'
        })

    message.is_read = True
    message.save()

    return JsonResponse({
        'ok': True,
        'code': 200,
    })

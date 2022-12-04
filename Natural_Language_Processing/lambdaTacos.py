import json

def get_bill(slots):

    prices = {
        'alambreVeg': 115,
        'alambrePech': 120,
        'alambreBist': 120,
        'alambreChul': 120,
        'alambreCost': 130,
        'alambreArra': 145,
        'costraPastor': 30,
        'costraPechuga': 35,
        'costraBistec': 35,
        'volcanPastor': 22,
        'volcanPechuga': 22,
        'volcanBistec': 28,
        'tortaPastor': 50,
        'tortaMaciza': 50,
        'tortaSuadero': 50,
        'tortaLonganiza': 50,
        'tortaPechuga': 50,
        'tortaBistec': 65,
        'tortaChuleta': 65,
        'refresco': 23,
        'aguaNatural': 20,
        'aguaJamaica': 24,
        'aguaHorchata': 24,
        'botellaCerveza': 33,
        'barrilCerveza': 33,
        'litroCerveza': 80,
        'michelada': 90,
        'michelato': 90,
        'arrozLeche': 30,
        'pastelChocolate': 35,
        'fresasCrema': 35,
        'gelatina': 20,
        'flan': 30
    }

    try:
        bill = 0
        for i in slots:
            if (i not in ["tipoPedido", "tipoPlatillo", "tipoBebida", "boolPedirMas"]):
                bill += prices[i]*int(slots[i]['value']['interpretedValue'])
        return "Su cuenta es de $" + str(bill) + "."
    except:
        return 'Sorry! An error occurred while calculating your bill.'


""" --- Main handler --- """


def lambda_handler(event, context):

    intent_name = event['interpretations'][0]['intent']['name']
    slots = event['interpretations'][0]['intent']['slots']
    message = get_bill(slots)

    response = {
       'sessionState' : {
            'dialogAction' : {
                'type' : 'Close'
            },
            'intent' : {
                'name' : intent_name,
                'state' : 'Fulfilled'
            }
       },
        'messages': [
             {
                'contentType' : 'PlainText',
                'content' : message
             }
        ]
    }

    return response
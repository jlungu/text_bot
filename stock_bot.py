from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
import requests
import locale
from datetime import date

app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def incoming_sms():
    body = request.values.get('Body', None)

    resp = MessagingResponse()

    if body == 'STONK':
        resp.message("\nSTONKS ONLY GO UP. TRUST IN ME. INK JUST REPLACED.\n -J POW")
    # In this upcoming case, the market bot gives a market update!
    elif body.lower() == 'market update' or body.lower() == "market":
        # Here, we grab a quote from our Stock API. Quotes for ^DJI, ^GSPC, and ^IXIC
        # DOW JONES INDUSTRIAL AVERAGE
        dji = requests.get('https://finnhub.io/api/v1/quote?symbol=^DJI&token=brain17rh5rbgnjpuck0')
        dji_close = dji.json()['c'] # price
        dji_change = dji_close - dji.json()['pc'] # change
        dji_perchange =  (dji_change / dji_close) * 100 # % change
        dji_perchange = '%.2f' % dji_perchange + '%'
        if dji_change > 0:# put + if its a positive number
            dji_change = '+' + ('%.2f' % dji_change)
            dji_perchange = "+"+  dji_perchange
        else:
            dji_change = '%.2f' % dji_change
            dji_close = '$' +  f"{dji_close:,}"
        # S & P 500
        gspc = requests.get('https://finnhub.io/api/v1/quote?symbol=^GSPC&token=brain17rh5rbgnjpuck0')
        gspc_close = gspc.json()['c']
        gspc_change = gspc_close - gspc.json()['pc'] # change
        if gspc_change < 0:
            up = False
        else:
            up = True
        gspc_perchange =  (gspc_change / gspc_close) * 100 # % change
        gspc_perchange = '%.2f' % gspc_perchange + '%'
        if gspc_change > 0:
            gspc_change = '+' + ('%.2f' % gspc_change)
            gspc_perchange = "+"+  gspc_perchange
        else:
            gspc_change = '%.2f' % gspc_change
        gspc_close = '$' +  f"{gspc_close:,}"
        # NASDAQ
        ixic = requests.get('https://finnhub.io/api/v1/quote?symbol=^IXIC&token=brain17rh5rbgnjpuck0')
        ixic_close = ixic.json()['c']
        ixic_change = ixic_close - ixic.json()['pc'] # change
        ixic_perchange =  (ixic_change / ixic_close) * 100 # % change
        ixic_perchange = '%.2f' % ixic_perchange + '%'
        if ixic_change > 0:
            ixic_change = '+' + ('%.2f' % ixic_change)
            ixic_perchange = "+"+  ixic_perchange
        else:
            ixic_change = '%.2f' % ixic_change
        ixic_close = '$' +  f"{ixic_close:,}"

        # Need todays date...
        today = date.today().strftime("%B %d, %Y")
        # Now we create the master string, formatted to send the text!
        if up == True:
            resp.message("Market Update | " + str(today) + "\n" + "Market is UP:\n" +
            "- DOW J: " + str('%.2f' % dji_close) + " (" + str(dji_change) +")\n- S&P 500: " + 
            str('%.2f' % gspc_close) + " (" + str(gspc_change) + ")\n- NASDAQ: " + str('%.2f' % ixic_close) 
            + " (" + str(ixic_change)+")")
        else:
            resp.message("Market Update | " + str(today) + "\n" + "Market is DOWN:\n" +
            "- DOW J: " + str('%.2f' % dji_close) + " (" + str(dji_change) +")\n- S&P 500: " + 
            str('%.2f' % gspc_close) + " (" + str(gspc_change) + ")\n- NASDAQ: " + str('%.2f' % ixic_close) + 
            " (" + str(ixic_change) + ")")


    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)

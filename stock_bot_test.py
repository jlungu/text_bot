import requests
import locale
from datetime import date
import datetime

## USED TO TEST TEXTS BEFORE I SEND, TO SAVE TEXTING MONEY.

# COVID updates
states = {'alabama': 'AL',
    'alaska': 'AK',
    'american samoa': 'AS',
    'arizona': 'AZ',
    'arkansas': 'AR',
    'california': 'CA',
    'colorado': 'CO',
    'connecticut': 'CT',
    'delaware': 'DE',
    'district of columbia': 'DC',
    'florida': 'FL',
    'georgia': 'GA',
    'guam': 'GU',
    'hawaii': 'HI',
    'idaho': 'ID',
    'illinois': 'IL',
    'indiana': 'IN',
    'iowa': 'IA',
    'kansas': 'KS',
    'kentucky': 'KY',
    'louisiana': 'LA',
    'maine': 'ME',
    'maryland': 'MD',
    'massachusetts': 'MA',
    'michigan': 'MI',
    'minnesota': 'MN',
    'mississippi': 'MS',
    'missouri': 'MO',
    'montana': 'MT',
    'nebraska': 'NE',
    'nevada': 'NV',
    'new hampshire': 'NH',
    'new jersey': 'NJ',
    'new mexico': 'NM',
    'new york': 'NY',
    'north carolina': 'NC',
    'north dakota': 'ND',
    'northern mariana islands':'MP',
    'ohio': 'OH',
    'oklahoma': 'OK',
    'oregon': 'OR',
    'pennsylvania': 'PA',
    'puerto rico': 'PR',
    'rhode island': 'RI',
    'south carolina': 'SC',
    'south dakota': 'SD',
    'tennessee': 'TN',
    'texas': 'TX',
    'utah': 'UT',
    'vermont': 'VT',
    'virgin islands': 'VI',
    'virginia': 'VA',
    'washington': 'WA',
    'west virginia': 'WV',
    'wisconsin': 'WI',
    'wyoming': 'WY'}
# Takes state as input, and returns the latest covid numbers for that state.
state = "New Yrk"
if state.lower() in states:
    state = states[state.lower()] # Grabbing the states abbreviation
else:
    print("poop")
#state = states[state.lower()] # Grabbing the states abbreviation
cases = requests.get('https://covidtracking.com/api/v1/us/current.json')
cases = cases.json()
updated = datetime.datetime(int(cases[0]['lastModified'][:4]), int(cases[0]['lastModified'][5:7]), int(cases[0]['lastModified'][8:10]), int(cases[0]['lastModified'][11:13]), int(cases[0]['lastModified'][14:16]), int(cases[0]['lastModified'][17:19]), 0)
update = "COVID-19 Update | UNITED STATES\n- New Cases: "+ f"{cases[0]['positiveIncrease']:,}" + "\n- New Deaths: " + f"{cases[0]['deathIncrease']:,}" + "\n- Total Cases: " + f"{cases[0]['positive']:,}" + "\n- Total Deaths: " + f"{cases[0]['death']:,}," + "\nUpdated " + date.strftime(updated, "%B %d, %Y %I:%M%p")
print(update)

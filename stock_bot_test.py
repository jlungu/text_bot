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
state = "New York"
state = states[state.lower()] # Grabbing the states abbreviation
cases = requests.get('https://covidtracking.com/api/v1/states/' + state.lower() + '/current.json')
cases = cases.json()
updated = datetime.datetime(int(cases['dateModified'][:4]), int(cases['dateModified'][5:7]), int(cases['dateModified'][8:10]), int(cases['dateModified'][11:13]), int(cases['dateModified'][14:16]), int(cases['dateModified'][17:19]), 0)
update = "COVID-19 Update | NEW YORK - USA\n- New Cases: "+ f"{cases['positiveIncrease']:,}" + "\n- New Deaths: " + f"{cases['deathIncrease']:,}" + "\n- Total Cases: " + f"{cases['positive']:,}" + "\n- Total Deaths: " + f"{cases['death']:,}," + "\nUpdated " + date.strftime(updated, "%B %d, %Y %I:%M%p")
print(update)

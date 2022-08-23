alert_failure_count = 0

def network_alert_stub(celcius):
    print(f'ALERT: Temperature is {celcius} celcius')
    # Return 200 for ok
    # Return 500 for not-ok
    # stub always succeeds and returns 200
    if celcius < 100:
        return 200
    else:
        return 500

class converter:
    @staticmethod
    def to_celcius(temp):
        if temp < 32:
           raise ValueError("Temperature below freezing point")            
        elif temp > 212:
            raise ValueError("Temperature above Boiling point")
        elif temp <= -459:
            raise ValueError("Temperature below -459 is not possible") 
        return (temp-32)*5/9
 
def alert_in_celcius(farenheit):
    celcius = converter.to_celcius(farenheit)
    returnCode = network_alert_stub(celcius)
    if returnCode != 200:
        # non-ok response is not an error! Issues happen in life!
        # let us keep a count of failures to report
        # However, this code doesn't count failures!
        # Add a test below to catch this bug. Alter the stub above, if needed.
        global alert_failure_count
        alert_failure_count += 1


alert_in_celcius(400.5)
alert_in_celcius(303.6)
print(f'{alert_failure_count} alerts failed.')
#print('All is well (maybe!)')

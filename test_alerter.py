import alerter
alert_failure_count = 0
alerter.alert_in_celcius(400.5)
alerter.alert_in_celcius(303.6)
print(f'{alert_failure_count} alerts failed.')

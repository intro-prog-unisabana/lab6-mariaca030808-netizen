def trigger_alarm(temperatures, threshold= 80):
    sensoresSuperados= []
    if temperatures== {}:
        return []
    for sensor, tempera in temperatures.items():
        if tempera > threshold:
            sensoresSuperados.append(sensor)
    return sensoresSuperados
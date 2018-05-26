def put(str):
    print(str, end=' ')

tens = ['oh', ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen'], 'twenty', 'thirty', 'forty', 'fifty']
ones = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

inputTime = input("> Input time: ").split(':')
hour = int(inputTime[0])
ampm = 'am'
minute = int(inputTime[1])

if hour >= 12:
    ampm = 'pm'
    hour = hour % 12

put('It\'s')

if hour == 0:
    put(tens[1][2])
elif hour <= 9:
    put(ones[hour - 1])
else:
    put(tens[1][hour - 10])

if minute != 0:
    if minute <= 9:
        put(tens[0])
        put(ones[minute - 1])
    elif minute <= 19:
        put(tens[1][minute - 10])
    else:
        put(tens[minute // 10])
        if minute % 10 != 0:
            put(ones[minute % 10 - 1])

print(ampm)

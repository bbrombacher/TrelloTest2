import inspect

def log(message=None):
    # str(inspect.stack()[1].filename
    if message is None:
        print(str(inspect.getmodulename(inspect.stack()[1].filename)) + ': ' +
              inspect.stack()[1].function)
    else:
        print(str(inspect.getmodulename(inspect.stack()[1].filename)) + ': ' +
              inspect.stack()[1].function + ': ' + message)


def getActualKeys(json):
    log()
    actual_keys = []
    for x in json:
        actual_keys.append(x)

    log('actual keys: ' + str(actual_keys))
    log('actual keys length: ' + str(len(actual_keys)))

    return actual_keys
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                        'AppleWebKit/537.36 (KHTML, like Gecko) '
                        'Chrome/64.0.3282.186 Safari/537.36'}


def dict2proxy(dic):
    s = dic['type'] + '://' + dic['ip'] + ':' + str(dic['port'])
    return {'http': s, 'https': s}

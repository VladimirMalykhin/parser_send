class Check(object):
    Values = {
'title': {'max': 75, 'stop': 1},
'keywords': {'max': 60, 'stop': 1},
'description': {'max': 150, 'stop': 0},
'h1': {'max': 50, 'stop': 1},
'h2': {'max': 90, 'stop': 1}
    }

    def check(self, tag, value):
        length = self.Values[tag]['max']
        stop = self.Values[tag]['stop']
        if(len(value)) is 0:
            return 'no'
        if len(value) > length:
            #return str(len(value)) + '>' + str(length)
            return 'long'

        elif stop is 1:

            if '!' in value or ',' in value or '.' in value:
                return 'Stop symvols'
            else:
                return 'all right'
        else:
            return 'all right'





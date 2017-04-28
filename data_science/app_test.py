import httplib

# use this server for dev
SERVER = '54.202.125.6:5000'
# SERVER = '0.0.0.0:5000'


# use this server for prod, once it's on ec2
# SERVER = 'xxxxx.aws.ec2.com:5000'


def get_default():
    out = dict()
    h = httplib.HTTPConnection(SERVER)
    # want the url to look something like this
    # 'http://localhost:5000/restaurants/borough/counts'
    h.request('GET', 'http://' + SERVER + '/success')
    resp = h.getresponse()
    out = resp.read()
    return out


def get_resource(var):
    out = dict()
    h = httplib.HTTPConnection(SERVER)
    # want the url to look something like this
    # 'http://localhost:5000/resource/<var>'
    h.request('GET',
              'http://' + SERVER + '/success?ORIGIN=ATL&CRS_DEP_TIME=1102&UNIQUE_CARRIER=UA&DATE=06%2F26%2F17&DEST=BOS&FL_NUM=292')
    resp = h.getresponse()
    out = resp.read()
    return out


if __name__ == '__main__':
    print "************************************************"
    print "test of my flask app running at ", SERVER
    print "created by Donny Chen, Matthew Wang, Zefeng Zhang"
    print "************************************************"
    print " "
    print "******** resource **********"
    print "Our app returns the probability of flight delay more than 15 minutes, "
    print "given flight date, departure time, airline, flight number, depature airport, and arrival airport."
    print "e.g. \"06/26/17\", \"2302\", \"UA\", \"292\", \"ATL\", and \"BOS\""
    print get_resource('test')

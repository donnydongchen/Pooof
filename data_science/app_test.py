import httplib

# use this server for dev
SERVER = '54.202.125.6:5000'

# use this server for prod, once it's on ec2
# SERVER = 'xxxxx.aws.ec2.com:5000'


def get_default():
    out = dict()
    h = httplib.HTTPConnection(SERVER)
    # want the url to look something like this
    # 'http://localhost:5000/restaurants/borough/counts'
    h.request('GET', 'http://'+ SERVER + '/success')
    resp = h.getresponse()
    out = resp.read()
    return out

def get_resource(var):
    out = dict()
    h = httplib.HTTPConnection(SERVER)
    # want the url to look something like this
    # 'http://localhost:5000/resource/<var>'
    h.request('GET', 'http://'+SERVER+'/success/?CRS_DEP_TIME=1103&ORIGIN_CITY_NAME=San+Francisco%2C+CA&DATE=06%2F26%2F17&FL_NUM=292&UNIQUE_CARRIER=UA&DEST_CITY_NAME=Orlando%2C+FL')
    resp = h.getresponse()
    out = resp.read()
    return out


if __name__ == '__main__':
    print "************************************************"
    print "test of my flask app running at ", SERVER
    print "created by Bob Ross"
    print "************************************************"
    print " "
    print "******** resource **********"
    print "Our app returns the probability of flight delay more than 15 minutes, "
    print "given flight date, departure time, airline, flight number, depature city, and arrival city."
    print "e.g. \"06/26/17\", \"1103\", \"UA\", \"292\", \"San Francisco, CA\", and \"Orlando, FL\""
    print get_resource('test')
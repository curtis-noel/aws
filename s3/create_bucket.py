'''
Created on Mar 26, 2018

@author: curtis
'''

import boto3
import random
import string
import datetime




if __name__ == '__main__':
    rand_str = lambda n: ''.join([random.choice(string.lowercase) for i in xrange(n)])
    s = rand_str(10) + "-temp"
    print ("%s: Starting" % datetime.datetime.utcnow())
    print ("%s: opening session" % datetime.datetime.utcnow())
    session = boto3.Session(profile_name='default')
    print ("%s: getting s3 resource" % datetime.datetime.utcnow())
    s3 = session.resource('s3')
    print ("%s: creating bucket" % datetime.datetime.utcnow())
    s3.create_bucket(Bucket = s)
    print ("%s: deleting bucket" % datetime.datetime.utcnow())
    bucket = s3.Bucket(s)
    bucket.delete();
    print ("%s: finished" % datetime.datetime.utcnow())